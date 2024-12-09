# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import io
import os

# Load SpaceX dataset
spacex_df = pd.read_csv('spacex_launch_dash.csv')

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "SpaceX Launch Dashboard"

# App layout
app.layout = html.Div([
    # Cover section with video
    html.Div(
        id='cover-section',
        style={
            'position': 'relative',
            'width': '100%',
            'height': '70vh',
            'overflow': 'hidden',
        },
        children=[
            html.Video(
                id='video-background',
                src='/assets/blackhole.mp4',
                autoPlay=True,
                loop=True,
                muted=True,
                controls=False,
                style={
                    'position': 'absolute',
                    'top': '0',
                    'left': '0',
                    'width': '100%',
                    'height': '100%',
                    'objectFit': 'cover'
                }
            ),
            html.Div(
                className="cover-content",
                style={
                    'position': 'absolute',
                    'top': '50%',
                    'left': '50%',
                    'transform': 'translate(-50%, -50%)',
                    'color': 'white',
                    'textAlign': 'center',
                    'zIndex': 10
                },
                children=[
                    html.H1("SpaceX Launch Records Dashboard", style={'fontSize': '3rem'}),
                    html.P("Explore SpaceX Launch Data and Statistics", style={'fontSize': '1.5rem'})
                ]
            )
        ]
    ),
    # Dashboard container with graphs and controls
    html.Div(
        className="dashboard-container",
        children=[
            # Dropdown to select launch sites
            html.Div(
                className="selector-container",
                children=[
                    html.Div(
                        className="box",
                        children=[
                            dcc.Dropdown(
                                id='site-dropdown',
                                options=[
                                    {'label': 'All Sites', 'value': 'ALL'},
                                    {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                    {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                    {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                    {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
                                ],
                                value='ALL',
                                placeholder="Select a Launch Site here",
                                searchable=True,
                                style={'width': '100%'}
                            ),
                        ]
                    ),
                ]
            ),
            html.Br(),  # Space to separate the Dropdown from other elements
            
            # Pie chart
            html.Div(
                className="graph-container box",
                children=[
                    dcc.Graph(id='success-pie-chart')
                ]
            ),
            html.Br(),

            # Payload range slider
            html.Div(
                className="slider-container box",
                children=[
                    html.P("Payload range (kg):"),
                    dcc.RangeSlider(
                        id='payload-slider',
                        min=0, max=10000, step=1000,
                        marks={i: str(i) for i in range(0, 10001, 1000)},
                        value=[min_payload, max_payload]
                    ),
                ]
            ),
            html.Br(),

            # Scatter plot
            html.Div(
                className="graph-container box",
                children=[
                    dcc.Graph(id='success-payload-scatter-chart')
                ]
            ),

            # Questions and Answers section
            html.Div(
                id='qa-section',
                className="qa-container box",
                style={
                    'padding': '20px',
                    'backgroundColor': '#f0f0f0',
                    'borderRadius': '10px',
                    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
                    'marginBottom': '50px'  # Aumentamos el margen inferior aquí
                },
                children=[
                    html.H2("Questions and Answers about SpaceX Launches", style={'fontSize': '2rem'}),
                    html.Div(id='question-1', children=html.Span("1. Which site has the highest number of successful launches?", style={'fontWeight': 'bold', 'fontSize': '1.2rem'})),
                    html.Div(id='answer-1', children="Loading..."),
                    html.Br(),
                    html.Div(id='question-2', children=html.Span("2. Which site has the highest launch success rate?", style={'fontWeight': 'bold', 'fontSize': '1.2rem'})),
                    html.Div(id='answer-2', children="Loading..."),
                    html.Br(),
                    html.Div(id='question-3', children=html.Span("3. Which payload range has the highest launch success rate?", style={'fontWeight': 'bold', 'fontSize': '1.2rem'})),
                    html.Div(id='answer-3', children="Loading..."),
                    html.Br(),
                    html.Div(id='question-4', children=html.Span("4. Which payload range has the lowest launch success rate?", style={'fontWeight': 'bold', 'fontSize': '1.2rem'})),
                    html.Div(id='answer-4', children="Loading..."),
                    html.Br(),
                    html.Div(id='question-5', children=html.Span("5. Which version of the F9 rocket (v1.0, v1.1, FT, B4, B5, etc.) has the highest success rate?", style={'fontWeight': 'bold', 'fontSize': '1.2rem'})),
                    html.Div(id='answer-5', children="Loading..."),
                ]
            ),
        ]
    ),

    # Footer section with author info and WhatsApp icon (lilas)
    html.Footer(
        style={
            'position': 'relative',  # Changed from fixed to relative
            'bottom': '0',
            'width': '100%',
            'backgroundColor': '#333',
            'color': 'white',
            'textAlign': 'center',
            'padding': '10px 0',
            'fontSize': '1rem',
            'zIndex': '1000'
        },
        children=[
            html.P("Dashboard created by ", style={'margin': '0', 'fontSize': '1rem'}),
            html.P("Crisel Nublo", style={'margin': '0', 'fontSize': '1.5rem', 'fontWeight': 'bold'}),
            # Icono 🪻
            html.Span("🪻", style={'fontSize': '3rem', 'marginLeft': '10px'}),
        ]
    ),
])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='class', 
                     names='Launch Site', 
                     title='Total Success Launches By Site')
        return fig
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(filtered_df, names='class', 
                     title=f'Total Success Launches for site {entered_site}')
        return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id="payload-slider", component_property="value")]
)
def update_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & 
                            (spacex_df['Payload Mass (kg)'] <= high)]
    
    if entered_site == 'ALL':
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', 
                         color='Booster Version Category',
                         title='Correlation between Payload and Success for all Sites')
        return fig
    else:
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', 
                         color='Booster Version Category',
                         title=f'Correlation between Payload and Success for {entered_site}')
        return fig

# TASK 5: Callback for answering the questions
@app.callback(
    [Output('answer-1', 'children'),
     Output('answer-2', 'children'),
     Output('answer-3', 'children'),
     Output('answer-4', 'children'),
     Output('answer-5', 'children')],
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_answers(entered_site, payload_range):
    low, high = payload_range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & 
                            (spacex_df['Payload Mass (kg)'] <= high)]
    
    # 1. Which site has the highest number of successful launches?
    site_success_count = filtered_df.groupby('Launch Site')['class'].sum()
    best_site_by_success = site_success_count.idxmax()

    # 2. Which site has the highest launch success rate?
    site_success_rate = filtered_df.groupby('Launch Site')['class'].mean()
    best_site_by_rate = site_success_rate.idxmax()

    # 3. Which payload range has the highest launch success rate?
    payload_success_rate = filtered_df.groupby('Payload Mass (kg)')['class'].mean()
    best_payload_range = payload_success_rate.idxmax()

    # 4. Which payload range has the lowest launch success rate?
    worst_payload_range = payload_success_rate.idxmin()

    # 5. Which version of the F9 rocket has the highest success rate?
    booster_success_rate = filtered_df.groupby('Booster Version Category')['class'].mean()
    best_booster_version = booster_success_rate.idxmax()

    return (f'{best_site_by_success} has the highest number of successful launches.',
            f'{best_site_by_rate} has the highest launch success rate.',
            f'The payload range with the highest success rate is: {best_payload_range} kg.',
            f'The payload range with the lowest success rate is: {worst_payload_range} kg.',
            f'The F9 rocket version with the highest success rate is: {best_booster_version}.')

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host='0.0.0.0', port=port, debug=False)
