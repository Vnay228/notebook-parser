import requests
from bs4 import BeautifulSoup
from multiprocessing import pool


def appdate_proxy_list():
	http = 'https://free-proxy-list.net/'
	data_infor = {}
	flag = ''
	rq = requests.get(http)
	soup = BeautifulSoup(rq.text, 'lxml')
	data = soup.find('tbody').find_all('tr')
	for item in data:
		for index, element in enumerate(item.find_all('td')):
			if (index+1) % 8 == 1:
				flag = 'http://' + element.text
			elif (index+1) % 8 == 2:
				flag += ':' + element.text
			elif (index+1) % 8 == 7:
				if element.text == 'yes':
					data_infor.update({'http': flag})

	return data_infor
