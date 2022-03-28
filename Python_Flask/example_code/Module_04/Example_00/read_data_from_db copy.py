import sqlite3
con = sqlite3.connect('myweb.db')
cur = con.cursor()
# querydata = cur.execute('SELECT * FROM user ORDER BY id')
querydata = cur.execute('SELECT * FROM user WHERE `email`="benctw@gmail.com"')
results = cur.fetchall()
if results:
    print(results[0])
else:
    print('ng')

# for row in querydata:
#     print(row)
con.close
