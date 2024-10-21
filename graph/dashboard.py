import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Sample Data (just load the whole dataset)
data = [
    {
        "State": "Delaware",
        "Total": 993635,
        "NonHispanic": 894939,
        "Hispanic": 98696,
        "WhiteTotal": 634244,
        "BlackTotal": 218266,
        "OtherTotal": 96881,
        "TwoOrMoreTotal": 64130
    },
    {
        "State": "District of Columbia",
        "Total": 670587,
        "NonHispanic": 593419,
        "Hispanic": 77168,
        "WhiteTotal": 265633,
        "BlackTotal": 297101,
        "OtherTotal": 78157,
        "TwoOrMoreTotal": 47278
    },
    {
        "State": "Florida",
        "Total": 21634500,
        "NonHispanic": 15896200,
        "Hispanic": 5738280,
        "WhiteTotal": 13807400,
        "BlackTotal": 3355707,
        "OtherTotal": 3789025,
        "TwoOrMoreTotal": 2743468
    },
    {
        "State": "Georgia",
        "Total": 10722300,
        "NonHispanic": 9643870,
        "Hispanic": 1078460,
        "WhiteTotal": 5820024,
        "BlackTotal": 3373953,
        "OtherTotal": 1017540,
        "TwoOrMoreTotal": 638881
    }
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create the Dash App
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Demographic Dashboard'),

    # Total Population per State (Bar Chart)
    dcc.Graph(
        id='total-population',
        figure={
            'data': [
                go.Bar(
                    x=df['State'],
                    y=df['Total'],
                    name='Total Population'
                )
            ],
            'layout': go.Layout(
                title='Total Population per State',
                xaxis={'title': 'State'},
                yaxis={'title': 'Population'}
            )
        }
    ),

    # Hispanic vs Non-Hispanic Population (Pie Chart)
    dcc.Graph(
        id='hispanic-non-hispanic',
        figure={
            'data': [
                go.Pie(
                    labels=['Hispanic', 'Non-Hispanic'],
                    values=[df['Hispanic'].sum(), df['NonHispanic'].sum()],
                    hole=.3
                )
            ],
            'layout': go.Layout(
                title='Hispanic vs Non-Hispanic Population'
            )
        }
    ),

    # White and Black Population Comparison (Bar Chart)
    dcc.Graph(
        id='white-black-population',
        figure={
            'data': [
                go.Bar(
                    x=df['State'],
                    y=df['WhiteTotal'],
                    name='White Population'
                ),
                go.Bar(
                    x=df['State'],
                    y=df['BlackTotal'],
                    name='Black Population'
                )
            ],
            'layout': go.Layout(
                title='White and Black Population Comparison',
                barmode='group',
                xaxis={'title': 'State'},
                yaxis={'title': 'Population'}
            )
        }
    ),

    # Two or More Races Population (Pie Chart)
    dcc.Graph(
        id='two-or-more-races',
        figure={
            'data': [
                go.Pie(
                    labels=df['State'],
                    values=df['TwoOrMoreTotal'],
                    hole=.3
                )
            ],
            'layout': go.Layout(
                title='Two or More Races Population Distribution'
            )
        }
    ),

    # Population Breakdown by Race (Stacked Bar Chart)
    dcc.Graph(
        id='population-breakdown',
        figure={
            'data': [
                go.Bar(
                    x=df['State'],
                    y=df['WhiteTotal'],
                    name='White Population'
                ),
                go.Bar(
                    x=df['State'],
                    y=df['BlackTotal'],
                    name='Black Population'
                ),
                go.Bar(
                    x=df['State'],
                    y=df['OtherTotal'],
                    name='Other Population'
                ),
                go.Bar(
                    x=df['State'],
                    y=df['TwoOrMoreTotal'],
                    name='Two or More Races'
                )
            ],
            'layout': go.Layout(
                title='Population Breakdown by Race',
                barmode='stack',
                xaxis={'title': 'State'},
                yaxis={'title': 'Population'}
            )
        }
    ),

    # Breakdown of Other Races (Bar Chart)
    dcc.Graph(
        id='other-races',
        figure={
            'data': [
                go.Bar(
                    x=df['State'],
                    y=df['OtherTotal'],
                    name='Other Population'
                )
            ],
            'layout': go.Layout(
                title='Other Races Population',
                xaxis={'title': 'State'},
                yaxis={'title': 'Population'}
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
