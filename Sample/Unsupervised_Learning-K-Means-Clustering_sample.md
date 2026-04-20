# Caso Práctico: K-Means en Segmentación de Clientes

# Caso Real: Personalización de Audiencias


¿Cómo tratas a miles de clientes de forma personalizada sin conocerlos uno a uno? K-Means agrupa
automáticamente a tus usuarios por comportamiento, permitiéndote descubrir quiénes son tus fans leales y
quiénes necesitan un impulso para volver.

**Guía de Negocio:** Haz clic en cada etapa para entender
cómo transformamos una base de datos desordenada en perfiles de cliente accionables.

1

### Objetivo Estratégico

Pasar de un marketing masivo ("talla única") a estrategias
personalizadas por nicho.

Analizamos una base de 100,000 clientes. El negocio quiere identificar grupos con necesidades
similares para enviar promociones que realmente les interesen, optimizando el presupuesto
publicitario.

Identificación de Patrones

Optimización de ROI

Aprendizaje No Supervisado

2

### Variables de Selección

Elegimos las dimensiones de comportamiento: Recencia, Frecuencia y
Valor Monetario (RFM).

¿Cuándo fue su última compra? ¿Qué tan seguido nos visita? ¿Cuánto dinero gasta en total? Estas
tres dimensiones permiten a K-Means trazar un mapa 3D donde cada punto es un cliente.

Frecuencia de Compra

Gasto Promedio (Ticket)

Días desde última visita

3

### Estandarización

Igualamos las escalas para que un gasto de $5,000 no opaque a una
frecuencia de 5 visitas.

K-Means usa distancias. Si no normalizamos, el algoritmo pensará que el dinero es lo único que
importa por tener números más grandes. Llevamos todo a una escala comparable (ej. 0 a 1) para un
análisis justo.

Escalamiento de Atributos

Eliminación de Sesgos

Precisión Geométrica

4

### Hallar el Valor K

Determinamos cuántos grupos de clientes son necesarios para que el
análisis sea útil.

Usamos el **Método del Codo** (Elbow Method). Graficamos la cohesión de los grupos
y buscamos el punto donde añadir más clusters ya no aporta claridad. Para este negocio,
decidimos que 4 grupos es lo óptimo.

Análisis de Inercia

Optimización de Grupos

Simplicidad vs Detalle

5

### El Algoritmo en Acción

Los centroides se mueven hasta encontrar el corazón de cada tipo de
cliente.

El algoritmo asigna a cada cliente al centroide más cercano. Luego, mueve el centroide al
promedio del grupo. Repite esto hasta que los grupos son estables y ya no hay cambios.

Agrupación por Similitud

Convergencia de Datos

Cohesión Interna

6

### Identidad de los Grupos

Ponemos nombre y cara a los 4 clusters descubiertos basándonos en sus
promedios.

Descubrimos: **1. Campeones** (Gasto alto, frecuencia alta), **2.
Promesas** (Visitas recientes, gasto bajo), **3. En Riesgo** (No han
vuelto en meses) y **4. Ocasionales** (Visitas raras).

Caracterización de Nichos

Arquetipos de Consumo

Insights de Negocio

7

### Marketing de Precisión

Lanzamos campañas diferenciadas para cada grupo y medimos el aumento
en ventas.

A los "Campeones" les damos un programa VIP. A los "En Riesgo" les enviamos un cupón de "Te
extrañamos". Resultado: La tasa de conversión subió un 20% al dejar de enviar spam genérico.

Campañas Personalizadas

Reducción de Churn

Crecimiento del LTV

## El Poder de la Segmentación

K-Means es la herramienta fundamental para el **Customer Discovery**. Permite que el
negocio deje de adivinar y empiece a escuchar lo que los datos dicen sobre quiénes son realmente sus
clientes.

Accionable
No
Supervisado
Escalable

> [**Algoritmo - K-Means Clustering**](../Algoritmo/Unsupervised_Learning-K-Means-Clustering.md)
• 
> [**Codigo - K-Means Clustering**](../Code/Unsupervised_Learning-K-Means-Clustering.md)
• 
> [**Practica - Análisis de Componentes Principales**](Unsupervised_Learning-PCA.md)
---