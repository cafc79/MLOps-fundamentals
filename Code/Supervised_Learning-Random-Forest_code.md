# Random Forest & MLOps

# Ingeniería de Ensamble y Ciclo MLOps

#### Criterios de Selección: ¿Por qué Random Forest?

Es el algoritmo "Estado del Arte" para datos tabulares cuando:

• Existen relaciones **no lineales y complejas**.

• El dataset tiene **muchas variables** (High Dimensionality).

• Se busca resistencia al **sobreajuste** sin tunear demasiados parámetros.

• Se requiere una validación interna robusta sin sacrificar datos (OOB Error).

#### Elemento Distintivo: Bagging

"A diferencia de los modelos lineales, Random Forest utiliza la **sabiduría de las
masas**. Reduce la varianza promediando cientos de árboles descorrelacionados,
convirtiéndose en uno de los modelos más estables para producción."

Fase 1: Ingesta & Data Lineage

## Muestreo Aleatorio y Estratificación

La calidad del bosque depende de la diversidad de los datos. En problemas de
fraude, el split debe ser quirúrgico para capturar la clase minoritaria.

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta versionada (DVC / Snapshot)
df = pd.read\_csv('fraud\_dataset\_v4.csv')
# Identificar desbalance: Fraude suele ser < 1%
print(df['is\_fraud'].value\_counts(normalize=True))
# Split Estratificado: Obligatorio para mantener la señal de fraude en
test
X\_train, X\_test, y\_train, y\_test = train\_test\_split(
df.drop('is\_fraud', axis=1),
df['is\_fraud'],
test\_size=0.2,
stratify=df['is\_fraud'],
random\_state=42
)

#### Error Común: Ignorar el Desbalance

Entrenar un bosque en datos altamente desbalanceados
sin ajustar pesos. El modelo aprenderá que "nunca hay fraude" y tendrá 99.9% de precisión, pero 0%
de utilidad de negocio.

Fase 2: Preprocessing & Supuestos

## Codificación Invariante de Escala

Una de las mayores ventajas: Random Forest **no requiere escalado de
características**. Es inmune a las magnitudes de las variables.

from sklearn.preprocessing import
OrdinalEncoder
# Mejor Práctica: Para modelos de árboles, el OrdinalEncoding es preferible
# al One-Hot masivo, ya que evita la dispersión extrema de datos.
encoder = OrdinalEncoder(handle\_unknown='use\_encoded\_value', unknown\_value=-1)
X\_train\_encoded = encoder.fit\_transform(X\_train)
X\_test\_encoded = encoder.transform(X\_test)
# NOTA: No usamos StandardScaler(). Los árboles deciden por umbrales, no
distancias.

#### Diferenciador: Inmunidad a Outliers

A diferencia de la Regresión Lineal, los valores atípicos (outliers)
en las X no distorsionan el modelo, ya que solo afectan a un nodo, no a la "pendiente" global.

Fase 3: Model Training & Experiment Tracking

## El Comité de Expertos (Ensamble)

Configuramos el bosque para que sea robusto mediante el uso de
**Out-of-Bag Score** para validación inmediata.

from sklearn.ensemble import
RandomForestClassifier
import mlflow
with mlflow.start\_run(run\_name="random\_forest\_prod\_v1"):
model = RandomForestClassifier(
n\_estimators=200, # Cantidad de árboles
max\_depth=15, # Control de complejidad
class\_weight='balanced', # Corrección de desbalance
automática
oob\_score=True, # Validación "gratis" con datos
no usados
random\_state=42,
n\_jobs=-1 # Paralelización total
)
model.fit(X\_train\_encoded, y\_train)
# Registro en MLflow
mlflow.log\_metric("oob\_score",
model.oob\_score\_)

Fase 4: Evaluación y Chequeo de Salud

## Diagnóstico de Ensamble

### Model Health Check

OOB Score (Consistencia)
Objetivo > 0.85

ROC-AUC (Discriminación)
Meta > 0.90

Train vs OOB Gap
Overfitting < 5%

Precision-Recall AUC
Alta en Fraude

from sklearn.metrics import
classification\_report
# Validación por Importancia de Variables
importances = pd.Series(model.feature\_importances\_, index=X.columns)
importances.nlargest(5).plot(kind='barh')
# Elemento Distintivo: Si la importancia es dominada
# por una sola variable sospechosa, revisa si hay leakage.

#### Trampa: Curva de Complejidad

Aumentar `n_estimators` mejora el modelo pero aumenta
linealmente la latencia y el peso del archivo. **Mejor Práctica:** Encuentra el punto
donde el error OOB se estabiliza (usualmente entre 100 y 300 árboles) y detente ahí.

Fase 5: Serving & Artifact Registry

## Empaquetado de la Selva Digital

El archivo de un Random Forest puede ser pesado (varios MB). Usamos
compresión para optimizar el despliegue en microservicios.

import joblib
# Bundle Atómico: Encoder + Bosque
model\_package = {
"metadata": {"version": "1.0.0", "framework": "sklearn-1.4"},
"transformer": encoder,
"forest": model
}
# Compresión nivel 3 para reducir peso del artefacto
joblib.dump(model\_package, 'fraud\_service\_bundle.joblib', compress=3)

Fase 6: Observabilidad & Data Drift

## Vigilancia de la Estabilidad

Monitoreamos el cambio en el comportamiento de las variables clave que el
bosque identificó como importantes.

#### Alertas de Re-entrenamiento:

##### Feature Drift

Si el monto promedio de transacciones cambia > 20%
vs entrenamiento.

##### Model Degradation

Si el Precision de la clase Fraude baja de 0.85 en
producción.

Continuous Training (CT) Pipeline

## Checklist de Validación MLOps

##### Estratificación Confirmada

¿Se utilizó `stratify` para evitar que el set de
test sea ciego al fraude?

##### Análisis OOB vs Test

¿Son las métricas OOB consistentes con los
resultados del set de test?

##### Clase Balanceada

¿Se aplicó `class\_weight='balanced'` para
penalizar errores en fraude?

##### Empaquetado de Transformador

¿El bundle incluye el `OrdinalEncoder` ajustado
para el preprocesamiento?

##### Validación de Latencia

¿El tiempo de inferencia cumple el SLA del negocio
(ej. < 50ms)?

##### Trazabilidad en Registry

¿El modelo está vinculado a una versión inmutable
del dataset en el registro?

> [**Algoritmo - Random Forest**](../Algoritmos/Supervised_Learning-Random-Forest.md)
• 
> [**Sample - Random Forest**](../Sample/Supervised_Learning-Random-Forest.md)
• 
> [**Codigo - Regresion Lineal**](Supervised_Learning-SVM.md)
---