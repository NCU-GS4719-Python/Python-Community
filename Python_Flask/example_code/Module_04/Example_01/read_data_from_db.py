import sqlite3
con = sqlite3.connect('mywebsite.db')
cur = con.cursor()
querydata = cur.execute('SELECT * FROM user ORDER BY id')
for row in querydata:
    print(row)
con.close
