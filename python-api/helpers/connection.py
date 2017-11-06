from flask import Flask, jsonify, request
import psycopg2
import json

def connectDB():
	try:
		db = json.load(open('config/db.json'))
		db = db['local']
		dbString = ("dbname='{0}' host='{1}' user='{2}' password='{3}'".
		format(db['dbname'], db['host'], db['user'], db['password']))
		return psycopg2.connect(dbString)
	except:
		print('cannot connect')