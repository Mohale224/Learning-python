import dash
import dash_core_components as dcc
import dash_html_components as html

# Create a Dash Application
app = dash.Dash(__name__)

# Define the layout of the Dashboard
app.layout = html.Div(
    children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            id="My Graph",
            figure={
                'data': [  # Corrected from 'Data' to 'data'
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Bar chart'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': 'Line chart'}
                ],
                'layout': {  # Corrected from 'Layout' to 'layout'
                    'title': 'My chart',
                    'xaxis': {'title': 'x-axis'},
                    'yaxis': {'title': 'y-axis'}
                }
            }
        )
    ]
)

# Run the Dash Application
if __name__ == '__main__':
    app.run_server(debug=True)
