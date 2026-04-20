Caso Práctico: RNN en Predicción Bursátil

Caso Real: Análisis de Series Temporales

# Predicción Financiera con RNN

¿Puede una máquina predecir el valor de una acción mañana basándose en los últimos 10 años? La Red
Neuronal Recurrente (RNN) es el único algoritmo que entiende que el precio de hoy depende directamente
del orden de los eventos de ayer.

**Guía de Negocio:** Haz clic en cada etapa para entender
cómo transformamos gráficos de velas en una ventaja competitiva mediante el aprendizaje secuencial.

1

### Ingesta Histórica

Recopilamos precios de cierre, volumen y apertura de los últimos 2,500
días de bolsa.

A diferencia de otros datos, aquí el orden es sagrado. No podemos barajar las filas. La RNN
necesita ver la "película" completa del mercado para entender si estamos en una tendencia
alcista o una corrección técnica.

Continuidad Temporal

Múltiples Atributos (OHLCV)

Limpieza de Gaps

2

### Muestreo Deslizable

Creamos bloques de datos (ej. 60 días) para predecir el valor del día
61.

Usamos una "ventana móvil". El algoritmo mira los días 1-60 para predecir el 61; luego mira del
2-61 para predecir el 62. Esto enseña a la red a reconocer patrones de corto y mediano plazo de
forma repetitiva.

Time-Steps configurables

Estructura de Memoria

Normalización de Precios

3

### La Memoria Viva

La red mantiene un "resumen" de lo ocurrido en los días previos dentro
de cada neurona.

Es el "Hidden State" ($h\_t$). Cuando la red procesa el precio del lunes, guarda una parte de esa
información para usarla cuando analice el precio del martes. Es como un inversor que recuerda la
noticia de ayer antes de comprar hoy.

Persistencia de Info

Contexto Secuencial

Actualización Recurrente

4

### Arquitectura LSTM

Implementamos celdas especiales que deciden qué noticias "olvidar" y
cuáles mantener.

Las RNN comunes olvidan rápido. Usamos **LSTM** (Long Short-Term Memory) para que
el modelo recuerde eventos importantes de hace meses (ej. un cambio de CEO) mientras ignora el
ruido diario insignificante.

Puerta de Olvido (Forget)

Memoria de Largo Plazo

Estabilidad del Gradiente

5

### Ajuste Temporal

La red se auto-corrige comparando su predicción con el precio real del
día siguiente.

Mediante Backpropagation Through Time (BPTT), la red ajusta los pesos de sus neuronas para
minimizar la diferencia entre el precio proyectado y el real. Aprende a no sobre-reaccionar a
picos de pánico temporales.

Error Cuadrático Medio

Optimización de Pesos

Validación Temporal

6

### Prueba de Estrategia

Simulamos inversiones en el pasado para ver cuánto dinero habría
ganado el modelo.

Probamos el modelo entrenado con datos de un año que "no conoce". Si la predicción de la RNN
coincide con el movimiento real del mercado en un 70%, el fondo de inversión valida el algoritmo
para producción.

Simulación Realista

Medición de Drawdown

Sharpe Ratio

7

### Inferencia en Vivo

El modelo genera alertas de Compra/Venta automáticas cada mañana antes
de abrir el mercado.

El sistema recibe los datos de cierre de hoy y en milisegundos proyecta la tendencia de mañana.
Los traders usan esta señal para tomar decisiones de alta velocidad con una base estadística
sólida.

Trading Algorítmico

Alertas Proactivas

Escalabilidad Global

## El Dominio del Tiempo

Las RNN son la herramienta definitiva para mercados volátiles porque **aprenden de la
historia** sin quedar atrapadas en ella. Al entender el contexto secuencial, permiten que
las empresas anticipen cambios de ciclo antes que la competencia.

Secuencial
Predictivo
Contextual

> [* Algoritmo - Redes Neuronales Recurrentes**](../algoritmos/Deep_Learning-RNN.md)
 • 
> [* Practica - Redes Neuronales Recurrentes**](../Sample/Deep_Learning-RNN.md)
---