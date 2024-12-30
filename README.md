[![Python](https://img.shields.io/badge/Python-v3.9-3572A5.svg)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-v6.4.5-DA5B0C.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](https://github.com/CriselPy/King-County-Housing-Analysis/blob/main/LICENSE/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-6495ed.svg)](https://github.com/CriselPy/King-County-Housing-Analysis/issues)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Cristina_Ortega-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/cristina-ortega-451750275/)
[![GitHub](https://img.shields.io/badge/GitHub-CriselPy-pink?logo=github&style=flat-square)](https://github.com/CriselPy)
[![GitHub stars](https://img.shields.io/github/stars/CriselPy/King-County-Housing-Analysis?style=social&label=Stars)](https://github.com/CriselPy/King-County-Housing-Analysis/stargazers)
[![Issues](https://img.shields.io/github/issues/CriselPy/King-County-Housing-Analysis?style=flat-square&color=673ab7)](https://github.com/CriselPy/King-County-Housing-Analysis/issues)
# Falcon 9 Data Science Project

Este proyecto predice si la primera etapa del Falcon 9 aterrizará con éxito utilizando datos de lanzamientos de SpaceX. El repositorio contiene varios notebooks de Jupyter que cubren la recolección de datos, el análisis exploratorio, la limpieza de datos y la visualización interactiva.

## Aplicación en Render

La aplicación Dash está desplegada en Render. Puedes acceder a ella en el siguiente enlace:

[SpaceX Launch Dashboard en Render]([https://your-render-app-link](https://spacex-launch-data.onrender.com/))

## Estructura del Proyecto

- **Collecting the Data**
  - `dataset_part_1.csv`
  - `jupyter-labs-spacex-data-collection-api-v2.ipynb`
  - `jupyter-labs-webscraping.ipynb`
  - `spacex_web_scraped.csv`

- **Data Wrangling**
  - `dataset_part_2.csv`
  - `labs-jupyter-spacex-Data wrangling-v2.ipynb`

- **Exploratory Analysis Using Pandas and Matplotlib**
  - `dataset_part_3.csv`
  - `jupyter-labs-eda-dataviz-v2.ipynb`

- **Exploratory Analysis Using SQL**
  - `jupyter-labs-eda-sql-coursera_sqllite.ipynb`

- **Interactive Visual Analytics and Dashboard**
  - `lab-jupyter-launch-site-location-v2.ipynb`

- **Predictive Analysis (Classification)**
  - `SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb`

- **SpaceX Dash App**
  - `spacex_dash_app.py`
  - `requirements.txt`

## Requisitos

Para ejecutar los notebooks y la aplicación Dash, necesitas instalar las siguientes librerías:

- requests
- pandas
- numpy
- matplotlib
- seaborn
- beautifulsoup4
- scikit-learn
- dash
- plotly
- folium
- wget

Puedes instalar todas las dependencias utilizando el archivo `requirements.txt`:

```sh
pip install -r SpaceX\ Dash\ App/requirements.txt

## Uso

1. **Recolección de Datos**: Utiliza los notebooks en la carpeta `Collecting the Data` para recolectar datos de la API de SpaceX y realizar web scraping.
2. **Limpieza de Datos**: Usa los notebooks en la carpeta `Data Wrangling` para limpiar y preparar los datos.
3. **Análisis Exploratorio**: Los notebooks en `Exploratory Analysis Using Pandas and Matplotlib` y `Exploratory Analysis Using SQL` te ayudarán a realizar análisis exploratorios.
4. **Visualización Interactiva**: Utiliza `Interactive Visual Analytics and Dashboard` para crear visualizaciones interactivas con Folium.
5. **Predicción**: Usa los notebooks en `Predictive Analysis (Classification)` para construir modelos de predicción.
6. **Aplicación Dash**: Ejecuta `spacex_dash_app.py` para iniciar la aplicación Dash y visualizar los resultados.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Autores

- Crisel Nublo 🪻

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.
