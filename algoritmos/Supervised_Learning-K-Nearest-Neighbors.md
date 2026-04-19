# Aprendizaje Basado en Instancias (Perezoso)

# K-Nearest Neighbors

KNN es uno de los algoritmos más simples e intuitivos: predice la etiqueta de un dato basándose en la
clase de sus vecinos más cercanos en el espacio de características.

**Guía del Algoritmo:** Haz clic en cada tarjeta para explorar
cómo la cercanía geométrica define la clasificación y el impacto del parámetro K.

1

### Similitud

El concepto central: "Dime con quién andas y te diré quién eres". Los
datos similares están cerca unos de otros.

KNN asume que las cosas similares existen en una proximidad cercana. Para clasificar un punto
nuevo, el algoritmo busca en el conjunto de datos los ejemplos que más se le parecen
geométricamente.

Proximidad Espacial

Asunción de Similitud

Intuitivo y Directo

2

### El Valor de K

Define cuántos vecinos se consultarán para tomar la decisión. Es el
hiperparámetro crítico del modelo.

Un **K pequeño** (ej. 1) hace que el modelo sea sensible al ruido (overfitting). Un
**K grande** hace que el modelo sea más estable pero puede ignorar patrones locales
(underfitting).

Balance Sesgo-Varianza

K Impar (Evita Empates)

Selección por Validación

3

### Métricas de Distancia

¿Cómo medimos la "cercanía"? El algoritmo calcula la separación
matemática entre puntos.

La más común es la **Distancia Euclidiana** (línea recta), pero también se usan la
**Manhattan** (bloques de ciudad) o la **Minkowski** para casos más
complejos.

Geometría Euclidiana

Distancia Manhattan

Similitud de Coseno

4

### Aprendizaje Perezoso

No hay una fase de entrenamiento real; el algoritmo simplemente
memoriza los datos y trabaja al predecir.

KNN no genera una función matemática. En lugar de eso, guarda todos los datos de entrenamiento y
realiza los cálculos costosos solo cuando se le pide una predicción.

Sin Fase de Entrenamiento

Predicción Costosa

Basado en Instancias

5

### Predicción

La salida final se obtiene consultando a los K vecinos encontrados.

Para **Clasificación**, se toma el voto mayoritario de los vecinos. Para
**Regresión**, se calcula el promedio de sus valores. También se puede asignar peso
según la distancia.

Votación por Mayoría

Promedio Ponderado

Salida Continua/Discreta

6

### Necesidad de Escalado

Crucial: si las variables tienen escalas distintas, el cálculo de
distancia se verá distorsionado.

Como KNN depende de distancias, una variable con valores grandes (ej. Salario) dominará sobre
una con valores pequeños (ej. Edad). Es obligatorio normalizar o estandarizar antes de usarlo.

Normalización (Min-Max)

Estandarización (Z-Score)

Unidades Comparables

7

### Dimensionalidad

El enemigo de KNN: a medida que aumentan las variables, la distancia
entre puntos pierde sentido.

En espacios de muchas dimensiones, los puntos tienden a estar "lejos" de todo, haciendo que la
búsqueda de vecinos falle. KNN funciona mejor con pocas variables altamente relevantes.

Degradación de Distancia

Necesidad de Reducción

Costo en Espacios Grandes

## Valor de KNN

Es el algoritmo ideal cuando no conoces la distribución de tus datos (no paramétrico) y tienes un
conjunto de datos pequeño o mediano. Su simplicidad lo hace perfecto como modelo base o "baseline"
para cualquier proyecto.

No
Paramétrico
Fácil
Implementación
Baseline
Robusto

> [* Prev *](/Supervised_Learning-Naive-Bayes.md "Naive-Bayes")
> [* Practica - K-Nearest Neighbors *](Sample/Supervised_Learning-K-Nearest-Neighbors.md)
> [* Codigo - K-Nearest Neighbors *](Code/Supervised_Learning-K-Nearest-Neighbors.md)
> [* Algoritmo - Árboles de Decisión *](Supervised_Learning-Arboles-Decision.md)
---