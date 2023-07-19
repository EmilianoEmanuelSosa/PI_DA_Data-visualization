import streamlit as st
import pandas as pd
import plotly.express as px

# Carga de los conjuntos de datos
df1 = pd.read_csv('../Datasets/Data_proceses/Analysis_geo_cuant.csv')
df2 = pd.read_csv('../Datasets/Data_proceses/Analysis_geo_global.csv')
df3 = pd.read_csv('../Datasets/Data_proceses/Analysis_geo_temp.csv')

# Personalización del tema de Streamlit
# Cambia los colores y el tema según tus preferencias
dark_theme = """
    <style>
    body {
        color: white;
        background-color: #222;
    }
    </style>
    """
st.markdown(dark_theme, unsafe_allow_html=True)

# Filtros interactivos
selected_year = st.selectbox('Selecciona el año', df1['Año'].unique())

# Filtrar los datos según los filtros seleccionados
filtered_df1 = df1[(df1['Año'] == selected_year)]
filtered_df2 = df2[(df2['Año'] == selected_year)]
filtered_df3 = df3[(df3['Año'] == selected_year)]

# Gráfico de mapa interactivo
fig_map = px.choropleth(filtered_df1, locations='Provincia', locationmode='country names',
                        color='Red', scope='south america')
st.plotly_chart(fig_map)

# Otros gráficos (dispersión, barras, líneas, etc.)
# Utiliza los conjuntos de datos filtrados (filtered_df1, filtered_df2, filtered_df3)
# y crea los gráficos que desees utilizando la biblioteca Plotly Express

# Ejemplo: Gráfico de dispersión
fig_scatter = px.scatter(filtered_df2, x='Columna1', y='Columna2', color='Blue')
st.plotly_chart(fig_scatter)

# Ejemplo: Gráfico de barras
fig_bar = px.bar(filtered_df3, x='Columna4', y='Columna5')
st.plotly_chart(fig_bar)

# Ejemplo: Gráfico de líneas
fig_line = px.line(filtered_df1, x='Columna6', y='Columna7')
st.plotly_chart(fig_line)
