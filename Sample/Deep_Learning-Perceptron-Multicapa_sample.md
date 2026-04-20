# Caso Práctico: MLP en Reconocimiento de Documentos

# Caso Real: Digitalización Automatizada

# Reconocimiento con MLP

¿Cómo lee un banco miles de cheques escritos a mano cada hora? El Perceptrón Multicapa (MLP) actúa como
un cerebro digital capaz de interpretar patrones de píxeles y convertirlos en datos financieros
precisos.

**Guía de Inteligencia:** Haz clic en cada etapa para
entender cómo una red neuronal transforma trazos de tinta en información transaccional.

1

### Capa de Entrada

Convertimos la imagen del cheque en una matriz numérica que la red
pueda "ver".

Escaneamos el documento y aislamos los dígitos. Cada imagen de 28x28 píxeles se convierte en un
vector de 784 neuronas de entrada. Los valores representan la intensidad del gris en cada punto
del trazo.

Segmentación de caracteres

Normalización de escala

Representación vectorial

2

### Capas Ocultas

Donde la red neuronal descompone el dígito en formas abstractas y
rasgos clave.

Diseñamos dos capas intermedias con 128 y 64 neuronas. Aquí, el MLP aprende a identificar
curvas, bucles y líneas rectas. Es el nivel de abstracción donde se diferencia un "8" de un "3".

Extracción de características

Jerarquía de patrones

Profundidad de aprendizaje

3

### Función ReLU

La lógica que decide qué neuronas "se disparan" para confirmar una
forma detectada.

Aplicamos la activación ReLU para que la red pueda aprender relaciones complejas no lineales. Si
la señal es negativa (ruido), se apaga; si es positiva y fuerte, pasa a la siguiente capa con
intensidad.

Umbral de decisión

Eficiencia de cómputo

Mitigación de ruido

4

### Entrenamiento

El proceso de aprendizaje mediante el cual la red ajusta sus
conexiones internas.

Usamos el dataset MNIST con 60,000 ejemplos. Mediante **Retropropagación**, la red
"entiende" cuándo se equivoca al leer un número y ajusta los pesos de sus neuronas para no
repetir el error.

Descenso del gradiente

Corrección de error

Optimización iterativa

5

### Clasificación

El resultado final: la red elige a qué categoría (del 0 al 9)
pertenece la imagen.

La última capa tiene 10 neuronas. Cada una representa un número. Usamos **Softmax**
para que la red nos diga: "Estoy un 99.5% segura de que este garabato es un número 7".

Probabilidad de clase

Selección del máximo

Etiquetado digital

6

### Evaluación Real

Probamos el MLP con cheques reales que nunca han sido procesados por
el sistema.

Medimos la tasa de acierto. Si la confianza es menor al 90%, el cheque se deriva a un humano. Un
MLP bien entrenado puede procesar el 95% de los cheques sin intervención, reduciendo costos
operativos.

Umbral de confianza

Reducción de costos

Precisión operativa

7

### Servicio Masivo

Implementación final del cerebro digital en la red de cajeros
automáticos.

El banco ahora liquida depósitos en segundos. El MLP permite una escalabilidad infinita:
procesar 10 o 10,000,000 de documentos cuesta prácticamente lo mismo una vez que el modelo está
entrenado.

Disponibilidad 24/7

Velocidad de respuesta

Valor al cliente final

## Inteligencia Profunda

El Perceptrón Multicapa es la base de la IA moderna. Su capacidad para **aprender
automáticamente** representaciones complejas permite que los bancos dejen de programar
reglas fijas y empiecen a usar modelos que "entienden" la diversidad del mundo real.

Aproximador
Universal
Escalable
Automatizado

> [**Algoritmo - Perceptrón Multicapa**](../Algoritmos/Deep_Learning-Perceptron-Multicapa.md)
• 
> [**Codigo - Perceptrón Multicapa**](../Code/Deep_Learning-Perceptron-Multicapa.md)
• 
> [**Practica - Redes Neuronales Convolucionales**](Deep_Learning-CNN.md)
---