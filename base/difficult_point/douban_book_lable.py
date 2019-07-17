#!/usr/bin/env python3

import requests
u = "https://book.douban.com/tag/%E6%BC%AB%E7%94%BB"
r = requests.get(url=u)

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'lxml')

lis = soup.find('ul', class_="subject-list").find_all('li')
lil = lis[0]
dic = {}
dic['Name'] = li1.h2.text.replace(' ', '').replace('\n', '')
dic['Other'] = li1.find('div', class_="pub").text.replace()
dic['point'] = li1.find('span', class_='rating')
