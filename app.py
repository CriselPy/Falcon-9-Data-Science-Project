# Importar las bibliotecas necesarias
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Leer los datos del archivo CSV
spacex_df = pd.read_csv('spacex_launch_geo.csv')

# Crear la aplicación Dash
app = dash.Dash(
    __name__,
    external_stylesheets=['/assets/styles.css'],  # Ahora usamos la hoja de estilo externa
    external_scripts=[
        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/js/all.min.js'  # Iconos Font Awesome
    ],
    suppress_callback_exceptions=True  # Permitir que las excepciones en callbacks se ignoren mientras se carga
)


# Definir las opciones del dropdown (menú desplegable) para los sitios de lanzamiento
launch_sites = spacex_df['Launch Site'].unique()

# Definir el diseño de la aplicación (layout)
app.layout = html.Div(id='main-container', className='day-mode', children=[  # Definir clase por defecto como 'day-mode'
    # Título principal
    html.H1("Analítica de Lanzamientos de SpaceX", style={'text-align': 'center'}),

    # Botón para cambiar entre modo noche/día con un icono
    html.Div([
        html.Button(
            html.I(className="fas fa-sun"),  # Icono de sol por defecto
            id='toggle-button', n_clicks=0,
        ),
    ], style={'position': 'relative', 'z-index': 1}),

    # Panel de controles (Dropdown y Slider)
    html.Div([
        # Dropdown para seleccionar el sitio de lanzamiento
        html.Div([
            html.Label('Seleccionar Sitio de Lanzamiento', style={'font-size': '16px', 'font-weight': 'bold', 'margin-bottom': '5px'}),
            dcc.Dropdown(
                id='launch-site-dropdown',
                options=[{'label': site, 'value': site} for site in launch_sites],
                value=launch_sites[0],
            )
        ], className='dropdown-container'),

        # Slider para seleccionar el rango de masa de la carga útil
        html.Div([
            html.Label('Seleccionar Rango de Masa de Carga Útil', style={'font-size': '16px', 'font-weight': 'bold', 'margin-bottom': '5px'}),
            dcc.RangeSlider(
                id='payload-slider',
                min=spacex_df['Payload Mass (kg)'].min(),
                max=spacex_df['Payload Mass (kg)'].max(),
                step=500,
                marks={i: str(i) for i in range(
                    int(spacex_df['Payload Mass (kg)'].min()),
                    int(spacex_df['Payload Mass (kg)'].max()) + 1, 500
                )},
                value=[spacex_df['Payload Mass (kg)'].min(), spacex_df['Payload Mass (kg)'].max()],
                tooltip={"placement": "bottom", "always_visible": True}
            )
        ], className='slider-container'),
    ], style={
        'display': 'flex',
        'flex-direction': 'column',
        'align-items': 'center',
        'padding': '20px',
        'gap': '20px'
    }),

    # Contenedor para los gráficos y el mapa
    html.Div([
        html.Div([dcc.Graph(id='success-pie-chart')], style={'width': '100%', 'height': '400px'}),
        html.Div([dcc.Graph(id='success-payload-scatter-chart')], style={'width': '100%', 'height': '400px'}),
        html.Div([html.Iframe(id='launch-map', srcDoc=None, width='100%', height='600px')], style={'width': '100%', 'height': '600px'})
    ], style={'display': 'flex', 'flexDirection': 'column', 'gap': '10px'}),
])

# Callback para actualizar el gráfico circular basado en el sitio de lanzamiento seleccionado
@app.callback(
    Output('success-pie-chart', 'figure'),
    [Input('launch-site-dropdown', 'value')]
)
def update_pie_chart(launch_site):
    filtered_data = spacex_df[spacex_df['Launch Site'] == launch_site]
    success_counts = filtered_data['class'].value_counts()
    fig = px.pie(values=success_counts, names=success_counts.index, title=f'Tasa de Éxito en {launch_site}')
    return fig

# Callback para actualizar el gráfico de dispersión según el rango de carga útil
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('payload-slider', 'value')]
)
def update_scatter(payload_range):
    min_payload, max_payload = payload_range
    filtered_data = spacex_df[(spacex_df['Payload Mass (kg)'] >= min_payload) & (spacex_df['Payload Mass (kg)'] <= max_payload)]
    fig = px.scatter(filtered_data, x='Payload Mass (kg)', y='class', color='Launch Site',
                     labels={'Payload Mass (kg)': 'Masa de Carga (kg)', 'class': 'Éxito de Lanzamiento'},
                     title=f'Éxito vs Masa de Carga')
    return fig

# Callback para alternar entre modo día y noche con íconos diferentes
@app.callback(
    [Output('toggle-button', 'children'),
     Output('main-container', 'className')],
    [Input('toggle-button', 'n_clicks')]
)
def toggle_day_night(n_clicks):
    if n_clicks % 2 == 0:
        # Usar ícono de sol con tamaño grande para el día
        return html.I(className="fas fa-sun fa-5x"), 'day-mode'
    else:
        # Usar ícono de luna con tamaño grande para la noche
        return html.I(className="fas fa-moon fa-5x"), 'night-mode'

# Callback para actualizar el mapa Folium basado en el sitio seleccionado
@app.callback(
    Output('launch-map', 'srcDoc'),
    [Input('launch-site-dropdown', 'value')]
)
def update_map(launch_site):
    site_data = spacex_df[spacex_df['Launch Site'] == launch_site]
    m = folium.Map(location=[site_data['Lat'].mean(), site_data['Long'].mean()], zoom_start=7)
    marker_cluster = MarkerCluster().add_to(m)

    for _, row in site_data.iterrows():
        folium.Marker(
            location=[row['Lat'], row['Long']],
            popup=f"{row['Launch Site']}<br>Éxito: {'Sí' if row['class'] == 1 else 'No'}",
            icon=folium.Icon(color='green' if row['class'] == 1 else 'red')
        ).add_to(marker_cluster)

    return m._repr_html_()

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)

