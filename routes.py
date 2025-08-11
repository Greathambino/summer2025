from flask import Flask, request
from flask import render_template
import os, requests
import controller

app = Flask(__name__)

@app.route("/")
def hello_world(name=None):
    return render_template('index.html', person=name)

@app.route("/weather-app")
def weather_app():
    return render_template('weather.html')

@app.route("/weather-history")
def weather_history():
    controller.history_controller()

# @app.route("/entirely different project")
# def different_project():
#     return render_template('someProject.html')

@app.route("/weather-data")
def weather_data():
    cityName = request.args.get('cityName')
    return controller.weather_data_controller(cityName)

 #http://localhost:5000/weather-data?cityName=%27torrance%27
 # http://127.0.0.1:5000/weather-data?cityName=Torrance

 