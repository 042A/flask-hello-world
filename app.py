from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return "hello world"

    r = requests.get('https://a.4cdn.org/pol/catalog.json')
    r = r.json() 
    print ("Returning 4Chan Raw Cat Data")
    return r
