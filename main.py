#!/usr/bin/python
import calendar
monthFirst = 6
dayFirst = 21
monthLast = 9 + 1
dayLast = 22
year = 2018

import urllib2
from bs4 import BeautifulSoup

data = []

for i in range(monthFirst, monthLast): 
	if (i == monthLast): 
		days = dayLast
	else:
		days = calendar.monthrange(year,i)[1] + 1
	if (i == monthFirst):
		first = dayFirst
	else:
		first = 1
	for j in range(first, days): 
		quote_page = 'http://aa.usno.navy.mil/rstt/onedaytable?ID=AA&year=' + format(year) +'&month='+ format(i) +'&day=' + format(j) + '&state=MN&place=Minneapolis'
		page = urllib2.urlopen(quote_page)
		soup = BeautifulSoup(page, 'html.parser')
		tag = soup.findAll('td')
		CT = tag[3].text
		SR = tag[5].text
		ST = tag[7].text
		SS = tag[9].text
		ECT = tag[11].text
		date = soup.find('td', attrs={'class':'tdAleft'}).text
		data.append((date,CT,SR,ST,SS,ECT))

import csv
from datetime import datetime

with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow(['date','Civil Twilight','Sunrise','Sun transit','Sunset','End civil twilight'])
 for date,CT,SR,ST,SS,ECT in data:
 	writer.writerow([date,CT,SR,ST,SS,ECT])
