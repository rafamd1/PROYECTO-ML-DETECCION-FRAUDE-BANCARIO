# DETECCION DE FRAUDE BANCARIO

## Descripción del Proyecto
El objetivo principal de este proyecto es predecir transacciones fraudulentas aplicando técnicas de Machine Learning. Para abordar este problema de clasificación binaria (fraude o no fraude), se han implementado cinco modelos de aprendizaje automático (cuatro supervisados y uno no supervisado) utilizando una base de datos con más de 1,2 millones de transacciones reales realizadas entre el 01/01/2019 y el 30/06/2020. Previamente, se ha realizado un EDA y feature engineering para encontrar las mejores variables explicativas para los modelos. Asimismo, los datos han sido escalados y tratados con técnicas de rabalanceo (en entrenamiento) para que los modelos aprendan de las transacciones fraudulentas, que son una minoría dentro del dataset. Tras realizar y evaluar los modelos, en este caso con un enfoque especial en el Recall de las transacciones fraudulentas a fin de minimizar los falsos negativos, se ha seleccionado el mejor y se ha desplegado como app en Streamlit para hacer una demostración a clientes. Finalmente, se han realizado dos presentaciones, una técnica y otra no técnica, para comunicar los resultados de forma efectiva con públicos con conocimientos distintos.

## Modelos Supervisados implementados:
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost
  
## Modelo No Supervisado implementado:
- K-Means clustering

Además se ha utilizado GMM para la detección de anomalías

## Evaluación
La evaluación de los modelos se ha realizado utilizando varias métricas, con un enfoque especial en el Recall de las transacciones fraudulentas para asegurar que la mayor cantidad de transacciones fraudulentas son detectadas.

## Despliegue en una app con Streamlit
Por último, tras evaluar los modelos se ha seleccionado el mejor modelo (Random Forest- Recall: 0,95; Accuracy: 0,85) y se ha desplegado como un aapp en Streamlit para hacer una demostración a clientes.
