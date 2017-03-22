import requests
import json
from datetime import datetime, timedelta
import re
import mysql.connector

DBCONFIG = {
    'host': '115.28.48.229',
    'user': 'root',
    'password': 'cnscarb',
    'port':3306,
    'database': 'movie',
    'charset': 'utf8'
}
conn = mysql.connector.connect(**DBCONFIG)
cursor = conn.cursor()

def str2date(str):
    '''
    将 yyyy-m-d 的字符串转换成 yyyymmdd
    比如将 2017-3-3 转换成 20170303
    :param str: 待转换字符串
    :return: 转换好的字符串
    '''
    r = re.match(r'^(\d{4})-(\d{1,2})-(\d{1,2})', str)
    text = r.group(1)
    for i in [2, 3]:
        if r.group(i).__len__() == 1:
            text = text + '0' + r.group(i)
        else:
            text = text + r.group(i)
    return text

def crawCinema(i):
    url = 'http://www.cbooo.cn/Screen/getScreenData?days=' + str(i)
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
    current_Date = datetime.now() - timedelta(days=abs(i))
    print(current_Date.strftime('%Y-%m-%d'))
    test_json = json.loads(text)
    for js in test_json['data4']:
        print(js)
    cityMovieData = test_json['data2']
    for city in cityMovieData:
        for id in test_json['data3']:
            if city['cityname'] == id['name']:
                city['cityid'] = id['id']
        city['date'] = str2date(current_Date.strftime('%Y-%m-%d'))
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
def getCrawedMovieSceneDate():
    date1 = cursor.execute("select * from movie_scene")
    print((date1))
#for i in range(0,3):
    #crawCinema(i)
getCrawedMovieSceneDate()