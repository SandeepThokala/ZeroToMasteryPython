import requests
from bs4 import BeautifulSoup
import pprint

new_page = 'news'
for i in range(3):
	res = requests.get('https://news.ycombinator.com/' + new_page)
	soup = BeautifulSoup(res.text, 'html.parser')
	links = soup.select('.storylink')
	votes = soup.select('.score')
	pages = soup.select('.morelink')
	l = []
	for ind, item in enumerate(links):
		try:
			if len(votes[ind]):
				if int(votes[ind].get_text().replace(' points',''))>99:
					l.append({'score': votes[ind].get_text(),'title': item.get_text(), 'link': item.get('href', None)})
		except IndexError:
			break

	new_page = pages[0].get('href')
pprint.pprint(sorted(l, key = lambda x: x['score'], reverse = True))
