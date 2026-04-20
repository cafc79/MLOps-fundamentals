# Caso Práctico: Regresión Logística  Retención Estratégica de Clientes

# Predicción de Abandono (Churn)

¿Cómo sabe una empresa de telecomunicaciones que vas a cancelar tu contrato antes de que lo hagas? La
Regresión Logística analiza tu comportamiento pasado para asignarte una probabilidad de riesgo.

**Guía de Negocio:** Haz clic en cada etapa para entender
cómo transformamos datos de uso en una estrategia de retención automática.

1

### Definición de Salida

El objetivo es binario: El cliente se queda (0) o el cliente se va
(1).

Aislamos una ventana de tiempo (ej. los últimos 6 meses). Si un cliente no renovó o canceló, se
marca como "1". Esta etiqueta es la que el algoritmo aprenderá a predecir basándose en patrones
históricos.

Variable Target Binaria

Limpieza de historial

Etiquetado de datos

2

### Variables de Entrada

Elegimos los comportamientos que indican insatisfacción o cambio de
hábito.

Analizamos factores como: ¿Cuánto paga al mes? ¿Cuántas veces llamó a soporte? ¿Qué tipo de
contrato tiene? Estas "señales" alimentan la ecuación matemática para determinar el riesgo.

Antigüedad del cliente

Cargos Mensuales

Tickets de soporte abiertos

3

### Función Sigmoide

Convertimos los datos de uso en una puntuación entre 0% y 100%.

Aquí ocurre la "magia". El modelo suma los pesos de tus comportamientos. Si tienes un contrato
mes a mes y muchos tickets de quejas, la función sigmoide empujará tu puntuación hacia el
extremo del 1 (Abandono).

Puntuación de Riesgo

Compresión de datos

Significado estadístico

4

### Frontera de Decisión

¿A partir de qué porcentaje consideramos que un cliente está "en
peligro"?

Normalmente es 0.5 (50%), pero el negocio puede decidir que si un cliente tiene un 70% de
probabilidad de irse, se le marque como "Crítico". Este umbral permite equilibrar el presupuesto
de marketing.

Sensibilidad de alarma

Optimización de costos

Clasificación Final

5

### Métricas de Valor

¿Cuántos clientes en riesgo logramos identificar correctamente
(Recall)?

Usamos la Matriz de Confusión. No nos importa solo la precisión total, sino evitar los "Falsos
Negativos": clientes que el modelo dijo que se quedarían, pero terminaron cancelando.

Capacidad de Detección

Evitar pérdidas reales

Validación de negocio

6

### Estrategia de Acción

El modelo no solo predice, sino que dispara procesos automáticos de
fidelización.

Si un cliente entra en el "Riesgo Crítico", el sistema le envía automáticamente un cupón de
descuento o una oferta de actualización de plan para asegurar su permanencia un año más.

Ofertas personalizadas

Alertas a soporte

Retención Proactiva

7

### Ahorro Estimado

Calculamos el Retorno de Inversión (ROI) del modelo implementado.

Al final del trimestre, comparamos cuántos clientes marcados como "riesgo" salvamos vs. el costo
de las campañas de retención. Un modelo bien ajustado puede reducir el abandono hasta en un 15%.

ROI de Datos

Mejora de CLV

Estabilidad Financiera

## Impacto en la Empresa

Mantener un cliente actual es **5 veces más económico** que adquirir uno nuevo. La
Regresión Logística transforma una empresa reactiva en una organización predictiva que cuida su
activo más valioso: la lealtad.

Prevención
Eficiencia
Fidelización

> [**Algoritmo - Regresion Logistica**](../Algoritmos/Supervised_Learning-Regresion-Logistica.md)
• 
> [**Codigo - Regresion Logistica**](../Code/Supervised_Learning-Regresion-Logistica.md)
• 
> [**Practica - Random Forest**](Supervised_Learning-Random-Forest.md)
---