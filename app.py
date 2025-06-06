import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# Título de la app
st.title('Análisis de vehículos usados')

# Cargar los datos
df = pd.read_csv('vehicles_us.csv')
df_clean = df.dropna(subset=['price', 'odometer'])

# Casilla de verificación
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Gráfico de dispersión: Precio vs Kilometraje')

    # Crear el gráfico usando solo matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df_clean['odometer'], df_clean['price'], alpha=0.5, s=10)
    ax.set_title('Relación entre precio y kilometraje de vehículos usados')
    ax.set_xlabel('Kilometraje (odometer)')
    ax.set_ylabel('Precio (USD)')
    ax.grid(True)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)