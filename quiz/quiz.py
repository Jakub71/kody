#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#  
from flask import Flask, g
from flask import render_template, request
from modele import *

app = Flask(__name__)

@app.before_request
def before_request():
    g.db = baza
    g.db.connect()
    
@app.after_request
def after_request(response):
    g.db.close()
    return response
    
@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/lista")
def lista():
    pytania = Pytanie.select()
    return render_template('lista.html', query = pytania)
    
@app.route("/quiz")
def quiz():
    pytania = Pytanie.select().join(Odpowiedz).distinct()
    return render_template('quiz.html', query = pytania)
    
@app.route("/klasa")
def klasa():
    return render_template('klasa.html')
    
if __name__ == '__main__':
    app.run(debug=True)
