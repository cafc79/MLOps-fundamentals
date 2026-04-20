# Naive Bayes


#### Lógica de Selección: ¿Por qué Naive Bayes?

Es el algoritmo de referencia para clasificación de texto cuando:

• Se requiere una **velocidad de entrenamiento** casi instantánea.

• El dataset tiene **alta dimensionalidad** (vocabulario masivo).

• Se necesita un **Baseline robusto** para comparar contra modelos de Deep
Learning (Transformers).

• Los datos son escasos y la independencia de variables es una suposición aceptable.

#### Elemento Distintivo: Independencia Condicional

"Naive Bayes es 'ingenuo' porque asume que la presencia de una palabra es independiente de las
demás. Aunque esto es falso en el lenguaje, matemáticamente permite una eficiencia imbatible en
Big Data."

Fase 1: Ingesta & Text Preprocessing

## Tokenización y Limpieza de Corpus

La calidad del modelo Bayesiano depende de la pureza del vocabulario. El
error común es dejar "ruido" que infla las probabilidades de forma errónea.

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta inmutable desde repositorio de datos
df = pd.read\_csv('spam\_corpus\_v1.csv')
# Limpieza de texto (Lowercasing, Stopwords, No-Punctuation)
# El algoritmo es sensible a palabras que no aportan valor semántico.
df['clean\_text'] = df['text'].str.lower().replace(r'[^\w\s]', '', regex=True)
# Split Estratificado: Mantiene la proporción de Spam/Ham
X\_train, X\_test, y\_train, y\_test = train\_test\_split(
df['clean\_text'],
df['label'],
test\_size=0.2,
stratify=df['label'],
random\_state=42
)

#### Error Común: Mezcla de Vocabularios

Ajustar el Vectorizador (TF-IDF/Count) con todo el
dataset. Esto es **Data Leakage**: el modelo conoce palabras del set de prueba antes de
tiempo. Ajusta `fit` solo en Train.

Fase 2: Vectorización & TF-IDF

## Transformación a Bolsa de Palabras

Convertimos texto en números. Naive Bayes Multinomial funciona mejor con
frecuencias de términos (TF-IDF).

from sklearn.feature\_extraction.text import TfidfVectorizer
# Mejor Práctica: Limitar max\_features para evitar overfitting en palabras
raras
vectorizer = TfidfVectorizer(max\_features=5000,
stop\_words='english')
# fit\_transform solo en TRAIN
X\_train\_tfidf = vectorizer.fit\_transform(X\_train)
# transform solo en TEST (usando el vocabulario de train)
X\_test\_tfidf = vectorizer.transform(X\_test)

#### Diferenciador: Multinomial vs Bernoulli

Usa **MultinomialNB** si cuentas cuántas veces aparece
una palabra (frecuencia). Usa **BernoulliNB** si solo te importa si la palabra aparece
o no (0 o 1). Para texto largo, Multinomial es el estándar.

Fase 3: Model Training & Laplace Smoothing

## El Truco de Laplace (Alpha)

Si una palabra nueva aparece en producción, su probabilidad sería 0 y
anularía todo el cálculo. Usamos **Suavizado de Laplace** para evitarlo.

from sklearn.naive\_bayes import
MultinomialNB
import mlflow
with mlflow.start\_run(run\_name="naive\_bayes\_baseline"):
# alpha=1.0 es el suavizado de Laplace por defecto
model = MultinomialNB(alpha=1.0)
model.fit(X\_train\_tfidf, y\_train)
# Registro de parámetros en MLOps tracking
mlflow.log\_param("alpha", 1.0)
mlflow.log\_param("vocab\_size", 5000)

Fase 4: Evaluación & Model Health

## Diagnóstico de Probabilidades Calibradas

### Model Health Check

Precision (Evitar Falsos Positivos)
Target > 0.99

Recall (Captura de Spam)
Meta > 0.90

Log-Loss (Error Probabilístico)
Bajo

Ratio Ham/Spam en Preds
Equilibrado

from sklearn.metrics import
classification\_report, confusion\_matrix
y\_pred = model.predict(X\_test\_tfidf)
# En Spam, el Precision es REY.
# No queremos mover un correo importante a la papelera.
print(classification\_report(y\_test, y\_pred))
# Validación distintiva: ¿Predice con 0 o 1?
# Naive Bayes tiende a dar probabilidades extremas
(sobre-confianza).

#### La Trampa de la Sobre-confianza

Debido a la asunción de independencia, Naive Bayes suele dar
probabilidades de 0.999 o 0.001, sin puntos medios. \*\*No confíes ciegamente en el porcentaje de
probabilidad\*\*, confía en la métrica de Precision del set de test.

Fase 5: Serving & In-Memory Efficiency

## Empaquetado Atómico del Servicio

El modelo es extremadamente ligero (pocos KBs). Debe viajar con su
vocabulario (Vectorizer) para poder procesar texto crudo en la API.

import joblib
# El bundle de producción: Vectorizador + Clasificador
spam\_service\_bundle = {
"version": "1.0.4",
"vectorizer": vectorizer,
"model": model
}
joblib.dump(spam\_service\_bundle, 'spam\_filter\_v1.joblib')

Fase 6: Monitoring & Language Drift

## Vigilancia del Slang y Vocabulario

El lenguaje evoluciona. Si los spammers empiezan a usar palabras nuevas (ej.
emojis o términos de crypto), el modelo fallará por obsolescencia.

#### Alertas de Re-entrenamiento:

##### Vocabulary Drift

Si el 30% de las palabras entrantes no están en el
vocabulario entrenado.

##### Precision Drop

Si los usuarios marcan como "No es Spam" correos
filtrados por el modelo.

Continuous Learning Sync

## Checklist de Validación MLOps (NB)

##### Laplace Smoothing Activo

¿Se validó que alpha > 0 para evitar el colapso ante palabras
desconocidas?

##### Fit only on Train

¿Se garantizó que el Vectorizer no vio los datos de test durante
el ajuste?

##### Precision Benchmark

¿El precision en la clase Spam es superior al 99% para evitar
falsos positivos críticos?

##### Bundling Vectorizer

¿El artefacto exportado incluye el objeto TF-IDF ajustado
exactamente al vocabulario?

##### Inferencia Sub-milisecond

¿Se verificó que el tiempo de respuesta es apto para filtrado en
tiempo real?

##### Lineage en MLflow

¿Está el modelo vinculado a la versión exacta del corpus de
entrenamiento?

> [**Algoritmo - Naive-Bayes**](../algoritmos/Supervised_Learning-Naive-Bayes.md)
• 
> [**Practica - Naive-Bayes**](../Sample/Supervised_Learning-Naive-Bayes.md)
• 
> [**Codigo - Regresion Lineal**](Supervised_Learning-K-Nearest-Neighbors.md)
---