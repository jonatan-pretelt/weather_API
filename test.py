import requests
import json

r = requests.get('https://api.weather.gov/points/28.1946971,-82.3459212')

params = r.json()

location = params['properties']['forecast']
# print(location)
def jprint(obj):
	text = json.dumps(obj,sort_keys=True, indent=4)
	print(text)

#print(jprint(r.json()))


forecast = requests.get('https://api.weather.gov/gridpoints/TOP/31,80/forecast')
# print(forecast.json()['properties']['periods'])
# print('\n')

for item in forecast.json()['properties']['periods']:
	print(item,'\n')