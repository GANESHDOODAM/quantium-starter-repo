import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data (replace this with your actual sales data)
data = {
    'date': ['2021-01-01', '2021-01-02', '2021-01-15', '2021-01-16', '2021-01-20'],
    'sales': [150, 200, 250, 275, 300]
}

# Load data into a DataFrame
df = pd.DataFrame(data)

# Convert 'date' to datetime format
df['date'] = pd.to_datetime(df['date'])

# Sort by date
df = df.sort_values('date')

# Create a line chart using Plotly
fig = px.line(df, x='date', y='sales', title="Sales Before and After Pink Morsel Price Increase",
              labels={'date': 'Date', 'sales': 'Sales Amount'})

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div(children=[
    html.H1("Soul Foods Sales Visualizer"),
    dcc.Graph(id='sales-line-chart', figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
