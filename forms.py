# -*- coding: utf-8 -*-

from flask_wtf import Form
from wtforms import TextField, TextAreaField, validators

RequiredBR = validators.Required(message=u'Esse Campo é Obrigatório')

class SeriesForm(Form):
    name = TextField('Name', validators=[RequiredBR])
    description = TextAreaField('Description', validators=[RequiredBR])
    image = TextField('Image URL')
