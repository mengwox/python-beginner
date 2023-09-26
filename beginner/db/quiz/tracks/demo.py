import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()
cur.execute('select * from Album where title = ?', ('abc',))
print(cur.fetchone())
