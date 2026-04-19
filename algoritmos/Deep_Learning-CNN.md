# Algoritmo CNN (Convolutional Neural Networks)

# Deep Learning / Computer Vision

Las CNN son arquitecturas especializadas en procesar datos con estructura de cuadrícula, como imágenes.
Su capacidad para extraer patrones espaciales las hace el estándar para el reconocimiento de objetos y
rostros.

**Guía del Algoritmo:** Haz clic en cada tarjeta para explorar
cómo las CNN "ven" y descomponen una imagen en píxeles, bordes y objetos complejos.

1

### Capa de Entrada

Representación de la imagen en tensores numéricos con dimensiones de
Altura, Ancho y Canales (RGB).

A diferencia de un MLP, la CNN mantiene la estructura espacial. Una imagen de color se
descompone en 3 matrices (Rojo, Verde, Azul). Los valores de píxel (0-255) suelen normalizarse
para facilitar el entrenamiento.

Matriz de Píxeles

Canales de Color

Preservación Espacial

2

### Capa Convolucional

El núcleo del algoritmo. Usa "kernels" o filtros que se deslizan sobre
la imagen para detectar características.

Los filtros aprenden a detectar bordes, texturas o colores. El resultado es un "Feature Map"
(mapa de características) que resalta dónde aparece cada patrón dentro de la imagen original.

Filtros Aprendibles

Mapas de Características

Operación Matemática Dot

3

### Capa ReLU

Introduce no-linealidad al sistema, eliminando los valores de píxel
negativos (los vuelve cero).

Crucial para que la red aprenda relaciones complejas. ReLU (Rectified Linear Unit) es la función
estándar porque ayuda a mitigar el problema del gradiente desvaneciente y acelera el
entrenamiento.

No-Linealidad

Eficiencia Computacional

Supresión de Señal Negativa

4

### Capa de Pooling

Reduce las dimensiones espaciales de la imagen para disminuir
parámetros y controlar el sobreajuste.

El **Max Pooling** es el más común: selecciona el valor máximo en una ventana (ej.
2x2). Esto resume la información y hace que la red sea invariante a pequeñas traslaciones de los
objetos.

Downsampling (Submuestreo)

Invarianza Espacial

Reducción de Cómputo

5

### Flattening

Transforma los mapas de características 2D resultantes en un vector
unidimensional largo.

Este paso es el puente entre la extracción de características visuales y la clasificación
lógica. Los datos "aplanados" se preparan para ser entregados a una red neuronal tradicional.

Conversión 2D a 1D

Vector de Atributos

Preparación de Datos

6

### Capa Densa (FC)

Red Neuronal tradicional que utiliza las características extraídas
para tomar la decisión final.

Aquí se realiza la clasificación basada en el razonamiento de alto nivel. La red combina las
formas detectadas (ej. orejas, hocico, ojos) para determinar qué objeto hay en la imagen.

Clasificación de Alto Nivel

Votación de Características

Integración Total

7

### Softmax / Predicción

Genera probabilidades finales para cada categoría (ej: Gato: 98%,
Perro: 1%, Ave: 1%).

La función Softmax asegura que la suma de todas las salidas sea igual a 1 (100%). El modelo
elige la clase con el porcentaje más alto como su predicción oficial.

Distribución de Probabilidad

Etiquetado de Imagen

Confianza de Salida

## El Poder de la Jerarquía Visual

Las CNN revolucionaron la IA porque eliminaron la necesidad de extraer características a mano. El
modelo aprende automáticamente qué es importante en una imagen, superando el desempeño humano en
muchas tareas de visión.

Visión por
Computadora
Auto-Feature
Extraction
Deep
Learning


> [* Prev *](Deep_Learning-Perceptron-Multicapa.md "Perceptrón Multicapa")
> [* Practica - Redes Neuronales Convolucionales *](Sample/Deep_Learning-CNN.md)
> [* Codigo - Redes Neuronales Convolucionales *](Code/Deep_Learning-CNN.md)
> [* Algoritmo - Redes Neuronales Recurrentes *](Deep_Learning-RNN.md)
---
