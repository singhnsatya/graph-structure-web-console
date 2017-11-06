from flask import Flask, jsonify, request
import psycopg2
import json

def connectDB():
	try:
		print('Database Connected')
		return psycopg2.connect(
		"dbname='graph' host='localhost' user='postgres' password='graph'")
	except:
		print('cannot connect')