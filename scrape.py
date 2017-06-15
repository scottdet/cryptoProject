from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from threading import Thread
import argparse
import platform
import time

"""
Helper funciton to get selenium firefox driver
"""
def get_driver():
	if "Darwin" in platform.system():
		return webdriver.Firefox()
	else:
		capabilities = webdriver.DesiredCapabilities().FIREFOX
		capabilities["marionette"] = False
		binary = FirefoxBinary(r'/usr/bin/firefox')
		driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)
		return driver
"""
Scrape coin price from cryptocompare.com
"""
def scrape_price(driver):
	price = driver.find_elements_by_class_name("price-value")[0].text
	price = str(float(price.split()[1].replace(",","")))
	return price

"""
Scrape volume from cryptocompare.com
"""
def scrape_volume(driver):
	vol_header = driver.find_elements_by_class_name("width20p")[0]
	children = vol_header.find_elements_by_css_selector("*")
	vol_str = children[8].text.split()
	vol_str[2] = vol_str[2].replace(")","")
	vol = float(vol_str[1])
	if len(vol_str) > 2:
		if vol_str[2] == "M":
			vol *= 1e6
		elif vol_str[2] == "K":
			vol *= 1e3
	vol = str(vol)
	return vol

"""
Get current time
"""
def get_time():
	return str(time.time()*1000.0)

"""
Generalized loop for scraping
"""
def scrape(url,filename,delay):
	driver = get_driver()
	driver.get(url)
	while True:
		time.sleep(delay)
		f = open(filename,'a')
		t = get_time()
		price = scrape_price(driver)
		vol = scrape_volume(driver)
		print(price+ "\t" + vol + "\t" + t)
		f.write(price + ","+ vol + "," + t + "\n") 
		f.close()

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--time')
	parser.add_argument('--file')
	parser.add_argument('--currency')
	args = parser.parse_args()
	delay = args.time
	if not delay:
		delay = 600
	delay = float(delay)
	currency = args.currency
	filename = None
	if args.file:
		filename = args.file
	if not currency or currency == "bitcoin":
		url = "https://www.cryptocompare.com/coins/btc/overview/USD"
		if not filename:
			filename = "prices-bitcoin.csv"
		scrape(url,filename,delay)
	elif currency == "eth":
		url = "https://www.cryptocompare.com/coins/eth/overview/USD"
		if not filename:
			filename = "prices-eth.csv"
		scrape(url,filename,delay)
	elif currency == "litecoin":
		url = "https://www.cryptocompare.com/coins/ltc/overview/USD"
		if not filename:
			filename = "prices-litecoin.csv"
		scrape(url,filename,delay)
	elif currency == "all":
		urls = ["https://www.cryptocompare.com/coins/btc/overview/USD",
			"https://www.cryptocompare.com/coins/eth/overview/USD",
			"https://www.cryptocompare.com/coins/ltc/overview/USD"]
		filenames = ["prices-bitcoin.csv",
			    "prices-eth.csv",
			    "prices-litecoin.csv"]
		t1 = Thread(target=scrape,args=(urls[0],filenames[0],delay))
		t2 = Thread(target=scrape,args=(urls[1],filenames[1],delay))
		t3 = Thread(target=scrape,args=(urls[2],filenames[2],delay))
		t1.start()
		t2.start()
		t3.start()
		t1.join()
		t2.join()
		t3.join()
	else:
		print("Invalid currency")
		return
	
if __name__ == "__main__":main()