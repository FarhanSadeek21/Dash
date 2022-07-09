from dash import Dash, dcc, html
import numpy as np
import pandas as pd
import plotly.express as px
from torch import Graph

app = Dash(__name__)

df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

app.layout = html.Div(children=[
    html.H1(children = 'Hello World'),
    html.Div(children = 'Hello World'),
    dcc.Graph(id = 'graph', figure = fig)
])

if __name__ == '__main__':
    app.run_server(debug = True)