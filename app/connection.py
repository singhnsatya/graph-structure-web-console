# name, age, address, parent, birthdate, empid, id

import psycopg2

class Crud:

	def __init__(self):
		try:
			self.conn = psycopg2.connect(
				"dbname='graph' host='localhost' user='postgres' password='graph'")
			self.conn.autocommit = True
			self.cursor = self.conn.cursor()
			print('connected')
		except:
			print('cannot connect')

	def test(self):
		try:
			fhandle = open('data', 'r')
			self.cursor.copy_from(fhandle, 'newstruct', sep="|")
			self.conn.commit()
			self.cursor.execute("""SELECT * from newstruct""")
			rows = self.cursor.fetchall()
			for rs in rows:
				print(rs)
		except Exception as e:
			print('not executed', e)


crud = Crud()
crud.test()