# -*- coding: utf-8 -*-

from flask import Flask, flash, request, redirect, render_template, url_for

from flask.ext.pymongo import PyMongo
from flask_wtf.csrf import CsrfProtect

from forms import SeriesForm


app = Flask(__name__)
CsrfProtect(app)
app.config.from_object('configs')
mongo = PyMongo(app)


@app.route("/")
def index():
    series = mongo.db.series.find()
    return render_template("index.html", series=series)


@app.route("/series/add/", methods=['GET', 'POST'])
def add():
    form = SeriesForm()
    if request.method == 'POST':
        if form.validate():
            mongo.db.series.insert(form.data)
            flash(u'Yes! Você acaba de adicionar mais um seriado à lista!', 'success')
            return redirect(url_for('index'))
        else:
            flash(u'Oops! Não foi possível adicionar o seriado! :(', 'error')
    return render_template("add.html", form=form)


@app.route("/series/<ObjectId:serie_id>/edit/", methods=['GET', 'POST'])
def edit(serie_id):
    serie = mongo.db.series.find_one({'_id': serie_id})
    form = SeriesForm(**serie)
    if request.method == 'POST':
        if form.validate():
            serie.update(form.data)
            mongo.db.series.save(serie)
            flash(u'Yes! O seriado foi editado com sucesso!', 'success')
            return redirect(url_for('index'))
        else:
            flash(u'Oops! Não foi possível editar esse seriado! :(', 'error')
    return render_template("edit.html", form=form, serie_id=serie_id)


@app.route("/series/<ObjectId:serie_id>/delete/", methods=['POST'])
def delete(serie_id):
    mongo.db.series.remove({'_id': serie_id})
    flash(u'Yes! O seriado foi excluído com sucesso!', 'success')
    return redirect(url_for('index'))


@app.route("/series/<ObjectId:serie_id>/rating/<rating>/", methods=['GET'])
def rating(serie_id, rating):
    serie = mongo.db.series.find_one({'_id': serie_id})
    serie['rating'] = rating
    mongo.db.series.save(serie)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
