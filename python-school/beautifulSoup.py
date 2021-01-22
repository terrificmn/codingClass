import requests, re, os
from bs4 import BeautifulSoup as bs
import urllib.request as ur

'''
url = "https://quotes.toscrape.com/"
html = ur.urlopen(url)

#html tag를 읽어온다 
#print(html)
#print(html.read()[:100])

#BeautifulSoup 
# <tag>정보만 읽어 온다 
#soup = bs(html.read(), 'html.parser')
soup = bs(html.read(), 'html.parser')
#print(soup)

quote = soup.find_all('span')
#quote에 들어온 태그 리스트에서 0번째를 출력 .text 는 text만 보여준다
#print(quote[0].text)

#반복문으로 quote로 만들어진 클래스 다 받아온다
#for i in quote:
#    print(i.text)

#'div'를 찾고 class명도 찾아온다
#t = soup.find_all('div', {"class":"quote"})

#t = soup.find_all('div', {"class":"quote"})[0].text
#print(t)

#반복문 실행하기
for i in soup.find_all('div', {"class":"quote"}):
    print(i.text)

'''

#다음에서 뉴스 크롤링하기
url = "https://news.daum.net/"
html = ur.urlopen(url)


