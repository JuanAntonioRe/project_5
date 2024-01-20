import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('datasets/vehicles_us.csv') # leer los datos
st.header('Análisis exploratorio de datos')
hist_button = st.button('Construir histograma', help='Histograma con base al odometro') # crear un botón
scatter_button = st.button('Contruir un gráfico de disperción', help='Odometro vs precio') # crea un segundo boton
    
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# al hacer clic en el botón para el gráfico de dispersión
if scatter_button:
    # Se escribe un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crea el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Muestra el gráfico de dispersión 
    st.plotly_chart(fig_scatter, use_container_width=True)