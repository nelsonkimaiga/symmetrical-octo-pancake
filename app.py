from flask import Flask, render_template, request
import requests


app = Flask(__name__)


url = 'http://api.worldbank.org/v2/datacatalog?format=json'
response = requests.get(url)
data = response.json()
print(data)

@app.route('/worldbank')
def worldbank():
	return response.text