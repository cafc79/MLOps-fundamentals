# Árboles de Decisión • Sistema de Riesgo Crediticio

# Aprobación de Créditos Bancarios 

¿Debería el banco prestar dinero a este solicitante? Los Árboles de Decisión transforman los datos
financieros en una serie de preguntas lógicas que cualquier analista de crédito puede entender y
auditar.

**Guía de Negocio:** Haz clic en cada tarjeta para entender
cómo un flujo de datos financieros se convierte en una decisión crediticia automática.

1

### Objetivo del Negocio

Predecir si un solicitante pagará su deuda (Aprobado) o si entrará en
mora (Rechazado).

Aislamos el comportamiento de 10,000 clientes pasados. Etiquetamos como "Aprobado" a quienes
pagaron a tiempo y como "Rechazado" a quienes fallaron. El árbol aprenderá las reglas que
separan estos dos grupos.

Variable Target: Solvencia

Análisis Histórico

Minimización de Riesgo

2

### Datos del Perfil

Seleccionamos los atributos financieros clave que influyen en la
capacidad de pago.

Analizamos variables como: Ingresos Mensuales, Nivel de Deuda Actual, Puntaje de Crédito (Score)
y Estabilidad Laboral. Estas preguntas serán los "nodos" que bifurcan el árbol.

Nivel de Ingresos

Ratio Deuda/Ingreso

Antecedentes Legales

3

### La Pregunta Raíz

El algoritmo identifica cuál es el factor más determinante para
separar buenos de malos pagadores.

Tras analizar los datos, el árbol determina que el **Puntaje de Crédito** es el
filtro inicial más fuerte. Si el score es > 700, la probabilidad de pago es altísima desde el
primer segundo.

Ganancia de Información

Selección de Nodo Raíz

Máxima Diferenciación

4

### Caminos de Decisión

Se crean ramificaciones secuenciales basadas en umbrales numéricos
precisos.

Ejemplo de flujo: ¿Score > 650? -> Sí -> ¿Ingresos > $2000? -> Sí -> **Aprobado**.
Si el score es bajo pero tiene un aval, el árbol explora esa rama secundaria antes de decidir.

Reglas IF-THEN

Estructura Jerárquica

Transparencia Lógica

5

### Evaluación de Nodos

El modelo busca que al final de cada rama, casi todos los clientes
sean del mismo tipo.

Usamos el **Índice Gini**. Si una rama termina con 95% de pagadores y solo 5% de
morosos, se considera un nodo "Puro". Esto garantiza que la predicción final sea muy segura.

Índice Gini Bajo

Consistencia de Clientes

Validación de Grupos

6

### Resultado Ejecutable

El sistema entrega una etiqueta final basada en el camino recorrido
por el solicitante.

Llega un cliente nuevo. El árbol lo procesa en milisegundos a través de sus preguntas y termina
en una "Hoja". La decisión sale: **"Aprobar Crédito: 98% Confianza"**. El banco
puede automatizar el desembolso.

Clasificación Instantánea

Explicación para el cliente

Proceso sin Sesgos Humanos

7

### Eficiencia Bancaria

Medimos la reducción en el tiempo de respuesta y la baja en la tasa de
morosidad.

Al implementar este árbol, el banco redujo el tiempo de aprobación de 3 días a 10 segundos.
Además, al basarse en datos objetivos, la morosidad cayó un 12% al detectar patrones de riesgo
invisibles para humanos.

Reducción de Costo Operativo

Escalabilidad de Negocio

Auditoría Regulatoria Fácil

## La Ventaja de la Caja Blanca

A diferencia de las Redes Neuronales, los Árboles de Decisión son **Interpretables**.
Si el banco niega un crédito, puede decirle exactamente al cliente: "Se le negó porque su ratio de
deuda supera el 40%". Esto genera confianza y cumple con las leyes de transparencia financiera.

Transparencia
Auditoría
Rapidez

© 2024 Laboratorio de Ciencia de Datos • Caso Práctico: Credit Scoring con Árboles de Decisión
> [**Algoritmo - Árboles de Decisión**](../Algoritmos/Supervised_Learning-Arboles-Decision.md)
 • 
> [**Codigo - Árboles de Decisión**](../Code/Supervised_Learning-Arboles-Decision.md)
 • 
> [**Practica - K-Means Clustering**](Unsupervised_Learning-K-Means-Clustering.md)
---