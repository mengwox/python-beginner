from beginner.db.db_handler import DbConn

# 不能这样写, 这样过了当前行后, DbConn()就被GC掉了
# cur = DbConn().get_cursor()
conn = DbConn()
cur = conn.get_cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

# Code: http://www.py4e.com/code3/db1.py
