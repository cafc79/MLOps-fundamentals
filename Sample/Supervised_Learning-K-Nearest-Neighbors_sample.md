# Caso Práctico: KNN en Recomendaciones

# Caso Real: Recomendación por Similitud de Retail con KNN

# Personalización con KNN

¿Qué producto debería sugerirle a este nuevo cliente? KNN encuentra a los usuarios más "parecidos" en
nuestra base de datos para predecir qué artículos le interesarán, basándose en la premisa de que
clientes con gustos similares compran cosas similares.

**Guía de Negocio:** Haz clic en cada etapa para entender cómo
transformamos coordenadas matemáticas en sugerencias de compra altamente efectivas.

1

### Criterio de Vecindad

Identificamos qué hace que dos clientes sean "vecinos" en nuestro
espacio digital.

Analizamos el historial de 50,000 usuarios. No buscamos amigos, buscamos "gemelos estadísticos":
personas que compran en las mismas categorías, a las mismas horas y con tickets promedio
similares.

Perfil de Usuario 360°

Mapeo de Comportamiento

Segmentación Dinámica

2

### Variables de Perfil

Elegimos las características numéricas que nos permitirán calcular
distancias matemáticas.

Consideramos: Edad, Frecuencia de compra (mensual), Gasto promedio por pedido y afinidad por
categorías (0-1). Estos datos se convierten en las "coordenadas" del cliente en nuestro mapa de
mercado.

Recencia de Compra

Valor de Vida (CLV)

Datos Demográficos

3

### Normalización

Crucial: Ajustamos todas las variables para que tengan el mismo peso
en la recomendación.

Sin esto, el algoritmo creería que el "Salario" es 1000 veces más importante que la "Frecuencia
de compra" solo por tener números más grandes. Llevamos todo a una escala de 0 a 1 para una
comparación justa.

Equilibrio de Atributos

Min-Max Scaling

Precisión de Distancia

4

### Métrica Euclidiana

El algoritmo mide la "línea recta" imaginaria entre nuestro cliente y
todos los demás.

KNN calcula instantáneamente qué tan lejos está el perfil actual de cada registro histórico. Los
clientes con la distancia más corta son declarados los "Vecinos más Cercanos" y son la base de
la sugerencia.

Proximidad Matemática

Identificación de Patrones

Clasificación Espacial

5

### El Número K

Decidimos cuántos vecinos consultaremos (ej. K=5) para generar la
recomendación final.

Si K es muy pequeño (1), somos vulnerables a excepciones extrañas. Si es muy grande (100), la
recomendación se vuelve genérica. Con un K=5 bien ajustado, capturamos el nicho perfecto del
usuario.

Optimización de Hiperparámetro

Balance de Sesgo-Varianza

Validación Técnica

6

### Voto de Preferencia

Analizamos qué compraron esos 5 vecinos que nuestro cliente actual aún
no tiene.

Si 4 de los 5 vecinos compraron una "Cámara Pro", el sistema asume que el cliente actual también
la querrá. Es una recomendación basada en la "experiencia prestada" de otros usuarios similares.

Votación por Mayoría

Filtrado Colaborativo

Salida Personalizada

7

### Aumento de Conversión

Medimos el éxito mediante el incremento en el CTR y las ventas por
sugerencia.

Al implementar KNN, la relevancia de los anuncios subió un 25%. El cliente siente que la tienda
"lo conoce", lo que reduce la fricción de búsqueda y maximiza el valor del carrito de compra de
forma orgánica.

ROI de Datos

Fidelización de Cliente

Personalización de Escala

## La Inteligencia del "Parezco"

KNN es el algoritmo más humano de todos porque replica cómo tomamos decisiones: **preguntando
a quienes son como nosotros**. No necesita modelos matemáticos complejos de entender,
solo un buen mapa de proximidad.

Intuitivo
Sin
Entrenamiento
Basado en
Datos

© 2024 Laboratorio de Ciencia de Datos • Caso Práctico: Recomendador de Retail con KNN
> [**Algoritmo - K-Nearest Neighbors**](../algoritmos/Supervised_Learning-K-Nearest-Neighbors.md)
• 
> [**Codigo - K-Nearest Neighbors**](../code/Supervised_Learning-K-Nearest-Neighbors.md)
• 
> [**Practica - Árboles de Decisión**](Supervised_Learning-Arboles-Decision.md)
---