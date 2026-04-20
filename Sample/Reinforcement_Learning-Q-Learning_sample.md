# Q-Learning en Robótica Logística

# Optimización con Q-Learning: Navegación Autónoma de AGVs

¿Cómo aprende un robot a entregar paquetes en un almacén gigante sin mapas previos? Q-Learning permite
que el agente explore el entorno y aprenda la ruta más corta mediante un sistema de premios y castigos,
sin intervención humana.

**Guía de Inteligencia:** Haz clic en cada etapa para
entender cómo un robot "ciego" se convierte en un experto en logística mediante el refuerzo.

1

### El Espacio de Estados

Definimos el almacén como una cuadrícula donde cada celda es un
"Estado" posible.

El robot necesita saber dónde está. Dividimos el piso en coordenadas (X, Y). Algunas celdas son
pasillos libres, otras son estanterías (obstáculos) y una es el punto de carga (meta). Hay 100
estados posibles en este mapa.

Grilla de navegación

Mapeo de obstáculos

Punto de entrega final

2

### El Set de Acciones

El robot solo puede realizar 4 movimientos básicos en cada turno.

En cualquier estado $S$, el agente puede elegir una acción $A$: Norte, Sur, Este u Oeste. El
objetivo del aprendizaje es saber cuál de estas cuatro opciones es la mejor para el estado
actual.

Movimientos discretos

Toma de decisiones local

Simplicidad de control

3

### La Función de Recompensa

Le decimos al robot qué está bien y qué está mal mediante valores
numéricos.

Diseñamos el feedback: **+100** por llegar a la meta, **-10** si choca
con una estantería, y **-1** por cada segundo que pasa (para obligarlo a ser
rápido). El robot "siente" el número y busca maximizar la suma total.

Refuerzo Positivo (Meta)

Penalización de colisión

Incentivo de velocidad

4

### Creación de la Q-Table

El robot crea una tabla vacía donde anotará el valor de cada acción en
cada celda.

Es una matriz de 100 filas (estados) x 4 columnas (acciones). Al principio todos los valores son
0. A medida que el robot se mueve y recibe premios, va "anotando" cuáles movimientos valen más
la pena en cada posición.

Almacén de experiencia

Referencia de valor

Actualización iterativa

5

### Exploración vs Explotación

El robot realiza 1,000 "partidas" de prueba para aprender el mapa.

Usamos el factor $\epsilon$ (Epsilon). Al inicio, el robot se mueve al azar para descubrir el
premio (Exploración). Una vez que lo encuentra, empieza a usar su Q-Table para repetir los
caminos exitosos (Explotación).

Curiosidad artificial

Aprendizaje acumulado

Salida de mínimos locales

6

### Política Óptima

La Q-Table se estabiliza. El robot ya no duda: sabe exactamente qué
hacer.

Tras el entrenamiento, extraemos la "Política" ($\pi$). Si el robot está en la celda (3,4), mira
su tabla y ve que "Este" tiene el valor más alto (ej. 85.5). Ha aprendido la ruta más eficiente
evitando todos los obstáculos.

Comportamiento Maestro

Rutas sin errores

Estabilidad de decisión

7

### Valor Operativo

Implementamos el cerebro aprendido en la flota real de AGVs.

El almacén ahora es 100% autónomo. Los robots consumen un 15% menos de batería al no dar vueltas
innecesarias y el tiempo de entrega de paquetes se reduce drásticamente. El sistema se
auto-ajusta si movemos una estantería.

Eficiencia Energética

Adaptabilidad Dinámica

Escalabilidad Logística

## Inteligencia Sin Manuales

Q-Learning es la base de la robótica moderna porque permite que las máquinas aprendan a resolver
problemas donde **no existen ejemplos previos**. El robot no necesita que un humano le
diga qué hacer; solo necesita saber cuál es la meta.

Autonomía
Refuerzo
Optimización

> [**Algoritmo - Q-Learning**](../algoritmos/Reinforcement_Learning-Q-Learning.md)
• 
> [**Codigo - Q-Learning**](../Code/Reinforcement_Learning-Q-Learning.md)
• 
> [**Practica - Perceptrón Multicapa**](Deep_Learning-Perceptron-Multicapa.md)
---
