# Aprendizaje por Refuerzo (RL)

# Q-Learning: La Inteligencia del Refuerzo

Q-Learning es un algoritmo de aprendizaje por refuerzo fuera de política (off-policy) que busca
encontrar la mejor acción a tomar dado un estado actual, aprendiendo a través de la interacción directa
con un entorno.

**Guía del Algoritmo:** Haz clic en cada tarjeta para
explorar cómo un agente autónomo aprende a maximizar sus recompensas mediante la prueba y el error.

1

### Ciclo de Interacción

El núcleo del algoritmo: un agente que observa un estado, ejecuta una
acción y recibe una consecuencia.

El **Agente** es la entidad que toma decisiones. El **Entorno** es el
mundo donde vive. En cada paso, el agente pasa del Estado $S$ al Estado $S'$ mediante una Acción
$A$, recibiendo una Recompensa $R$.

Percepción del Estado ($S$)

Ejecución de Acción ($A$)

Transición de Entorno

2

### Q-Table (Memoria)

Una matriz de referencia donde el agente guarda el "valor" o calidad
de cada acción en cada estado.

Es la "hoja de trucos" del agente. Las filas son estados y las columnas son acciones. El valor
**Q(s, a)** representa la recompensa total esperada a largo plazo si se toma la
acción $a$ en el estado $s$.

Mapeo Estado-Acción

Valores de Calidad (Q)

Almacenamiento de Experiencia

3

### Feedback Escalar

El sistema de guía. Las recompensas positivas refuerzan acciones, las
negativas las penalizan.

A diferencia del aprendizaje supervisado, no hay etiquetas. El agente solo sabe que lo hizo
"bien" o "mal" mediante un valor numérico. El objetivo es maximizar la \*\*Recompensa Acumulada\*\*
total.

Refuerzo Positivo

Señal de Error/Acierto

Optimización de Objetivo

4

### Epsilon-Greedy

El dilema constante: ¿Usar lo que ya sé (Explotar) o probar algo nuevo
(Explorar)?

Mediante el parámetro $\epsilon$, el agente elige acciones al azar un porcentaje del tiempo para
descubrir mejores caminos, reduciendo esta curiosidad a medida que se vuelve experto.

Factor de Curiosidad ($\epsilon$)

Descubrimiento de Estrategias

Salida de Mínimos Locales

5

### Fórmula de Actualización

La regla matemática que permite al agente aprender de sus errores y
actualizar la Q-Table.

$Q(s,a) = Q(s,a) + \alpha [R + \gamma \max Q(s', a') - Q(s,a)]$. Combina la recompensa actual
con la mejor estimación de recompensas futuras, ajustada por un factor de aprendizaje
($\alpha$).

Tasa de Aprendizaje ($\alpha$)

Factor de Descuento ($\gamma$)

Valor Temporal

6

### Aprendizaje TD

El agente no espera al final de la partida para aprender; se
auto-corrige en cada paso individual.

Es la diferencia entre lo que el agente esperaba recibir y lo que realmente recibió. Esta
"sorpresa" o error de predicción es lo que impulsa el ajuste constante de los valores en la
memoria.

Actualización Paso a Paso

Reducción de Error de Predicción

Eficiencia Temporal

7

### Convergencia

El resultado final: una estrategia (política) que garantiza el mejor
desempeño posible en el entorno.

Una vez que los valores Q dejan de cambiar significativamente, el agente simplemente elige la
acción con el valor más alto en cada estado. Ha aprendido a "jugar a la perfección".

Política $\pi^\*$ Óptima

Comportamiento Maestro

Estabilidad de Decisiones

## La Meta: Autonomía Total

Q-Learning es la base de la robótica, los videojuegos inteligentes y la logística compleja. Permite
que las máquinas aprendan a resolver problemas donde no hay ejemplos previos, solo metas y reglas.

Auto-Aprendizaje
Robusto
Dinámico

> [* Prev *](Unsupervised_Learning-Hierarchical-Clustering.md "Agrupamiento Jerárquico")
> [* Practica - Q-Learning *](Sample/Reinforcement_Learning-Q-Learning.md)
> [* Codigo - Q-Learning *](Code/Reinforcement_Learning-Q-Learning.md)
> [* Algoritmo - Perceptrón Multicapa *](Deep_Learning-Perceptron-Multicapa.md)
---