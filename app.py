import streamlit as st
import pandas as pd
import plotly.express as px

#Lectura de Documento 
source = pd.read_csv('vehicles_us.csv')

#Header insertion
st.header('Proyecto 7, Desarrollo Web: Automoviles Usados')
st.subheader('Seccion de Botones', divider="gray")

#Histogram creation
hist_button = st.button('Generar Histograma')

if hist_button:
    st.write('Generado: Histograma con datos para la promocion de vehiculos usados')
    fig = px.histogram(source, x='odometer',
                       x_label='Odometer (KM)')
    st.plotly_chart(fig, use_container_width=True)

#Scatterplot creation
scatter_button = st.button('Generar Diagrama de Dispersion')

if scatter_button:
    st.write('Generado: Diagrama de Dispersion con datos para la promocion de vehiculos usados')
    fig = px.scatter(source, x='odometer', y='price',
                     x_label='Odometer (KM)', y_label='Price (USD)')
    st.plotly_chart(fig, use_container_width=True)

#Sub-Header insertion
st.subheader('Seccion de Casillas', divider="gray")

#Checkbox creation (Histogram and Scatterplot)
hist_checkbox = st.checkbox('Generar Histograma')

if hist_checkbox:
    st.write('Generado: Histograma con datos odometricos para la promocion de vehiculos usados')
    fig = px.histogram(source, x='odometer',
                       x_label='Odometer (KM)')
    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox = st.checkbox('Generar Diagrama de Dispersion')

if scatter_checkbox:
    st.write('Generado: Diagrama de Dispersion con datos para la promocion de vehiculos usados')
    fig = px.scatter(source, x='odometer', y='price',
                     x_label='Odometer (KM)', y_label='Price (USD)')
    st.plotly_chart(fig, use_container_width=True)