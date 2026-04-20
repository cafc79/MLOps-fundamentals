# Modelos de Clasificación (Supervisados)

# Regresión Logística

A pesar de su nombre, la Regresión Logística es el algoritmo fundamental para problemas de clasificación
binaria, prediciendo la probabilidad de que una instancia pertenezca a una categoría específica.

**Guía del Algoritmo:** Haz clic en cada tarjeta para
explorar la transición de valores continuos a categorías binarias y la función Sigmoide.

1

### Naturaleza Binaria

A diferencia de la regresión lineal, este algoritmo predice etiquetas
discretas (0 o 1, Sí o No).

Se utiliza cuando la variable dependiente es categórica. Es el estándar para detectar correos
spam, diagnosticar enfermedades o predecir si un cliente abandonará un servicio (churn).

Resultados Categóricos

Probabilidad de Pertenencia

Clasificación de Clases

2

### Función Sigmoide

La magia matemática: comprime cualquier valor de entrada a un rango
entre 0 y 1.

Representada por **σ(z) = 1 / (1 + e⁻ᶻ)**. Esta curva en forma de "S" permite
interpretar el resultado del modelo como una probabilidad porcentual.

Mapeo de (0, 1)

Transformación Logística

Suavizado de Salida

3

### Log-Odds (Logit)

El modelo calcula el logaritmo de las "posibilidades" de éxito frente
a las de fracaso.

Permite que la relación entre las variables independientes y la probabilidad sea lineal en
términos de log-odds, facilitando el cálculo de coeficientes interpretables.

Probabilidad vs Ratio

Interpretación de Coeficientes

Base del Modelo Lineal

4

### Umbral (Threshold)

El punto de corte que decide si una probabilidad se convierte en Clase
A o Clase B.

Normalmente fijado en **0.5**: si la probabilidad es > 0.5, es Clase 1. Sin
embargo, en medicina o fraude, este umbral puede ajustarse para ser más o menos estricto.

Frontera de Decisión

Ajuste de Sensibilidad

Clasificación Final

5

### Costo Log-Loss

El modelo no usa mínimos cuadrados; usa entropía cruzada para
penalizar predicciones erróneas y seguras.

Penaliza masivamente al modelo si predice una probabilidad cercana a 0 cuando el resultado real
era 1. Esto obliga al modelo a "aprender" la frontera correcta.

Entropía Cruzada

Optimización Convexa

Máxima Verosimilitud

6

### Validación Técnica

El éxito no se mide con R², sino con la precisión de sus etiquetas y
la matriz de confusión.

Evaluamos mediante la **Precisión**, **Recall** (Exhaustividad) y el
**F1-Score**. También es vital analizar la curva ROC y el área bajo la curva (AUC).

Matriz de Confusión

ROC-AUC Score

F1-Score (Balance)

7

### Multiclase

Extensión del modelo para clasificar en más de dos categorías (ej:
Perro, Gato, Ave).

Utiliza estrategias como **One-vs-Rest (OvR)** o la función
**Softmax** para calcular probabilidades separadas para múltiples etiquetas a la
vez.

Estrategia OvR

Regresión Multinomial

Expansión de Etiquetas

## Valor de la Regresión Logística

Es el "caballo de batalla" de la clasificación. Su gran fortaleza es que no solo te dice la clase,
sino qué tan seguro está de ella (probabilidad), lo que la hace indispensable en la toma de
decisiones basada en riesgos.

Probabilística
Transparente
Escalable

> [**Prev**](Supervised_Learning-Regresion_Lineal.md "Regresion Lineal")
• 
> [**Practica - Regresion Logistica**](../Sample/Supervised_Learning-Regresion-Logistica.md)
• 
> [**Codigo - Regresion Logistica**](../Code/Supervised_Learning-Regresion-Logistica.md)
• 
> [**Algoritmo - Random Forest**](Supervised_Learning-Random-Forest.md)
---