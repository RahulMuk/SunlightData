#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

data = []

for i in range(1, 15): 
	quote_page = 'http://aa.usno.navy.mil/rstt/onedaytable?ID=AA&year=2018&month=7&day=' + format(i) + '&state=MN&place=Minneapolis'
	page = urllib2.urlopen(quote_page)
	soup = BeautifulSoup(page, 'html.parser')
	tag = soup.findAll('td')
	time = tag[3].text
	date = soup.find('td', attrs={'class':'tdAleft'}).text
	data.append((time, date))

import csv
from datetime import datetime

with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow(['time', 'date'])
 for time, date in data:
 	writer.writerow([time, date])
