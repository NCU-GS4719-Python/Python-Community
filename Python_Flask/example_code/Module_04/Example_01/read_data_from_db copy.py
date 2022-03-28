import sqlite3
con = sqlite3.connect('mywebsite.db')
cur = con.cursor()
# querydata = cur.execute('SELECT * FROM user ORDER BY id')
querydata = cur.execute('SELECT * FROM user WHERE `email`="benctw2@gmail.com"')
results = cur.fetchall()
if results:
    print('ok')

# for row in querydata:
#     print(row)
con.close
