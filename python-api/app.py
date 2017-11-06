from helpers.server import app
from helpers.connection import connectDB

if __name__ == '__main__':
	connectDB()
	app.run(debug=True)