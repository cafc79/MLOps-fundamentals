# K-Means Industrial

Segmentación No Supervisada y MLOps

#### Lógica de Selección: ¿Por qué K-Means?

Es el estándar para descubrimiento de arquetipos cuando:

• No existen etiquetas previas (Aprendizaje No Supervisado).

• Se busca \*\*cohesión interna\*\* y máxima \*\*separación\*\* entre grupos.

• La escalabilidad a millones de registros es crítica (Mini-Batch).

• Se requiere una interpretación geométrica clara (Centroides).

#### Diferenciador: El Centroide

"K-Means no solo agrupa; crea 'puntos ideales'. El centroide de un grupo de clientes VIP define
el comportamiento promedio de ese segmento, permitiendo crear estrategias de marketing
quirúrgicas."

Fase 1: Ingesta & Data Lineage

## Tratamiento de Outliers y Muestreo

K-Means usa medias aritméticas; por tanto, un solo valor atípico puede
desplazar el centroide de forma catastrófica.

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta desde repositorio inmutable
df = pd.read\_csv('customer\_behavior\_v2.csv')
# VALIDACIÓN CRÍTICA: Eliminar outliers antes de calcular centroides
# K-means es extremadamente sensible a puntos extremos (distancia
euclidiana)
q\_low = df["spending"].quantile(0.01)
q\_hi = df["spending"].quantile(0.99)
df\_filtered = df[(df["spending"] < q\_hi) & (df[
"spending"] > q\_low)]
# Split: En clustering, usamos el test set para validar estabilidad de
grupos
train\_data, test\_data = train\_test\_split(df\_filtered, test\_size=0.2, random\_state=42)

#### Error Común: Ignorar la Escala

K-Means se basa en distancias. Si los "Ingresos" están
en miles y la "Edad" en unidades, el algoritmo ignorará la edad por completo. **El escalado es
mandatorio.**

Fase 2: Preprocessing & Dimensionality

## Escalado Robusto y Selección de Atributos

Buscamos variables que aporten variabilidad. Si todas las variables tienen la
misma varianza, los clusters no serán claros.

from sklearn.preprocessing import
StandardScaler
from sklearn.decomposition import PCA
# Estandarización (Z-Score)
scaler = StandardScaler()
X\_train\_scaled = scaler.fit\_transform(train\_data)
# Elemento Distintivo: PCA para visualización de clusters
# Reducimos a 2D solo para validar visualmente la separación de grupos
pca = PCA(n\_components=2)
X\_visual = pca.fit\_transform(X\_train\_scaled)

#### Mejor Práctica: Reducción de Dimensionalidad

Evita usar demasiadas variables. K-Means sufre con la "maldición de
la dimensionalidad". Selecciona solo los 3-5 drivers de comportamiento más potentes (ej. RFM:
Recency, Frequency, Monetary).

Fase 3: Model Training & Finding K

## Método del Codo y Coeficiente de Silueta

No adivinamos K; lo optimizamos mediante métricas de inercia y tracking de
experimentos.

from sklearn.cluster import KMeans
from sklearn.metrics import
silhouette\_score
import mlflow
with mlflow.start\_run():
# n\_init=10 asegura que probamos diferentes puntos de inicio aleatorios
model = KMeans(n\_clusters=5, n\_init=10, init='k-means++', random\_state=42)
model.fit(X\_train\_scaled)
# Métricas de validación de cluster
inertia = model.inertia\_
sil\_score = silhouette\_score(X\_train\_scaled, model.labels\_)
mlflow.log\_metrics({"inertia": inertia, "silhouette": sil\_score})

Fase 4: Evaluación & Model Health

## Diagnóstico de Estabilidad

### Model Health Check

Silhouette Coefficient
Ideal > 0.5

Cluster Size Balance
Sin grupos vacíos

Centroid Stability
Variación < 5%

Separación Inter-Cluster
Máxima

#### Validación de Negocio (Profiling)

"Un cluster es saludable solo si el equipo de
marketing puede ponerle un nombre comercial."

- • **Cluster 0:** 'Campeones' (Gasto alto, frecuencia alta).
- • **Cluster 1:** 'En Riesgo' (Gasto bajo, mucha inactividad).
- • **Cluster 2:** 'Nuevas Promesas' (Gasto medio, registro reciente).

#### La Trampa de los Mínimos Locales

K-Means puede converger en una mala solución dependiendo de dónde
empiecen los centroides. **Usa siempre `init='k-means++'`** para una
inicialización inteligente y `n_init` alto para asegurar que encuentras el mejor
agrupamiento global.

Fase 5: Serving & Registry

## Empaquetado Atómico del Segmentador

El modelo de producción debe ser capaz de asignar un nuevo cliente a un
cluster en milisegundos.

import joblib
# El bundle DEBE incluir el scaler original
segmentation\_service = {
"v": "1.0.2",
"preprocessor": scaler,
"clusterer": model
}
joblib.dump(segmentation\_service, 'customer\_segmenter.pkl')
# Inferencia: scaler.transform(new\_x) -> model.predict(scaled\_x)

Fase 6: Observation & Drift

## Vigilancia de la Migración de Centroides

Monitoreamos si los clientes están cambiando su comportamiento base, lo que
requeriría un re-posicionamiento de los grupos.

#### Alertas MLOps:

##### Centroid Drift

Si la distancia entre los centroides de producción
vs entrenamiento crece > 10%.

##### Cluster Depletion

Si un cluster se queda sin miembros (indicativo de
cambio radical en el mercado).

Unsupervised Continuous Training

## Checklist de Validación MLOps (K-Means)

##### Escalado de Atributos

¿Se utilizó `StandardScaler` para evitar que las
unidades distorsionen la distancia?

##### Optimización de K (Elbow)

¿Se validó el punto de inflexión de la inercia para evitar
sobre-segmentación?

##### Tratamiento de Nulos

¿Se imputaron o eliminaron valores faltantes? K-Means no tolera
NaNs.

##### Invarianza de Semilla

¿Se fijó el `random_state` para asegurar que los
clusters no cambien en cada despliegue?

##### Profiling de Perfil

¿Cada cluster tiene una descripción cualitativa validada por el
área de negocio?

##### Integridad del Bundle

¿El archivo exportado contiene el `Scaler` ajustado
exclusivamente con datos de entrenamiento?

> [**Algoritmo - K-Means Clustering**](../Algoritmo/Unsupervised_Learning-K-Means-Clustering.md)
• 
> [**Practica - K-Means Clustering**](../Sample/Unsupervised_Learning-K-Means-Clustering.md)
• 
> [**Codigo - Análisis de Componentes Principales**](Unsupervised_Learning-PCA.md)
---