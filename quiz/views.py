#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  views.py
#  
from flask import Flask
from flask import render_template, request
from flask import redirect, url_for, flash
from modele import *
from forms import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/lista")
def lista():
    pytania = Pytanie.select()
    return render_template('lista.html', query = pytania)

@app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        print(request.form)
        wynik = 0
        for pid, oid in request.form.items():
            if Odpowiedz().get(Odpowiedz.id == int(oid)).odpok:
                wynik += 1
        print("Poprawne:", wynik)
        flash('Poprawne odpowiedzi: {}'.format(wynik), 'info')
        return redirect(url_for('index'))
    
    pytania = Pytanie.select().join(Odpowiedz).distinct().order_by(Pytanie.id)
    return render_template('quiz.html', query = pytania)


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            if type(error) is list:
                error = error[0]
            flash("Błąd: {}. Pole: {}".format(
                error, 
                getattr(form, field).label.text))

@app.route("/dodaj", methods=['GET', 'POST'])
def dodaj():
    form = PytanieForm()
    form.kategoria.choices = [(k.id, k.kategoria) for k in Kategoria.select()]
    
    if form.validate_on_submit():
        print(form.data)
        p = Pytanie(pytanie=form.pytanie.data, kategoria=form.kategoria.data)
        p.save()
        for o in form.odpowiedzi.data:
            odp = Odpowiedz(odpowiedz=o['odpowiedz'], 
                            pytanie=p.id, 
                            odpok=int(o['odpok']))
            odp.save()
        return redirect(url_for('lista'))
    elif request.method == 'POST':
        flash_errors(form)
        
    return render_template('dodaj.html', form=form)
