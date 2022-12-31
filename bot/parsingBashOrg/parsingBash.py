import requests
from bs4 import BeautifulSoup 
import random

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}


def getRandomJoke():
  try:
    url = "http://bashorg.org/casual" 
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', {"id": "quotes"})
    quote = quotes.find('div', class_="q")
    joke = quote.findAll('div')
    return joke[1].text
  except:
    return "Упс, при парсинге странице произошла ошибка =("


def getPageOrYearJoke(pageOrYear=1, amountJokes=1):
  try:
    url = f"http://bashorg.org/page/{pageOrYear}" 
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml') 
    quotes = soup.find('div', {"id": "quotes"})  
    quote = quotes.findAll('div', class_="q")  
    for _ in range(1, amountJokes+1):
      joke = quote[random.randint(0,len(quote)-1)].find('div', class_="quote" ).text
      yield joke
  except:
    return "Упс, при парсинге странице произошла ошибка =("


def getBestJoke():
  try:
    url = f"http://bashorg.org/best" 
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml') 
    quotes = soup.find('div', {"id": "quotes"})  
    quote = quotes.findAll('div', class_="q")
    joke = quote[random.randint(0,len(quote)-1)].find('div', class_="quote" ).text   
    return joke
  except:
    return "Упс, при парсинге странице произошла ошибка =("