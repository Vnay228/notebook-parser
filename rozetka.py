from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool


def pars_max_roz(roz):
	rootRoz = 'https://rozetka.com.ua/'
	soup_r = BeautifulSoup(roz.text, 'lxml')
	all_li_from_page = soup_r.find_all('li')

	links = []
	max_pages = []
	catalogs = '/notebooks/c80004/'

	for item in all_li_from_page:
		for link in item.find_all('a'):
			quq = link.get('href')
			links.append(quq)

	for item in links:
		if type(item) == type('1'):
			if rootRoz not in item:
				if '/notebooks/c80004/page=' in item:
					max_pages.append(item)
	# maximum pages
	return int(max_pages[-1][-3:-1])


def formation_rq_roz(root, domen, page, header=0, Proxy=0):
	if header == 0:
		Headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

		if Proxy != 0:
			return requests.get(root + domen + str(page), headers=Headers, proxies=Proxy)
		else:
			return requests.get(root + domen + str(page), headers=Headers)

	else:
		if Proxy != 0:
			return requests.get(root + domen + str(page), headers=header, proxies=Proxy)
		else:
			return requests.get(root + domen + str(page), headers=header)


def get_links_roz(namber=1):
	'''
	get all list in list of pages with smth namber( need one int parameter )
	'''
	links_form_roz = []
	namber_page = [i for i in range(1, namber+1)]
	print(namber_page[-1], namber)
	pool = Pool(processes=30)
	data = []
	data.extend(pool.map(pars_page_roz, namber_page))
	return data


def pars_page_roz(page):
	url = 'https://rozetka.com.ua/notebooks/c80004/'
	links_form_roz = []
	rq = formation_rq_roz(url, 'page=', page)
	soup = BeautifulSoup(rq.text, 'lxml')
	all_block = soup.find('div', class_='layout_with_sidebar')
	one_ul = all_block.find('ul')
	li_links = one_ul.find_all('li')
	links = []
	for item in li_links:
		flag = ''
		for link in item.find_all('a'):
			if len(links) != 0:
				flag = links[-1]
			quq = link.get('href')
			if flag == quq:
				continue
			if '/comments/' not in quq:
				links = []
				links_form_roz.append(quq)
			else:
				continue

	return links_form_roz
