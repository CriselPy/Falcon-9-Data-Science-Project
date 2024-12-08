from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
from math import sin, cos, sqrt, atan2, radians
import io
from folium.features import DivIcon
import os

# Cargar el dataset de SpaceX
spacex_df = pd.read_csv('Interactive Visual Analytics and Dashboard/spacex_launch_geo.csv')

# Asegurarse de que las fechas están correctamente formateadas
spacex_df['Date'] = pd.to_datetime(spacex_df['Date'], format='%d-%m-%Y', errors='coerce')

launch_sites_df = spacex_df[['Launch Site', 'Lat', 'Long']].drop_duplicates()

# Inicializar la aplicación Dash
app = Dash(__name__)
app.title = "SpaceX Launch Dashboard"

# Layout de la app
app.layout = html.Div([
    # Portada con video
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
    # Contenedor del dashboard con los gráficos y controles
    html.Div(
        className="dashboard-container",
        children=[
            # Dropdown para seleccionar sitios de lanzamiento
            html.Div(
                className="selector-container",
                children=[
                    html.Div(
                        className="box",
                        children=[
                            dcc.Dropdown(
                                id='site-dropdown',
                                options=[{'label': 'All Sites', 'value': 'ALL'}] +
                                        [{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()],
                                value='ALL',
                                placeholder='Select a Launch Site',
                                searchable=True,
                                style={'width': '100%'}
                            ),
                        ]
                    ),
                ]
            ),
            html.Br(),

            # Gráfico de pie
            html.Div(
                className="graph-container box",
                children=[
                    dcc.Graph(id='success-pie-chart')
                ]
            ),
            html.Br(),

            # Slider para el rango de payload
            html.Div(
                className="slider-container box",
                children=[
                    html.P("Payload range (kg):"),
                    dcc.RangeSlider(
                        id='payload-slider',
                        min=spacex_df['Payload Mass (kg)'].min(),
                        max=spacex_df['Payload Mass (kg)'].max(),
                        step=100,
                        marks={i: f'{i} kg' for i in range(0, int(spacex_df['Payload Mass (kg)'].max()), 1000)},
                        value=[spacex_df['Payload Mass (kg)'].min(), spacex_df['Payload Mass (kg)'].max()]
                    ),
                ]
            ),
            html.Br(),

            # Gráfico de dispersión
            html.Div(
                className="graph-container box",
                children=[
                    dcc.Graph(id='success-payload-scatter-chart')
                ]
            ),
            html.Br(),

            # Mapa de Folium
            html.Div(
                className="map-container box",
                children=[
                    html.Div(id='map', style={'height': '100%', 'width': '100%'})
                ]
            )
        ]
    )
])

# Callback para actualizar el gráfico de pie
@app.callback(
    Output('success-pie-chart', 'figure'),
    [Input('site-dropdown', 'value')]
)
def update_pie_chart(selected_site):
    # Si se selecciona "ALL", contamos los lanzamientos exitosos y fallidos en todo el DataFrame
    if selected_site == 'ALL':
        launch_outcomes = spacex_df['class'].value_counts()
        fig = px.pie(
            names=launch_outcomes.index,
            values=launch_outcomes.values,
            title='Total Success Launches Across All Sites',
            color=launch_outcomes.index,
            color_discrete_map={0: 'red', 1: 'green'},  # 0 para fallido, 1 para exitoso
            hole=0.3
        )
    else:
        # Si se selecciona un sitio específico, filtrar por ese sitio y contar los lanzamientos exitosos y fallidos
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        if filtered_df.empty:
            return px.pie(
                names=['No Data'],
                values=[1],
                title=f'No launches found for site {selected_site}'
            )

        launch_outcomes = filtered_df['class'].value_counts()
        fig = px.pie(
            names=launch_outcomes.index,
            values=launch_outcomes.values,
            title=f'Success Launches for Site {selected_site}',
            color=launch_outcomes.index,
            color_discrete_map={0: 'red', 1: 'green'},
            hole=0.3
        )

    return fig


    # Personalización adicional: ajustar la fuente y el tamaño del título
    fig.update_layout(
        title_font=dict(family="Arial, sans-serif", size=24, color='black'),  # Cambiar la fuente y tamaño del título
        legend_title=dict(font=dict(size=20)),  # Cambiar el tamaño de la leyenda
        legend=dict(
            orientation="h",  # Colocar la leyenda en horizontal
            x=0.5,  # Centrar la leyenda
            xanchor="center"
        ),
        margin=dict(t=70, b=40, l=40, r=40)  # Ajustar los márgenes
    )
    
    return fig


# Callback para actualizar el gráfico de dispersión
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= payload_range[0]) &
        (spacex_df['Payload Mass (kg)'] <= payload_range[1])
    ]

    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == selected_site]

    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Orbit',
        title='Payload vs. Outcome for All Sites' if selected_site == 'ALL' else f'Payload vs. Outcome for {selected_site}',
        labels={'class': 'Launch Success'}
    )
    return fig


