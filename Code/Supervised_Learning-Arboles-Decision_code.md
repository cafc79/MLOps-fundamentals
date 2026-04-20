# Decision Trees

# Interpretabilidad Radical en Producción

#### Selección Arquitectónica: ¿Por qué este modelo?

Los Árboles son superiores a modelos de "caja negra" cuando:

• El negocio exige **auditabilidad completa** de cada regla.

• Existen relaciones **no lineales y complejas** entre variables categóricas.

• No se desea realizar **escalado de datos** (los árboles son invariantes a la
escala).

#### Diferenciador Clave: La Caja Blanca

"Un árbol de decisión no solo predice; documenta. Cada rama es una regla de negocio explícita
que permite justificar legalmente por qué un crédito fue aprobado o rechazado."

Fase 1: Ingesta & Data Lineage

## Manejo de Valores Faltantes y Split

Los árboles manejan bien el ruido, pero son extremadamente sensibles a
cambios pequeños en el dataset si no se controlan.

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta desde lago de datos (S3 / DVC)
df = pd.read\_csv('credit\_scoring\_v3.csv')
# Los árboles manejan NaNs (dependiendo de la implementación),
# pero en Scikit-Learn debemos imputar antes del split.
df = df.fillna(df.median())
# Split Estratificado: Mantiene la proporción de morosidad en ambos sets
X\_train, X\_test, y\_train, y\_test = train\_test\_split(
df.drop('solvencia', axis=1),
df['solvencia'],
test\_size=0.25,
stratify=df['solvencia'],
random\_state=42
)

#### Error Común: "Greedy nature"

Confiar en que el árbol encontrará el óptimo global.
Los árboles usan algoritmos codiciosos (greedy) que eligen la mejor división **local**
en cada paso. Esto puede llevar a estructuras ineficientes si no se limitan.

Fase 2: Preprocessing & Codificación

## Manejo de Categorías y "No-Scaling"

Una ventaja distintiva: los árboles no requieren que escales o normalices los
datos numéricos.

from sklearn.preprocessing import
LabelEncoder
# Mejor Práctica: Para árboles, One-Hot Encoding puede crear matrices demasiado
# esparcidas que "confunden" al split. LabelEncoding suele ser más
eficiente.
le = LabelEncoder()
X\_train['tipo\_vivienda'] = le.fit\_transform(X\_train['tipo\_vivienda'])
X\_test['tipo\_vivienda'] = le.transform(X\_test['tipo\_vivienda'])
# NOTA: Saltamos StandardScaler() - Los árboles son invariantes de
escala.

#### Elemento Distintivo: Monotonicidad

El árbol solo mira el orden de los valores, no su magnitud. Esto lo
hace inmune a los **Outliers** en las variables independientes (X).

Fase 3: Entrenamiento & Control de Crecimiento

## Poda (Pruning) e Hiperparámetros

Un árbol sin límites memorizará el ruido. Controlamos la complejidad para
asegurar generalización.

from sklearn.tree import
DecisionTreeClassifier
import mlflow
with mlflow.start\_run(run\_name="credit\_tree\_v1"):
# Max\_depth y min\_samples\_leaf son tus frenos de mano contra el
Overfitting
model = DecisionTreeClassifier(
criterion='gini',
max\_depth=5,
min\_samples\_leaf=20,
class\_weight='balanced' # Manejo de desbalance
interno
)
model.fit(X\_train, y\_train)
# Log de parámetros para MLOps Tracking
mlflow.log\_params({"max\_depth": 5, "criterion": "gini"})

Fase 4: Validación & Diagnóstico

## Salud de la Jerarquía Lógica

### Model Health Check

Gini / Entropía (Pureza)
Target < 0.1 en hojas

Delta Accuracy (Train vs Test)
Tolerancia < 4%

Variable Importance Stability
Consistente

Path Depth (Auditabilidad)
Max 7 niveles

from sklearn.tree import export\_text
# Validación distintiva: Inspección de reglas humanas
tree\_rules = export\_text(model, feature\_names=list(X.columns))
print(tree\_rules)
# Si el árbol es demasiado profundo, la salud es "Pobre"
# porque pierde su valor de interpretabilidad.

#### La Trampa de la Inestabilidad

Pequeños cambios en los datos pueden generar un árbol totalmente
distinto. **Solución:** Valida la importancia de variables con permutaciones para
asegurar que los "nodos raíz" sean estables.

Fase 5: Serving & Registry

## Persistencia de la Estructura

Convertimos el objeto de Python en un servicio que puede responder en
microsegundos.

import joblib
# Bundle de Producción
scoring\_service = {
"model\_version": "v1.0.4",
"encoder\_map": {"vivienda":
le.classes\_.tolist()},
"classifier": model
}
joblib.dump(scoring\_service, 'credit\_engine.joblib')

Fase 6: Monitoring & Logic Drift

## Vigilancia del Comportamiento

Monitorizamos no solo el error, sino si las "hojas" se están llenando de
forma inusual.

#### Alertas MLOps:

##### Distribution Shift

Si un nodo hoja que solía tener 10% de tráfico
ahora tiene 40%.

##### Feature Drift

Si los ingresos de los solicitantes cambian
drásticamente.

Model Governance Active

## Checklist de Validación MLOps

##### Control de Profundidad

¿Se limitó `max\_depth` para evitar que el modelo
sea una copia del set de entrenamiento?

##### Fuga de Datos (Leakage)

¿Se validó que el `LabelEncoder` no vio datos de
test durante su ajuste?

##### Métrica de Pureza

¿Se comparó Gini vs Entropía para asegurar que el
split sea el más informativo?

##### Auditoría Humana

¿Se exportó el árbol a texto/PDF para validación
por los expertos de negocio?

##### Manejo de Desbalance

¿Se usó `class\_weight='balanced'` o técnicas de
muestreo (SMOTE)?

##### Trazabilidad Total

¿Existe el registro en MLflow que asocia este
modelo con el dataset versionado?

> [**Algoritmo - Árboles de Decisión**](../Algoritmos/Supervised_Learning-Arboles-Decision.md)
• 
> [**Practica - Árboles de Decisión**](../Sample/Supervised_Learning-Arboles-Decision.md)
• 
> [**Codigo - K-Means Clustering**](Unsupervised_Learning-K-Means-Clustering.md)
---