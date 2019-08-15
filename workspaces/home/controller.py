# -*- coding: utf-8 -*-
from flask import render_template, redirect, flash, url_for, jsonify
from flask_restplus import Namespace
from server import icityServer
from workspaces.home import BaseRoutes
from workspaces.home.model import GetZipCode
from workspaces.home.service import ValidationInput

ns = Namespace(BaseRoutes.API_BASE_NAME, description='Print Hello Word')

@ns.route('/')
@ns.route('/zipcode', methods=['POST'])
@ns.route('/zipcode/<zip_code>', methods=['GET'])
@ns.doc('Mostra página inicial e Valida a entrada de dados')
class HomeRoutes(BaseRoutes):

    @ns.doc('Mostra o formulário principal')
    def get(self, zip_code=None):
        self.resultStatusCode = 200
        if (zip_code is None):
            form = GetZipCode()
            return render_template('index.html', form=form)
        else:
            Val = ValidationInput()
            return jsonify(Val.CheckStringValue(zip_code))
    
    @ns.doc('Recebe e trata os dados do formulário')
    def post(self):
        self.resultStatusCode = 200
        form = GetZipCode()
        if (form.validate_on_submit()):
            return jsonify(data={
                'zip_code': form.zip_code,
                'locality': 'some local'
            })
        else:
            print('------------------> Entrada de dados do form não validada!!!')
        return jsonify(data={'error': form.errors})


icityServer.icity_api.add_namespace(ns, path=BaseRoutes.PATH_API)

api_functions = HomeRoutes.as_view(BaseRoutes.API_BASE_NAME)
icityServer.icity_app.add_url_rule('/', view_func=api_functions, methods=['GET'])
icityServer.icity_app.add_url_rule('/zipcode', view_func=api_functions, methods=['POST'])
icityServer.icity_app.add_url_rule('/zipcode/<zip_code>', view_func=api_functions, methods=['GET'])
