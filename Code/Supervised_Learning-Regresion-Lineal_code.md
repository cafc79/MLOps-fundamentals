# Regresión Industrial

Ciclo MLOps de 6 Fases •
Caso: Tasación de Activos

La Regresión Lineal es el cimiento de la predicción. En producción, su valor no reside en la
complejidad del modelo, sino en su **explicabilidad radical** y **eficiencia
computacional** extrema.

#### ¿Por qué es el mejor algoritmo aquí?

"Si la relación entre variables es aditiva y lineal, este
modelo ganará por la Navaja de Ockham: es la solución más robusta y menos propensa a sobreajuste
frente a redes neuronales complejas."

Fase 1: Ingesta y Control de Linaje

## Estratificación e Inmutabilidad

El linaje del dato asegura que podamos reproducir un modelo meses después. El split debe ser inmutable
para evitar que el azar contamine los resultados.

import pandas as pd
from sklearn.model\_selection import
train\_test\_split
# Ingesta desde almacenamiento versionado (S3/DVC)
df = pd.read\_csv('housing\_prod\_v1.csv')
# Pre-validación: Eliminar outliers extremos que sesgan la media
df = df[df['price'] < df['price'].quantile(0.99)]
# Split: random\_state=42 es la convención para reproducibilidad
técnica
X\_train, X\_test, y\_train, y\_test = train\_test\_split(
df[['sqft\_living', 'grade', 'condition']],
df['price'],
test\_size=0.2, random\_state=42
)

Error Común

Data Leakage: Normalizar el dataset completo antes
del split. Esto permite que la información de test "ayude" al entrenamiento.

Mejor Práctica

Uso de Semillas: Hard-codear el random\_state
para que otros ingenieros obtengan exactamente tu misma partición.

Fase 2: Preprocesamiento y Supuestos

## Estandarización y Multicolinealidad

La Regresión Lineal asume que las variables son independientes. Debemos validar el **VIF (Variance
Inflation Factor)** para evitar pesos redundantes.

from sklearn.preprocessing import
StandardScaler
from statsmodels.stats.outliers\_influence import variance\_inflation\_factor
# Escalamiento: Obligatorio para comparar coeficientes directamente
scaler = StandardScaler()
X\_train\_scaled = scaler.fit\_transform(X\_train)
X\_test\_scaled = scaler.transform(X\_test)
# Validación distintiva: ¿Hay variables que dicen lo mismo?
vif\_data = [variance\_inflation\_factor(X\_train\_scaled, i) for i in range(X\_train\_scaled.shape[1])]
# Meta: VIF < 5 para todas las variables clave

#### Elemento Distintivo

"A diferencia de una Red Neuronal, aquí los
datos escalados nos permiten extraer los **Pesos Beta**. Un peso de 0.8 en 'Metros' vs
0.2 en 'Estado' nos dice exactamente qué prioriza el modelo."

Fase 3: Entrenamiento y Tracking

## El Laboratorio Trazable

En MLOps, no entrenamos en silencio. Registramos cada versión en un sistema de tracking (ej. MLflow).

from sklearn.linear\_model import
LinearRegression
import mlflow
with mlflow.start\_run(run\_name="linear\_reg\_v1"):
model = LinearRegression()
model.fit(X\_train\_scaled, y\_train)
# Registro de Coeficientes para auditoría legal/XAI
mlflow.log\_params({"features": features\_list,
"intercept": model.intercept\_})
print("Modelo ajustado mediante OLS (Mínimos Cuadrados
Ordinarios)")

Fase 4: Validación y Chequeo de Salud

## Diagnóstico de Residuos

Chequeo de Salud del Modelo
(The Health Check):

1. R² (Bondad de Ajuste)
Requerido: > 0.70

2. Distribución de Errores
Meta: Gaussianos

3. MAE vs Precio Medio
Límite: < 10%

# Validación estadística de Homocedasticidad
residuals = y\_test - model.predict(X\_test\_scaled)
plt.scatter(y\_pred, residuals)
# BUSCA: Una nube aleatoria sin forma de embudo.
# ALERTA: Si hay forma, el modelo es insuficiente.

Error Común

Heterocedasticidad: Ignorar cuando los errores crecen
proporcionalmente al valor. Esto invalida los intervalos de confianza en casas de lujo.

Fase 5: Registro y Empaquetado Atómico

## El Pipeline Inmutable

En producción, el modelo es inútil sin su escalador. Debemos empaquetarlos como una sola unidad lógica.

import joblib
# Empaquetado Atómico: Escalador + Modelo + Versión
model\_artifact = {
"pipeline\_id": "housing\_v1.2.4",
"scaler": scaler,
"model": model,
"input\_schema": ['sqft\_living', 'grade', 'condition']
}
joblib.dump(model\_artifact, 'pricing\_service.joblib')

Fase 6: Monitoreo y Re-entrenamiento

## Detección de Data Drift

El mundo cambia. Si los precios inmobiliarios suben por inflación, el modelo "morirá" (Model Decay).

#### Trigger de Ciclo

- **Programado:** Re-entrenar cada 1ro de mes.
- **Por Deriva:** Si la media de X\_input
  cambia > 15% vs el entrenamiento original.
- **Por Performance:** Si el MAE
  sube del umbral de negocio.

CONTINUOUS TRAINING (CT) ENABLED

DATA OPS

MODEL OPS

DEV OPS

> [**Algoritmo - Regresion Lineal**](../Algoritmos/Supervised_Learning-Regresion_Lineal.md)
• 
> [**Practica - Regresion Lineal**](../Sample/Supervised_Learning-Regresion_Lineal.md)
• 
> [**Codigo - Regresion Logistica**](Supervised_Learning-Regresion_Logistica.md)
---