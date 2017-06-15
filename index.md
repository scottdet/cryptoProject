## Introduction

I'm currently a fourth year student at UCLA studying computational mathematics. For this project I am pulling various cryptocurrencies pricing and volume data with the aim of making more informed trades based on a few features I will calculate using this data. I am also hoping to implement sentiment analysis in order to determine if bulk sentiment holds any merit in making future predictions. 

## Goals

- Write a script to pull pricing and volume data from a web browswer (do not want to pay for data or be rescrticed to large time scales)
- Store data locally 
- Pull Tweets containing key words like "Bitcoin" and "Ethereum"
- Calculate covariances between cryptocurrencies

## Future Directions

- Calculate more technical features. What is predictive of future price?
- Merge various scripts into a working pipeline
- Deploy a trading algorithm

## Code

- [Scraper](https://raw.githubusercontent.com/scottdet/cryptoProject/master/scrape.py)
- Tweets
- [Ticker](https://raw.githubusercontent.com/scottdet/cryptoProject/master/ticker.py)
- [Covariance](https://raw.githubusercontent.com/scottdet/cryptoProject/master/covariance.py)

## Progress Reports 

- Week 5
  - Project approved
  - Starting to research where I will get my data from

- Week 6
  - Working with Selenium in Python to pull data
  - Significant difficulties getting dependencies and Selenium subprocceses working 

- Week 7
  - First real Progress, scraper is operational for BTC, ETH, Litecoin
  - Starting to pull volume data 
  - Need to parse data correctly and output cleaning to a file

- Week 8
  - Previous weeks todo is done, going to dive into pulling Tweets based on keywords
  - Researching Twitter's policy on pull requests and bot regulations
  
- Week 9
  - Getting tweets based on keywords
  - There are a few sentiment analysis libraries for Python, need to research pros and cons/implementation
  - Beginning to calculate other features that could be helpful in prediction

- Week 10
  - Starting to store data from other script, need a decent backlog before I can find meaningful patterns
  - Getting current data from a different source to calculate covariances for future use
  - I will need to learn a lot more about economics before this trading bot is operational
  - Putting it together here for a better presentation
  
## Relation to PIC 10C

### Constructors: 

The way Python and C++ construct objects have some similarities. Both languages call a function with a relatively simple responsibility. In Python this means calling \__new\__ for an object instance whereas in C++ we call some version of operator new for raw memory. Both languages then call a function which has the opportunity to do more work to initialize the object into a useful state. In Python we use \__init\__ and in C++ we create a constructor.

There are also key differences between constructors in these two languages. As far as the Python language is concerned, you have a valid object of the specified type before you even enter \__init\__. It is then not a "constructor" in the way we learned during this course. In C++ and in my understanding of the definition, a constructor turns an invalid, pre-constructed object into a "proper" completed object of the type.

Basically \__new\__ in Python is defined to return "the new object instance", whereas C++ new operators just return some memory, which is not yet an instance of any class. However, \__init\__ in Python is where you first establish some important class attributes so as I am conerned it functions similarly to a constructor.

One more key difference is that in C++, no-argument constructors for base classes are called automatically in the appropriate order if necessary, whereas for \__init\__ in Python, you have to explicitly initialize your base in your own \__init\__ function.

### Descrutors: 

As far as I understand, the main difference between destructors in Python and C++ is that in C++, we have a mechanism for what happens when a constructor throws an exception. By this I mean in terms of calling destrcutors for sub-objects that have already been constructed. Many of these differences arise due to Python being unconcerned with raw memory. In C++ there is no garbage collection whereas Python handles much of this for the user and calls \_\_del\__, the counterpart to \__init\__ during runtime.

### Iterators
 
The iterators we learned to implement during this course are very flexible. This is an advantage that C++ has in control over our code. In C++ it is easy to change underlying container types. For example, we might decide later that the number of insertions and deletions is so high that a list would be more efficient than a vector, and our iterator can be easily used for this list even when it was created for a vector. Moreover, we can easily use our iterator bidirectionaly, such as with ++ or --. This is very useful to parse a stream like objects.

In Python it did not seem like these things would be easy to accomplish. However, after some time on stackoverflow it seems like these implemenations are possible without _too much_ trouble. Consider the following examples:

If we want to replace objects in the underlying container. For dictionaries, iterate over the keys or items, not only the values:
```
for key, value in my_dict.iteritems():
    if conditiion(value):
        my_dict[key] = new_value
```
For lists use enumerate():
```
for index, item in enumerate(my_list):
    if condition(item):
        my_list[index] = new_item
```
If we want an iterator with one "look-ahead" value. Here is a general solution:
```
def iter_with look_ahead(iterable, sentinel=None):
    iterable, it_ahead = itertools.tee(iterable)
    next(it_ahead, None)
    return izip_longest(iterable, it_ahead, fillvalue=sentinel)

for current, look_ahead in iter_with look_ahead(tokens):
    # your code here
```
If we want to iterate in reverse, it is straight forward to use reversed() for containers that support it. Finally, to create a random access iterator in Python just turn your iterable into a list and use indices:
```
my_list = list(my_iterable)
```
