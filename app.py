from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	response = requests.get('https://api.weather.gov/points/28.1946971,-82.3459212')
	params = response.json()
	forecast_url = params['properties']['forecast']
	forecast = requests.get(forecast_url)
	data = forecast.json()['properties']['periods']
	return render_template('index.html', data=data)