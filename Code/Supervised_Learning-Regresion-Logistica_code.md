Pipeline Industrial: Regresión Logística & MLOps

# Regresión Logística

#### ¿Por qué elegir Regresión Logística?

A diferencia de SVM o Bosques, es el estándar cuando:

• Necesitas una **probabilidad calibrada** (0-100%).

• El impacto de las variables es **independiente y aditivo**.

• Se requiere una **solución base (Baseline)** rápida antes de escalar a Deep
Learning.

#### Elemento Distintivo: La Sigmoide

"Su esencia radica en comprimir el espacio lineal infinito en una curva S. Es el modelo más
honesto: si no está seguro, te dará un 0.5, permitiéndote decidir el umbral de riesgo de
negocio."

Fase 1: Ingesta & Estratificación

## Manejo de Desbalance y Split

En clasificación, el error fatal es no considerar la proporción de clases. Si
el 99% de los datos son "No Fraude", un modelo inútil tendrá 99% de precisión.

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta inmutable
df = pd.read\_csv('churn\_data\_v2.csv')
# Validar balance de clases
print(df['target'].value\_counts(normalize=True))
# SPLIT ESTRATIFICADO: Mantiene la proporción de la clase en train y
test
X\_train, X\_test, y\_train, y\_test = train\_test\_split(
df.drop('target', axis=1),
df['target'],
test\_size=0.2,
stratify=df['target'], # CRÍTICO
random\_state=42
)

#### Error Común: Nombre Confuso

Confundirla con una regresión para valores continuos.
La Regresión Logística **es un algoritmo de clasificación**. No intentes predecir el
"precio" de algo con ella; predice la "probabilidad" de que algo suceda.

Fase 2: Preprocessing & Multicolinealidad

## Escalado y Validación Logit

El modelo asume una relación lineal entre las variables y los
**log-odds** del target.

from sklearn.preprocessing import
StandardScaler
from statsmodels.stats.outliers\_influence import variance\_inflation\_factor
# La Logística usa regularización por defecto (L2), requiere escalado
scaler = StandardScaler()
X\_train\_scaled = scaler.fit\_transform(X\_train)
# Chequeo de Multicolinealidad (VIF)
# Si VIF > 5, las variables están correlacionadas y los coeficientes
fallan
vif = [variance\_inflation\_factor(X\_train\_scaled, i) for i in range(X\_train\_scaled.shape[1])]

#### Validación Crucial: Independencia

Asegúrate de que no haya variables que sean derivadas de otras (ej.
Edad y Año de Nacimiento). La Regresión Logística es extremadamente sensible a esto y colapsará en
producción si existen variables redundantes.

Fase 3: Model Training & Tuning

## Regularización y Optimizador

No solo entrenamos; ajustamos la penalización para evitar el sobreajuste.

from sklearn.linear\_model import
LogisticRegression
import mlflow
with mlflow.start\_run():
# C: Inverso de la fuerza de regularización (menor C = más
regularización)
model = LogisticRegression(penalty='l2',
C=1.0, solver='liblinear')
model.fit(X\_train\_scaled, y\_train)
# Log de coeficientes: El impacto marginal real
mlflow.log\_params({"penalty": "l2", "C": 1.0})

Fase 4: Evaluación & Model Health

## Diagnóstico de Clasificación

### Model Health Check

ROC-AUC (Discriminación)
Meta > 0.80

Precision-Recall Balance
F1 > 0.75

Calibración de Prob.
Brier Score < 0.1

Falsos Negativos (Riesgo)
Crítico: < 5%

from sklearn.metrics import
classification\_report, roc\_auc\_score
y\_proba = model.predict\_proba(X\_test\_scaled)[:, 1]
y\_pred = (y\_proba > 0.7).astype(int) # Umbral de negocio conservador
print(classification\_report(y\_test, y\_pred))
print(f"AUC: {roc\_auc\_score(y\_test,
y\_proba)}")

#### La Trampa del Accuracy

Nunca uses el Accuracy en clases desbalanceadas. Un modelo de fraude
con 99.9% de accuracy puede estar fallando en detectar el único caso de fraude que importa.
**Usa el F1-Score o el área bajo la curva Precision-Recall.**

Fase 5: Serving & Registry

## Empaquetado Atómico del Inferencia

El modelo no viaja solo; debe ir acompañado de su escalador para garantizar
la integridad de la entrada.

import joblib
# El "Bundle" de Producción
inference\_service = {
"version": "2.1.0",
"scaler": scaler,
"classifier": model,
"threshold": 0.7 #
Hardcoded por decisión de negocio
}
joblib.dump(inference\_service, 'fraud\_detector.pkl')

Fase 6: Monitoring & Drift

## Vigilancia de la Calibración

Monitoreamos si las probabilidades predichas coinciden con la frecuencia real
observada.

#### Alarmas de Re-entrenamiento:

##### Data Drift

Si la media de los scores de entrada cambia > 10%.

##### Label Shift

Si la proporción de fraude real en el mercado
aumenta.

Continuous Training Active

## Checklist de Validación Industrial

##### Estratificación Confirmada

¿Se usó `stratify` en el split para mantener el
balance de clases?

##### VIF < 5

¿Se eliminaron las variables con alta
multicolinealidad?

##### Métrica Alienada al Negocio

¿Se validó el Recall para minimizar el riesgo de
falsos negativos?

##### Escalador Serializado

¿El bundle de producción incluye el
`StandardScaler` original?

##### Umbral de Decisión Optimizada

¿Se seleccionó el threshold basado en la curva
Precision-Recall y no en 0.5 arbitrario?

##### Tracking de Linaje

¿Existe un rastro (MLflow) que conecte el
artefacto final con el dataset `vX.Y.Z`?

> [**Algoritmo - Regresion Logistica**](../Algoritmos/Supervised_Learning-Regresion-Logistica.md)
• 
> [**Practica - Regresion Logistica**](../Sample/Supervised_Learning-Regresion-Logistica.md)
• 
> [**Codigo - Random Forest**](Supervised_Learning-Random-Forest.md)
---