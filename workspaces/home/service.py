# -*- coding: utf-8 -*-
import re

class ValidationInput:

    data = []
    
    def CheckStringIsNumeric(self, value: str):
        ''' Verifica se a string contém somente dados numéricos '''
        if (re.search(r'[^0-9]', value, re.M|re.I)):
            self.data.append('CEP deve conter somente números!')

    def CheckStringRange(self, value: str):
        ''' Verifica se os dígitos da string são maiores que 100000 e menores que 999999 '''
        value = re.sub(r'^0+', '', value)
        if ((re.match(r'\d{7,}', value, re.M|re.I)) or (int(value) < 100000)):
            self.data.append('CEP deve ser maior que 100000 e menor que 999999!')

    def CheckStringNotPair(self, value: str):
        ''' Verifica se a string contém digitos repetidos em pares '''
        if (re.search(r'(\d)(?=\d\1)', value)):
            self.data.append('CEP não deve ter dígitos repetidos em pares!')

    def CheckStringValue(self, value: str) -> dict:
        ''' Faz todas as verificações na string '''
        self.data = []
        self.CheckStringIsNumeric(value)
        if (len(self.data) <= 0):
            self.CheckStringRange(value)
            self.CheckStringNotPair(value)
        data = {
            'data': value, 
            'status': 200 if (len(self.data) == 0) else 401, 
            'errors': self.data
        }
        return data
