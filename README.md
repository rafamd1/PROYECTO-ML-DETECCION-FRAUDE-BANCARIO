# PROYECTO DE DETECCION FRAUDE BANCARIO

## Descripción del Proyecto
El objetivo principal de este proyecto es predecir transacciones fraudulentas aplicando técnicas de Machine Learning. Para abordar este problema de clasificación binaria (fraude o no fraude), se han implementado cinco modelos de aprendizaje automático (cuatro supervisados y uno no supervisado) utilizando una base de datos con más de 1,2 millones de transacciones reales realizadas entre el 01/01/2019 y el 30/06/2020. Previamente, los datos han sido escalados y tratados con técnicas de rabalanceo (en los datos de entrenamiento) para que los modelos aprendan de las transacciones fraudlentas, que son una minoría. Finalmente, los modelos se han evaluado con un enfoque especial en el Recall de las transacciones fraudulentas, a fin de minimizar los falsos negativos.

## Modelos Implementados
### Modelos Supervisados:
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost
  
### Modelo No Supervisado
- K-Means clustering
- También se ha utilizado GMM para la detección de anomalías

## Evaluación
La evaluación de los modelos se ha realizado utilizando varias métricas, con un enfoque especial en el Recall de las transacciones fraudulentas para asegurar que la mayor cantidad posible de transacciones fraudulentas sean detectadas.
