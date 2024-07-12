import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Cargar el modelo entrenado
with open('best_model1.pkl', 'rb') as file:
    model = pickle.load(file)

# Definir la interfaz de la aplicación
st.title("Predicción de transacciones fraudulentas")

# Crear entradas para los datos de entrada del modelo
amt = st.number_input('Monto de transacción', min_value=0, max_value=1000000, step=1)
is_fraud_zip = st.selectbox('¿La transacción se está realizando desde uno de los códigos postales detectados como fraudulentos?', ['No', 'Sí'])
is_frequent_fraudster = st.selectbox('¿Es el cliente un defraudador habitual?', ['No', 'Sí'])

def procesar_entrada(amt, is_fraud_zip, is_frequent_fraudster):
    # Convertir entradas de selectbox a valores binarios
    is_fraud_zip = 1 if is_fraud_zip == 'Sí' else 0
    is_frequent_fraudster = 1 if is_frequent_fraudster == 'Sí' else 0
    
    # Crear un diccionario con los datos
    data = {
        'amt': amt,
        'is_fraud_zip': is_fraud_zip,
        'is_frequent_fraudster': is_frequent_fraudster
    }
    
    # Convertir a DataFrame
    df = pd.DataFrame(data, index=[0])
    return df

if st.button("Predecir"):
    input_data = procesar_entrada(amt, is_fraud_zip, is_frequent_fraudster)
    prediction = model.predict(input_data)
    st.write(f'La predicción es: {"Fraudulenta" if prediction[0] == 1 else "No fraudulenta"}')