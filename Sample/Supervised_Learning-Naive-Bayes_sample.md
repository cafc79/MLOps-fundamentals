# Caso Práctico: Naive Bayes en Filtros de Spam

# Caso Real: Clasificación de Texto en Tiempo Real

# Filtro de Spam con Naive Bayes

¿Cómo decide tu correo qué mensajes van a la bandeja de entrada y cuáles al basurero? Naive Bayes
utiliza probabilidades matemáticas puras para analizar palabras clave y tomar una decisión instantánea.

**Guía de Negocio:** Haz clic en cada etapa para entender
cómo transformamos un texto crudo en una decisión de seguridad basada en evidencias.

1

### Objetivo del Filtro

Categorizar mensajes en dos grupos: Spam (No deseado) y Ham
(Deseado/Legítimo).

Analizamos un historial de millones de correos ya etiquetados por humanos. El algoritmo
estudiará la frecuencia de aparición de cada palabra en ambos grupos para construir su
"conocimiento previo".

Variable Target Binaria

Aprendizaje de Frecuencias

Base de Datos Histórica

2

### Bolsa de Palabras

Convertimos el texto del correo en una lista de evidencias contables.

El algoritmo no lee frases, cuenta palabras clave como: "Gana", "Bitcoin", "Urgente" o
"Descuento". Ignora el orden y se enfoca en cuántas veces aparece cada término sospechoso.

Tokenización de Texto

Eliminación de Relleno (Stopwords)

Vector de Características

3

### Conocimiento Previo

¿Qué tan probable es recibir spam antes de siquiera leer el correo?

Si en la historia del banco el 30% de los correos han sido spam, esa es nuestra base. Naive
Bayes empieza con esta suposición y la irá actualizando a medida que encuentre palabras en el
nuevo mensaje.

Probabilidad Inicial P(Spam)

Proporción de Clases

Punto de Partida Estadístico

4

### Simplificación Naive

Asumimos que las palabras son independientes entre sí para ganar
velocidad.

Aunque "Gana" y "Dinero" suelen ir juntas, el algoritmo las trata como si no tuvieran relación.
Esto parece erróneo, pero permite que los cálculos sean extremadamente rápidos, lo cual es vital
para procesar millones de correos.

Independencia de Atributos

Alta Eficiencia Computacional

Escalabilidad Masiva

5

### Cálculo de Veracidad

¿Qué tan probable es ver estas palabras si el correo fuera realmente
spam?

Multiplicamos las probabilidades individuales. Si la palabra "Gratis" aparece en el 80% del spam
pero solo en el 1% del correo bueno, su presencia empuja fuertemente la decisión hacia la
categoría de Spam.

Multiplicación de Evidencias

Peso de Palabras Clave

Actualización Bayesiana

6

### Veredicto Final

Comparamos la probabilidad de ser Spam vs. la de ser Ham. La mayor
gana.

Es el principio **Maximum A Posteriori**. El algoritmo emite una puntuación:
"Probabilidad de Spam: 99.8%". El sistema de correo lee esta cifra y mueve el mensaje a la
carpeta de correo no deseado sin que lo veas.

Selección de la Clase Ganadora

Acción de Carpeta Automática

Respuesta en Milisegundos

7

### Eficiencia de Escala

Logramos filtrar miles de millones de mensajes diarios con un costo de
servidor mínimo.

Gracias a su simplicidad matemática, Naive Bayes es imbatible en velocidad. Esto permite que las
empresas de correo analicen tu buzón en tiempo real sin retrasar la entrega de mensajes
importantes.

Bajo Consumo de RAM/CPU

Procesamiento Instantáneo

Fiabilidad en Big Data

## La Magia de la Simplicidad

Naive Bayes es el ejemplo perfecto de que **"más complejo no siempre es mejor"**. Para
la clasificación de texto, su rapidez y robustez ante datos irrelevantes lo mantienen como el
estándar de la industria después de décadas.

Ultra
Veloz
Probabilístico
Maestro del
NLP

> [**Algoritmo - Naive-Bayes**](../algoritmos/Supervised_Learning-Naive-Bayes.md)
• 
> [**Codigo - Naive-Bayes**](../Code/Supervised_Learning-Naive-Bayes.md)
• 
> [**Practica - Regresion Lineal**](Supervised_Learning-K-Nearest-Neighbors.md)
---