# MLP Industrial

# Redes Neuronales Feedforward y Ecosistema MLOps

#### Lógica de Selección: ¿Por qué MLP?

Se elige sobre modelos lineales o de ensamble cuando:

• Existen \*\*interacciones no lineales de alto orden\*\* entre variables.

• Se requiere un \*\*Aproximador Universal\*\* para funciones complejas.

• Los datos son densos, continuos y están bien estructurados.

• Se busca integrar el modelo en un ecosistema de \*\*Deep Learning\*\* (PyTorch/TensorFlow).

#### Elemento Distintivo: Capas Ocultas

"El MLP trasciende la regresión al introducir capas ocultas que actúan como extractores
automáticos de características. No necesita que le digas cómo interactúan las variables; la red
lo 'descubre' mediante el ajuste de pesos."

Fase 1: Ingesta & Data Quality

## Split Determinista y Fuga de Datos

En aprendizaje profundo, el volumen de datos es clave, pero la integridad del
split es sagrada. Un error aquí invalida la capacidad de generalización de la red.

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta desde repositorio versionado
df = pd.read\_csv('risk\_data\_v16.csv')
# Gestión de Nulos: MLP no tolera valores faltantes
df = df.fillna(df.median())
# Split: Stratify asegura que la proporción del target sea idéntica
X\_train, X\_test, y\_train, y\_test = train\_test\_split(
df.drop('target', axis=1),
df['target'],
test\_size=0.2,
stratify=df['target'],
random\_state=42
)

#### Error Común: Mezcla de Datos (Leakage)

Entrenar el escalador con el dataset completo. Las
redes neuronales son "esponjas" de información; si el escalador conoce el rango de los datos de
test, el modelo sobrestimará su propia precisión.

Fase 2: Preprocessing & Scaling

## El Oxígeno del MLP: Estandarización

Debido a funciones de activación como Sigmoide o Tanh, las entradas deben
estar en rangos pequeños para evitar la saturación del gradiente.

from sklearn.preprocessing import
StandardScaler
# SIN ESTANDARIZACIÓN, EL MLP NO CONVERGE CORRECTAMENTE
scaler = StandardScaler()
X\_train\_scaled = scaler.fit\_transform(X\_train)
X\_test\_scaled = scaler.transform(X\_test)
# Validación Distintiva: Comprobar que media ~ 0 y std ~ 1
print(X\_train\_scaled.mean(axis=0))

#### Mejor Práctica: One-Hot Encoding

A diferencia de los árboles, los MLP requieren que
las variables categóricas sean convertidas en vectores binarios (One-Hot), ya que la red
interpretará números secuenciales como magnitudes de peso erróneas.

Fase 3: Model Development & Tracking

## Arquitectura y Optimización Adam

Definimos la topología de la red. Cada capa oculta aumenta la capacidad de
representación pero también el riesgo de overfitting.

from sklearn.neural\_network import
MLPClassifier
import mlflow
with mlflow.start\_run(run\_name="mlp\_deep\_risk\_v1"):
# Arquitectura: 2 capas ocultas de 100 y 50 neuronas
model = MLPClassifier(
hidden\_layer\_sizes=(100, 50),
activation='relu',
solver='adam',
alpha=0.0001, # Regularización L2
learning\_rate\_init=0.001,
max\_iter=500,
early\_stopping=True, # MLOps best
practice
random\_state=42
)
model.fit(X\_train\_scaled, y\_train)
# Registro de hiperparámetros
mlflow.log\_params({"layers": "100,50", "solver": "adam"})

Fase 4: Evaluación & Model Health

## Diagnóstico de Convergencia de Pérdida

### Model Health Check

Loss Convergence
Objetivo: Estable

Generalization Gap
Delta < 5%

Dead Neurons Check
Pocas/Ninguna

Confidence Calibration
Score ECE bajo

import matplotlib.pyplot as plt
# Validación distintiva: Curva de Pérdida
# Si la pérdida no baja o es errática, el learning rate es muy alto.
plt.plot(model.loss\_curve\_)
plt.title('Convergencia de Entrenamiento')
# Si hay un salto enorme entre train y validación: OVERFITTING.

#### La Trampa del Mínimo Local

El MLP puede quedar atrapado en una mala solución. \*\*Mejor Práctica:\*\*
Usa siempre `early_stopping=True` para detener el entrenamiento cuando el error de
validación deje de mejorar, salvando la mejor versión del modelo.

Fase 5: Deployment & Artifact Registry

## Persistencia de Pesos y Sesgos

Una red neuronal es una colección de matrices. El empaquetado debe ser
inmutable y contener el preprocesador.

import joblib
# El "Bundle" de Producción
neural\_service = {
"v": "16.4.2",
"input\_scaler": scaler,
"mlp\_weights": model
}
# Inferencia: scaler.transform -> model.predict\_proba
joblib.dump(neural\_service, 'risk\_neural\_engine.joblib')

Fase 6: Monitoring & Performance Drift

## Vigilancia de la Distribución de Salida

Las redes neuronales pueden fallar silenciosamente. Monitoreamos el
histograma de las probabilidades predichas.

#### Alertas MLOps (Neural):

##### Probability Shift

Si el modelo solía predecir 10% de riesgo y ahora
predice 40% súbitamente.

##### Input Covariate Drift

Si la media de las características escaladas se
aleja de 0 significativamente.

Deep Learning CT Pipeline

## Checklist de Validación MLOps (MLP)

##### Estandarización Rigurosa

¿Se garantizó que la entrada a la red tenga media 0 y varianza 1?

##### Validación de Arquitectura

¿Se probó que una red más pequeña no obtiene el mismo resultado?
(Evitar sobre-complejidad).

##### Early Stopping Activo

¿Existe un mecanismo de parada automática para prevenir la
memorización del dataset?

##### Bundling de Transformadores

¿El artefacto exportado incluye el objeto StandardScaler exacto
usado en entrenamiento?

##### Calibration Check

¿Las probabilidades predichas (predict\_proba) reflejan la
frecuencia real de los eventos?

##### Tracking de Linaje

¿Está la corrida de entrenamiento vinculada a la versión del
código en Git y al hash del dato?

> [* Algoritmo - Perceptrón Multicapa *](../algoritmos/Deep_Learning-Perceptron-Multicapa.md)
 • 
> [* Practica - Perceptrón Multicapa *](../Sample/Deep_Learning-Perceptron-Multicapa.md)
 • 
> [* Codigo - Redes Neuronales Convolucionales *](Deep_Learning-CNN.md)
---