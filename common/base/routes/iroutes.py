# -*- coding: utf-8 -*-
from flask.views import MethodView
from flask_restplus import reqparse

from common.helpers.operationResults import OperationResults

"""
    Class that manage categories table by restfull api
    * class      RouteCategories
    * requires   python 3.+
    * version    1.0.0
    * package    iCity
    * subpackage iCity/Admin
    * author     Alcindo Schleder <alcindoschleder@gmail.com>
    * copyright  Vocatio Telecom <https://www.vocatiotelecom.com.br>
""" 

class InterfaceRoutes(MethodView, OperationResults):

    PAGE = reqparse.RequestParser()
    PAGE.add_argument('start', type=int, default=1, help='Página inicial da lista')
    PAGE.add_argument(
        'limit', 
        type=int, 
        default=20, 
        help='Registros por paǵina', 
        choices=[0, 10, 20, 30, 40, 50]
    )

    def __init__(self, *args, **kwargs):
        super(InterfaceRoutes, self).__init__(args, kwargs)
        self.result['page'] = {
            'count': 0,
            'start': 0,
            'limit': 0,
            'url': '/'
        }
        self.db = None

    def get(self):
        raise NotImplementedError()
    