def pars_elorado(eld):
	soup_e = BeautifulSoup(eld, 'lxml')
	data = soup_e.find_all('a')
	for i in data:
		try:
			if i.text == '1':
				max_page = int(data[data.index(i) + 8].text)
				break

			else:
				continue

		except Exception:
			continue

def get_links_eld(namber=1):
	pass
