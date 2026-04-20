# Modelos de Ensamble (Bagging)

# Algoritmo Random Forest

Random Forest es un método de aprendizaje supervisado que construye una multitud de árboles de decisión
durante el entrenamiento para obtener una predicción más robusta, precisa y estable que un solo árbol.

**Guía del Algoritmo:** Haz clic en cada tarjeta para
explorar los fundamentos técnicos y las mecánicas internas del bosque aleatorio.

1

### Sabiduría de Masas

El principio fundamental: un conjunto de "aprendices débiles" puede
formar un "aprendiz fuerte" si trabajan en conjunto.

En lugar de confiar en un solo modelo complejo, Random Forest utiliza múltiples árboles de
decisión. La diversidad de opiniones entre los árboles ayuda a cancelar los errores individuales
y el ruido de los datos.

Reducción de varianza

Estabilidad del modelo

Evita el sobreajuste

2

### Bootstrapping (Muestreo)

Cada árbol en el bosque se entrena con un subconjunto diferente y
aleatorio de los datos de entrenamiento.

Esta técnica (también llamada Bagging) consiste en tomar muestras aleatorias con reemplazo. Esto
asegura que cada árbol vea una versión ligeramente diferente de la realidad, fomentando la
independencia entre ellos.

Muestreo con reemplazo

Datos "Out-of-Bag" (OOB)

Diversidad de muestras

3

### Feature Bagging

En cada nodo de cada árbol, solo se considera un subconjunto aleatorio
de variables para decidir la división.

Esta es la clave del componente "Random". Al limitar las opciones de cada nodo, forzamos a los
árboles a considerar variables menos obvias, descorrelacionando los árboles y mejorando la
generalización.

Descorrelación de árboles

Parámetro 'mtry'

Robustez ante ruido

4

### Crecimiento Independiente

Los árboles crecen de forma masiva y profunda, sin necesidad de podas
complejas individuales.

A diferencia de otros algoritmos secuenciales (como Boosting), los árboles de un Random Forest
se construyen de forma independiente. Esto permite el procesamiento en paralelo y facilita el
manejo de grandes volúmenes de datos.

Entrenamiento en paralelo

Árboles profundos

Manejo de No-Linealidad

5

### Agregación Final

La decisión final se toma combinando las predicciones individuales de
todos los árboles del bosque.

Para problemas de **Clasificación**, se utiliza la "Votación por Mayoría". Para
problemas de **Regresión**, se utiliza el promedio de todas las predicciones. Este
consenso es lo que otorga la precisión superior al modelo.

Voto mayoritario

Promedio de resultados

Consistencia estadística

6

### Feature Importance

El algoritmo permite identificar qué variables son las más
determinantes para realizar las predicciones.

Al analizar cuánto se reduce la impureza (Gini o Entropía) cada vez que se usa una variable,
Random Forest ofrece una medida de importancia. Esto ayuda en la selección de características y
en la interpretabilidad del modelo.

Reducción de impureza Gini

Ganancia de información

Ranking de variables

7

### Evaluación OOB

Un método interno de validación que estima el error sin necesidad de
un set de prueba separado.

Aproximadamente 1/3 de los datos no se usan para entrenar un árbol específico. Estos datos
"Out-of-Bag" se utilizan para predecir y evaluar el desempeño, proporcionando una métrica de
precisión interna muy confiable.

Validación interna automática

Estimación de error

Eficiencia de datos

## Por qué elegir Random Forest

Es uno de los algoritmos más versátiles y confiables en la caja de herramientas de un científico de
datos. Es robusto ante datos faltantes, maneja bien valores atípicos y requiere muy poco
preprocesamiento.

Alta
Precisión
No-Paramétrico
Versátil

> [**Prev**](Supervised_Learning-Regresion-Logistica.md "Regresion Lineal")
• 
> [**Practica - Random Forest**](../Sample/Supervised_Learning-Random-Forest.md)
• 
> [**Codigo - Random Forest**](../Code/Supervised_Learning-Random-Forest.md)
• 
> [**Algoritmo - Regresion Lineal**](Supervised_Learning-SVM.md)
---