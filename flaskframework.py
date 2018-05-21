from flask import Flask, request 
import os 

app  = Flask(__name__)





if __name__ -- "__main__": 
        app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv('PORT', 0000)))