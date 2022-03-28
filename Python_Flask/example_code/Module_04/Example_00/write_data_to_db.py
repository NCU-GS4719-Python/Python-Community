import sqlite3, datetime, time
t1 = time.time()
con = sqlite3.connect('myweb.db')
cur = con.cursor()
# Insert a row of data
# for _ in range(1000):
cur.execute(f"INSERT INTO user (`name`, `email`, `password`, `modify_datetime`) VALUES ('John','john@gmail.com','333333', '{datetime.datetime.utcnow()}')")
con.commit()
# cur.execute("INSERT INTO user (`name`, `email`, `password`) VALUES ('John2','john@gmail.com','333333')")
# Save (commit) the changes

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
t2 = time.time()
print(t2-t1)