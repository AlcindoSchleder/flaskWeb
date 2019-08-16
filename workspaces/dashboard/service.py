# -*- coding: utf-8 -*-
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
from common.helpers.operationResults import OperationResults

class CreateCharts(OperationResults):
    
    # def __init__(self):
    #     super(CreateCharts, self).__init__(None, None)

    def create_BarChart(self):
        N = 40
        x = np.linspace(0, 1, N)
        y = np.random.randn(N)
        df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe

        data = [
            go.Bar(
                x=df['x'], # assign x as the dataframe column 'x'
                y=df['y']
            )
        ]

        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

        return graphJSON

Plot = CreateCharts()
