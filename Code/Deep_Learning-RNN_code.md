# RNN/LSTM & MLOps

# Series Temporales y Ecosistema MLOps

#### Lógica de Selección: ¿Por qué LSTM/GRU?

Se elige sobre modelos tradicionales (ARIMA) o densos (MLP) cuando:

• Existen \*\*dependencias de largo plazo\*\* en los datos.

• El orden secuencial es el factor determinante del resultado.

• Se requiere capturar patrones estacionales complejos no lineales.

• Se dispone de datos masivos con múltiples variables correlacionadas en el tiempo.

#### Elemento Distintivo: Estado Oculto

"A diferencia de otros modelos, la RNN posee una 'memoria' interna ($h\_t$). No mira cada dato de
forma aislada; mantiene un resumen del pasado que condiciona la interpretación del presente."

Fase 1: Ingesta & Temporal Lineage

## Manejo de Ventanas y Evitación de Look-ahead

En series de tiempo, el error fatal es el "Look-ahead bias": permitir que el
modelo vea información del futuro durante el entrenamiento.

import pandas as pd
import numpy as np
# Ingesta inmutable: NO barajar (shuffle=False)
df = pd.read\_csv('energy\_demand\_v1.csv',
parse\_dates=['timestamp'])
# Time Series Split: El set de prueba debe ser cronológicamente
posterior
train\_size = int(len(df) \* 0.8)
train, test = df.iloc[:train\_size], df.iloc[train\_size:]
# Creación de Ventanas Deslizantes (Sliding Windows)
def create\_windows(data, window\_size=24):
X, y = [], []
for i in range(len(data) - window\_size):
X.append(data[i:i+window\_size])
y.append(data[i+window\_size])
return np.array(X), np.array(y)

#### Error Común: Shuffling Aleatorio

Usar `train_test_split` con barajado
destruye la autocorrelación temporal. El modelo entrenará con datos del futuro para predecir el
pasado, inflando las métricas ficticiamente.

Fase 2: Preprocessing & Scaling

## Escalamiento y Estacionariedad

Las RNN son extremadamente sensibles a la escala debido a las funciones de
activación (tanh/sigmoid). Además, removemos tendencias para estabilizar la media.

from sklearn.preprocessing import
MinMaxScaler
# MinMaxScaler es preferible para RNNs para mantener rangos [0, 1]
scaler = MinMaxScaler(feature\_range=(0, 1))
train\_scaled = scaler.fit\_transform(train[['demand']])
test\_scaled = scaler.transform(test[['demand']])
# Mejor Práctica: Diferenciación para hacer la serie estacionaria
# df\_diff = df.diff().dropna()

#### Validación Crucial: Estacionariedad

Aplica el test de **Dickey-Fuller
(ADF)**. Si la serie no es estacionaria (su media cambia con el tiempo), la RNN tendrá
dificultades para converger. La diferenciación es tu mejor aliada.

Fase 3: Model Training & Architecture

## Arquitectura LSTM Trazable

Implementamos celdas de Memoria de Largo Plazo (LSTM) para combatir el
desvanecimiento del gradiente.

from tensorflow.keras.models import
Sequential
from tensorflow.keras.layers import
LSTM, Dense, Dropout
import mlflow
with mlflow.start\_run(run\_name="lstm\_demand\_forecaster"):
model = Sequential([
# input\_shape=(time\_steps, features)
LSTM(50, return\_sequences=True, input\_shape=(24, 1)),
Dropout(0.2),
LSTM(50, return\_sequences=False),
Dense(1)
])
model.compile(optimizer='adam', loss='mse')
mlflow.log\_param("window\_size", 24)

Fase 4: Evaluación & Model Health

## Diagnóstico de Residuos Temporales

### RNN Health Check

RMSE / MAPE
Tolerancia < 5%

Autocorrelación de Residuos
Cero (Ruido blanco)

Look-ahead Bias Check
Validado

Loss Stability
Convergencia OK

#### Validación Crítica: Backtesting

"Una RNN saludable no solo minimiza el error, sino que
sus errores no están correlacionados en el tiempo. Si el error de hoy ayuda a predecir el de
mañana, el modelo está incompleto."

WALK-FORWARD VALIDATION: PASSED

#### La Trampa del "Lag 1"

A veces la RNN simplemente aprende a copiar el valor del paso anterior
($Y\_{t-1}$) como predicción para $Y\_t$. Esto da un error bajo pero no genera valor predictivo real.
\*\*Compara siempre tu modelo contra un baseline ingenuo (Persistence Model).\*\*

Fase 5: Deployment & Streaming

## Serving Secuencial e Inferencia

El despliegue de una RNN requiere una gestión de estado. La API debe mantener
los últimos $N$ pasos para predecir el siguiente.

import joblib
# Bundle inmutable: Escalador + Modelo H5
forecasting\_bundle = {
"v": "18.2.0",
"input\_scaler": scaler,
"rnn\_model": "saved\_model.h5",
"lookback": 24
}
joblib.dump(forecasting\_bundle, 'demand\_service.pkl')
# Nota: El servicio de Serving debe reconstruir el tensor
# de entrada con la forma (1, 24, 1) antes de .predict()

Fase 6: Monitoring & Time Drift

## Vigilancia de la Estacionalidad

Los patrones temporales cambian (ej. cambio de hábitos por confinamiento).
Monitoreamos la deriva del concepto temporal.

#### Alertas MLOps (RNN):

##### Variance Drift

Si la volatilidad de la demanda aumenta
drásticamente.

##### Concept Drift

Si el error residual del modelo sube > 15%
sostenidamente.

Online Training Loop Active

## Checklist de Validación MLOps (RNN)

##### Temporal Integrity

¿Se garantizó que el split de entrenamiento y prueba fue
puramente cronológico?

##### Windowing Logic

¿El tamaño de la ventana ($T$) es suficiente para capturar la
estacionalidad mínima (ej. 24h)?

##### Scaling Persistency

¿Se está usando el mismo objeto `MinMaxScaler` para transformar
las entradas de la API?

##### Residuals Whiteness

¿Se comprobó que los errores no tienen autocorrelación
significativa?

##### Architectural Benchmark

¿La LSTM supera realmente a un modelo autorregresivo simple
(ARIMA) en precisión?

##### Monitoring Trigger

¿Existe una alerta automática ante la pérdida de precisión por
cambio de ciclo estacional?

> [* Algoritmo - Redes Neuronales Recurrentes**](../algoritmos/Deep_Learning-RNN.md)
 • 
> [* Practica - Redes Neuronales Recurrentes**](../Sample/Deep_Learning-RNN.md)
---