# Pipeline Industrial: Redes Convolucionales & MLOps

# Visión Artificial y Ecosistema MLOps

#### Lógica de Selección: ¿Por qué CNN?

Es la arquitectura mandatoria para datos con estructura de cuadrícula cuando:

• Se requiere \*\*invarianza a la traslación\*\* (detectar el objeto esté donde esté).

• El dataset tiene \*\*jerarquías espaciales\*\* (bordes -> formas -> objetos).

• Se busca reducir parámetros mediante \*\*pesos compartidos\*\* (vs. capas densas).

• El problema exige el estado del arte en \*\*Computer Vision\*\*.

#### Elemento Distintivo: Convolución

"A diferencia de un MLP que intenta aprender cada píxel por separado, la CNN utiliza 'filtros'
que escanean la imagen buscando patrones locales. Esto imita la corteza visual humana y es la
clave de su eficiencia."

Fase 1: Ingesta & Data Lineage

## Gestión de Repositorios de Imágenes

En visión, el dato es pesado. Usamos linaje de carpetas y versionado de
artefactos para asegurar que el entrenamiento sea auditable.

import tensorflow as tf
from tensorflow.keras.preprocessing import image\_dataset\_from\_directory
# Ingesta desde S3/Cloud Storage montado
# image\_size debe ser uniforme para el tensor de entrada
train\_ds = image\_dataset\_from\_directory(
'data/factory\_inspection\_v2/train',
image\_size=(224, 224),
batch\_size=32,
label\_mode='binary',
seed=42 # Inmutabilidad del split
)
# Optimización de lectura en disco (Prefetching)
train\_ds = train\_ds.prefetch(buffer\_size=tf.data.AUTOTUNE)

#### Error Común: Resoluciones Mixtas

Entrenar con imágenes de diferentes tamaños sin un paso
de redimensionamiento (Resizing) consistente. Esto causa errores de dimensiones en las capas de
pooling y flatten.

Fase 2: Preprocessing & Augmentation

## Normalización y Aumento de Datos

Las CNN sufren si los píxeles (0-255) no se escalan. Además, usamos
Augmentation para que el modelo sea robusto ante giros o cambios de luz.

from tensorflow.keras import layers
# Pipeline de Preprocesamiento Integrado
data\_augmentation = tf.keras.Sequential([
layers.Rescaling(1./255), # Normalización a rango [0, 1]
layers.RandomFlip("horizontal\_and\_vertical"),
layers.RandomRotation(0.2),
layers.RandomContrast(0.1)
])

#### Validación Crucial: Leakage en Augmentation

El aumento de datos (rotaciones, brillo) debe
aplicarse \*\*exclusivamente al set de entrenamiento\*\*. El set de validación debe mantenerse puro y
representar imágenes reales de la cámara de la fábrica.

Fase 3: Model Training & Architecture

## Arquitectura de Extracción Jerárquica

Diseñamos el "esqueleto" de la red. Cada bloque Conv-Pool profundiza en la
complejidad de los rasgos visuales.

import mlflow
with mlflow.start\_run(run\_name="cnn\_quality\_v1"):
model = tf.keras.Sequential([
data\_augmentation,
# Bloque 1: Bordes y Texturas
layers.Conv2D(32, (3, 3), activation='relu', input\_shape=(224, 224, 3)),
layers.MaxPooling2D((2, 2)),
# Bloque 2: Formas Complejas
layers.Conv2D(64, (3, 3), activation='relu'),
layers.GlobalAveragePooling2D(), # Alternativa
robusta a Flatten
# Capa Densa Final
layers.Dense(1, activation='sigmoid')
])
# Log de arquitectura en MLOps
mlflow.log\_param("optimizer", "adam")
model.compile(optimizer='adam', loss='binary\_crossentropy', metrics=['accuracy'])

Fase 4: Evaluación & Model Health

## Diagnóstico Visual del Error

### CNN Health Check

Activation Maps (Grad-CAM)
Focalizado en objeto

Saturation Gap
Delta Loss < 0.1

Pixel Distribution Shift
Estable

Inferencia Latency (ms)
Objetivo < 50ms

#### Validación Crítica: Grad-CAM

"Una CNN es saludable si 'mira' el lugar correcto. Si
clasifica una pieza como defectuosa basándose en el fondo de la imagen, el modelo no es
robusto."

AUDIT VISUAL: HEATMAPS OK

#### La Trampa del Pooling Temprano

Reducir el tamaño de la imagen demasiado rápido (pooling agresivo)
puede destruir rasgos finos como micro-grietas en piezas industriales. \*\*Mantén resoluciones altas
en las primeras capas.\*\*

Fase 5: Serving & Artifact Registry

## Exportación a Formatos de Inferencia

El modelo de visión suele ser pesado. Para producción industrial (Edge),
convertimos a formatos optimizados como ONNX o TFLite.

import tensorflow\_model\_optimization as
tfmot
# Serialización inmutable del artefacto
model.save('models/cnn\_quality\_prod\_v1.h5')
# Mejor Práctica: Cuantización (INT8) para ejecución en GPUs de borde
(Edge)
converter = tf.lite.TFLiteConverter.from\_keras\_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite\_model = converter.convert()

Fase 6: Monitoring & Image Drift

## Vigilancia del Entorno de Captura

Si el operario mueve la cámara o cambia la iluminación de la planta, los
píxeles cambian y el modelo falla. Monitoreamos la "Deriva de Píxeles".

#### Alertas MLOps (Vision):

##### Illumination Drift

Si el histograma de brillo de las imágenes de
producción cambia > 20%.

##### Sensor Decay

Detección de "píxeles muertos" o desenfoque en la
lente física de la cámara.

Vision Pipeline Health: ACTIVE

## Checklist de Validación MLOps (CNN)

##### Normalización Z-Score/MinMax

¿Se garantizó que los tensores de entrada estén en rango [0, 1] o
[-1, 1]?

##### Grad-CAM Visual Audit

¿Los mapas de calor confirman que la red mira los defectos y no
el ruido de fondo?

##### Augmentation Bias Check

¿Se validó que el aumento de datos no está introduciendo patrones
irreales?

##### Cuantización Validada

¿La pérdida de precisión tras convertir a INT8/FP16 es aceptable
para el negocio?

##### Latency SLA (Edge)

¿El tiempo de predicción es menor al tiempo que tarda la pieza en
pasar por la cinta?

##### Linaje de Imágenes

¿Está el hash del dataset vinculado a la versión del modelo en el
registro?

• Caso Práctico: Quality Control con CNN
> [**Algoritmo - Redes Neuronales Convolucionales**](../algoritmos/Deep_Learning-CNN.md)
 • 
> [**Practica - Redes Neuronales Convolucionales**](../Sample/Deep_Learning-CNN.md)
 • 
> [**Codigo - Redes Neuronales Recurrentes**](Deep_Learning-RNN.md)
--