from dash import dcc, Dash, html
import pandas as pd
import numpy as np
import plotly.express as px

app = Dash(__name__)

df = pd.DataFrame({
    'Fruit' : np.array(['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas']),
    'Amount' : np.array([4, 5, 9, 6, 3, 1]),
    'City' : np.array(['San Fransisco', 'San Fransisco', 'San Fransisco', 'New York', 'New York', 'New York'])
})

df
fig = px.bar(df, x = 'Fruit', y = 'Amount', color = 'City', barmode = 'group')

app.layout = html.Div(children = [
    html.H1('Dash'),
    html.Div('Dash : An interactive plottig tutorial'),
    dcc.Graph(id = 'graph', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug = True)
