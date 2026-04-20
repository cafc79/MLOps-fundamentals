# Ecosistema MLOps

## Operationalizing Machine Learning at Scale

### Definición

MLOps es la cultura y práctica de ingeniería que unifica el desarrollo de sistemas de ML (Dev)
con la operación de sistemas de ML (Ops). A diferencia del DevOps tradicional, MLOps debe
gestionar la \*\*trilogía crítica\*\*: Código, Datos y Modelos.

#### El Mantra MLOps

"Si no es reproducible, no es ciencia. Si no es
monitoreable, no es producción."

## Conceptos Pilares

Automatización (CT): Pipelines que se
auto-ejecutan ante cambios en datos o código.

Reproducibilidad: Capacidad de recrear exactamente
un modelo de hace meses (DVC + Git).

Escalabilidad: Capacidad de servir miles de
predicciones/segundo sin degradación.

## Análisis de Valor

#### Ventajas

- • Time-to-market reducido
- • Calidad de predicción constante
- • Auditoría y cumplimiento

#### Desventajas

- • Alta inversión inicial
- • Complejidad técnica
- • Necesidad de perfiles híbridos

## El Ciclo de Vida en 6 Fases

Fase 1: [**Data Management**](/docs/1.Gestion-Datos.md "Data Management")

### Gestión de Datos y Feature Stores

Tratamos los datos como código versionado. El objetivo es
eliminar el "Training-Serving Skew".

Ingesta inmutable y
versionada (DVC).

Catálogo central de
características (Feature Store).

Fase 2: [**Experimentation**](/docs/2.Desarrollo-modelo.md)

### Desarrollo del Modelo y Tracking

El laboratorio donde se prueban algoritmos. Todo experimento
debe dejar un rastro digital (Metadata).

Registro de
hiperparámetros (MLflow).

Validación de algoritmos
base (Baseline).

Fase 3: [**ML Pipeline Automation**](/docs/3.AutomatizacionCI-CD.md)

### CI/CD/CT (Integración y Entrega Continua)

Automatizamos el flujo: Código -> Pipeline -> Modelo ->
Evaluación -> Registro.

Unit testing para código
de ML.

Pipelines de entrenamiento
automático (Kubeflow).

Fase 4: [**Model Serving**](/docs/4.Despliegue.md)

### Despliegue e Inferencia

Puesta en producción mediante APIs, procesos Batch o
despliegues en el borde (Edge).

Contenerización inmutable
(Docker).

Estrategias Canary y A/B
Testing.

Fase 5: [**Monitoring & Observability**](/docs/5.Monitoreo.md)

### Monitoreo de Deriva y Salud

Vigilancia constante. Un modelo en producción es un ente que
se degrada naturalmente.

Detección de Data Drift
(Cambio en X).

Detección de Model Decay
(Pérdida de Precisión).

Fase 6: [**Governance & Security**](/docs/6.Gobernabilidad.md)

### Gobernanza, Ética y Auditoría

El pilar final: asegurar que el sistema sea explicable,
seguro y cumpla la ley.

Explicabilidad
(SHAP/LIME).

Control de acceso (RBAC) y
Seguridad de datos.

## [**Ingeniería de Decisión**](/docs/ArquitecturaModelos.md)

#### ¿Cómo elegir el mejor algoritmo?

En MLOps aplicamos la \*\*Navaja de Ockham\*\*: Si una Regresión Lineal obtiene resultados
similares a una Red Neuronal, elegimos la Regresión por su estabilidad, bajo costo y
facilidad de auditoría.

Regla de Oro: No despliegues complejidad
que no puedas explicar o monitorear económicamente.

#### Errores Comunes en Producción

- **Manual
  Overrides:** Ajustar pesos del modelo "a mano" rompiendo el pipeline.
- **Silent
  Failures:** El modelo responde 200 OK pero sus predicciones son basura.
- **Lack of
  Ownership:** Nadie es dueño del modelo una vez desplegado.

## [**Model Health Check**](8.ModelHealthCheck.md)

#### Salud Técnica

- • Latencia de Inferencia (P99)
- • Uso de GPU/Memoria estable
- • Disponibilidad del API (>99.9%)

#### Salud de Datos

- • Distribución de entrada (JS Divergence)
- • Ausencia de nulos inesperados
- • Estabilidad de las fuentes

#### Salud Funcional

- • F1-Score en tiempo real
- • Alineación con KPIs de Negocio
- • Tasa de Falsos Negativos

## Checklist de Validación MLOps

##### Linaje del Dato

¿Sabemos exactamente con qué versión de datos se
entrenó este modelo?

##### Validación Cross-Env

¿El modelo corre igual en mi máquina que en el
contenedor de producción?

##### Trigger de Retraining

¿Existe una alerta automática ante la caída del
performance?

##### Auditoría de Inferencia

¿Guardamos las predicciones y las entradas para
futuros análisis?

##### Safety Gate

¿El despliegue falla automáticamente si el Accuracy
baja de un umbral X?

##### Explicabilidad Activa

¿Podemos justificar por qué el modelo dio ese
resultado específico?

> [*Next*](../docs/ArquitecturaModelos.md "Arquitectura de Modelos")
---