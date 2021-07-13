from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool


def pars_max_fox(fox):
    rootFox = 'https://www.foxtrot.com.ua/'
    soup_f = BeautifulSoup(fox.text, 'lxml')
    


def formation_rq_fox(root, domen, page, header=0, Proxy=0):
    if header == 0:
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        if Proxy != 0:
            return requests.get(root + domen + str(page), headers=Headers, proxies=Proxy)
        else:
            return requests.get(root + domen + str(page), headers=Headers)

    else:
        if Proxy != 0:
            return requests.get(root + domen + str(page), headers=header, proxies=Proxy)
        else:
            return requests.get(root + domen + str(page), headers=header)


def get_links_fox(namber=1):
    pass


def pars_page_fox(page):
    pass
