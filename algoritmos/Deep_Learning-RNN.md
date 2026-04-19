# Deep Learning / Secuencias Temporales

# Redes Neuronales Recurrentes: Memoria en Movimiento

Las RNN son arquitecturas diseñadas para procesar datos donde el orden importa. A diferencia de las
redes tradicionales, poseen una "memoria" que les permite recordar información de pasos anteriores para
influir en el presente.

**Guía del Algoritmo:** Haz clic en cada tarjeta para
explorar cómo las RNN gestionan el tiempo, mantienen estados ocultos y superan las limitaciones de la
memoria corta.

1

### Secuencias (Inputs)

Procesa datos donde la posición de cada elemento depende de los
anteriores (texto, audio, series de tiempo).

En una RNN, las entradas no son independientes. Cada elemento $X\_t$ se procesa en un paso de
tiempo específico. La red entiende que "Hola" seguido de "Mundo" tiene un significado distinto a
las palabras aisladas.

Dependencia Temporal

Longitud Variable

Procesamiento Paso a Paso

2

### Estructura Cíclica

La característica distintiva: conexiones que apuntan hacia atrás,
permitiendo que la información persista.

Visualmente, una RNN parece un bucle. Para entrenarla, "desenrollamos" este bucle en el tiempo,
creando una cadena de neuronas idénticas donde cada una pasa un mensaje a su sucesora.

Feedback Loops

Parámetros Compartidos

Desenrollado Temporal

3

### Hidden State ($h\_t$)

Es la "memoria" de la red. Almacena un resumen de todo lo que ha
ocurrido hasta el momento actual.

En cada paso $t$, el estado oculto se actualiza: $h\_t = f(h\_{t-1}, X\_t)$. Combina lo que acaba
de ver con lo que ya recordaba. Es el corazón de la capacidad predictiva secuencial.

Vector de Memoria

Resumen de Contexto

Actualización Recurrente

4

### Vanishing Gradient

El gran obstáculo: a medida que la secuencia es más larga, la red
olvida los primeros elementos.

Durante el entrenamiento, el error se propaga hacia atrás. En secuencias largas, la señal se
vuelve tan pequeña que los pesos de los primeros pasos no cambian, perdiendo la memoria de largo
plazo.

Pérdida de Contexto

Problema de Dependencia Larga

Limitación de RNN "Vanilla"

5

### Celdas de Memoria

Soluciones avanzadas (Long Short-Term Memory) que usan "compuertas"
para controlar qué recordar.

Las **LSTM** introducen puertas de entrada, salida y olvido. Esto les permite
decidir activamente qué información borrar y qué mantener durante miles de pasos, resolviendo el
olvido.

Puerta de Olvido (Forget Gate)

Estado de Celda Global

Memoria de Largo Plazo

6

### Aprendizaje BPTT

Algoritmo de entrenamiento especializado que calcula gradientes a lo
largo de toda la secuencia.

Backpropagation Through Time suma los errores de cada paso temporal y los propaga hacia atrás.
Es costoso computacionalmente pero necesario para que la red aprenda la estructura del tiempo.

Optimización Temporal

Acumulación de Error

Entrenamiento Secuencial

7

### Topologías RNN

Versatilidad en mapeos: uno-a-muchos, muchos-a-uno (sentimiento) o
muchos-a-muchos (traducción).

La RNN puede configurarse para recibir una palabra y generar una frase, o leer un párrafo y
devolver una etiqueta de sentimiento. Es la arquitectura más flexible en cuanto a dimensiones de
E/S.

Análisis de Sentimiento

Traducción Automática

Generación de Texto

## El Dominio del Tiempo

Las RNN permitieron que las máquinas comprendieran el lenguaje y predijeran el futuro (bolsa,
clima). Aunque los Transformers son ahora más populares, las RNN siguen siendo vitales para sistemas
de tiempo real y dispositivos con recursos limitados.

Secuencial
Contextual
Dinámico

> [ *Prev* ](Deep_Learning-CNN.md "Redes Neuronales Convuncionales")
> [ *Practica - Redes Neuronales Recurrentes* ](Sample/Deep_Learning-RNN.md)
> [ *Codigo - Redes Neuronales Recurrentes* ](Code/Deep_Learning-RNN.md)
---
