from flask import Flask, request 
import os
import datetime

app  = Flask(__name__)

@app.route("/")
def say_hi(): 
    return "hi there"

@app.route("/Photos")
def photo_page(): 
    return "<h1>This is the photo page<h1>"

@app.route("/Time")
def show_time(): 
    timing = datetime.datetime.now()
    time = timing.strftime("%H:%M:%S")
    return "The time is " + time
    # Can also be written as return timing.strftime("%H:%M:%S")

if __name__ == "__main__": 
        app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv('PORT', 8080)), debug=True)


# 