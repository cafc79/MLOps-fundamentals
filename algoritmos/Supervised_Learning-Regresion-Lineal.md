# Modelos Estadísticos (Supervisados)
# Algoritmo Regresión Lineal

La Regresión Lineal es el algoritmo fundamental para modelar y predecir una variable continua basándose
en la relación lineal entre variables independientes y dependientes.

**Guía del Algoritmo:** Haz clic en cada tarjeta para explorar
los fundamentos matemáticos y la lógica detrás de la línea de mejor ajuste.

1

### Relación de Variables

Busca modelar cómo una variable de entrada (X) impacta directamente en
una variable de salida (Y).

El objetivo es encontrar una correlación matemática donde un cambio en la variable independiente
resulte en un cambio proporcional en la dependiente. Es la base de las proyecciones y
tendencias.

Variable Dependiente (Target)

Variable Independiente (Feature)

Análisis de Correlación

2

### Función Hipótesis

La representación matemática: Y = β₀ + β₁X + ε. Define la línea recta
que atraviesa los datos.

**β₀** es el sesgo (donde la línea cruza el eje Y), **β₁** es el peso
o pendiente (la fuerza del impacto de X), y **ε** es el error residual que el
modelo no puede explicar.

Coeficientes (Pesos)

Intercepto (Sesgo)

Término de Error

3

### Optimización OLS

El método de Mínimos Cuadrados Ordinarios busca minimizar la suma de
los errores al cuadrado.

El algoritmo ajusta la línea de forma que las distancias (residuos) entre los puntos reales y la
línea de predicción sean las más pequeñas posibles en conjunto, penalizando los errores grandes.

Minimización de Residuos

Función de Costo

Mejor Ajuste Global

4

### Supuestos del Modelo

Para que la regresión sea confiable, los datos deben cumplir con
ciertos principios estadísticos.

Incluye la **Linealidad** (relación recta), **Homocedasticidad**
(varianza constante del error), e **Independencia** de las observaciones. Ignorar
estos supuestos invalida las predicciones.

Normalidad de Errores

No-Multicolinealidad

Varianza Constante

5

### Métricas de Éxito

¿Qué tan bien se ajusta la línea a la realidad? Medimos la precisión
mediante indicadores técnicos.

El **R-cuadrado (R²)** indica cuánta varianza de los datos explica el modelo. El
**Error Cuadrático Medio (MSE)** y el MAE miden la magnitud de las equivocaciones
en las unidades del target.

R² Score (Bondad de ajuste)

MSE / RMSE

Error Absoluto Medio (MAE)

6

### Complejidad

La regresión puede escalar desde una sola variable hasta cientos de
ellas simultáneamente.

La **Regresión Simple** usa una X para predecir Y. La **Regresión
Múltiple** utiliza múltiples X, permitiendo capturar influencias combinadas de
diferentes factores sobre el resultado final.

Regresión Univariada

Regresión Multivariada

Pesos Relativos

7

### Regularización

Técnicas para evitar el sobreajuste mediante la penalización de
coeficientes demasiado grandes.

Modelos como **Ridge (L2)** y **Lasso (L1)** añaden un término de
penalización a la función de costo. Esto simplifica el modelo, reduce el ruido y mejora la
capacidad de generalizar con datos nuevos.

Penalización L1 / L2

Prevención de Overfitting

Selección de Atributos

## Valor de la Regresión Lineal

Es el punto de partida esencial para cualquier análisis predictivo. Su simplicidad ofrece una
interpretabilidad inigualable: permite saber exactamente cuánto valor aporta cada variable al
resultado final.

Interpretación
Directa
Bajo Costo
Computacional
Tendencias
Claras

> [* Prev *](../docs/MLOps.md "Arquitectura de Modelos")
> [* Practica - Regresion Lineal *](../Sample/Supervised_Learning-Regresion_Lineal.md)
> [* Codigo - Regresion Lineal *](../Code/Supervised_Learning-Regresion_Lineal.md)
> [* Algoritmo - Regresion Logistica *](Supervised_Learning-Regresion-Logistica.md)
---
