# Arquitectura de *Modelos*
> **Guía de Selección v2.0**

Elegir el algoritmo correcto es el corazón del Machine Learning. Aquí exploramos los pilares que definen cómo las máquinas aprenden y deciden.

## 📖 Definición
Un algoritmo de machine learning es un conjunto definido de pasos que se utilizan para entrenar un modelo para que pueda hacer predicciones útiles en su caso de uso del mundo real. Comprende no solo la forma en que el modelo asigna un punto de datos de entrada a su salida correspondiente, sino también el proceso de optimización de las predicciones del modelo para "ajustar" un conjunto de datos de entrenamiento de ejemplos relevantes. Es un algoritmo que permite a una máquina aprender de los datos.

---

## 🧭 Leyenda / Tipologías
- ✅ **Supervisado:** Predicción con guía
- 🔀 **No Supervisado:** Descubrimiento autónomo
- 🧠 **Deep Learning:** Representación compleja

---

## 🧩 Catálogo de Algoritmos

### 1. Regresión Lineal `Supervisado`
> El abuelo de los algoritmos. Predice un valor numérico continuo basándose en la relación lineal entre variables.
- 🎯 **¿Para qué se usa?:** Predicción de precios, Tendencias de ventas, Estimación de demanda
- ✔️ **Ventajas:** Muy rápido, Fácil de interpretar, No requiere mucho poder cómputo
- 💡 **Características:** Relación lineal, Baja complejidad, Sensible a outliers

### 2. Random Forest `Supervisado`
> Un conjunto de múltiples árboles de decisión que "votan" para dar un resultado más robusto y preciso.
- 🎯 **¿Para qué se usa?:** Detección de fraude, Clasificación de clientes, Diagnóstico médico
- ✔️ **Ventajas:** Alta precisión, Maneja datos faltantes, Evita el sobreajuste (overfitting)
- 💡 **Características:** Ensemble learning, Alta interpretabilidad, Funciona bien con datos tabulares

### 3. K-Means Clustering `No Supervisado`
> Agrupa datos similares en "K" grupos basándose en sus características, sin conocer etiquetas previas.
- 🎯 **¿Para qué se usa?:** Segmentación de clientes, Compresión de imágenes, Análisis de perfiles
- ✔️ **Ventajas:** Descubre patrones ocultos, Escalable a grandes datasets, Simple de implementar
- 💡 **Características:** Basado en distancias, Requiere definir K, No requiere etiquetas

### 4. Support Vector Machines `Supervisado`
> Busca el hiperplano óptimo que separa los datos en diferentes clases con el máximo margen posible.
- 🎯 **¿Para qué se usa?:** Reconocimiento facial, Clasificación de texto, Bioinformática
- ✔️ **Ventajas:** Efectivo en espacios de alta dimensión, Versátil con Kernels, Robusto ante ruido
- 💡 **Características:** Maximización de margen, Complejidad matemática, Eficiencia en memoria

### 5. Redes Neuronales (Deep Learning) `Deep Learning`
> Inspiradas en el cerebro humano. Capas de neuronas artificiales que aprenden representaciones complejas de datos.
- 🎯 **¿Para qué se usa?:** Visión por computadora, Procesamiento de lenguaje (NLP), Generación de contenido
- ✔️ **Ventajas:** Aprende características automáticamente, Máxima precisión en datos masivos, Extremadamente flexible
- 💡 **Características:** Capas ocultas, Requiere mucha GPU, Caja negra (difícil de explicar)

### 6. XGBoost / Gradient Boosting `Supervisado`
> Algoritmo de optimización que construye modelos de forma secuencial, corrigiendo los errores de los anteriores.
- 🎯 **¿Para qué se usa?:** Competiciones de Kaggle, Predicción de clics (CTR), Sistemas de recomendación
- ✔️ **Ventajas:** Rendimiento estado del arte, Maneja penalizaciones (L1/L2), Procesamiento en paralelo
- 💡 **Características:** Gradient Descent, Alta eficiencia, Muchos hiperparámetros

---

## ⚖️ Ingeniería de Decisión: ¿Cuál elegir?
No hay un algoritmo "mejor" para todo. La elección depende de la cantidad de datos, el tipo de problema y los recursos disponibles.

| Escenario | Recomendación |
|---|---|
| 📉 **Pocos datos + Rapidez** | Regresión Lineal o Naive Bayes |
| 📊 **Datos Tabulares + Precisión** | XGBoost o Random Forest |
| 🖼️ **Imágenes / Audio / Texto** | Redes Neuronales (CNN/Transformers) |
| 🧩 **Sin etiquetas + Segmentar** | K-Means o DBSCAN |

---

## 🔄 Ciclo de Mejora Continua
`01. Definir` → `02. Probar` → **`03. Iterar`**

*Conceptos de Ciencia de Datos • 2024*

---