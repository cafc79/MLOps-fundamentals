Masterclass: DVC en el Ciclo MLOps

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Fira+Code:wght@400;500&display=swap');
body { font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; line-height: 1.6; }
.code-block { font-family: 'Fira Code', monospace; background-color: #0f172a; color: #e2e8f0; padding: 1.25rem; border-radius: 0.75rem; font-size: 0.8rem; line-height: 1.6; border-left: 4px solid #06b6d4; overflow-x: auto; margin-bottom: 1.5rem; }
.bash-cmd { color: #4ade80; }
.bash-comment { color: #64748b; font-style: italic; }
.section-card { @apply bg-white p-8 rounded-3xl border border-slate-200 shadow-sm mb-12 transition-all hover:shadow-md; }
.pill { @apply px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-widest mb-4 inline-block bg-cyan-100 text-cyan-700; }
.health-badge { @apply px-2 py-0.5 rounded text-[10px] font-bold border flex items-center gap-1 bg-white; }
.step-indicator { @apply w-12 h-12 rounded-2xl bg-slate-900 text-white flex items-center justify-center font-bold text-lg mb-4 border-2 border-cyan-400 shadow-lg; }

# DVC Engineering

Data Version Control: El Git de los Grandes Datos

**DVC (Data Version Control)** es la herramienta de código abierto que permite versionar datasets, modelos y pipelines de ML con la misma simplicidad que Git gestiona el código. En MLOps, DVC es el motor que garantiza que cada modelo en producción esté vinculado de forma inmutable al dato exacto que lo originó.

### Conceptos de Versionalización

**Data Pointers (.dvc files):** Archivos pequeños de texto que Git rastrea. Contienen metadatos y un hash (md5) que apunta al dataset real almacenado en la nube.

**Remote Storage:** El lugar donde residen los datos pesados (S3, GCS, Azure, SSH). DVC actúa como el transportista entre el código y este almacén.

**Pipeline Tracking:** DVC no solo guarda datos; registra los comandos, dependencias y salidas (Dags) para automatizar el re-entrenamiento.

### Análisis de Valor

#### Ventajas

- • **Git Friendly:** No sobrecarga Git con archivos binarios pesados.
- • **Agnóstico al Almacenamiento:** Cambia de AWS a Google Cloud sin tocar el código.
- • **Reproducibilidad:** "Git checkout" cambia el código Y el dato simultáneamente.

#### Desventajas

- • **Overhead de Comandos:** Requiere ejecutar comandos de DVC además de los de Git.
- • **Gestión de Cache:** Los discos locales pueden llenarse rápido si no se limpia el caché.
- • **Curva de Aprendizaje:** Entender el flujo de punteros vs. datos reales.

## Pipeline de Gestión de Datos

01

Etapa 1: Ingesta Inmutable

### Inicialización y Rastreo

Preparamos el repositorio para manejar datos. El comando `dvc add` genera el puntero que Git rastreará, mientras que el dato real se ignora automáticamente.

# 1. Inicializar DVC en el proyecto Git
dvc init
# 2. Configurar almacenamiento remoto (ej. AWS S3)
dvc remote add -d storage s3://mi-bucket-mlops/data
# 3. Empezar a rastrear un dataset pesado
dvc add data/training\_dataset.csv
# 4. Git solo rastrea el puntero .dvc
git add data/training\_dataset.csv.dvc .gitignore
git commit -m "Track: Dataset v1.0 versionado con DVC"

02

Etapa 2: Linaje de Proceso

### Pipeline de Entrenamiento

Definimos un paso del pipeline. DVC rastrea las dependencias (scripts/datos) y las salidas (modelos). Si nada ha cambiado, DVC salta el paso para ahorrar cómputo.

# Definir un paso de entrenamiento automático
dvc run -n train \
-d src/train.py -d data/training\_dataset.csv \
-o models/model.pkl \
python src/train.py
# Si el dataset cambia, DVC sabe que debe volver a correr 'train'
dvc repro

### Zoom: Validación Cruzada en el Linaje DVC

En MLOps, la **Validación Cruzada (K-Fold)** no es solo una prueba algorítmica. DVC permite crear "Data Slices" versionados para que cada fold sea reproducible. Esto asegura que el **Health Check** del modelo no dependa de un split aleatorio, sino de una validación sistemática sobre datos inmutables.

#### Sinergia DVC + CV

DVC garantiza que cada fold de entrenamiento use exactamente la misma semilla y snapshot de datos, permitiendo auditar por qué el modelo falló en un "Slice" específico del dataset.

#### Evitar el "Drift Ciego"

Al versionar los datos con DVC, la Validación Cruzada permite detectar si la caída del performance en producción se debe a un cambio en el dato (Data Drift) comparando contra el fold histórico idéntico.

## Diagnóstico de Salud: DVC Phase

#### Punteros Válidos

Integridad 100%

¿Todos los archivos .dvc tienen su binario correspondiente en el remoto?

#### Lineage Graph

DAG Correcto

¿Podemos rastrear el modelo hasta la fuente de datos cruda sin interrupciones?

#### Storage Quota

Bajo Límite

¿Se está limpiando el caché antiguo para evitar costos de almacenamiento excesivos?

#### Errores de Producción (Red Flags)

- **Dangling Pointers:** Hacer "git commit" del archivo .dvc pero olvidar hacer "dvc push". El compañero verá el puntero pero no podrá descargar el dato.
- **Unchecked Remotes:** No validar la conexión al bucket de S3/GCS en el CI/CD, causando fallos en los pipelines de entrenamiento automático.
- **Hardcoded Paths in DVC:** Usar rutas absolutas (C:/Users/...) que rompen el pipeline cuando se ejecuta en el clúster de producción o contenedores.

## Consideraciones Profesionales

#### Seguridad en DVC

- • **PII Sanitization:** Asegúrate de que el dataset esté anonimizado ANTES de ejecutar `dvc add`. Los datos binarios en el remoto son inmutables.
- • **Access Control:** Implementa permisos de lectura/escritura (IAM) granulares en el bucket remoto. No todos los usuarios deben poder borrar versiones antiguas.
- • **Signed Links:** Usa URLs firmadas para el acceso temporal a datos en clústeres de inferencia externos.

#### Madurez en MLOps

- • **Semantic Versioning:** Etiqueta tus punteros .dvc con nombres claros (ej. `dataset_v1.4_churn_fixed`) para facilitar la búsqueda.
- • **DVC Metrics:** Usa `dvc metrics show` para comparar resultados de diferentes versiones de datos directamente en la terminal.
- • **Incremental Repro:** Aprovecha el caché de DVC para no re-procesar datos que no han cambiado, optimizando el tiempo de CI/CD.

## Checklist de Validación MLOps (DVC)

##### Sincronización Git-DVC

¿Se confirmó que por cada commit de Git con un archivo .dvc se realizó el correspondiente `dvc push`?

##### Integridad del Remoto

¿Se ha verificado la accesibilidad del almacenamiento remoto desde el entorno de producción (Staging/Prod)?

##### Validación de Pipeline (DAG)

¿Ejecutar `dvc status` muestra que todos los pasos del entrenamiento están actualizados?

##### Snapshot de Validación Cruzada

¿El resultado del Cross-Validation está registrado y vinculado al hash del dataset versión X?

##### Sanitización de Datos Sensibles

¿Se confirmó que el dataset versionado no contiene información personal identificable (PII) sin cifrar?

##### Métrica de Reproducibilidad

¿Otro ingeniero puede descargar el dato y obtener exactamente el mismo modelo ejecutando un solo comando?

Google Cloud AI Standards • MLOps Engineering • 2024