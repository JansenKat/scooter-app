from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import datetime as dt
import numpy as np
import random


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Resources/hawaii.sqlite"
db = SQLAlchemy(app)

@app.route("/")
def home():
    # list of links to other routes
    return render_template("index.html")

@app.route("/random")
def generate_scooter():
    # generate random # - display scooter ride
    return render_template("index.html")

@app.route("/difference")
def zipcode_vs_census():
    # 2 addresses same zipcode, diff census track, how the data differs
    return render_template("index.html")

@app.route("/<zipcode>")
def zip_stats():
    # % compaint, # rides in,m # rides out, max expense, min expense, avg, complaints, maps and other stats
    return render_template("index.html")

@app.route("/long")
def longest():
    # display longest ride distance/time
    return render_template("index.html")

@app.route("/nowhere")
def nowhere():
    # rides that go nowhere, some plots on this. where/when
    return render_template("index.html")

@app.route("/red_zone")
def red_zone():
    #  red zone zip code (10 worst neighbor hoods to leave scooter in)
    return render_template("index.html")

@app.route("/api/")
def api():
    # return json api based on parameters from url
    return render_template("index.html")

@app.route("/api_docs")
def api_docs():
    # Documentation for API
    return render_template("index.html")