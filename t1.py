import requests
import lxml
from bs4 import BeautifulSoup

def crawlCityCinema():
    url = 'http://theater.mtime.com/China_Fujian_Province_Fuqing/6124/info.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    }
    text = ''
    print("Crawling city cinema ...")
    try:
        print('Requesting url=', url)
        text = requests.get(url, headers=headers, timeout=20).text
    except Exception as e:
        print('Error when request url=', url)
        print(e)
        return None
    soup = BeautifulSoup(text, "lxml")
    cinemaInner = soup.find('table', class_='lovetable').find_all('p')
    cinemacinemaPhoneTimeAdd = soup.find('div', class_='ci_title').find_all('p')
    cimenaRequept = soup.find('div', class_='ci_mon').find_all('p')
    #print(cinemaInner[0].get_text().split()[0])
    #print(cinemaInner[1].get_text().split()[0])
    #print(cinemacinemaPhoneTimeAdd[1].get_text())
    #print(cinemacinemaPhoneTimeAdd)
    for p in cimenaRequept:
        if p.find('b').get_text() == '可停车：':
            print(p.find('span').get_text().rstrip().lstrip())
    #print(cimenaRequept)
    #print(cinemacinemaPhoneTimeAdd[1].get_text().split())
    #print(cinemaInner[0].get_text()[-2:])
crawlCityCinema()