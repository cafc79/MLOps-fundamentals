# Caso Practico: Detección de Fraude Bancario

# Seguridad con Random Forest

¿Es esta compra legítima o un robo de identidad? Random Forest consulta a un "comité" de cientos de
árboles de decisión para validar transacciones en milisegundos, protegiendo millones de cuentas
simultáneamente.

**Guía de Negocio:** Haz clic en cada etapa para entender
cómo el "Bosque" analiza el riesgo financiero mediante la diversidad y la votación masiva.

1

### Objetivo Crítico

Identificar transacciones fraudulentas (1) entre millones de
operaciones legítimas (0).

El fraude es un evento raro (desbalanceado). Necesitamos un modelo extremadamente robusto que no
se confunda con comportamientos de compra inusuales pero honestos (ej. compras en vacaciones).

Variable Target: Fraude vs
Legítimo

Análisis de Desbalance

Seguridad Transaccional

2

### Atributos de Entrada

Recopilamos las características que definen el ADN de cada
transacción.

Analizamos: Monto de la compra, Ubicación geográfica, Hora del día, Frecuencia de uso y tipo de
comercio. Estas "features" serán el alimento para los cientos de árboles del bosque.

Geolocalización IP

Patrones de Gasto Histórico

Velocidad de Transacción

3

### El Comité de Árboles

Entrenamos 200 árboles de decisión independientes usando la técnica de
Bagging.

En lugar de un solo árbol gigante (que se equivocaría fácilmente), creamos un bosque. Cada árbol
se entrena con una muestra aleatoria diferente de los datos. Esto asegura que el bosque tenga
"perspectivas" distintas.

Muestreo aleatorio (Bootstrapping)

Diversidad de Conocimiento

Reducción de Varianza

4

### Feature Randomness

En cada división, el árbol solo puede elegir entre un subconjunto
aleatorio de variables.

Si el "Monto" fuera la variable más obvia, todos los árboles la usarían igual. Al forzar la
aleatoriedad, obligamos a algunos árboles a especializarse en "Ubicación" o "Hora", descubriendo
fraudes más sutiles que otros modelos ignorarían.

Descorrelación de Árboles

Especialización de Ramas

Resistencia al Ruido

5

### Votación Mayoritaria

Cuando llega una transacción, cada árbol emite su voto: ¿Fraude o
Legítimo?

Si 180 árboles dicen "Legítimo" y 20 dicen "Fraude", la transacción se aprueba. Si 150 dicen
"Fraude", se bloquea inmediatamente. Esta "sabiduría colectiva" es mucho más precisa que la
opinión de un solo modelo.

Consenso Democrático

Estabilidad en la Salida

Baja probabilidad de error único

6

### Feature Importance

El bosque nos revela qué variables son las más determinantes para
atrapar criminales.

Tras el entrenamiento, descubrimos que la "Ubicación IP inusual" y la "Velocidad de gasto" son
los delatores más fuertes del fraude. El banco puede usar este conocimiento para crear reglas de
seguridad adicionales.

Ranking de Variables

Inteligencia de Negocio

Optimización de Atributos

7

### Valor Operativo

Medimos la reducción de pérdidas millonarias y la mejora en la
confianza del cliente.

El sistema procesa 5,000 transacciones por segundo. Al reducir los "Falsos Positivos" (bloquear
a clientes buenos), el banco mejora la experiencia del usuario y evita pérdidas por fraude en un
30% anual.

Inferencia en milisegundos

Escalabilidad Masiva

Protección 24/7

## La Resiliencia del Bosque

Random Forest es el algoritmo predilecto para la seguridad porque es **Inmune al
Ruido**. Si un dato viene corrupto o falta una variable, los otros 199 árboles compensan
el error, garantizando que el banco nunca baje la guardia.

Robustez
Total
Precisión
Alta
Multi-Perspectiva

> [**Algoritmo - Random Forest**](../Algoritmos/Supervised_Learning-Random-Forest.md)
• 
> [**Codigo - Random Forest**](../Code/Supervised_Learning-Random-Forest.md)
• 
> [**Practica - Regresion Lineal**](Supervised_Learning-SVM.md)
---