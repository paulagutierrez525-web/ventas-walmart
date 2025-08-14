import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo
modelo = joblib.load("modelo_walmart.pkl")

st.title("Predicción de Ventas Walmart")
st.write("Ingrese los datos para estimar las ventas semanales:")

# Inputs
temp = st.number_input("Temperatura (°F)", value=70.0)
fuel = st.number_input("Precio Combustible", value=3.5)
cpi = st.number_input("CPI (Índice de Precios)", value=210.0)
unemp = st.number_input("Desempleo (%)", value=7.5)

# Botón de predicción
if st.button("Predecir Ventas"):
    datos = pd.DataFrame({
        'Temperature': [temp],
        'Fuel_Price': [fuel],
        'CPI': [cpi],
        'Unemployment': [unemp]
    })
    pred = modelo.predict(datos)
    st.success(f"Ventas estimadas: ${pred[0]:,.2f}")