# Función para calcular la distancia entre dos puntos
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6373.0  # Radio aproximado de la Tierra en km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

@app.callback(
    Output('map', 'children'),
    [Input('site-dropdown', 'value')]
)
def update_map(selected_site):
    # Verificar si selected_site es válido
    print(f"Selected site: {selected_site}")
    
    # Si se selecciona 'ALL', usar el centro predeterminado
    if selected_site == 'ALL':
        center = [29.559684, -95.083097]
    else:
        site_data = launch_sites_df[launch_sites_df['Launch Site'] == selected_site]
        
        # Verificar si site_data no está vacío
        if not site_data.empty:
            center = [site_data['Lat'].iloc[0], site_data['Long'].iloc[0]]
        else:
            # En caso de que el sitio seleccionado no esté en el DataFrame, usar coordenadas por defecto
            center = [29.559684, -95.083097]  # Puedes cambiar este valor según tus necesidades

    folium_map = folium.Map(location=center, zoom_start=10)
    marker_cluster = MarkerCluster().add_to(folium_map)

    # Añadir marcadores para cada lanzamiento
    for _, row in spacex_df.iterrows():
        folium.Marker(
            location=[row['Lat'], row['Long']],
            icon=folium.Icon(color='green' if row['class'] == 1 else 'red', icon='rocket', prefix='fa'),
            popup=f"Payload: {row['Payload']}<br>Orbit: {row['Orbit']}<br>Success: {row['class']}"
        ).add_to(marker_cluster)

    # Si no es 'ALL', añadir los puntos de interés y calcular las distancias
    if selected_site != 'ALL':
        site_data = launch_sites_df[launch_sites_df['Launch Site'] == selected_site]
        launch_lat, launch_lon = site_data['Lat'].iloc[0], site_data['Long'].iloc[0]

        # Puntos de interés
        points_of_interest = [
            {'name': 'Coastline', 'lat': 28.56367, 'long': -80.56772, "color": "cadetblue", "icon": "fa-water"},
            {'name': 'Highway', 'lat': 28.56357, 'long': -80.57081, "color": "blue", "icon": "fa-road"},
            {'name': 'City', 'lat': 28.07923, 'long': -80.6051, "color": "red", "icon": "fa-building"},
            {'name': 'Railway', 'lat': 28.57221, 'long': -80.58528, "color": "purple", "icon": "fa-train"},
        ]

        # Añadir marcadores y las distancias
        for point in points_of_interest:
            distance = calculate_distance(launch_lat, launch_lon, point['lat'], point['long'])
            folium.Marker(
                location=[point['lat'], point['long']],
                popup=f"{point['name']} - {distance:.2f} KM",
                icon=DivIcon(icon_size=(70, 70), html=f'<i class="fa {point["icon"]}" style="font-size: 30px; color:{point["color"]};"></i>')
            ).add_to(folium_map)

        # Añadir marcador para el sitio de lanzamiento (con un cohete)
        folium.Marker(
            location=[launch_lat, launch_lon],
            popup="Launch Site",
            icon=DivIcon(icon_size=(90, 90), html='<i class="fa fa-rocket" style="font-size: 40px; color: violet;"></i>')
        ).add_to(folium_map)

        # Añadir líneas de distancia
        for point in points_of_interest:
            folium.PolyLine(
                locations=[(launch_lat, launch_lon), (point['lat'], point['long'])],
                color="red", weight=3, opacity=1
            ).add_to(folium_map)

    # Generar HTML del mapa en memoria
    map_html = io.BytesIO()
    folium_map.save(map_html, close_file=False)
    map_html.seek(0)

    # Retornar el mapa en un iframe
    return html.Iframe(
        srcDoc=map_html.read().decode('utf-8'),
        width='100%',
        height='600px'
    )

# Correr el servidor 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host='0.0.0.0', port=port, debug=False)  # Render se encarga del servidor en producción