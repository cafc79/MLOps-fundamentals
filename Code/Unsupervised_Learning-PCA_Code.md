# Pipeline Industrial: PCA & MLOps

# Síntesis de Información y Ecosistema MLOps

#### ¿Por qué PCA frente a otros?

Es la técnica de elección para reducción de dimensionalidad cuando:

• Se busca \*\*eliminar la multicolinealidad\*\* (variables redundantes).

• Se requiere una \*\*compresión lineal\*\* rápida y determinista.

• El objetivo es la \*\*visualización\*\* o el preprocesamiento para otros modelos.

• Se necesita filtrar el \*\*ruido\*\* de datos de sensores masivos.

#### Elemento Distintivo: Proyección Ortogonal

"PCA no solo elimina columnas; crea nuevas 'súper-variables' (PCs) que son totalmente
independientes entre sí. Es el purificador definitivo para modelos que sufren ante variables
correlacionadas."

Fase 1: Ingesta & Data Cleaning

## Tratamiento de Alta Dimensionalidad

Cargamos datos con cientos de variables (ej. 150 sensores industriales). El
primer paso es asegurar que no haya sesgos por nulos que distorsionen la varianza global.

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta de datos de sensores (versionado DVC)
df = pd.read\_csv('sensor\_factory\_data\_v1.csv')
# Eliminación de variables con varianza cero (constantes)
# No aportan información y causan errores en la matriz de covarianza
df = df.loc[:, df.var() > 0]
# Split: PCA es no supervisado, pero el split previene el leakage en el
pipeline final
X\_train, X\_test = train\_test\_split(df, test\_size=0.2, random\_state=42)

#### Error Común: Ignorar el Escalado

PCA busca maximizar la varianza. Si una variable tiene
valores de 0-1000 y otra 0-1, la primera será identificada como el "componente principal"
erróneamente solo por su escala. **El StandardScaler es innegociable.**

Fase 2: Preprocessing & Standardization

## El Mandato de la Estandarización

Centramos los datos en 0 y los llevamos a una desviación estándar de 1 para
que el álgebra lineal capture la forma real de los datos.

from sklearn.preprocessing import
StandardScaler
# Ajuste del escalador SOLO en Train para mantener el linaje de MLOps
scaler = StandardScaler()
X\_train\_scaled = scaler.fit\_transform(X\_train)
X\_test\_scaled = scaler.transform(X\_test)

#### Validación Crucial: Correlación

PCA es más efectivo cuando la correlación entre
variables es alta. Si tus variables ya son independientes, PCA solo añadirá complejidad sin reducir
dimensiones de forma útil.

Fase 3: Model Training & Component Selection

## Ajuste y Análisis de Varianza

Ajustamos el modelo para extraer todos los componentes y luego decidimos el
punto de corte (Criterio de Kaiser o Codo).

from sklearn.decomposition import PCA
import mlflow
with mlflow.start\_run(run\_name="pca\_sensor\_reduction"):
# n\_components=0.95 significa "mantén los PCs suficientes para explicar el 95%
de la varianza"
pca = PCA(n\_components=0.95)
X\_train\_pca = pca.fit\_transform(X\_train\_scaled)
# Logging de MLOps
mlflow.log\_param("original\_dim",
X\_train.shape[1])
mlflow.log\_param("reduced\_dim",
pca.n\_components\_)
mlflow.log\_metric("total\_variance\_explained",
sum(pca.explained\_variance\_ratio\_))

Fase 4: Evaluación & Model Health

## Chequeo de Salud del PCA

### Model Health Check

Varianza PC1 + PC2
Objetivo > 40%

Ratio de Compresión
Ideal > 5:1

Error de Reconstrucción
Mínimo

Estabilidad de Cargas
Consistente

# Diagnóstico Distintivo: ¿Qué variables dominan el PC1?
# Si el PC1 solo representa ruido, la salud es Pobre.
loadings = pd.DataFrame(
pca.components\_.T,
columns=[f'PC{i+1}' for i in range(pca.n\_components\_)],
index=X\_train.columns
)
print(loadings['PC1'].sort\_values(ascending=False).head(5))

#### La Trampa de los PCs Irrelevantes

Muchos ingenieros conservan demasiados componentes. Si el componente 15
solo explica el 0.01% de la varianza, es ruido. \*\*Elimínalo\*\*. La meta de PCA es la parsimonia:
explicar lo máximo con lo mínimo.

Fase 5: Deployment & Packaging

## Persistencia del Pipeline Atómico

El objeto PCA por sí solo es peligroso. En producción, el dato de entrada
debe ser escalado exactamente igual que en el entrenamiento.

import joblib
# El artefacto de Serving DEBE ser la dupla inmutable
compression\_bundle = {
"version": "v13.4.0",
"scaler": scaler,
"pca\_model": pca,
"input\_features": list(X\_train.columns)
}
joblib.dump(compression\_bundle, 'sensor\_reducer.joblib')

Fase 6: Monitoring & Reconstruction Drift

## Vigilancia del Espacio Latente

Monitoreamos si el modelo puede seguir reconstruyendo los datos originales a
partir de los componentes (Reconstruction Error).

#### Alertas de Re-entrenamiento:

##### Variance Decay

Si los componentes actuales ya no explican el 95%
de la varianza en producción.

##### Reconstruction Error

Si la diferencia entre el dato original y el
comprimido-recuperado sube > 20%.

Unsupervised Drift Detection

## Checklist de Validación MLOps (PCA)

##### StandardScaler Confirmado

¿Se validó que todas las variables tengan varianza 1 antes del
PCA?

##### Análisis de Kaiser

¿Se eliminaron todos los componentes con autovalores menores a 1?

##### Linealidad Validada

¿Se comprobó que no hay relaciones no lineales fuertes (ej.
curvas) que PCA no capture?

##### Bundling de Inferencia

¿El archivo de despliegue contiene el objeto Scaler ajustado en
entrenamiento?

##### Interpretación de Cargas

¿Se validó qué variables físicas componen los primeros PCs para
dar sentido al modelo?

##### Latencia de Compresión

¿El paso de transformación cumple con el SLA de tiempo real
(sub-milisegundo)?

> [**Algoritmo - Análisis de Componentes Principales**](../Algoritmos/Unsupervised_Learning-PCA.md)
• 
> [**Practica - Análisis de Componentes Principales**](../Sample/Unsupervised_Learning-PCA.md)
• 
> [**Codigo - Agrupamiento Jerárquico**](Unsupervised_Learning-Hierarchical-Clustering.md)
---