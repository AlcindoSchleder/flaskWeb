# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp

class GetZipCode(FlaskForm):

    zip_code = StringField('zip_code', validators=[
        DataRequired(), 
        Regexp(r'[0-9]', message='CEP deve conter somente dígitos numéricos!'),
        Regexp(r'\d{7,}', message='CEP deve ser menor que 999999!'),
        Regexp(r'(\d)(?=\d\1)', message='CEP não pode conter dígitos repetidos em pares!')
    ])