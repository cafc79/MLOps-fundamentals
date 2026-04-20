# Caso Práctico: CNN en Control de Calidad

# Caso Real: Inspección Visual Industrial

# Control de Calidad con CNN

¿Cómo detecta una fábrica piezas defectuosas a una velocidad de 60 por segundo? La Red Neuronal
Convolucional (CNN) emula la visión humana para identificar grietas, manchas o piezas faltantes con una
precisión inalcanzable para el ojo humano.

**Guía de Negocio:** Haz clic en cada etapa para entender cómo
transformamos una imagen de cámara industrial en una decisión de descarte automatizada.

1

### Capa de Entrada

Cámaras de alta velocidad capturan imágenes de las piezas sobre la
cinta transportadora.

La imagen se descompone en tensores (matrices numéricas) de píxeles. Una foto de 224x224 píxeles
en color genera una matriz tridimensional (RGB) que sirve como entrada cruda para que la red
empiece su análisis.

Captura en tiempo real

Preprocesamiento de brillo

Normalización de píxeles

2

### Convolución

Filtros inteligentes "escanean" la pieza buscando bordes, sombras o
patrones de grietas.

La red usa "Kernels" que detectan irregularidades. Si hay una grieta, el mapa de características
(Feature Map) resaltará esa zona con valores altos, ignorando las partes lisas y perfectas de la
pieza.

Detección de bordes

Filtros de textura

Extracción de anomalías

3

### Capa ReLU

Eliminamos el ruido de fondo para que la red se concentre solo en las
señales de defecto.

La función de activación ReLU apaga las neuronas con señales negativas. Esto limpia la imagen
mental de la red, dejando solo los rasgos de alto contraste (donde es más probable que esté el
fallo).

Limpieza de ruido visual

Enfoque en irregularidades

Eficiencia de aprendizaje

4

### Max Pooling

Resumimos la información para que la red detecte el defecto incluso si
la pieza está girada.

El Pooling reduce el tamaño de los datos manteniendo solo los valores máximos. Esto otorga
"invarianza espacial": la red encontrará la grieta sin importar si está un centímetro a la
izquierda o a la derecha.

Reducción de parámetros

Robustez de posición

Ahorro de cómputo

5

### Flattening

Aplanamos los mapas visuales en un vector para que la red neuronal
tome una decisión racional.

Pasamos de "ver" formas en 2D a tener una lista de atributos abstractos. Este vector contiene
toda la "experiencia visual" recopilada en los pasos anteriores, lista para ser juzgada por la
lógica final.

Conversión Visual-Datos

Preparación de vector

Puente de arquitectura

6

### Capa Densa (FC)

La red razona sobre los datos: "Si hay borde irregular + mancha oscura
= DEFECTUOSA".

Mediante capas totalmente conectadas, la red combina los rasgos detectados. El resultado es una
puntuación de confianza para cada categoría posible: Pieza Óptima vs Pieza con Defecto.

Votación de rasgos

Clasificación final

Cálculo de probabilidad

7

### Ejecución Real

Si la confianza en defecto es > 95%, un brazo robótico retira la pieza
de la línea.

El sistema no solo informa, actúa. Se ahorran millones en reclamos de clientes al asegurar que
ninguna pieza fallida salga de la planta. El modelo se actualiza semanalmente con las fotos de
los nuevos errores detectados.

Descarte automatizado

Registro de errores

Zero-Defect Strategy

## La Revolución de la Visión

Las CNN eliminan la fatiga humana del control de calidad. Mientras que un inspector puede
distraerse, la red neuronal mantiene una **precisión del 99.9% las 24 horas**,
garantizando la excelencia operativa y la seguridad del consumidor.

Infalible
Escalable
En Tiempo
Real

• Caso Práctico: Quality Control con CNN
> [**Algoritmo - Redes Neuronales Convolucionales**](../algoritmos/Deep_Learning-CNN.md)
 • 
> [**Codigo - Redes Neuronales Convolucionales**](../Code/Deep_Learning-CNN.md)
 • 
> [**Practica - Redes Neuronales Recurrentes**](Deep_Learning-RNN.md)
---