import urllib.request as request ,urllib.parse as parse
import sqlite3
import json
import time
import ssl
import sys

api_key = False

if api_key is False:
    serviceurl= "http://py4e-data.dr-chuck.net/geojson?"
else:
    serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"


scontext = None

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 : 
        print('Retrieved 200 locations, restart to retrieve more')
        break
    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",(memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    print('Resolving', address)
    url = serviceurl + parse.urlencode({"sensor":"false", "address": address})
    print('Retrieving', url)
    uh = request.urlopen(url, context=scontext)
    data = uh.read().decode()
    print ('Retrieved',len(data),'characters',data[:20].replace('\n',' '))
    count = count + 1
    try: 
        js = json.loads(str(data))
    except: 
        continue

    if ('status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS')) : 
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    cur.execute('''INSERT INTO Locations (address, geodata) VALUES ( ?, ? )''', ( memoryview(address.encode()),memoryview(data.encode()) ) )
    conn.commit() 
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can visualize it on a map.")