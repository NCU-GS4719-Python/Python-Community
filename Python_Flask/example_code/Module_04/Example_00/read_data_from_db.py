import sqlite3, datetime
con = sqlite3.connect('myweb.db')
cur = con.cursor()
# sql=f'SELECT * FROM user ORDER BY id where julianday(`modify_datetime`)-julianday(now)>60'
sql=f'select julianday("{datetime.datetime.utcnow()}")-julianday(`modify_datetime`) from user'
print(sql)
querydata = cur.execute(sql)
for row in querydata:
    print(row)
con.close
