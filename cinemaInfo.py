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
    cinemaInner = soup.find('table', class_='lovetable').find_all('b')
    cinemacinemaPhoneTimeAdd = soup.find('div', class_='ci_title').find_all('p')
    cimenaRequept = soup.find('div', class_='ci_mon').find_all('dd')
    try:
        cityCinemaDict['hallsum'] = cinemaInner[0].get_text().split()[0]
    except Exception as e:
        print(e)
        cityCinemaDict['hallsum'] = 'None'
    try:
        cityCinemaDict['sitsum'] = cinemaInner[1].get_text().split()[0]
    except Exception as e:
        print(e)
        cityCinemaDict['sitsum'] = 'None'
    try:
        cityCinemaDict['address'] = cinemacinemaPhoneTimeAdd[0].get_text().split()[1]
    except Exception as e:
        print(e)
        cityCinemaDict['address'] = 'None'
    try:
        cityCinemaDict['tel'] = cinemacinemaPhoneTimeAdd[1].get_text().split()[0].split('：', 1)[1]
    except Exception as e:
        print(e)
        cityCinemaDict['tel'] = 'None'
    try:
        cityCinemaDict['bussinesshour'] = cinemacinemaPhoneTimeAdd[1].get_text().split()[1].split('：',1)[1]
    except Exception as e:
        print(e)
        cityCinemaDict['bussinesshour'] = 'None'
    print(cityCinemaDict)
    return cityCinemaDict
    #print(soup)
def saveCinemainfoIntoDatabase(cityCinemaDict):
    print('save cinema # ', cityCinemaDict['name'],'into db')
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    conn.commit()
    try:
        cursor.execute('replace into cinema'
                           '(CinemaID, CityID, DistrictID, Name, HallSum, SitSum, Address, Tel, BussinessHour)'
                           'values (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                           [cityCinemaDict['cinemaid'], cityCinemaDict['cityid'], cityCinemaDict['districtid'],
                            cityCinemaDict['name'], cityCinemaDict['hallsum'], cityCinemaDict['sitsum'],
                            cityCinemaDict['address'], cityCinemaDict['tel'], cityCinemaDict['bussinesshour']])
    except Exception as e:
        print(e)
        return None
    cursor.execute('SET FOREIGN_KEY_CHECKS=1')
    conn.commit()

def main():
    cursor.execute('select * from city')
    data1 = cursor.fetchall()
    cursor.execute('select * from cinema')
    data2 = cursor.fetchall()
    cityCinemaList = []
    crawlCinemaList = []
    for da1 in data1:
        for da2 in data2:
            cityCinemaDict = {'cinemaid': None,
                              'stringid': None,
                              'cityid': None,
                              'districtid': None,
                              'name': None}
            if da1[0] == da2[2]:
                cityCinemaDict['stringid'] = da1[2]
                cityCinemaDict['cinemaid'] = da2[0]
                cityCinemaDict['cityid'] = da2[1]
                cityCinemaDict['districtid'] = da2[2]
                cityCinemaDict['name'] = da2[3]
                cityCinemaList.append(cityCinemaDict)
    for cityCinemaDict in cityCinemaList:
        crawlCinemaList.append(crawlCityCinema(cityCinemaDict))
    for cityCinemaDict in crawlCinemaList:
        saveCinemainfoIntoDatabase(cityCinemaDict)
        print(cityCinemaDict)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()