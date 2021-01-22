import requests, re, os
from bs4 import BeautifulSoup as bs
import urllib.request as ur 

#경로 바꾸기
os.chdir(r'C:\Users\5-20\projects\python-school')
#url 정보
url = "https://news.daum.net/"
html = ur.urlopen(url)

'''
soup = bs(html.read(), 'html.parser')
#div tag의 cont_thumb라는 클래스 tag만 받아오기
title = soup.find_all('div', {"class":"cont_thumb"})
print(title)
'''
soup = bs(html.read(), 'html.parser')
link = soup.find_all('a')
#print(link)

