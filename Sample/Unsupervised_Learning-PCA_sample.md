# Caso Práctico: PCA en Análisis de Clientes

# Caso Real: Reducción de Dimensionalidad

# Simplificación con PCA

¿Cómo entender a un cliente si medimos 50 variables distintas de su comportamiento? PCA destila esas 50
columnas en 2 o 3 "súper variables" que capturan la esencia del usuario, permitiendo visualizar patrones
imposibles de ver a simple vista.

**Guía de Negocio:** Haz clic en cada etapa para entender
cómo transformamos un mar de datos irrelevantes en una visión estratégica de alta definición.

1

### Carga de Multivariables

Recibimos un dataset con 50 columnas por cliente: desde clics y tiempo
de sesión hasta categorías de productos.

Tener demasiadas variables causa la "Maldición de la Dimensionalidad": los modelos se vuelven
lentos y es imposible graficar los datos para que un humano los entienda. PCA será nuestro
filtro inteligente.

Exceso de ruido visual

Redundancia de información

Complejidad computacional

2

### Estandarización

Obligatorio: Llevamos todas las variables a una media de 0 y varianza
de 1.

Si un cliente gasta $10,000 (número grande) pero visita la web 2 veces (número pequeño), PCA
creería que el gasto es más importante solo por su escala. Al estandarizar, todas las variables
compiten en igualdad de condiciones.

Normalización Z-Score

Comparabilidad de Atributos

Eliminación de Sesgos de Escala

3

### Matriz de Covarianza

El algoritmo analiza qué comportamientos suelen ocurrir juntos
(correlación).

Descubrimos que "Tiempo en página" y "Número de clics" están muy relacionados. Tienen
información redundante. PCA usará estas relaciones para fusionar variables y reducir el espacio
sin perder el significado.

Detección de Redundancia

Estructura Interna de Datos

Análisis de Multicolinealidad

4

### Componentes Principales

Calculamos las nuevas direcciones (PC) que contienen la mayor
"varianza" o información.

El primer componente (PC1) podría representar la "Intensidad de Compra", combinando gasto,
frecuencia y clics. El segundo (PC2) podría ser la "Diversidad de Interés". Hemos pasado de 50
columnas a conceptos abstractos potentes.

Eigenvectors (Direcciones)

Eigenvalues (Importancia)

Ortogonalidad (Sin Correlación)

5

### Varianza Explicada

Decidimos cuántos componentes conservar para mantener el 90% de la
"verdad" de los datos.

Usamos el Scree Plot. Descubrimos que con solo 3 componentes principales capturamos el 92% de la
información que antes estaba dispersa en 50 columnas. Descartamos el 8% restante como ruido
irrelevante.

Análisis de Scree Plot

Umbral de Información

Compresión Optimizada

6

### Proyección 2D/3D

Mapeamos a los miles de clientes en un simple gráfico de dos ejes para
ver grupos.

Al proyectar sobre PC1 y PC2, grupos de clientes "flotan" juntos. Ahora el equipo de Marketing
puede ver claramente 4 nubes de puntos: Clientes VIP, Cazadores de Ofertas, Usuarios Inactivos y
Nuevas Promesas.

Mapa de Segmentos

Claridad de Negocio

Identificación de Outliers

7

### Aceleración de Modelos

Usamos los componentes como entrada para otros algoritmos de Machine
Learning.

En lugar de entrenar un Random Forest con 50 columnas, lo entrenamos con 3. El modelo es 10
veces más rápido, consume menos memoria y generaliza mejor al haber eliminado el ruido
innecesario de los datos.

Eficiencia en Entrenamiento

Reducción de Costos Cloud

Estabilidad Predictiva

## La Inteligencia de lo Esencial

PCA no solo reduce datos, **crea claridad**. En un mundo saturado de métricas, este
algoritmo permite que el negocio se enfoque en los ejes fundamentales que realmente mueven la aguja
del crecimiento, eliminando lo que sobra.

Síntesis
Eficiencia
Visualización

> [**Algoritmo - Análisis de Componentes Principales**](../algoritmos/Unsupervised_Learning-PCA.md)
• 
> [**Codigo - Análisis de Componentes Principales**](../Code/Unsupervised_Learning-PCA.md)
• 
> [**Practica - Agrupamiento Jerárquico**](Unsupervised_Learning-Hierarchical-Clustering.md)
---