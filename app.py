import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np

# Creating the Dash App
app = dash.Dash(__name__)

server = app.server

# Layout of the app
app.layout = html.Div([
    dcc.Graph(figure=go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=7,
        mode="gauge+number+delta",
        title={'text': "Happiness"},
        delta={'reference': 5},
        gauge={'axis': {'range': [None, 10]},
               'steps': [
                   {'range': [0, 10], 'color': "lightgray"}]})))
])

# Run the app with explicit server and port
if __name__ == '__main__':
    app.run_server()