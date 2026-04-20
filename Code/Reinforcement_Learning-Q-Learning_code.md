# Q-Learning Pro

# Optimización por Refuerzo y Ecosistema MLOps

#### Lógica de Selección: ¿Por qué Q-Learning?

Es el algoritmo de elección para control autónomo cuando:

• El espacio de estados y acciones es **discreto y finito**.

• No existe un dataset de "respuestas correctas" (solo premios/castigos).

• Se requiere una **política fuera de política (Off-policy)** para aprender de
la exploración.

• El entorno puede ser modelado como un Proceso de Decisión de Markov (MDP).

#### Elemento Distintivo: La Q-Table

"Q-Learning no predice valores; estima la calidad de las acciones futuras. Es un buscador de la
'Ecuación de Bellman', permitiendo que una máquina aprenda a navegar el caos mediante la
persistencia de la experiencia."

Fase 1: Diseño de Entorno & Recompensas

## Modelado del Espacio de Estados

En RL, los "datos" son el entorno. El error fatal es un diseño de recompensas
ambiguo que permite el **Reward Hacking**.

import numpy as np
# Definición del entorno (Grilla de 10x10 para robot AGV)
n\_states = 100
n\_actions = 4 # Arriba, Abajo, Izquierda,
Derecha
# Inicialización de la Q-Table con ceros (o valores pequeños aleatorios)
q\_table = np.zeros((n\_states, n\_actions))
# Ejemplo de Función de Recompensa (Diseño MLOps)
def get\_reward(current\_state, action):
if reached\_goal: return 100
if hit\_obstacle: return -50
return -1 #
Penalización por tiempo (incentiva eficiencia)

#### Error Común: Sparse Rewards

Dar una recompensa solo al final (meta). Si el camino
es largo, el agente nunca encontrará el premio. **Solución:** Usa "Reward Shaping" para
dar pequeñas pistas positivas o negativas durante el trayecto.

Fase 2: Representación & Hiperparámetros

## Discretización y Factores de Aprendizaje

Debemos decidir qué tan rápido aprende el agente ($\alpha$) y qué tanto
valora el futuro sobre el presente ($\gamma$).

# Hiperparámetros Críticos de MLOps
alpha = 0.1 # Learning Rate: Velocidad de
actualización de Q
gamma = 0.95 # Discount Factor: Importancia de
recompensas futuras
epsilon = 1.0 # Exploration Rate inicial
epsilon\_decay = 0.995 # El agente debe volverse
menos curioso con el tiempo

#### Validación Crucial: Explosión de Estados

Si tu espacio de estados es continuo (ej: coordenadas
GPS exactas), la Q-Table será infinita. \*\*Discretiza\*\* el espacio en una cuadrícula o usa Deep
Q-Networks (DQN) si el espacio es inabarcable.

Fase 3: Model Training & Tracking

## Ciclo de Aprendizaje Temporal (TD)

El agente aprende mediante la diferencia temporal entre lo esperado y lo
recibido. Registramos la recompensa acumulada por episodio.

import mlflow
with mlflow.start\_run(run\_name="q\_learning\_warehouse\_v1"):
for episode in range(total\_episodes):
state = env.reset()
# Epsilon-greedy: Decidir si explorar o explotar
if np.random.uniform(0, 1) < epsilon: action=env.action\_space.sample()
else:
action = np.argmax(q\_table[state, :])
# Actualización de Bellman
next\_state, reward = env.step(action)
old\_value = q\_table[state, action]
next\_max = np.max(q\_table[next\_state, :])
# Nueva estimación Q
q\_table[state, action] = old\_value + alpha \* (reward + gamma \* next\_max - old\_value)
# Logging de performance
mlflow.log\_metric("epsilon", epsilon,
step=episode)

Fase 4: Evaluación & Model Health

## Diagnóstico de Convergencia

### RL Health Check

Estabilidad de Q-Values
Delta < 0.001

Recompensa Promedio
Tendencia Alcista

Exploración Final
Epsilon < 0.01

Tasa de Éxito (Goal Reach)
> 98%

#### Validación de Política

"Un agente saludable es aquel que encuentra la ruta
óptima de forma consistente, sin 'titubear' entre estados."

# Verificar acciones deterministas
policy = np.argmax(q\_table, axis=1)
# Si la política cambia drásticamente en
# los últimos episodios, no hay convergencia.

#### La Trampa de los Ciclos Infinitos

Si el agente se queda atrapado en un bucle (ej: Izquierda -> Derecha ->
Izquierda), tu penalización por paso es insuficiente. \*\*Aumenta el castigo negativo por cada segundo
transcurrido\*\* para forzar la búsqueda de la salida.

Fase 5: Serving & Deployment

## Exportación de la Política Maestra

En producción, no desplegamos el bucle de entrenamiento, solo la Q-Table
final (o la política derivada).

import joblib
# Extraemos la mejor acción por estado (Política Determinista)
best\_policy = np.argmax(q\_table, axis=1)
# El artefacto de producción es ligero y extremadamente rápido
navigation\_bundle = {
"version": "v15.1.0",
"map\_id": "warehouse\_sector\_A",
"q\_table": q\_table,
"policy": best\_policy
}
joblib.dump(navigation\_bundle, 'agv\_navigator.joblib')

Fase 6: Monitoring & Environment Drift

## Vigilancia de la Dinámica del Entorno

Si movemos una estantería en el almacén, la Q-Table se vuelve obsoleta. El
monitoreo debe detectar colisiones inesperadas.

#### Alertas MLOps (RL):

##### Collision Drift

Si el número de colisiones sube > 0.1% en
producción.

##### Latency vs Path

Si el tiempo promedio para llegar a la meta
aumenta un 15%.

Online Retraining Triggered

## Checklist de Validación MLOps (RL)

##### Reward Stability

¿Se validó que el agente no está explotando un bug del entorno
para ganar puntos (Reward Hacking)?

##### Convergence Monitoring

¿Se inspeccionaron los valores Q para confirmar que han dejado de
oscilar drásticamente?

##### State Discretization

¿El nivel de granularidad del mapa es suficiente para la
precisión requerida sin causar lentitud?

##### Exploration Strategy

¿Epsilon decae lo suficientemente lento para que el agente vea
todos los estados?

##### Policy Serving Latency

¿La latencia de búsqueda en la Q-Table cumple con los
microsegundos requeridos por el hardware?

##### Linaje del Mapa

¿Está la versión de la Q-Table vinculada a la versión específica
del layout del almacén (Map Versioning)?

> [**Algoritmo - Q-Learning**](../Algoritmos/Reinforcement_Learning-Q-Learning.md)
• 
> [**Practica - Q-Learning**](../Sample/Reinforcement_Learning-Q-Learning.md)
• 
> [**Codigo - Perceptrón Multicapa**](Deep_Learning-Perceptron-Multicapa.md)
---