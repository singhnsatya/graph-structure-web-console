const path = require('path');

const APP_DIR = path.resolve(__dirname, 'public');

module.exports = {
	entry: APP_DIR + '/src/main.js',
	output: {
		path: path.resolve(__dirname, 'build'),
		filename: 'bundle.js',
		publicPath: ''
	},
	devServer: {
		inline: true,
		port: 6030,
		contentBase: path.resolve(__dirname, 'public')
	},
	module: {
		loaders: [
			{
				test: /\.(js|jsx)$/,
				include: APP_DIR,
				loader: 'babel-loader'
			}
		]
	}
}