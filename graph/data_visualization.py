import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import json

# Create Dash application
app = dash.Dash(__name__)

# Sample data for the pie chart
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 30, 40]
}

# Function to convert data to JSON format
def get_json_data():
    return json.dumps(data)

# Create a pie chart using Plotly Express
def create_pie_chart(data_dict):
    fig = px.pie(data_dict, names="Category", values="Values", title="Pie Chart Example")
    return fig

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Dash App with Plotly Pie Chart and JSON Input"),
    
    # Dropdown for pie chart categories
    html.Label("Select Category to Display:"),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': i, 'value': i} for i in data["Category"]],
        value='A'
    ),

    # Pie chart display
    dcc.Graph(id='pie-chart'),

    # JSON input and output areas
    html.Label("Modify Data (JSON Format):"),
    dcc.Textarea(
        id='json-input',
        value=get_json_data(),
        style={'width': '100%', 'height': 200}
    ),

    html.Div(id='json-output', style={'whiteSpace': 'pre-line'})
])

# Define callbacks for interactivity

# Callback to update pie chart based on dropdown selection and JSON input
@app.callback(
    Output('pie-chart', 'figure'),
    [Input('category-dropdown', 'value'),
     Input('json-input', 'value')]
)
def update_pie_chart(selected_category, json_data):
    # Parse the JSON data
    try:
        data_dict = json.loads(json_data)
    except json.JSONDecodeError:
        data_dict = data  # Fallback to default data if JSON is invalid
    
    fig = create_pie_chart(data_dict)
    return fig

# Callback to display current JSON data
@app.callback(
    Output('json-output', 'children'),
    [Input('json-input', 'value')]
)
def display_json(json_data):
    return json_data

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

