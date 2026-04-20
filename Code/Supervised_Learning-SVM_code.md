# SVM & MLOps
# Geometría de Decisión y Pipeline MLOps

#### Lógica de Selección: ¿Por qué SVM?

Es el algoritmo superior para clasificación cuando:

• Se dispone de **muestras pequeñas** pero complejas.

• El dataset tiene **alta dimensionalidad** (muchas columnas, pocas filas).

• Se busca una frontera de decisión con un **margen de seguridad** explícito.

• El problema es intrínsecamente no lineal (vía Kernel Trick).

#### Elemento Distintivo: Vectores de Soporte

"A diferencia de otros modelos que miran todos los puntos, SVM solo depende de los
**ejemplos más difíciles** (los que están en el borde). Si un punto lejano cambia,
el modelo no se inmuta; esto le otorga una estabilidad única."

Fase 1: Ingesta & Data Quality

## Limpieza de Outliers y Split Estratificado

SVM es extremadamente sensible a los valores atípicos, ya que un solo outlier
cerca de la frontera puede distorsionar el hiperplano completo.

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta de datos versionados (DVC)
df = pd.read\_csv('medical\_diagnostics\_v1.csv')
# Limpieza de outliers: SVM busca márgenes "limpios"
# Un valor extremo puede forzar un margen muy estrecho.
df = df[df['biomarker\_alpha'].between(df['biomarker\_alpha'].quantile(0.01),
df['biomarker\_alpha'].quantile(0.99))]
# Split: Stratify asegura que la prevalencia de la enfermedad se mantenga
igual
X\_train, X\_test, y\_train, y\_test = train\_test\_split(
df.drop('diagnosis', axis=1),
df['diagnosis'],
test\_size=0.2,
stratify=df['diagnosis'],
random\_state=42
)

#### Error Común: Ignorar el Escalado

SVM maximiza la distancia geométrica. Si una variable
tiene rango 0-1000 y otra 0-1, la primera dominará el cálculo de distancia. **Sin escalado,
SVM es matemáticamente nulo.**

Fase 2: Preprocessing & Kernel Choice

## Estandarización y Selección de Kernel

Debemos decidir si los datos son separables linealmente o si necesitamos
elevar la dimensión mediante un Kernel (RBF, Polinómico).

from sklearn.preprocessing import
StandardScaler
# Estandarización (Z-Score): Crucial para modelos basados en distancia
scaler = StandardScaler()
X\_train\_scaled = scaler.fit\_transform(X\_train)
X\_test\_scaled = scaler.transform(X\_test)
# Mejor Práctica: Si el número de features > número de filas, usa
Kernel='linear'.
# Si no, Kernel='rbf' es el estándar de oro para no-linealidad.

#### Validación de Dimensionalidad

Utiliza PCA antes de SVM si tienes miles de columnas redundantes. SVM
es potente en alta dimensión, pero su coste computacional crece cuadráticamente con el número de
muestras ($N^2$).

Fase 3: Model Training & Hyperparameters

## Optimización de $C$ y $\gamma$

El éxito de SVM depende del balance entre el margen y el error de
clasificación.

from sklearn.svm import SVC
import mlflow
with mlflow.start\_run(run\_name="svm\_rbf\_optimized"):
# C: Penalización del error (Bajo C = Margen suave, Alto C = Margen
duro)
# Gamma: Radio de influencia de un solo ejemplo de entrenamiento
model = SVC(kernel='rbf', C=10.0, gamma='scale', probability=True)
model.fit(X\_train\_scaled, y\_train)
# Tracking de parámetros críticos
mlflow.log\_params({"C": 10.0, "kernel": "rbf",
"support\_vectors": len(model.support\_)})

Fase 4: Evaluación & Model Health

## Diagnóstico de Margen y Confianza

### Model Health Check

Número de Vectores de Soporte
Ideal < 20% del total

Brier Score (Calibración)
Target < 0.15

Recall en Clase Crítica
Mínimo 95%

Estabilidad del Hiperplano
Consistente

from sklearn.metrics import
plot\_roc\_curve
# Validación distintiva: ¿Demasiados vectores de soporte?
# Si el 80% de tus datos son vectores de soporte, el modelo
# está sobreajustando o el margen es demasiado blando.
sv\_ratio = len(model.support\_) / len(X\_train\_scaled)
print(f"Support Vector Ratio:
{sv\_ratio:.2%}")

#### La Trampa del Kernel RBF

Un $\gamma$ muy alto creará "islas" alrededor de cada punto,
memorizando el dataset. Un $\gamma$ muy bajo suavizará tanto el modelo que no aprenderá la forma de
los datos. **Usa Cross-Validation para hallar el dulce punto medio.**

Fase 5: Deployment & Packaging

## Persistencia Atómica

SVM no es solo una ecuación; es una colección de vectores de soporte que
deben viajar con el modelo.

import joblib
# El artefacto de producción DEBE contener el escalador
model\_bundle = {
"version": "v9.2.1",
"pipeline\_type": "SVM\_RBF",
"preprocessor": scaler,
"model": model
}
joblib.dump(model\_bundle, 'svm\_diagnostic\_service.joblib')

Fase 6: Monitoring & Latency

## Vigilancia de la Latencia de Inferencia

A diferencia de la Regresión Lineal, la velocidad de predicción de SVM
depende del número de vectores de soporte.

#### Alertas de Re-entrenamiento:

##### Latency Drift

Si el tiempo de respuesta sube de 50ms (indicador
de complejidad creciente).

##### Concept Drift

Si los biomarcadores del paciente cambian su
distribución vs entrenamiento.

Bio-Governance Active

## Checklist de Validación MLOps (SVM)

##### Escalado Crítico

¿Se validó que los datos tienen media 0 y varianza
1 antes del fit?

##### Consistencia de Soporte

¿El número de vectores de soporte es razonable
para evitar el overfitting?

##### Calibración de Probabilidad

¿Se activó `probability=True` (Platt Scaling) si
el negocio requiere % de confianza?

##### Kernel Benchmarking

¿Se probó un LinearSVM contra un RBF para
justificar la complejidad extra?

##### Bundling Inseparable

¿El archivo de despliegue contiene el objeto
`StandardScaler` original?

##### Trazabilidad en MLflow

¿Están registrados los valores óptimos de $C$ y
$\gamma$ vinculados al commit de Git?

> [**Algoritmo - Máquinas de Vectores de Soporte**](../Algoritmos/Supervised_Learning-SVM.md)
• 
> [**Practica - Máquinas de Vectores de Soporte**](../Sample/Supervised_Learning-SVM.md)
• 
> [**Codigo - Naive Bayes**](Supervised_Learning-Naive-Bayes.md)
---