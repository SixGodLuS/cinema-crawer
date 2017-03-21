import requests
import json
from bs4 import BeautifulSoup

def crawCinema():
    url = 'http://theater.mtime.com/China_Zhejiang_Province_Hangzhou/movie/195064/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    }  # headers这一段不需要改动
    text = ''
    try:
        print('Requesting url: ', url)
        text = requests.get(url, headers=headers, timeout=10).text
    except:
        print('Error when request url=', url)
        return None
    soup = BeautifulSoup(text, 'lxml')
    #test_json = json.load(soup)
    #print(test_json)
    #print(soup)
    result = soup.find_all('script', type="text/javascript")
    #for res in result:
        #print(res ,'\n')
    print(result[4])
    test_json = json.load(result[4])
    print(test_json)
crawCinema()
