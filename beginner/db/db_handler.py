import sqlite3
from sqlite3 import Connection, Cursor

from beginner.db.db_const import DB_FILE


class DbConn:
	"""
	sqlite连接器
	"""
	conn: Connection

	def __init__(self) -> None:
		"""
		初始创建数据库连接对象,并赋值给conn
		"""
		self.conn = sqlite3.connect(DB_FILE)
		print('db connection prepared')

	def __del__(self) -> None:
		"""
		对象销毁时,自动关闭数据库连接
		"""
		if self.conn is not None:
			self.conn.close()
			print('db connection destroyed')

	def get_cursor(self) -> Cursor:
		"""
		通过数据库连接对象, 获取操作游标
		:return: 游标
		"""
		if self.conn is None:
			self.__init__()
		return self.conn.cursor()
