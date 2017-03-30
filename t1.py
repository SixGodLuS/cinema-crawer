import requests
import lxml
from bs4 import BeautifulSoup

def crawlCityCinema():
    url = 'http://theater.mtime.com/China_Anhui_Province_Huangshan_Shexian/4579/info.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    }
    text = ''
    print("Crawling city cinema ...")
    try:
        print('Requesting url=', url)
        text = requests.get(url, headers=headers, timeout=10).text
    except Exception as e:
        print('Error when request url=', url)
        print(e)
        return None
    soup = BeautifulSoup(text, "lxml")
    result = soup.find_all('table', class_='lovetable')
    print(result[0])

crawlCityCinema()