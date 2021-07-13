import requests
import json
from bs4 import BeautifulSoup

from modules import rozetka
from modules import foxtrot
from modules import eldorado
from modules import comfy
from proxy import get_proxy
from random import choice
from pprintpp import pprint
from multiprocessing import Pool

# URL_notebook_com = 'https://comfy.ua/ua/notebook/'
# URL_notebook_fox = 'https://www.foxtrot.com.ua/uk/shop/noutbuki.html'
# URL_notebook_eld = 'https://eldorado.ua/notebooks/c1039096/'
# URL_notebook = 'https://rozetka.com.ua/notebooks/c80004/'


def rozetka_proces(hed, prox):
	roz = rozetka.formation_rq_roz('https://rozetka.com.ua/notebooks/c80004/', 'page=', 1, hed, prox)
	max_roz = rozetka.pars_max_roz(roz)
	links_from_roz = rozetka.get_links_roz(max_roz)


def foxtrot_proces(hed, prox):
	fox = foxtrot.formation_rq_fox('https://www.foxtrot.com.ua/uk/shop/noutbuki.html', '?page=', 1, hed, prox)


def main():
	print('! Appdating proxy.....')
	proxy = get_proxy.appdate_proxy_list()
	print(proxy)
	print('! Reading user-agents.....')
	user_agent_data = []
	with open('User_Agents.txt', 'r') as user_agents:
		agents = user_agents.read().split('\n')
		for agent in agents:
			user_agent_data.append({'User-Agent': agent})

	# parsing rozetka
	print('! Parsing rozetka.....')
	# rozetka_proces(choice(user_agent_data), proxy)
	#
	print('! Parsing foxtrot.....')
	foxtrot_proces(choice(user_agent_data), proxy)


if __name__ == '__main__':
	main()
