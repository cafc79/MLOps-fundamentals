# KNN & MLOps

# Aprendizaje Basado en Instancias y MLOps

#### ¿Por qué elegir KNN sobre otros?

Es el algoritmo ideal cuando:

• Los datos \*\*no siguen una distribución conocida\*\* (No-paramétrico).

• El dataset es de \*\*tamaño pequeño a mediano\*\* (< 100k registros).
• Se requiere una
\*\*frontera de decisión extremadamente flexible\*\*.

• El modelo debe ser capaz de aprender de \*\*nuevos datos instantáneamente\*\* (Lazy
Learning).

#### Elemento Distintivo: No-Training

"KNN no genera una fórmula; memoriza el dataset. Su 'entrenamiento' es instantáneo, pero su
'inferencia' es costosa, ya que debe calcular distancias contra todos los ejemplos conocidos en
cada predicción."

Fase 1: Ingesta & Data Quality

## Tratamiento de Outliers y Split

Como KNN se basa en distancias, un solo valor atípico (Outlier) puede
"atrapar" a los vecinos cercanos y arruinar la clasificación local.

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta desde Feature Store versionada
df = pd.read\_csv('customer\_segments\_v1.csv')
# Gestión de Outliers: KNN es altamente sensible a ruidos espaciales
# Filtramos el percentil 99 para evitar puntos "aislados" que atraigan
vecinos
df = df[df['spending\_score'].between(df['spending\_score'].quantile(0.01),
df['spending\_score'].quantile(0.99))]
# Split: Stratify es mandatorio para mantener la densidad de clases
local
X\_train, X\_test, y\_train, y\_test = train\_test\_split(
df.drop('category', axis=1),
df['category'],
test\_size=0.2,
stratify=df['category'],
random\_state=42
)

#### Error Común: Dataset Masivo

Intentar usar KNN en datasets de millones de filas sin
indexación (como KD-Trees o BallTrees). La inferencia se volverá prohibitivamente lenta al tener que
calcular millones de distancias euclidianas.

Fase 2: Preprocessing & Dimensionality

## El Mandato del Escalado (StandardScaler)

Si una variable tiene rango 0-1 y otra 0-1000, la distancia será dominada
totalmente por la segunda variable.

from sklearn.preprocessing import
StandardScaler
# SIN ESCALADO, KNN ES MATEMÁTICAMENTE INVÁLIDO
scaler = StandardScaler()
X\_train\_scaled = scaler.fit\_transform(X\_train)
X\_test\_scaled = scaler.transform(X\_test)
# Recomendación pro: Si tienes > 20 variables, usa PCA antes de KNN
# para combatir la "Maldición de la Dimensionalidad".

#### Validación de Dimensionalidad

KNN sufre cuando hay demasiadas columnas. En alta
dimensión, todos los puntos parecen estar "lejos" de todos, invalidando el concepto de "vecino
cercano". Limita tus features a las 10-15 más importantes.

Fase 3: Model Tuning & Tracking

## Optimización de $K$ y Métricas de Distancia

El valor de $K$ define el balance entre sesgo y varianza. Un $K$ pequeño
sobreajusta; un $K$ grande promedia demasiado.

from sklearn.neighbors import
KNeighborsClassifier
import mlflow
with mlflow.start\_run(run\_name="knn\_optimized\_k7"):
# K=7 (Impar para evitar empates), pesos ponderados por distancia
model = KNeighborsClassifier(n\_neighbors=7,
weights='distance', metric='euclidean')
model.fit(X\_train\_scaled, y\_train)
# Tracking de parámetros clave
mlflow.log\_params({"k": 7, "weights": "distance", "algorithm": "auto"})

Fase 4: Evaluación & Model Health

## Chequeo de Salud Espacial

### Model Health Check

Estabilidad ante cambio de K
Variación < 3%

Latencia de Inferencia
Objetivo < 100ms

Accuracy en Micro-clusters
Mínimo 85%

Ratio de Overfitting
Delta < 5%

from sklearn.metrics import
classification\_report
# Validación distintiva: Error de entrenamiento vs Test
# En KNN, si K=1, el error de entrenamiento es 0.
# Eso es una alerta roja de salud del modelo.
y\_pred = model.predict(X\_test\_scaled)
print(classification\_report(y\_test, y\_pred))

#### La Trampa del K=1

Usar un K demasiado pequeño capturará el ruido del dataset como si
fuera un patrón real. Valida siempre con un rango de K (ej. 3 a 15) y elige el que mantenga métricas
estables en el set de validación.

Fase 5: Deployment & Serving

## Serialización del "Dataset-Cerebro"

Recuerda: El bundle de producción debe contener el dataset de entrenamiento,
ya que KNN lo necesita para "comparar" en vivo.

import joblib
# El artefacto DEBE ser atómico (Scaler + Model)
production\_bundle = {
"pipeline\_v": "10.2.1",
"feature\_scaler": scaler,
"knn\_model": model
}
joblib.dump(production\_bundle, 'knn\_service.joblib')

Fase 6: Observation & Drift

## Vigilancia de la Distribución Espacial

Monitoreamos si los nuevos datos de los usuarios están cayendo en "tierras de
nadie" geométricas.

#### Alertas de Re-entrenamiento:

##### Latency Drift

Si el dataset crece, el tiempo de respuesta
aumenta. Alerta en > 150ms.

##### Data Drift

Si el 20% de las predicciones tienen una distancia
al vecino > umbral histórico.

Continuous Learning Sync

## Checklist de Validación MLOps (KNN)

##### Normalización Z-Score

¿Se validó que todas las variables tienen media 0 y varianza 1
antes de calcular distancias?

##### Estrategia de K-Impar

¿Se eligió un K que no permita empates en la votación de clases?

##### Dimensionalidad Bajo Control

¿Se eliminaron variables ruidosas o irrelevantes mediante
Selección de Características?

##### Indexación KD-Tree

¿Se configuró el parámetro `algorithm='kd\_tree'` para acelerar la
búsqueda en producción?

##### Pesos por Distancia

¿Se consideró `weights='distance'` para que los vecinos más
cercanos influyan más que los lejanos?

##### Inferencia SLA

¿Se ha medido el tiempo de respuesta con carga máxima simulada?
 
> [**Algoritmo - K-Nearest Neighbors**](../algoritmos/Supervised_Learning-K-Nearest-Neighbors.md)
• 
> [**Practica - K-Nearest Neighbors**](../Sample/Supervised_Learning-K-Nearest-Neighbors.md)
• 
> [**Codigo - Árboles de Decisión**](Supervised_Learning-Arboles-Decision.md)
---