# Modelos Probabilísticos (Supervisados)

# Naive Bayes

Un clasificador probabilístico basado en el Teorema de Bayes que destaca por su increíble velocidad y
eficacia en el procesamiento de lenguaje natural.

**Guía del Algoritmo:** Haz clic en cada tarjeta para
explorar la lógica bayesiana y por qué la "ingenuidad" (independence assumption) lo hace tan rápido.

1

### Teorema de Bayes

La base matemática: calcula la probabilidad de una hipótesis dada la
evidencia previa.

Representado por **P(A|B) = [P(B|A)P(A)] / P(B)**. Permite actualizar nuestras
creencias sobre una clase a medida que observamos nuevas características de los datos.

Probabilidad Condicional

Conocimiento Previo (Prior)

Actualización de Verosimilitud

2

### Independencia Fuerte

Por qué es "Ingenuo": asume que todas las características son
totalmente independientes entre sí.

Aunque en el mundo real las variables suelen estar relacionadas, esta simplificación permite que
el algoritmo sea extremadamente rápido y funcione bien incluso con pocos datos.

Desacoplamiento de Variables

Simplicidad Computacional

Eficiencia con Alta Dimensión

3

### Variantes del Modelo

Se adapta según la naturaleza de los datos: continuos, conteos o
binarios.

**Gaussiano:** Para datos numéricos continuos. **Multinomial:** Para
conteo de palabras (frecuencia). **Bernoulli:** Para presencia o ausencia (0/1).

Gaussian NB (Distribución Normal)

Multinomial NB (NLP)

Bernoulli NB (Binario)

4

### Dominio en Texto

Es el estándar histórico para clasificar documentos y detectar correos
no deseados.

Calcula la probabilidad de que un mensaje sea "Spam" basándose en la presencia de palabras clave
(ej: "gratis", "oferta"). Su ligereza lo hace ideal para filtros en tiempo real.

Clasificación de Documentos

Análisis de Sentimiento

Categorización Temática

5

### Suavizado de Laplace

Técnica para evitar que una sola probabilidad de "cero" anule todo el
cálculo del modelo.

Si una palabra nunca apareció en el entrenamiento, su probabilidad sería 0. Al multiplicar, el
resultado final sería 0. Laplace añade un pequeño valor (+1) para mantener el modelo funcional.

Corrección de Frecuencia Cero

Estabilidad Matemática

Manejo de Out-of-Vocab

6

### Rendimiento

Entrenamiento lineal: es uno de los algoritmos más rápidos de entrenar
en el ecosistema de ML.

Como solo requiere calcular frecuencias y promedios, escala perfectamente a millones de
registros con un consumo de memoria mínimo comparado con redes neuronales o SVM.

Tiempo de Ejecución O(n)

Bajo Costo de Cómputo

Ideal para Big Data

7

### MAP Decision

Maximum A Posteriori: la clase ganadora es aquella con la probabilidad
más alta.

El modelo calcula las probabilidades para todas las categorías posibles y selecciona la máxima.
Es una decisión puramente estadística basada en la evidencia presente en los datos de entrada.

Probabilidad A Posteriori

Comparación de Clases

Salida Categórica Segura

## Valor de Naive Bayes

Es el algoritmo de referencia cuando necesitas resultados rápidos con poco esfuerzo de
preprocesamiento. Su robustez ante datos irrelevantes y su facilidad para trabajar con texto lo
mantienen como un pilar fundamental en la IA moderna.

Ultra
Veloz
Maestro de
NLP
Eficiente en
Datos

> [* Prev *](Supervised_Learning-SVM.md "Máquinas de Vectores de Soporte")
> [* Practica - Naive-Bayes *](Sample/Supervised_Learning-Naive-Bayes.md)
> [* Codigo - Naive-Bayes *](Code/Supervised_Learning-Naive-Bayes.md)
> [* Algoritmo - Regresion Lineal *](Supervised_Learning-K-Nearest-Neighbors.md)
---