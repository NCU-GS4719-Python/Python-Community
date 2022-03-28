import sqlite3
con = sqlite3.connect('myweb.db')
cur = con.cursor()
cur.execute('SELECT * FROM user ORDER BY id')
result = cur.fetchall()
for row in result:
    print(row)
con.close
