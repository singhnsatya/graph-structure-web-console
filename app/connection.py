# name, age, address, parent, birthdate, empid, id

import psycopg2
import json

class Crud:

	def __init__(self):
		try:
			self.conn = psycopg2.connect(
				"dbname='graph' host='localhost' user='postgres' password='graph'")
			self.conn.autocommit = True
			self.cursor = self.conn.cursor()
			data = self.cursor.execute("select exists(select * from company)")
			datac = self.cursor.fetchall()
			if datac[0][0]:
				self.cursor.execute("delete from company")

			print('connected')
		except:
			print('cannot connect')

	def getAll(self):
		try:
			fhandle = open('data', 'r')
			self.cursor.copy_from(fhandle, 'company', sep="|")
			self.conn.commit()
			self.cursor.execute("SELECT * from company")
			rows = self.cursor.fetchall()
			for rs in rows:
				print(rs)
		except Exception as e:
			print('not executed', e)

# given a node, get the subtree under it.

	def subTree(self):	
		query = """with recursive subs as ( select empid, parent, name, age, joining 
		from company where empid = 1 union select
		e.empid, e.parent, e.name, e.age, e.joining
		from company e inner join subs s on s.empid = e.parent )
		select * from subs;"""
		self.cursor.execute(query)
		subtree = self.cursor.fetchall()
		for sub in subtree:
			print(sub)


crud = Crud()
crud.getAll()
crud.subTree()