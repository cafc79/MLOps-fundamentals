# Aprendizaje No Supervisado (Clustering Jerárquico)

# Agrupamiento Jerárquico: El Mapa de las Relaciones de Datos

Este algoritmo crea una jerarquía de grupos anidados. A diferencia de K-Means, no requiere que definas
el número de clusters de antemano, permitiendo visualizar la relación entre datos en múltiples niveles.

**Guía del Algoritmo:** Haz clic en cada tarjeta para explorar
cómo los datos se fusionan o dividen para formar estructuras de árbol (dendrogramas).

1

### Bottom-Up

El método más común (Aglomerativo): cada dato comienza como su propio
cluster y se fusiona con el más cercano.

El proceso es iterativo. En cada paso, el algoritmo busca los dos grupos más similares y los
combina en uno solo, repitiendo el ciclo hasta que todos los puntos forman un único gran cluster
raíz.

Fusión Iterativa

Estructura de "Abajo hacia Arriba"

Sin etiquetas previas

2

### Distancia

Define qué tan similares son dos puntos. Es el motor matemático que
decide las fusiones iniciales.

Se basa en una **Matriz de Proximidad**. Las métricas más usadas son la Distancia
Euclidiana (línea recta) o Manhattan (trayectoria en cuadrícula). La elección impacta
drásticamente en la forma de los clusters finales.

Matriz de Distancias

Similitud Geométrica

Normalización Requerida

3

### Linkage (Enlace)

¿Cómo medimos la distancia entre dos grupos que ya contienen múltiples
puntos?

**Single:** Distancia mínima entre puntos. **Complete:** Distancia
máxima. **Average:** Promedio de todas las distancias. **Ward:**
Minimiza la varianza interna del nuevo grupo.

Método de Ward (Más robusto)

Single Linkage (Efecto cadena)

Complete Linkage (Clusters
compactos)

4

### Dendrograma

La herramienta de visualización clave: un diagrama de árbol que
registra todas las fusiones realizadas.

El eje vertical representa la distancia (o desimilitud). Cuanto más larga sea la línea vertical
antes de una unión, más diferentes eran los grupos que se están fusionando. Es el mapa genético
de tus datos.

Registro de Historial

Visualización de Niveles

Relaciones Anidadas

5

### Corte de Jerarquía

Decide el número final de clusters realizando un "corte" horizontal en
el dendrograma.

Trazas una línea horizontal. El número de líneas verticales que cruzas determina cuántos
clusters obtendrás. Esto ofrece una flexibilidad única para elegir granularidades finas o
gruesas.

Determinación de K post-hoc

Análisis de Granularidad

Umbral de Distancia

6

### Top-Down (DIANA)

El opuesto menos común: comienza con todos los datos en un solo grupo
y los rompe sucesivamente.

El algoritmo DIANA (Divisive Analysis) busca en cada paso el cluster más heterogéneo y lo divide
en dos grupos más homogéneos. Es computacionalmente más costoso que el aglomerativo.

División de Arriba hacia Abajo

Mayor Costo de Cómputo

Análisis de Heterogeneidad

7

### Escalabilidad

A diferencia de K-Means, el clustering jerárquico no escala bien con
datasets gigantescos.

Debido a que necesita calcular y actualizar una matriz de distancias completa en cada paso, su
complejidad es O(n² log n). Es ideal para datos pequeños/medianos donde la jerarquía es vital.

Alto Consumo de Memoria

Limitado a pocos miles de registros

Irreversibilidad de Pasos

## Valor del Agrupamiento Jerárquico

Es inigualable para descubrir estructuras de parentesco, taxonomías biológicas o segmentaciones de
mercado donde existen grupos dentro de grupos. Su transparencia visual mediante el dendrograma lo
hace favorito para la investigación científica.

Taxonomías
Naturales
Visibilidad
Total
Anidamiento
Lógico

> [* Prev *](Unsupervised_Learning-PCA.md "Análisis de Componentes Principales")
> [* Practica - Agrupamiento Jerárquico *](Sample/Unsupervised_Learning-Hierarchical-Clustering.md)
> [* Codigo - Agrupamiento Jerárquico *](Code/Unsupervised_Learning-Hierarchical-Clustering.md)
> [* Algoritmo - Q-Learning *](Reinforcement_Learning-Q-Learning.md)
---