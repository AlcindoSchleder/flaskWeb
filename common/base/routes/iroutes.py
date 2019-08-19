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

    def __init__(self, *args, **kwargs):
        super(InterfaceRoutes, self).__init__(args, kwargs)
        self.db = None

    def get(self):
        raise NotImplementedError()
    