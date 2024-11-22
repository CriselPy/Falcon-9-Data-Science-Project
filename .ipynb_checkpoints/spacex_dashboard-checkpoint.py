import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import requests
import pandas as pd
from datetime import datetime
from dash_iconify import DashIconify
import utils

# Cargar los datos
df = utils.load_data()

# Coordenadas del sitio de lanzamiento y puntos de interés
launch_site_lat = 28.56341
launch_site_lon = -80.57679
points_of_interest = [
    {"name": "Highway", "lat": 28.56357, "lon": -80.57081, "color": "blue", "icon": "road"},
    {"name": "City", "lat": 28.07923, "lon": -80.6051, "color": "red", "icon": "building"},
    {"name": "Railway", "lat": 28.57221, "lon": -80.58528, "color": "purple", "icon": "train"},
    {"name": "Coastline", "lat": 28.56367, "lon": -80.56772, "color": "cadetblue", "icon": "water"}
]

# Crear el mapa de lanzamientos y guardarlo
launch_map = utils.create_launch_map(df, launch_site_lat, launch_site_lon, points_of_interest)
launch_map.save('assets/spacex_launch_map_combined.html')

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Función para obtener el próximo lanzamiento de SpaceX
def get_next_launch():
    url = 'https://api.spacexdata.com/v4/launches/next'
    response = requests.get(url)
    data = response.json()
    return data

# Definir el layout del dashboard
app.layout = html.Div(
    className='main-container',
    children=[
        html.H1(
            children=[
                DashIconify(icon="fa6-solid:rocket", className="icon", style={'margin-right': '10px'}),
                "SpaceX Launch Data Dashboard"
            ],
            className='title'
        ),
        html.P(
            "Explore the launch success of SpaceX missions based on different launch sites and payloads.",
            className='description'
        ),
        html.Div(
            children=[
                html.Label("Select Launch Site:", className='label'),
                dcc.Dropdown(
                    id='site-dropdown',
                    options=[{'label': site, 'value': site} for site in df['Launch Site'].unique()],
                    value=df['Launch Site'].unique()[0],
                    className='dropdown'
                ),
            ],
            className='dropdown-container'
        ),
        html.Div(
            children=[
                html.Label("Select Payload Mass (kg):", className='label'),
                dcc.RangeSlider(
                    id='mass-slider',
                    min=df['Payload Mass (kg)'].min(),
                    max=df['Payload Mass (kg)'].max(),
                    step=500,
                    marks={int(i): str(i) for i in range(int(df['Payload Mass (kg)'].min()), int(df['Payload Mass (kg)'].max())+1, 500)},
                    value=[df['Payload Mass (kg)'].min(), df['Payload Mass (kg)'].max()],
                    tooltip={"placement": "bottom", "always_visible": True}
                ),
            ],
            className='slider-container'
        ),
        dcc.Graph(id='launch-pie-chart', className='graph'),
        html.Div(
            children=[
                html.H3("Launch Site Map", className='subtitle'),
                html.Iframe(
                    src='/assets/spacex_launch_map_combined.html',
                    className='map-iframe'
                ),
            ],
            className='map-container'
        ),
        dcc.Graph(id='scatter-plot', className='graph'),
        
        # Gráfico de tendencias históricas
        dcc.Graph(id='launch-trends', className='graph'),
        
        # Cuenta regresiva
        html.Div(id='countdown', className='countdown'),
    ]
)

# Callbacks para actualizar gráficos
@app.callback(
    Output('launch-pie-chart', 'figure'),
    [Input('site-dropdown', 'value'), Input('mass-slider', 'value')]
)
def update_pie_chart(launch_site, mass_range):
    filtered_df = df[(df['Launch Site'] == launch_site) &
                     (df['Payload Mass (kg)'] >= mass_range[0]) &
                     (df['Payload Mass (kg)'] <= mass_range[1])]
    fig = px.pie(
        filtered_df,
        names='class',
        title='Launch Success Rate',
        labels={'class': 'Launch Outcome'},
        color_discrete_map={0: 'red', 1: 'green'}
    )
    fig.update_traces(textinfo='percent+label', pull=[0.1, 0.1, 0.1], marker=dict(line=dict(color='#000000', width=3)))  # Mejorar apariencia
    fig.update_layout(
        font=dict(family="Arial", size=14, color="white"),
        margin=dict(t=20, b=20, l=20, r=20),
        paper_bgcolor="#282828",  # Fondo oscuro
        plot_bgcolor="#383838",   # Fondo de la gráfica
        title_font=dict(size=22, family='Roboto', color='white'),
    )
    return fig

@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('site-dropdown', 'value'), Input('mass-slider', 'value')]
)
def update_scatter_plot(launch_site, mass_range):
    filtered_df = df[(df['Launch Site'] == launch_site) &
                     (df['Payload Mass (kg)'] >= mass_range[0]) &
                     (df['Payload Mass (kg)'] <= mass_range[1])]
    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='class',
        title='Payload Mass vs Launch Outcome',
        labels={'Payload Mass (kg)': 'Payload Mass (kg)', 'class': 'Launch Outcome'},
        color_continuous_scale='Viridis'
    )
    fig.update_traces(
        marker=dict(size=14, color='rgba(255, 165, 0, 0.8)', line=dict(width=3, color='darkorange')),
        selector=dict(mode='markers')
    )
    fig.update_layout(
        font=dict(family="Arial", size=14, color="white"),
        margin=dict(t=20, b=20, l=20, r=20),
        paper_bgcolor="#282828",  # Fondo oscuro
        plot_bgcolor="#383838",   # Fondo de la gráfica
        title_font=dict(size=22, family='Roboto', color='white'),
    )
    return fig

@app.callback(
    Output('launch-trends', 'figure'),
    [Input('site-dropdown', 'value')]
)
def update_trends(launch_site):
    filtered_df = df[df['Launch Site'] == launch_site]
    trend_df = filtered_df.groupby(filtered_df['Date'].dt.year)['class'].value_counts().unstack().fillna(0)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=trend_df.index, 
        y=trend_df[1], 
        name='Success', 
        marker_color='green',
        hoverinfo='x+y+name',  # Mejorar la visualización del hover
        opacity=0.8
    ))
    fig.add_trace(go.Bar(
        x=trend_df.index, 
        y=trend_df[0], 
        name='Failure', 
        marker_color='red',
        hoverinfo='x+y+name',
        opacity=0.8
    ))
    
    fig.update_layout(
        title='Launch Success & Failure Trends',
        xaxis_title='Year',
        yaxis_title='Number of Launches',
        barmode='stack',
        font=dict(family="Arial", size=14, color="white"),
        margin=dict(t=20, b=20, l=20, r=20),
        paper_bgcolor="#282828",  # Fondo oscuro
        plot_bgcolor="#383838",   # Fondo de la gráfica
        title_font=dict(size=22, family='Roboto', color='white'),
        legend=dict(font=dict(size=14, color='white'))
    )
    return fig

# Función para mostrar la cuenta regresiva
@app.callback(
    Output('countdown', 'children'),
    [Input('countdown', 'n_clicks')]
)
def update_countdown(n_clicks):
    next_launch = get_next_launch()
    launch_date = datetime.fromisoformat(next_launch['date_utc'].replace("Z", ""))
    now = datetime.utcnow()
    
    # Convertir las fechas a naive (sin zona horaria)
    launch_date_naive = launch_date.replace(tzinfo=None)
    now_naive = now.replace(tzinfo=None)

    countdown_time = launch_date_naive - now_naive
    return f"Next Launch in: {countdown_time}"

if __name__ == '__main__':
    app.run_server(debug=True) 