from flask import Flask, jsonify, request
import psycopg2
import json

app = Flask(__name__)

def connectDB():
	try:
		return psycopg2.connect(
		"dbname='graph' host='localhost' user='postgres' password='graph'")
	except:
		print('cannot connect')

@app.route('/')
def index():
	return 'INDEX'

@app.route('/insertData', methods=['GET'])
def test():
	try:
		conn = connectDB()
		cursor = conn.cursor()
		fhandle = open('data', 'r')
		cursor.copy_from(fhandle, 'company', sep="|")
		conn.commit()
		return jsonify({'success': True})
	except Exception as e:
		return jsonify({"success": False, "error": "Data insertion failed"})

@app.route('/addEmployee', methods=['POST'])
def addEmp():
	try:
		conn = connectDB()
		cursor = conn.cursor()
		cursor.execute("""insert into company (name, age, joining, address, parent) values (%s, %s, %s, %s, %s);""", 
		(request.json['name'], request.json['age'], request.json['joining'], request.json['address'], request.json['parent']))
		conn.commit()
		return jsonify({"success": True})
	except Exception as e:
		return jsonify({"success": False, "error": "Invalid data"})

@app.route('/subtree', methods=['get'])
def subtree():
	try:
		conn = connectDB()
		cursor = conn.cursor()
		query = """with recursive subs as ( select empid, parent, name, age, joining 
		from company where empid = 1 union select
		e.empid, e.parent, e.name, e.age, e.joining
		from company e inner join subs s on s.empid = e.parent )
		select * from subs;"""
		cursor.execute(query)
		subtree = cursor.fetchall()
		for sub in subtree:
			print(sub)
	
		return jsonify({'success': True})
	except Exception as e:
		raise e


if __name__ == '__main__':
	connectDB()
	app.run(debug=True)