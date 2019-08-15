# -*- coding: utf-8 -*-
from flask_restplus import fields

"""
    Classes that Define a serializer model
    * requires   python 3.+, PyQt5
    * version    1.0.0
    * package    icity_api
    * subpackage icity_api
    * author     Alcindo Schleder <alcindoschleder@gmail.com>
    * copyright  Vocatio Telecom <https://www.vocatiotelecom.com.br>
"""
class ModelBase:

    MODEL_FIELDS = {
        "start": fields.Integer(),
        "limit": fields.Integer(),
        "next": fields.String(),
        "prev": fields.String()
    }

    def getModel(self, api) -> object:
        ''' Retorna um objeto Model '''
        return api.model('ModelBase', self.MODEL_FIELDS)

    def fillData(self, url: str, start: int, limit: int, count: int) -> dict:
        ''' Retorna a paginação dos registros '''
        start = start
        limit = limit
        count = count
        if count > start and limit > 0:
            # make response
            self.MODEL_FIELDS['start'] = start
            self.MODEL_FIELDS['limit'] = limit
            self.MODEL_FIELDS['count'] = count
            # make URLs
            # make previous url
            if start == 1:
                self.MODEL_FIELDS['prev'] = ''
            else:
                start_copy = max(1, start - limit)
                limit_copy = start - 1
                self.MODEL_FIELDS['prev'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
            # make next url
            if start + limit > count:
                self.MODEL_FIELDS['next'] = ''
            else:
                start_copy = start + limit
                self.MODEL_FIELDS['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
        return self.MODEL_FIELDS
