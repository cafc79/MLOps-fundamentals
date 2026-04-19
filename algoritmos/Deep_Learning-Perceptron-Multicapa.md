# Redes Neuronales Artificiales (Supervisado)

# Perceptrón Multicapa (MLP): El Inicio de la IA Profunda

El MLP es la arquitectura clásica de Red Neuronal "Feedforward". Es un aproximador universal capaz de
aprender relaciones no lineales complejas mediante capas interconectadas de neuronas artificiales.

**Guía del Algoritmo:** Haz clic en cada tarjeta para
explorar la anatomía de una red neuronal, desde la entrada de datos hasta el ajuste de pesos por
gradiente.

1

### Capa de Entrada

El punto de contacto con el mundo real. Recibe las características
(features) del dataset original.

Cada neurona de entrada representa una variable. Es fundamental que los datos estén normalizados
(0 a 1) o estandarizados para que los pesos iniciales no se descontrolen durante el
entrenamiento.

Unidades por Feature

Recepción Pasiva

Normalización Crítica

2

### Capas Ocultas

Donde ocurre el aprendizaje. Estas capas intermedias extraen patrones
abstractos de los datos.

A medida que la información avanza, las capas ocultas combinan señales para detectar patrones
más complejos (ej. de bordes a formas, de formas a objetos). La "profundidad" define la
capacidad de abstracción.

Extracción de Atributos

Representación Jerárquica

Hiperparámetro: Profundidad

3

### Funciones de Activación

La "chispa" de la neurona. Decide si una neurona se activa basándose
en su entrada ponderada.

Sin ellas, el MLP sería solo una regresión lineal gigante. Funciones como **ReLU**,
**Sigmoid** o **Tanh** introducen la no linealidad necesaria para
aprender problemas complejos.

ReLU (Rectified Linear Unit)

Introducción de No-Linealidad

Umbral de Disparo

4

### Propagación Adelante

El flujo de información: Los datos viajan desde la entrada hasta la
salida multiplicándose por pesos.

Cada conexión tiene un **Peso (W)** y cada neurona un **Sesgo (b)**.
El cálculo $Z = W \cdot X + b$ transforma los datos secuencialmente capa por capa hasta generar
una predicción.

Suma Ponderada

Transformación de Señal

Predicción Inicial

5

### Cálculo del Error

El juez del modelo. Mide qué tan equivocada fue la predicción respecto
a la etiqueta real.

Se usan funciones como **MSE** para regresión o **Cross-Entropy** para
clasificación. El valor resultante (Loss) es el que el algoritmo intentará minimizar durante
todo el entrenamiento.

Magnitud de Error

Diferencial de Salida

Objetivo de Optimización

6

### Retropropagación

El motor del aprendizaje. Distribuye la culpa del error hacia atrás a
través de las capas.

Usando la **Regla de la Cadena** de cálculo, el algoritmo determina cuánto
contribuyó cada peso individual al error final. Se calculan los gradientes para saber en qué
dirección ajustar cada conexión.

Cálculo de Gradientes

Regla de la Cadena

Atribución de Error

7

### Ajuste de Pesos

La corrección final. Se actualizan los parámetros usando un
optimizador para reducir el error futuro.

El **Descenso del Gradiente** (u optimizadores como Adam) resta una pequeña
fracción del gradiente a los pesos actuales. La **Tasa de Aprendizaje (Learning
Rate)** controla qué tan grande es este paso.

Gradient Descent

Learning Rate Control

Iteración (Épocas)

## Valor del MLP

Es la puerta de entrada a la Inteligencia Artificial moderna. Su capacidad para aprender cualquier
función continua lo hace ideal para problemas complejos de visión, voz y predicción tabular donde
los modelos lineales fallan.

Aproximador
Universal
Deep
Learning Base
Altamente
Flexible

> [* Prev *](Reinforcement_Learning-Q-Learning.md "Q-Learning")
> [* Practica - Perceptrón Multicapa *](Sample/Deep_Learning-Perceptron-Multicapa.md)
> [* Codigo - Perceptrón Multicapa *](Code/Deep_Learning-Perceptron-Multicapa.md)
> [* Algoritmo - Redes Neuronales Convolucionales *](Deep_Learning-CNN.md)
---