import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('datasets/vehicles_us.csv') # leer los datos
st.header('Análisis exploratorio de datos')
hist_button = st.button('Construir histograma', help='Histograma con base al odometro') # crear un botón
scatter_button = st.button('Contruir un gráfico de disperción', help='Odometro vs precio') # crea un segundo boton
hist_checkbox = st.checkbox('Construir histograma de la condición del vehículo') # crea un segundo histograma
    
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
    # Muestra una explicación de lo que se observa en la gráfica
    st.write('Se observa que hay mayor cantidad de vehículos que tienen entre 100,000 km y 120,000 km recorridos')

# al hacer clic en el botón para el gráfico de dispersión
if scatter_button:
    # Se escribe un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crea el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Muestra el gráfico de dispersión 
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Muestra una explicación de lo que se observa en la gráfica
    st.write('Los vehículos con menor kilometraje son los que tienden a tener un precio más alto: Cuanto mayor meyor se el kilometreje \nmenor será el precio')
    
if hist_checkbox:
     # Se escribe un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crea el gráfico de dispersión
    fig_histogram = px.histogram(car_data, x="condition")
    
    # Muestra el gráfico de dispersión 
    st.plotly_chart(fig_histogram, use_container_width=True)
    
    # Muestra una explicación de lo que se observa en la gráfica
    st.write('La mayor cantidad de vehículos tienen uns candición excelente. Por otro lado, hay mucho menor cantidad de autos nuevos')