import requests
import json
from bs4 import BeautifulSoup
import re

def crawCinema():
    url = 'http://www.cbooo.cn/Screen/getScreenData?days=0'
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
    #soup = BeautifulSoup(text, 'lxml')
    test_json = json.loads(text)
    for js in test_json['data1']:
        print(js)
    for js in test_json['data2']:
        print(js)
    for js in test_json['data3']:
        print(js)
    for js in test_json['data4']:
        print(js)
    for js in test_json['data5']:
        print(js)
    for js in test_json['data6']:
        print(js)
    cityMovieData = test_json['data4']
    #for city in cityMovieData:
        #for id in test_json['data5']:
            #if city['cityname'] == id['name']:
                #city['cityid'] = id['cityid']
    for ci in cityMovieData:
        print(ci)
    #print(soup)
    #result = soup.find_all('script', type="text/javascript")
    #for res in result:
        #print(res ,'\n')
    #print(result[4])
    #list_t = re.findall(r'var cinemasJson = (.*);', result[4], re.S)
    #print(list_t)
    #test_json = json.load(result[4])
    #print(test_json)
crawCinema()
