[![Python](https://img.shields.io/badge/Python-v3.9-3572A5.svg)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter_Notebook-v6.4.5-DA5B0C.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/LICENSE/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-6495ed.svg)](https://github.com/CriselPy/Falcon-9-Data-Science-Project/issues)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Cristina_Ortega-blue?logo=linkedin&style=flat-square)](https://www.linkedin.com/in/cristina-ortega-451750275/)
[![GitHub](https://img.shields.io/badge/GitHub-CriselPy-pink?logo=github&style=flat-square)](https://github.com/CriselPy)
[![GitHub stars](https://img.shields.io/github/stars/CriselPy/Falcon-9-Data-Science-Project?style=social&label=Stars)](https://github.com/CriselPy/Falcon-9-Data-Science-Project/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/CriselPy/Falcon-9-Data-Science-Project)](https://github.com/CriselPy/Falcon-9-Data-Science-Project/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/CriselPy/Falcon-9-Data-Science-Project)](https://github.com/CriselPy/Falcon-9-Data-Science-Project/issues)
[![GitHub forks](https://img.shields.io/github/forks/CriselPy/Falcon-9-Data-Science-Project)](https://github.com/CriselPy/Falcon-9-Data-Science-Project/network)
[![GitHub watchers](https://img.shields.io/github/watchers/CriselPy/Falcon-9-Data-Science-Project)](https://github.com/CriselPy/Falcon-9-Data-Science-Project/watchers)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/CriselPy/Falcon-9-Data-Science-Project)](https://github.com/CriselPy/Falcon-9-Data-Science-Project/pulls)

## Screenshots

![Dashboard](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/SpaceX%20Dash%20App/assets/dashboard.gif)

## Table of Contents
- [Falcon 9 Data Science Project](#falcon-9-data-science-project)
  - [Application on Render](#application-on-render)
  - [Project Structure](#project-structure)
  - [Requirements and Installation](#requirements-and-installation)
  - [Usage](#usage)
  - [Preview and Access](#preview-and-access)
  - [License](#license)
  - [Contact](#contact)
  - [Contributions](#contributions)
  - [Project Status](#project-status)
  - [Authors](#authors)
- [Crisel Nublo 🪻](#crisel-nublo-)

# Falcon 9 Data Science Project

This project predicts whether the first stage of the Falcon 9 will successfully land using SpaceX launch data. The repository contains several Jupyter notebooks covering data collection, exploratory analysis, data cleaning, and interactive visualization.

## Application on Render

The Dash application is deployed on Render. You can access it at the following link:

[SpaceX Launch Dashboard on Render](https://spacex-launch-data.onrender.com/)

## Project Structure

- **Collecting the Data**
  - [`dataset_part_1.csv`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Collecting%20the%20Data/dataset_part_1.csv)
  - [`jupyter-labs-spacex-data-collection-api-v2.ipynb`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Collecting%20the%20Data/jupyter-labs-spacex-data-collection-api-v2.ipynb)
  - [`jupyter-labs-webscraping.ipynb`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Collecting%20the%20Data/jupyter-labs-webscraping.ipynb)
  - [`spacex_web_scraped.csv`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Collecting%20the%20Data/spacex_web_scraped.csv)

- **Data Wrangling**
  - [`dataset_part_2.csv`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Data%20Wrangling/dataset_part_2.csv)
  - [`labs-jupyter-spacex-Data wrangling-v2.ipynb`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Data%20Wrangling/labs-jupyter-spacex-Data%20wrangling-v2.ipynb)

- **Exploratory Analysis Using Pandas and Matplotlib**
  - [`dataset_part_3.csv`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Exploratory%20Analysis%20Using%20Pandas%20and%20Matplotlib/dataset_part_3.csv)
  - [`jupyter-labs-eda-dataviz-v2.ipynb`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Exploratory%20Analysis%20Using%20Pandas%20and%20Matplotlib/jupyter-labs-eda-dataviz-v2.ipynb)

- **Exploratory Analysis Using SQL**
  - [`jupyter-labs-eda-sql-coursera_sqllite.ipynb`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Exploratory%20Analysis%20Using%20SQL/jupyter-labs-eda-sql-coursera_sqllite.ipynb)

- **Interactive Visual Analytics and Dashboard**
  - [`lab-jupyter-launch-site-location-v2.ipynb`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Interactive%20Visual%20Analytics%20and%20Dashboard/lab-jupyter-launch-site-location-v2.ipynb)
  - [`spacex_launch_geo.csv`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Interactive%20Visual%20Analytics%20and%20Dashboard/spacex_launch_geo.csv)

- **Predictive Analysis (Classification)**
  - [`SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/Predictive%20Analysis%20(Classification)/SpaceX-Machine-Learning-Prediction-Part-5-v1.ipynb)

- **SpaceX Dash App**
  - [`spacex_dash_app.py`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/SpaceX%20Dash%20App/spacex_dash_app.py)
  - [`spacex_launch_dash.csv`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/SpaceX%20Dash%20App/spacex_launch_dash.csv)
  - [`requirements.txt`](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/SpaceX%20Dash%20App/requirements.txt)

## Requirements and Installation

To run the notebooks and the Dash application, you need to install the following libraries:

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

You can install all dependencies using the `requirements.txt` file:

1. Clone the repository:
    ```sh
    git clone https://github.com/CriselPy/Falcon-9-Data-Science-Project.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Falcon-9-Data-Science-Project
    ```
3. Install the dependencies:
    ```sh
    pip install -r SpaceX\ Dash\ App/requirements.txt
    ```

## Usage

1. **Data Collection**: Use the notebooks in the `Collecting the Data` folder to collect data from the SpaceX API and perform web scraping.
2. **Data Cleaning**: Use the notebooks in the `Data Wrangling` folder to clean and prepare the data.
3. **Exploratory Analysis**: The notebooks in `Exploratory Analysis Using Pandas and Matplotlib` and `Exploratory Analysis Using SQL` will help you perform exploratory analysis.
4. **Interactive Visualization**: Use `Interactive Visual Analytics and Dashboard` to create interactive visualizations with Folium.
5. **Prediction**: Use the notebooks in `Predictive Analysis (Classification)` to build prediction models.
6. **Dash Application**: Run `spacex_dash_app.py` to start the Dash application and visualize the results.

## Preview and Access

You can preview the PDF and presentation, as well as access the Dash application at the following links:

- [Preview PDF](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/ds-capstone-template-coursera.pdf)
- [Download Presentation](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/ds-capstone-template-coursera.pptx)
- [Access the Dash Application](https://spacex-launch-data.onrender.com/)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/CriselPy/Falcon-9-Data-Science-Project/blob/main/LICENSE) file for more details.

## Contact
For questions, please contact Crisel Nublo 🪻 on [LinkedIn](https://www.linkedin.com/in/cristina-ortega-451750275/).

## Contributions

Contributions are welcome. Please open an issue or a pull request to discuss any changes you would like to make.

## Project Status
This project is currently completed.

## Authors

# Crisel Nublo 🪻
