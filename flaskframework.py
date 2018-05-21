from flask import Flask, request, render_template 
import os
import datetime

app  = Flask(__name__)

@app.route("/")
def say_hi(): 
    return render_template("index.html")
    
@app.route("/search")
def do_search(): 
    return "Search Page"

# @app.route("/Photos")
# def photo_page(): 
#     return "<h1>This is the photo page<h1>"
    
@app.route("/Photos/<id>")
def show_photo(id): 
    return "<h1>This is photo {0}</h1>".format(id)
    
@app.route("/Cars/<car>/Image/<num>")
def show_car(car,num): 
    return "<h2>You got it! {1}<h2>".format(num,car)

@app.route("/Time")
def show_time(): 
    timing = datetime.datetime.now()
    time = timing.strftime("%H:%M:%S")
    return "The time is " + time
    # Can also be written as return timing.strftime("%H:%M:%S")

if __name__ == "__main__": 
        app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv('PORT', 8080)), debug=True)