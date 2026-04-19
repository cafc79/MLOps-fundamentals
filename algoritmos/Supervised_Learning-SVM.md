# Modelos de Clasificación y Regresión

# Máquinas de Vectores de Soporte

SVM es un algoritmo de aprendizaje supervisado extremadamente potente que busca encontrar el límite de
decisión óptimo para separar clases con la mayor precisión posible.

**Guía del Algoritmo:** Haz clic en cada tarjeta para
explorar la geometría de los datos y cómo SVM gestiona la separación en espacios de alta dimensión.

1

### Hiperplano

El objetivo principal: encontrar una frontera (línea, plano o
hiperplano) que separe perfectamente las clases.

En un espacio de 2D es una línea, en 3D un plano, y en dimensiones superiores se denomina
hiperplano. SVM busca aquel que divida los datos de manera óptima según sus etiquetas.

Límite de Decisión

Separación Geométrica

Clasificación Lineal

2

### Margen Máximo

SVM no solo separa; busca la calle más ancha posible entre las clases
para maximizar la seguridad.

El margen es la distancia entre el hiperplano y los puntos más cercanos de cada clase. Al
maximizar este margen, el modelo se vuelve más robusto y generaliza mejor ante datos nuevos.

Maximizador de Distancia

Robustez Predictiva

Zona de Seguridad

3

### Vectores de Soporte

Los puntos de datos críticos que tocan el margen y definen la posición
del hiperplano.

Son los ejemplos más difíciles de clasificar. Si eliminas estos puntos, el hiperplano cambiaría
de posición. El algoritmo se llama así porque solo depende de estos "vectores" clave.

Puntos de Influencia

Definición de Frontera

Eficiencia en Datos

4

### El Truco del Kernel

La capacidad de transformar datos no lineales en un espacio superior
donde sí son separables.

Cuando los datos están mezclados, el Kernel proyecta los datos a una dimensión mayor (ej. de 2D
a 3D) para encontrar un plano que los separe. Existen Kernels Lineales, Polinómicos y RBF.

Transformación Dimensional

Manejo de No-Linealidad

RBF / Polinómico

5

### Parámetro C

Controla el equilibrio entre maximizar el margen y minimizar los
errores de clasificación.

Un **C pequeño** prioriza un margen más ancho (más errores permitidos). Un
**C grande** prioriza clasificar todo correctamente (margen más estrecho),
arriesgando sobreajuste.

Margen Blando (Soft Margin)

Control de Overfitting

Penalización de Errores

6

### Parámetro Gamma

Específico para Kernels como RBF; define hasta qué distancia llega la
influencia de un punto.

**Gamma alto** hace que solo los puntos cercanos influyan (límite muy ajustado).
**Gamma bajo** hace que los puntos lejanos también influyan (límite más suave y
genérico).

Radio de Influencia

Definición de Curvatura

Ajuste Local vs Global

7

### Multiclase & SVR

Extensión para clasificar múltiples etiquetas y su aplicación para
problemas de Regresión (SVR).

Aunque es nativamente binario, usa técnicas como **One-vs-One** para manejar
múltiples clases. Además, el **Support Vector Regression (SVR)** aplica la misma
lógica para predecir valores continuos.

Estrategia OvO / OvR

Support Vector Regression

Flexibilidad de Modelo

## Valor de las SVM

SVM es excepcional para datos de alta dimensión (cuando tienes muchas columnas) y conjuntos de datos
pequeños pero complejos. Su base matemática sólida ofrece una frontera de decisión muy clara y
eficiente en memoria.

Alta
Dimensión
Precisión
Quirúrgica
Kernel
Magic

> [* Prev *](Supervised_Learning-Random-Forest.md "Random Forest")
> [* Practica - Máquinas de Vectores de Soporte *](Sample/Supervised_Learning-SVM.md)
> [* Codigo - Máquinas de Vectores de Soporte *](Code/Supervised_Learning-SVM.md)
> [* Algoritmo - Naive Bayes *](Supervised_Learning-Naive-Bayes.md)
---