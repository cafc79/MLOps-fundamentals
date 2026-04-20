# Aprendizaje No Supervisado (Clustering)

# K-Means Clustering: El Arte de Encontrar el Orden en el Caos

K-Means es el algoritmo líder para el agrupamiento de datos. Su objetivo es particionar un conjunto de
observaciones en 'K' grupos donde cada dato pertenece al grupo con el promedio más cercano.

**Guía del Algoritmo:** Haz clic en cada tarjeta para
explorar cómo las máquinas encuentran patrones ocultos y agrupan datos sin necesidad de etiquetas
previas.

1

### Agrupamiento

Descubre estructuras naturales en los datos basándose puramente en su
similitud geométrica.

A diferencia de la clasificación, aquí no hay "respuestas correctas" iniciales. El algoritmo
busca puntos que estén "cerca" entre sí en el espacio de características para formar clusters
cohesivos.

Sin etiquetas (Unsupervised)

Similitud de Atributos

Descubrimiento de Patrones

2

### Centroides Iniciales

El proceso comienza seleccionando 'K' puntos aleatorios que servirán
como los centros de los grupos.

La ubicación inicial de estos centroides es crucial. Una mala elección puede llevar a resultados
subóptimos. Técnicas modernas como **K-Means++** optimizan esta selección inicial.

Selección de K inicial

K-Means++ Algoritmo

Puntos de Referencia

3

### Asignación de Puntos

Cada dato del dataset se asigna al centroide más cercano, usualmente
mediante distancia euclidiana.

Se calcula la distancia matemática entre cada registro y todos los centroides. El registro pasa
a formar parte del cluster cuyo centroide esté a la menor distancia posible.

Distancia Euclidiana

Partición de Voronoi

Pertenencia de Grupo

4

### Mover Centroides

Una vez asignados los puntos, el centroide se recalcula moviéndose al
centro promedio del grupo.

El centroide se desplaza a la posición media (la media aritmética) de todos los puntos que le
fueron asignados. Este paso refina la representatividad de cada cluster.

Recálculo de Medias

Optimización de Centro

Refinamiento de Cluster

5

### Convergencia

El proceso de asignación y actualización se repite hasta que los
centroides dejan de cambiar de posición.

El algoritmo es iterativo. Se detiene cuando los clusters son estables o se alcanza un número
máximo de iteraciones definido. En este punto, el error (WSS) se ha minimizado localmente.

Estabilidad de Grupos

Límite de Iteraciones

Mínimo Local

6

### Elección de K

¿Cuántos grupos necesito? El Método del Codo ayuda a encontrar el
número óptimo de clusters.

Se grafica la inercia frente al número de clusters. El "codo" de la gráfica indica el punto
donde añadir más grupos deja de aportar una mejora significativa en la cohesión de los clusters.

Inercia (WSS)

Optimización de K

Análisis de Silueta

7

### Escalabilidad

Eficiencia computacional para manejar millones de datos en tiempo
récord.

K-Means es linealmente escalable. Variantes como **Mini-Batch K-Means** permiten
procesar conjuntos de datos masivos usando pequeñas muestras aleatorias, reduciendo
drásticamente el tiempo de cómputo.

Complejidad O(n)

Mini-Batch Processing

Eficiencia en Memoria

## Valor de K-Means

Es la herramienta fundamental para la **Segmentación de Clientes**, compresión de
imágenes y detección de anomalías. Su simplicidad y rapidez lo convierten en el primer paso para
cualquier análisis exploratorio de datos.

Segmentación
Rápida
Escalabilidad
Masiva
Fácil
Interpretación

> [**Prev**](Supervised_Learning-Arboles-Decision.md "Árboles de Decisión")
• 
> [**Practica - K-Means Clustering**](../Sample/Unsupervised_Learning-K-Means-Clustering.md)
• 
> [**Codigo - K-Means Clustering**](../Code/Unsupervised_Learning-K-Means-Clustering.md)
• 
> [**Algoritmo - Análisis de Componentes Principales**](Unsupervised_Learning-PCA.md)
---