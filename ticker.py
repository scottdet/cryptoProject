import urllib
import urllib2
import json
import time

def api_query():
    web = json.load(urllib2.urlopen(urllib2.Request('https://api.coinmarketcap.com/v1/ticker/?limit=25')))
    return web

if __name__ == "__main__":
	print["name", "price", "1h", "24h", "7d"]
	while True:
		
		data = api_query();
		for entry in range(len(data)):
			line = data[entry]['name']+", "+ data[entry]['price_usd']+", "+ data[entry]['percent_change_1h']+", "+ data[entry]['percent_change_24h']+", "+ data[entry]['percent_change_7d']
			with open("ticker.txt", "a") as myfile:
				myfile.write(str(line)+"\n")
		time.sleep(290)