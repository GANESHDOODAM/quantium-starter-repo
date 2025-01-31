import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load your data
df = pd.read_csv('/Users/ganeshdoodam/PycharmProjects/quantium-starter-repo/data/formatted_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Sales Data Visualization"),

    # Region filter radio button
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',  # Default value
        labelStyle={'display': 'block'}
    ),

    # Line chart for sales data
    dcc.Graph(id='sales-line-chart')
])


# Define callback to update the chart based on region filter
@app.callback(
    Output('sales-line-chart', 'figure'),
    [Input('region-filter', 'value')]
)
def update_chart(selected_region):
    # Filter the DataFrame based on region
    if selected_region != 'all':
        filtered_df = df[df['region'] == selected_region]
    else:
        filtered_df = df  # Show all data if 'all' is selected

    # Create the line chart
    fig = px.line(filtered_df, x='date', y='sales', title='Sales Over Time')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

