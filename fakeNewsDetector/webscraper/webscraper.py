import requests
import bs4


def headlinescraper(url):
    # if not url.startswith('https://') or not url.startswith('http://'):
    #     url = 'https://{}'.format(url)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    headline = soup.select('h1')
    return headline[0].getText()
