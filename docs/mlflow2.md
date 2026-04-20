Masterclass: MLflow Industrial

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Fira+Code:wght@400;500&display=swap');
body {
font-family: 'Inter', sans-serif;
background-color: #f8fafc;
color: #0f172a;
line-height: 1.6;
}
.code-block {
font-family: 'Fira Code', monospace;
background-color: #0f172a;
color: #e2e8f0;
padding: 1.25rem;
border-radius: 0.75rem;
font-size: 0.85rem;
line-height: 1.6;
border-left: 4px solid #6366f1;
overflow-x: auto;
margin-bottom: 1.5rem;
}
.py-comment {
color: #64748b;
font-style: italic;
}
.py-keyword {
color: #f472b6;
}
.py-func {
color: #38bdf8;
}
.py-str {
color: #fbbf24;
}
.phase-card {
@apply bg-white p-6 rounded-2xl border border-slate-200 shadow-sm mb-6 transition-all;
}
.mlflow-badge {
@apply inline-block px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest mb-4 bg-indigo-600 text-white shadow-sm;
}
.alert-card {
@apply bg-rose-50 border-l-4 border-rose-500 p-5 rounded-r-xl mb-8;
}
.best-practice {
@apply bg-emerald-50 border-l-4 border-emerald-500 p-5 rounded-r-xl mb-8;
}
.health-indicator {
@apply flex justify-between items-center p-2 border-b border-slate-100 text-xs;
}

# MLflow Industrial

Plataforma de Gestión del
Ciclo de Vida de ML

### Definición Técnica

MLflow es una plataforma de código abierto diseñada para gestionar el flujo de trabajo de
Machine Learning de extremo a extremo. Su arquitectura modular permite el **seguimiento de
experimentos**, la **reproducibilidad del código** y el
**despliegue centralizado** de modelos.

#### El Valor del Negocio

"MLflow elimina el caos de los notebooks y transforma la
experimentación en activos de software auditables, inmutables y listos para producción."

## Los 4 Pilares Core

#### 1. MLflow Tracking

Registro de parámetros, métricas, código y artefactos de
cada corrida de entrenamiento.

#### 2. MLflow Projects

Formato estándar para empaquetar código de forma
reproducible (Conda/Docker).

#### 3. MLflow Models

Manejo de múltiples "flavors" (PyTorch, Sklearn) para
despliegue en cualquier plataforma.

#### 4. Model Registry

Tienda central para gestionar versiones de modelos y
transiciones de estado (Prod/Staging).

## Análisis Comparativo

#### Ventajas Industriales

- • **Agnóstico:** Funciona con cualquier librería o lenguaje.
- • **Trazabilidad:** Conecta el modelo final con el dato exacto de
  origen.
- • **Estandarización:** Define un lenguaje común entre Data Science y
  Ops.

#### Desafíos y Desventajas

- • **Infraestructura:** Requiere un servidor de tracking centralizado.
- • **Pickle Safety:** La serialización de modelos requiere cuidado con
  las versiones de Python.
- • **No es Orquestador:** No reemplaza a herramientas como Airflow o
  Prefect.

## MLflow en el Ciclo MLOps

Fase 1: Data Management

### Linaje y Versionado de Datos

MLflow no almacena datos, pero registra el \*\*Dataset Hash\*\* o
la versión de DVC utilizada para cada experimento.

mlflow.log\_param("data\_version", "v1.4.2")
mlflow.log\_param("data\_query\_hash",
"sha256\_xyz...")

Fase 2: Experimentation

### Tracking y Comparación de Hiperparámetros

El laboratorio digital. Se registran métricas en tiempo real
para seleccionar el mejor algoritmo.

with mlflow.start\_run():
mlflow.log\_metric("auc\_score", 0.92)
mlflow.log\_artifact("confusion\_matrix.png")

Fase 3: ML Pipeline Automation

### CI/CD & MLflow Projects

Automatización de la ejecución del entrenamiento. Un commit
en Git dispara un `mlflow run` en un clúster remoto.

Fase 4: Model Serving

### Despliegue Multi-Nube

Empaquetado de modelos como contenedores Docker o despliegue
directo en AWS/GCP/Azure.

# Despliegue en un comando
mlflow models serve -m "models:/Spam\_Filter/Production" -p 5000

Fase 5: Monitoring & Observability

### Monitoreo de Deriva (Drift)

MLflow permite almacenar predicciones en producción (como
artefactos) para analizar la degradación del modelo.

Fase 6: Governance & Security

### Gobernanza y Auditoría

El Model Registry controla quién aprueba el paso a producción
y guarda el historial de firmas electrónicas.

## Ingeniería de Selección de Modelos

#### ¿Cómo elegir el mejor algoritmo?

MLflow permite automatizar esta decisión mediante el registro de **Métricas
Primarias**. No elijas el modelo con mayor Accuracy; elije aquel que:

- • Tiene el menor delta entre Train y Test (Estabilidad).
- • Cumple con el SLA de latencia de inferencia registrado.
- • Presenta una curva de calibración de probabilidad honesta.

#### Model Health Check (MLflow UI)

Validation Gap
< 0.05

Inference Time
< 20ms

Residual Dist.Gaussian

Artifact
IntegritySHA Valid

## Antipatrones y Errores en MLflow

#### Logging Masivo

Registrar millones de métricas por segundo (ej. pérdida en cada
step de una red neuronal). **Impacto:** El servidor de tracking se bloquea y la UI
es inutilizable. Registra solo al final de cada época.

#### Pickle Incompatibility

No registrar la versión de las dependencias (`conda.yaml`).
**Impacto:** El modelo corre en tu PC pero falla en producción por discrepancia de
versiones de librerías.

## Checklist de Validación Industrial

##### Linaje del Dataset

¿Se ha registrado el URI o hash de los datos de
entrenamiento en los parámetros?

##### Model Flavor Adecuado

¿Se ha usado el flavor específico (ej.
`mlflow.pytorch`) para optimizar la inferencia?

##### Entorno Reproducible

¿El artefacto del modelo incluye un archivo
`requirements.txt` o `conda.yaml` completo?

##### Seguridad (Secrets)

¿Se ha verificado que no se registraron credenciales
de base de datos en los parámetros?

Industrial Standard v11.0 • MLflow & MLOps Framework • 2024