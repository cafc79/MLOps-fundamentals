# Modelos Basados en Reglas
(Supervisados)

# Árboles de Decisión

Un modelo predictivo que utiliza una estructura de tipo diagrama de flujo para mapear decisiones y sus
posibles consecuencias, transformando datos complejos en reglas de decisión legibles.

**Guía del Algoritmo:** Haz clic en cada tarjeta para
explorar la jerarquía lógica, desde el nodo raíz hasta la toma de decisiones final.

1

### Nodo Raíz (Root)

El punto de partida de todo el árbol. Representa la característica que
mejor divide el conjunto de datos inicial.

El algoritmo evalúa todas las variables y selecciona aquella que proporciona la mayor separación
de clases. Es la decisión más importante, ya que define el primer nivel de jerarquía.

Punto de entrada único

Selección de variable óptima

Máxima diferenciación

2

### Criterios de Splitting

Las métricas matemáticas que deciden cómo "cortar" los datos: Impureza
de Gini y Entropía.

El **Índice Gini** mide qué tan a menudo un elemento aleatorio sería identificado
incorrectamente. La **Entropía** mide el desorden de la información. El objetivo
siempre es maximizar la pureza en los nodos hijos.

Minimización de Gini

Ganancia de Información

Homogeneidad de Nodos

3

### Nodos de Decisión

Nodos intermedios que plantean preguntas lógicas (Sí/No) para
subdividir los datos.

Cada nodo de decisión representa una prueba sobre un atributo. Dependiendo del resultado de la
prueba, los datos fluyen por una rama específica hacia un nivel más profundo del árbol.

Bifurcación Lógica

División de Atributos

Profundidad del Árbol

4

### Nodos Hoja (Leaves)

El destino final. Representa la etiqueta de clase o el valor numérico
predicho.

En estos nodos no ocurren más divisiones. La predicción final se basa en el voto mayoritario de
los datos que llegaron a esa hoja (clasificación) o el promedio (regresión).

Resultado Final

Nodos Terminales

Predicción de Salida

5

### El Riesgo: Overfitting

Los árboles tienden a crecer demasiado, "memorizando" el ruido de los
datos de entrenamiento.

Un árbol sin restricciones puede crear una regla para cada fila de datos, lo que resulta en una
precisión perfecta en el entrenamiento pero un desempeño pobre en la realidad.

Alta Varianza

Árboles muy profundos

Baja Generalización

6

### Poda (Pruning)

Técnicas para simplificar el árbol eliminando ramas que aportan poco
valor predictivo.

El **Pre-poda** detiene el crecimiento temprano (ej. limitando la profundidad). El
**Post-poda** elimina ramas después de que el árbol ha crecido totalmente para
mejorar la robustez.

Max\_Depth Control

Reducción de Complejidad

Coste-Complejidad

7

### Modelo CART

Classification and Regression Trees. La versatilidad de usar la misma
lógica para categorías o números.

Esta implementación permite que el árbol actúe como clasificador o como regresor, adaptando la
función de error (Gini para categorías, MSE para valores continuos).

Clasificación Binaria/Multi

Regresión No Lineal

Adaptabilidad de Datos

## Valor de los Árboles de Decisión

Su gran ventaja es la **Interpretabilidad**. Son "Cajas Blancas" que permiten a
cualquier humano seguir el camino de una decisión. Además, son la base fundamental de algoritmos más
potentes como Random Forest y XGBoost.

Caja
Blanca
Interpretable
No
Lineal

> [* Prev *](/Supervised_Learning-K-Nearest-Neighbors.md "K-Nearest Neighbors")
> [* Practica - Árboles de Decisión *](Sample/Supervised_Learning-Arboles-Decision.md)
> [* Codigo - Árboles de Decisión *](Code/Supervised_Learning-Arboles-Decision.md)
> [* Algoritmo - K-Means Clustering *](Unsupervised_Learning-K-Means-Clustering.md)
---