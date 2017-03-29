import mysql.connector
DBCONFIG = {
    'host': '106.14.26.144',
    'user': 'movie',
    'password': 'movie',
    'port':3306,
    'database': 'movie',
    'charset': 'utf8'
}
conn = mysql.connector.connect(**DBCONFIG)
cursor = conn.cursor()
cursor.execute("select * from city")
data = cursor.fetchall()
flashList = []
for da in data:
    #print(da)
    flashDict = {'id' : None,
                 'stringid' : None}
    if da[4] == None :
        #print(da[2].split('_'))
        str = ''
        for i in range(0,len(da[2].split('_'))-1):
            str = str + da[2].split('_')[i] + '_'
        #print(str.rstrip('_'))
        flashDict['id'] = da[1]
        flashDict['stringid'] = str.rstrip('_')
        flashList.append(flashDict)
#for fl in flashList:
    #print(fl)
