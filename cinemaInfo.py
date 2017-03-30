import mysql.connector
import requests
import lxml
from bs4 import BeautifulSoup
DBCONFIG = {
    'host': '106.14.26.144',
    'user': 'movie',
    'password': 'movie',
    'port':3306,
    'database': 'movie',
    'charset': 'utf8'
}

DEFAUT_TIME = 10

conn = mysql.connector.connect(**DBCONFIG)
cursor = conn.cursor()
def crawlCityCinema(cityCinemaDict):
    url = 'http://theater.mtime.com/' + cityCinemaDict['stringid'] + '/' + str(cityCinemaDict['cinemaid']) + '/info.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    }
    text = ''
    print("Crawling city cinema ...")
    try:
        print('Requesting url=', url)
        text = requests.get(url, headers=headers, timeout=DEFAUT_TIME).text
    except:
        print('Error when request url=', url)
        return None
    soup = BeautifulSoup(text, "lxml")
    print(soup)

def main():
    cursor.execute('select * from city')
    data1 = cursor.fetchall()
    cursor.execute('select * from cinema')
    data2 = cursor.fetchall()
    cityCinemaList = []
    for da1 in data1:
        for da2 in data2:
            cityCinemaDict = {'stringid': None,
                              'cinemaid': None}
            if da1[0] == da2[2]:
                cityCinemaDict['stringid'] = da1[2]
                cityCinemaDict['cinemaid'] = da2[0]
                cityCinemaList.append(cityCinemaDict)
    for da in cityCinemaList:
        print(da)
    crawlCityCinema(cityCinemaList[1])
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()