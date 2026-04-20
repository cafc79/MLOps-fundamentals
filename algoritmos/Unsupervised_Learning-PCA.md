# Reducción de Dimensionalidad (No Supervisado)

# PCA Análisis de Componentes Principales

PCA es la técnica estadística por excelencia para simplificar datos complejos. Transforma un conjunto de
variables correlacionadas en un número menor de variables no correlacionadas llamadas componentes
principales.

**Guía del Algoritmo:** Haz clic en cada tarjeta para
explorar cómo PCA comprime la información eliminando el ruido y resaltando las direcciones de mayor
varianza.

1

### Simplificación

Reduce el número de variables de un dataset manteniendo la mayor
cantidad de información posible.

En datasets con cientos de columnas, muchas variables suelen ser redundantes. PCA encuentra las
estructuras subyacentes para "resumir" los datos en dimensiones esenciales, facilitando la
visualización y el modelado.

Eliminación de redundancia

Compresión de atributos

Mitigación de ruido

2

### Estandarización

Es obligatorio escalar los datos para que todas las variables tengan
el mismo peso matemático.

Como PCA busca maximizar la varianza, una variable con valores grandes (ej. Ingresos) dominaría
injustamente sobre una con valores pequeños (ej. Edad). Se aplica Z-Score (media 0, varianza 1).

Normalización de escala

Media Centrada en Cero

Comparabilidad de Unidades

3

### Matriz de Relación

Calcula cómo las variables varían respecto a las demás para
identificar correlaciones.

La matriz de covarianza revela si las variables se mueven juntas. Si dos variables están muy
correlacionadas, contienen información similar; PCA usará esto para combinarlas en una sola.

Medición de Varianza

Detección de Correlación

Estructura Multivariada

4

### Dirección y Magnitud

Encuentra los ejes donde los datos tienen la mayor dispersión o
varianza.

Los **autovectores** definen la dirección del nuevo eje. Los
**autovalores** indican cuánta varianza hay en esa dirección. El eje con el
autovalor más alto es el Componente Principal 1 (PC1).

Eigenvectors (Direcciones)

Eigenvalues (Importancia)

Álgebra Lineal aplicada

5

### Nuevas Variables

Construye las nuevas columnas (PC) como combinaciones lineales de las
originales.

Los componentes principales son ortogonales (están a 90 grados), lo que garantiza que no haya
correlación entre ellos. El PC1 captura la mayor varianza posible, el PC2 la segunda mayor, y
así sucesivamente.

Ortogonalidad Total

Independencia Lineal

Orden de Varianza

6

### Criterio de Retención

Decide cuántos componentes conservar mirando el porcentaje de
información que representan.

Se utiliza el **Scree Plot**. Habitualmente se eligen suficientes componentes para
explicar entre el 70% y el 95% de la varianza total, descartando el resto como ruido
insignificante.

Ratio de Varianza Explicada

Análisis de Scree Plot

Codo de Información

7

### Proyección

Transforma el dataset original al nuevo espacio de menor dimensión.

Los datos originales se proyectan sobre los autovectores seleccionados. El resultado es un
dataset nuevo con menos columnas, listo para algoritmos de clasificación o visualización en
2D/3D.

Reducción de Columnas

Eficiencia Computacional

Visualización de Clústeres

## Valor del PCA

Es la herramienta fundamental para combatir la **"Maldición de la Dimensionalidad"**.
Permite entrenar modelos más rápidos, evitar el sobreajuste y visualizar relaciones ocultas en datos
masivos.

Compresión
Inteligente
Visualización
2D/3D
Velocidad de
Modelado

> [* Prev *](Unsupervised_Learning-K-Means-Clustering.md "K-Means Clustering")
• 
> [* Practica - Análisis de Componentes Principales *](Sample/Unsupervised_Learning-PCA.md)
• 
> [* Codigo - Análisis de Componentes Principales *](Code/Unsupervised_Learning-PCA.md)
• 
> [* Algoritmo - Agrupamiento Jerárquico *](Unsupervised_Learning-Hierarchical-Clustering.md)
---