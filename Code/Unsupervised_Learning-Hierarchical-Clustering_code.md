# Agrupamiento Jerárquico & MLOps

# Clustering Jerárquico

Descubrimiento Taxonómico y
Pipeline MLOps

#### Lógica de Selección: ¿Por qué este algoritmo?

Se prefiere sobre K-Means o DBSCAN cuando:

• Se busca entender la **relación de parentesco** entre grupos.

• El número de clusters (K) no es conocido y se desea inspeccionar la
**granularidad**.

• El dataset es pequeño o mediano (debido a complejidad computacional).

• Se requiere un **dendrograma** para validación por expertos de dominio.

#### Elemento Distintivo: El Dendrograma

"A diferencia de las particiones planas, el Agrupamiento Jerárquico ofrece un mapa genético de
los datos. Permite decidir el nivel de corte 'post-hoc', visualizando cómo los micro-grupos se
fusionan en macro-categorías."

Fase 1: Ingesta & Data Quality

## Manejo de Distancias y Outliers

El Agrupamiento Jerárquico es extremadamente sensible a los outliers,
especialmente con el método de 'Single Linkage', que puede generar el "Efecto Cadena".

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta versionada de datos taxonómicos
df = pd.read\_csv('product\_taxonomy\_v2.csv')
# TRATAMIENTO CRÍTICO: Los outliers pueden unir clusters que deberían estar
separados.
# Usamos aislamiento por desviación estándar para limpiar la muestra.
df\_clean = df[df['price\_index'].between(df['price\_index'].mean() - 3\*df['price\_index'].std(),
df['price\_index'].mean() + 3\*df['price\_index'].std())]
# Split: Mantenemos un set de validación para probar la estabilidad del
árbol.
train\_set, val\_set = train\_test\_split(df\_clean, test\_size=0.2, random\_state=42)

#### Error Común: Escala de Atributos

Al basarse en matrices de proximidad, si una variable
tiene una escala mayor, dictará toda la jerarquía. **Sin normalización, los resultados son
ruido matemático.**

Fase 2: Preprocessing & Proximity Matrix

## Estandarización y Métricas de Enlace

Debemos transformar los datos para que todas las dimensiones contribuyan
equitativamente a la "distancia".

from sklearn.preprocessing import
StandardScaler
from scipy.cluster.hierarchy import
linkage, dendrogram
# Estandarización Z-Score
scaler = StandardScaler()
X\_scaled = scaler.fit\_transform(train\_set)
# Cálculo de la matriz de enlace (Linkage Matrix)
# 'ward' minimiza la varianza dentro de los clusters (Estándar
Industrial)
Z = linkage(X\_scaled, method='ward',
metric='euclidean')

#### Validación Crucial: Linkage Method

Usa **Ward** si buscas clusters esféricos
y equilibrados. Usa **Complete** para evitar el efecto cadena de Single. Ward es
generalmente la opción más estable para segmentación de clientes.

Fase 3: Model Training & Dendrogram Analysis

## Construcción del Árbol de Decisiones

No entrenamos una partición plana; entrenamos la historia completa de
fusiones y la registramos en el tracking server.

from sklearn.cluster import
AgglomerativeClustering
import mlflow
with mlflow.start\_run(run\_name="hierarchical\_v1"):
# Definimos el corte basado en la inspección visual del dendrograma
model = AgglomerativeClustering(n\_clusters=4,
linkage='ward')
labels = model.fit\_predict(X\_scaled)
# Log de parámetros de MLOps
mlflow.log\_params({"linkage": "ward", "n\_clusters": 4})

Fase 4: Evaluación & Model Health Check

## Diagnóstico de la Estructura Jerárquica

### Model Health Check

Correlación Cofenética
Objetivo > 0.75

Coeficiente de Silueta
Ideal > 0.45

Invarianza de Muestreo
Bootstrap estable

Cluster Size Ratio
Max 5:1 entre
mayor/menor

from scipy.cluster.hierarchy import
cophenet
from scipy.spatial.distance import
pdist
# Validación distintiva: Correlación Cofenética
# Mide qué tan bien el dendrograma preserva las distancias
originales.
c, coph\_dists = cophenet(Z, pdist(X\_scaled))
print(f"Cophenetic Correlation: {c:.4f}")
# Si c < 0.7, la jerarquía es forzada y no representa la realidad.

#### La Trampa de la Memoria

El Agrupamiento Jerárquico tiene una complejidad temporal de $O(n^3)$ y
espacial de $O(n^2)$. En producción, si tu dataset crece a millones de filas, este algoritmo
colapsará. \*\*Considera usar BIRCH como alternativa jerárquica para Big Data.\*\*

Fase 5: Deployment & Packaging

## Persistencia de la Taxonomía

El modelo no puede predecir nuevos puntos fácilmente (nativamente). Debemos
desplegar un clasificador adjunto o usar el modelo para etiquetado masivo.

import joblib
# Empaquetado inmutable: Scaler + Clusterer Labels + Z Matrix
hierarchy\_bundle = {
"v": "14.0.1",
"preprocessor": scaler,
"linkage\_matrix": Z,
"assignment\_model": model
}
joblib.dump(hierarchy\_bundle, 'product\_hierarchy.joblib')

Fase 6: Monitoring & Structure Drift

## Vigilancia de la Estabilidad del Árbol

Monitoreamos si la introducción de nuevos productos rompe la estructura
jerárquica establecida.

#### Alertas MLOps:

##### Linkage Drift

Si la distancia de fusión del nodo raíz cambia >
20%.

##### Cluster Fragmentation

Si un cluster consolidado empieza a dividirse en
sub-ramas inestables.

Hierarchical CT Pipeline

## Checklist de Validación MLOps (HC)

##### Normalización Z-Score

¿Se garantizó que ninguna variable domine la distancia por su
magnitud?

##### Cofenet Check > 0.75

¿El dendrograma es una representación fiel de las distancias
originales?

##### Invarianza a Outliers

¿Se aplicó una limpieza previa para evitar distorsiones en la
unión de ramas?

##### Validación de Enlace (Linkage)

¿Se comparó Ward vs Complete para elegir la estructura más
compacta?

##### Consistencia de Granularidad

¿El nivel de corte (K) tiene sentido comercial para los expertos
humanos?

##### Linaje de Artefactos

¿Está el link de la matriz de enlace versionado junto al dataset
`vX.X`?

> [**Algoritmos - Agrupamiento Jerárquico**](../Algoritmos/Unsupervised_Learning-Hierarchical-Clustering.md)
• 
> [**Practica - Agrupamiento Jerárquico**](../Sample/Unsupervised_Learning-Hierarchical-Clustering.md)
• 
> [**Codigo - Q-Learning**](Reinforcement_Learning-Q-Learning.md)
---