# -*- coding: utf-8 -*-
from flask import render_template, redirect, flash, url_for, jsonify
from flask_restplus import Namespace
from server import icityServer
from workspaces.dashboard import BaseRoutes
from workspaces.dashboard.service import Plot

ns = Namespace(BaseRoutes.API_BASE_NAME, description='Gera uma pagina para dashboard')

@ns.route('/')
@ns.doc('Mostra página com um gráfico preparando para dashboard')
class DashRoutes(BaseRoutes):

    @ns.doc('Mostra os gráficos na página html')
    def get(self):
        self.resultStatusCode = 200
        BarChart = Plot.create_BarChart()
        return render_template('dashboard.html', plot=BarChart)
    
icityServer.icity_api.add_namespace(ns, path=BaseRoutes.PATH_API)

api_functions = DashRoutes.as_view(BaseRoutes.API_BASE_NAME)
icityServer.icity_app.add_url_rule(BaseRoutes.PATH_API, view_func=api_functions, methods=['GET'])
