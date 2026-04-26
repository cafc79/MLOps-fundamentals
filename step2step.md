# 🔍FASE 1: Del Caos al Problema (Problem Framing)  
### Objetivo:   
Que Melissa y Airis entiendan que no empezamos con código, sino con una necesidad de negocio mal definida.  

🎯 Preguntas para plantear:  
🗣️ "Imagina que el equipo de soporte recibe 10,000 correos diarios. 
    ¿Qué dolor concreto estamos intentando aliviar?"  

🗣️ "¿Qué pasaría si nuestro filtro bloquea un correo importante de un cliente? 
    ¿Es ese error igual de grave que dejar pasar un spam? ¿Por qué?"  

🗣️ "¿Cómo sabremos dentro de 3 meses si nuestro filtro funciona bien? 
    ¿Qué número mirarías en un dashboard?"  

"No es 'arreglar el correo', es 'reducir el tiempo que se pierde revisando spam'" y esto es el Problem Statement, Definir claramente qué queremos resolver y para quién

💡 Lo que buscas que ellas descubran:  
•	La diferencia entre problema de negocio ("reducir ruido") y problema de ML ("clasificación binaria").  
o	"Cada correo → 'spam' o 'ham' (legítimo)", "Como separar ropa: limpia/sucia, colores/blancos" y esto es Classification Problem, Tipo de problema donde asignamos una categoría a cada entrada  
•	Que los falsos positivos tienen costo de negocio.  
o	"FP = correo de cliente va a spam (grave). FN = spam llega a inbox (molesto)"
o	False Positive / False Negative Errores de clasificación: bloquear algo bueno o dejar pasar algo malo  
•	La necesidad de definir métricas de éxito antes de tocar datos.  
o	El impacto económico o operacional de cada tipo de error, Cost of Error

"Reducción del 80% en correos spam en inbox, con <1% de falsos positivos" y esto es el Success Metrics (Business), Cómo mediremos el éxito en términos de negocio

El Split de Datos: El spam es un evento raro (digamos que solo el 10% de los correos son spam). Cuando uses Python para dividir tus datos en Entrenamiento (Train) y Prueba (Test), ¿qué parámetro o técnica específica debes usar obligatoriamente para no arruinar el aprendizaje del modelo?

Inmutabilidad: Sabiendo que los analistas van a seguir añadiendo nuevos correos a este archivo la próxima semana, ¿qué herramienta de terminal vas a inicializar primero en tu proyecto para asegurar que el modelo que entrenemos hoy esté vinculado a esta versión exacta de los datos?
________________________________________
## Code
> > 
```
spam_filter_mlops/  
├── data/  
│   ├── raw/          # 📥 Datos crudos (nunca se modifican)  
│   └── processed/    # 🧼 Splits y features listas para modelar  
├── artifacts/        # 📦 Pipelines y modelos serializados  
├── src/  
│   ├── fase_01_setup.py  
│   ├── fase_02_eda_split.py  
│   └── fase_03_pipeline.py
├── requirements.txt  
└── README.md  
```

> 
```bash
pip install pandas
```

En MLOps, los datos no se procesan con listas de Python ni csv nativo. pandas introduce el concepto de DataFrame: una estructura tabular optimizada, con indexación alineada, operaciones vectorizadas y manejo nativo de tipos. Además, pd.read_csv() maneja codificaciones, saltos de línea y esquemas inconsistentes sin romper el script. Es la base para cualquier pipeline de datos porque garantiza que la ingesta sea determinista y reproducible, no dependiente de scripts frágiles.

> 
```python
# Creamos src/fase_01_setup.py
import pandas as pd
import os

# 1. Estructura de directorios inmutable
RAW_DIR = "data/raw"
os.makedirs(RAW_DIR, exist_ok=True)
DATA_PATH = os.path.join(RAW_DIR, "spam.csv")

# 2. Ingesta idempotente (solo descarga si no existe)
URL = " https://github.com/cafc79/MLOps-fundamentals/blob/main/data/spam.csv"

if not os.path.exists(DATA_PATH):
    print("📥 Descargando dataset...")
    df = pd.read_csv(URL, sep='\t', header=None, names=['label', 'message'])
    df.to_csv(DATA_PATH, index=False)
else:
    df = pd.read_csv(DATA_PATH)

# 3. Estandarización temprana de etiqueta
df['target'] = df['label'].map({'ham': 0, 'spam': 1})

print(f"✅ Cargado: {df.shape[0]} filas, {df.shape[1]} cols")
print(df.head(3))
```

Los datos crudos son la fuente de verdad inmutable. Si los editamos manualmente o los mezclamos con transformaciones, perdemos la capacidad de auditar qué entró originalmente al sistema. En MLOps, raw es de solo lectura; cualquier modificación vive en processed/. Esto permite reproducir cualquier experimento pasado y detectar si un cambio en métricas vino de los datos o del código.
________________________________________

***"Si el script falla a mitad de descarga, ¿qué garantía tenemos de que el archivo no quedó corrupto para futuros runs?"***  
🔍 La descarga no es atómica. Un corte de red deja un CSV parcial que pd.read_csv() podría leer silenciosamente o fallar de forma impredecible. En producción, se usan estrategias como descargar a .tmp y luego os.replace(), o verificar checksums (SHA-256). Este primer script enseña el principio: la ingestión debe ser segura o  el pipeline no es confiable.  

***"¿Cómo traducimos 'reducir spam sin bloquear correos de clientes' a algo que este script prepare para el futuro?"***  
🔍 Traducirlo implica mapear objetivos de negocio a variables técnicas. Aquí, target = 1 para spam nos permite entrenar un clasificador binario. Pero más importante: al estandarizar la etiqueta ahora, evitamos inconsistencias futuras ('Spam', 'spam', 1, True). MLOps exige normalización temprana de esquemas; si el esquema cambia después, el modelo falla en producción sin warning claro.  


# 📊 FASE 2: Selección y Exploración de Datos
### Objetivo:  
Entender que los datos no "aparecen", se seleccionan con criterio.

🎯 Preguntas para plantear:  
🗣️ "Tenemos acceso a: asunto, cuerpo, remitente, hora, adjuntos, headers completos. 
    ¿Todos son igualmente útiles? ¿Cuáles podrían ser 'ruido'?"  
•	Cada variable o característica que usamos para predecir. Feature

🗣️ "Si un spammer cambia 'Viagra' por 'V!agra', ¿nuestro modelo lo detectaría 
    si solo buscamos palabras exactas? ¿Qué nos dice eso sobre cómo representar el texto?"

🗣️ "¿Qué pasa si el 95% de nuestros correos son 'ham' (legítimos) y solo 5% spam? 
    ¿Podemos confiar en una métrica que solo mire 'porcentaje de aciertos'?"
•	"95% ham, 5% spam → el modelo podría 'aprender' a siempre decir 'ham'". Cuando una categoría tiene muchos más ejemplos que otra o Class Imbalance

🗣️ "¿Deberíamos incluir la dirección de email completa como feature? 
    ¿Qué riesgo hay si el modelo 'memoriza' dominios específicos del dataset de entrenamiento?"
•	"No es lo mismo tener harina que tener una masa lista para hornear",  Feature Engineering Transformar datos crudos en features útiles para el modelo

💡 Lo que buscas que ellas descubran:  
•	La importancia del feature engineering (no todo texto es igual).  
•	El problema del desequilibrio de clases.  
•	El riesgo de data leakage y sobreajuste.  
Data Leakage (Fuga de Datos): Vamos a tener que limpiar el texto (quitar signos de puntuación, pasar a minúsculas). ¿Vas a limpiar todo el dataset antes o después de hacer la división de Train/Test? Entonces, "Si incluimos 'fue marcado como spam por el usuario' como feature, el modelo 'hace trampa'" entonces Data Leakage, Cuando información del futuro o de test 'se filtra' al entrenamiento  
Investigar los datos antes de modelar: distribuciones, valores nulos, correlaciones, Exploratory Data Analysis (EDA)
________________________________________

## Code

> 
```bash
pip install scikit-learn
```

scikit-learn es el estándar industrial para utilidades de ML en Python. No la usamos aquí para modelar aún, sino por train_test_split, que implementa particiones estratificadas, reproducibles y libres de sesgo. Además, su API es consistente con la fase siguiente (pipelines, métricas, validación). En MLOps, usar una librería probada para splits evita errores silenciosos como fugas de datos o desbalances no intencionales.

> 
```python
# Creamos src/fase_02_eda_split.py
import pandas as pd
from sklearn.model_selection import train_test_split
import os

os.makedirs("data/processed", exist_ok=True)

# 1. Cargar crudos (nunca modificar raw)
df = pd.read_csv("data/raw/spam.csv")
df['target'] = df['label'].map({'ham': 0, 'spam': 1})

# 2. Feature engineering determinista
df['msg_length'] = df['message'].str.len()
df['num_exclamations'] = df['message'].str.count('!')

# 3. Split ANTES de cualquier transformación estadística
X = df[['message', 'msg_length', 'num_exclamations']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Persistir splits para reproducibilidad
X_train.to_csv("data/processed/X_train.csv", index=False)
X_test.to_csv("data/processed/X_test.csv", index=False)
y_train.to_csv("data/processed/y_train.csv", index=False)
y_test.to_csv("data/processed/y_test.csv", index=False)

print("✅ Splits guardados. Zero leakage garantizado.")
```
________________________________________

***"P1: ¿Por qué hacemos el train_test_split antes de crear TfidfVectorizer o escalar valores?"***  
🔍 Razonamiento esperado: Si vectorizamos o escalamos todo el dataset primero, el vectorizador "ve" la distribución completa de palabras, y el escalador calcula medias/desviaciones con datos de prueba incluidos. El modelo entonces recibe información indirecta de la prueba durante el entrenamiento: data leakage. En MLOps, la regla es sagrada: split → fit en train → transform en train y test. El split define el universo de conocimiento permitido.

***P2: "¿Qué hace stratify=y y por qué es crítico en un dataset de spam?"***  
🔍 Razonamiento esperado: El spam suele ser minoría (~10-20%). Sin stratify, el split aleatorio podría poner 0% o 2% de spam en test, haciendo que accuracy sea engañosa o que el modelo nunca vea ejemplos positivos. stratify=y fuerza que la proporción de clases se mantenga idéntica en train y test. MLOps exige representatividad estadística; si el test no refleja la realidad, las métricas son ilusorias.

***P3: "Si mañana se envía un correo nuevo, ¿cómo garantizamos que msg_length y num_exclamations se calculen exactamente igual que en entrenamiento?"***  
🔍 La lógica de feature engineering debe estar centralizada y versionada, no replicada en notebooks o scripts sueltos. Si hoy usamos .str.len() y mañana alguien cambia a .str.split().len(), el modelo en producción recibirá features distintas y fallará silenciosamente. En MLOps, las transformaciones se encapsulan en el mismo pipeline que se entrena (ver Fase 3), eliminando training-serving skew.

 
# 🧹 FASE 3: Limpieza y Preparación (Data Readiness)
### Objetivo: 
Que surja naturalmente la necesidad de un pipeline de preprocessing.

🎯 Preguntas para plantear:
🗣️ "Nuestro dataset tiene correos en HTML, otros en texto plano, algunos con emojis, 
    otros con codificación rara. ¿Qué le pasará al modelo si le damos esto 'crudo'?"  
•	"Eliminar correos duplicados, decodificar HTML, manejar caracteres raros", Data Cleaning Corregir o eliminar datos inconsistentes, incompletos o erróneos

🗣️ "Si hoy limpiamos los datos 'a mano' en un notebook, ¿qué pasa cuando lleguen 
    100 correos nuevos mañana? ¿Tenemos que repetir el proceso manualmente?"  
•	"Lowercasing → remover stopwords → stemming → vectorización"; Preprocessing Pipeline Secuencia automatizada y reproducible de transformaciones

🗣️ "¿Cómo garantizamos que la limpieza que aplicamos en entrenamiento 
    sea idéntica a la que aplicaremos en producción?"
•	"Si en entrenamiento usamos correos de 2020 y en producción llegan de 2026, el modelo puede fallar" Training-Serving Skew Cuando los datos en entrenamiento son distintos a los de producción

🗣️ "Si dos personas en el equipo limpian los datos de forma ligeramente distinta, 
    ¿cómo reproducimos los resultados?"  
•	"¿Qué hacemos si un correo no tiene asunto? ¿Lo eliminamos? ¿Usamos 'sin_asunto' como feature?" Missing Values Handling Estrategia para tratar datos faltantes: eliminar, imputar, marcar

💡 Lo que buscas que ellas descubran:  
•	La necesidad de pipelines reproducibles de preprocessing.  
•	Que la limpieza no es un paso "one-off", es parte del sistema.  
•	El concepto de training-serving skew.

*"Poner toda la ropa del mismo color antes de lavar" Text Normalization Estandarizar texto: minúsculas, eliminar puntuación, lematización*
________________________________________

## Code

> 
```bash
pip install joblib
```

pickle es la herramienta nativa de Python para serializar objetos, pero es lenta y maneja mal matrices grandes de numpy. joblib está optimizada específicamente para objetos numéricos y scikit-learn: comprime arrays, serializa en paralelo y produce archivos más ligeros. En MLOps, el artefacto que se despliega es el modelo serializado; usar joblib garantiza carga rápida en producción, menor consumo de memoria y compatibilidad garantizada con sklearn.

> 
```python
# Creamos src/fase_03_pipeline.py
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# 1. Cargar splits versionados
X_train = pd.read_csv("data/processed/X_train.csv")
y_train = pd.read_csv("data/processed/y_train.csv").squeeze()

# 2. Pipeline MLOps: preprocessing + modelo en un solo objeto
spam_pipeline = Pipeline([
    ('preprocessor', ColumnTransformer([
        ('text', TfidfVectorizer(stop_words='english', max_features=2000, ngram_range=(1,2)), 'message'),
        ('numeric', StandardScaler(), ['msg_length', 'num_exclamations'])
    ])),
    ('classifier', LogisticRegression(random_state=42, max_iter=1000))
])

# 3. Entrenamiento (solo una vez por versión)
print("🔄 Entrenando pipeline...")
spam_pipeline.fit(X_train, y_train)

# 4. Serialización del artefacto completo
import os
os.makedirs("artifacts", exist_ok=True)
joblib.dump(spam_pipeline, "artifacts/pipeline_v1.joblib")

# 5. Validación rápida sin leakage
X_test = pd.read_csv("data/processed/X_test.csv")
y_test = pd.read_csv("data/processed/y_test.csv").squeeze()
acc = spam_pipeline.score(X_test, y_test)
print(f"✅ Pipeline guardado. Accuracy en test: {acc:.3f}")
```
________________________________________

***P1: "¿Por qué metemos TfidfVectorizer y StandardScaler dentro de Pipeline en lugar de aplicarlos manualmente antes de fit()?"***  
🔍 Si aplicas transformaciones manualmente, debes recordar ejecutarlas en el mismo orden y con los mismos parámetros en producción. Un Pipeline encapsula el flujo completo como un solo objeto serializable. En fit(), aprende vocabulario y escalado solo de train. En predict(), aplica las mismas transformaciones automáticamente. Esto elimina errores humanos y garantiza Training == Serving.

***P2: "¿Qué pasa si en producción llega un mensaje con caracteres no UTF-8 o sin texto? ¿El pipeline se rompe?"***  
🔍 TfidfVectorizer tiene parámetros como de## Code_error='ignore' o lowercase=True. Si no se configuran, puede lanzar Uni## CodeDe## CodeError. MLOps exige robustez a datos sucios en producción. Además, ColumnTransformer maneja columnausentes si se configura con remainder='drop' o passthrough. La lección conceptual: un modelo no vive en un notebook limpio; vive en un entorno hostil. El pipeline debe anticipar fallas, no asumirlas.

***P3: "Guardamos pipeline_v1.joblib. ¿Qué más debemos registrar junto a este archivo para que sea verdaderamente reproducible en 6 meses?"***  
🔍 El .joblib solo contiene pesos y lógica interna. Para reproducibilidad MLOps necesitamos:  
•	Versión exacta de requirements.txt (pandas, sklearn, joblib)  
•	Hash de los datos usados (X_train.csv, y_train.csv)  
•	Parámetros de configuración (max_features=2000, C=1.0, random_state=42)  
•	Métricas de validación y métricas de negocio aceptadas Sin este contexto, el artefacto es una caja negra. Esto nos lleva directamente a la necesidad de MLflow Tracking y DVC (Fase 4), donde vinculamos código + datos + modelo + métricas en un único run auditable.
  

# 🔄 FASE 4: Versionado de Datos y Código
### Objetivo: 
Que entienda por qué git solo no basta en ML.

🎯 Preguntas para plantear:  
🗣️ "Imagina que el modelo v1.0 funcionaba perfecto. Hoy actualizamos el dataset 
    con correos de esta semana y el rendimiento cae. ¿Cómo sabemos si fue por:
a)	Los nuevos datos, b) Un cambio en el código, o c) Ambos?"  
•	"Poder recrear el modelo v1.3 exactamente: mismo código + mismos datos + mismos parámetros". Reproducibility Capacidad de obtener los mismos resultados partiendo de los mismos insumos  
•	"Este modelo se entrenó con dataset v2.1 → procesado con pipeline v3 → features X,Y,Z" Lineage Trazabilidad: saber de dónde vino cada dato y qué transformaciones sufrió  

🗣️ "Si Airis, Melissa y tú trabajan en paralelo, ella con el dataset de enero y tú con el de marzo, 
    ¿cómo comparan sus modelos de forma justa?"  
•	"Guardar cada cambio en el script de preprocessing o en la selección de features" "v1.0: dataset 2024-Q1; v1.1: + correos de Q2; v2.0: + features de headers" Data Versioning (DVC, LakeFS) Control de versiones para datasets 

🗣️ "¿Qué metadata necesitaríamos guardar de un dataset para poder 'volver al pasado' 
    y entender por qué un modelo se comportaba de cierta forma?"

🗣️ "¿Es lo mismo versionar 10 líneas de código que versionar 10 GB de correos procesados? 
    ¿Qué herramientas conoces que manejen esta diferencia?"

💡 Lo que buscas que ellas descubran:
•	La necesidad de DVC, Pachyderm o similar para datos.
•	Que la trazabilidad requiere vincular: código + datos + hiperparámetros + métricas.
________________________________________

## Code

> 
```bash
pip install dvc
```

Anteriormente, generamos data/raw/spam.csv, splits y artifacts/pipeline_v1.pkl. Git no está diseñado para archivos binarios o datasets >100MB: cada commit duplica el archivo, el repositorio se infla y el historial se vuelve inmanejable. dvc (Data Version Control) resuelve esto guardando los archivos pesados en almacenamiento externo (local, GCS, S3) y dejando en Git solo un puntero ligero (.dvc) con el hash SHA-256. Así versionamos datos sin romper Git.

> 
```bash
pip install mlflow
```

Tenemos un pipeline que entrena, pero si mañana cambiamos max_features, C o el algoritmo, ¿cómo comparamos qué versión fue mejor? ¿Dónde quedan los parámetros, las métricas y el artefacto de cada ejecución? mlflow es un sistema de experiment tracking: registra automáticamente parámetros, métricas, código y modelos en un servidor local o remoto. Responde a la pregunta: "¿Con qué configuración exacta se obtuvo este F1=0.92?" sin depender de notas en un notebook o nombres de archivos como model_final_v3_real.pkl.

> 
```bash
# CMD 
# 1. Inicializa DVC (crea .dvc/ y .dvcignore)
dvc init

# 2. Versiona el dataset crudo y los splits
dvc add data/raw/spam.csv
dvc add data/processed/X_train.csv data/processed/X_test.csv data/processed/y_train.csv data/processed/y_test.csv

# 3. Git solo rastrea los punteros (.dvc), no los datos
git add data/raw/spam.csv.dvc data/processed/*.dvc data/.gitignore
git commit -m "feat: versionar datos y splits con DVC"
```

Ahora, git log muestra cambios en código. dvc log (o el archivo .dvc) muestra cambios en datos. Si alguien clona el repo, corre dvc pull y recupera la versión exacta de los datos usada para ese commit. Reproducibilidad garantizada.

> 
```python
# Creamos src/fase_04_mlflow_tracking.py
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 1. Cargar datos versionados
X_train = pd.read_csv("data/processed/X_train.csv")
y_train = pd.read_csv("data/processed/y_train.csv").squeeze()
X_test  = pd.read_csv("data/processed/X_test.csv")
y_test  = pd.read_csv("data/processed/y_test.csv").squeeze()

# 2. Definir pipeline (misma estructura que Fase 3)
pipeline = Pipeline([
    ("preprocessor", ColumnTransformer([
        ("text", TfidfVectorizer(stop_words="english", max_features=2000, ngram_range=(1,2)), "message"),
        ("numeric", StandardScaler(), ["msg_length", "num_exclamations"])
    ])),
    ("classifier", LogisticRegression(random_state=42, max_iter=1000, C=1.0))
])

# 3. Configurar experimento en MLflow
mlflow.set_experiment("spam_filter_mlops")

# 4. Ejecutar run con tracking automático
with mlflow.start_run():
    # Entrenamiento
    pipeline.fit(X_train, y_train)
    
    # Evaluación
    y_pred = pipeline.predict(X_test)
    acc  = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec  = recall_score(y_test, y_pred)
    f1   = f1_score(y_test, y_pred)
    
    # 📝 Loguear parámetros del experimento
    mlflow.log_param("tfidf_max_features", 2000)
    mlflow.log_param("tfidf_ngram_range", "1-2")
    mlflow.log_param("logreg_C", 1.0)
    mlflow.log_param("logreg_max_iter", 1000)
    
    # 📊 Loguear métricas de negocio y técnicas
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("precision", prec)
    mlflow.log_metric("recall", rec)
    mlflow.log_metric("f1_score", f1)
    
    # 📦 Loguear el pipeline completo como artefacto versionado
    mlflow.sklearn.log_model(pipeline, "spam_pipeline")
    
    print(f"✅ Run {mlflow.active_run().info.run_id} completado.")
    print(f"   Accuracy: {acc:.3f} | Precision: {prec:.3f} | Recall: {rec:.3f} | F1: {f1:.3f}")
```    

Al ejecutar este script, MLflow crea una carpeta mlruns/ con:
•	run_id único
•	params/, metrics/, artifacts/
•	Interfaz web en **http://localhost:5000** para comparar runs, descargar modelos y ver gráficas.

Sin MLflow, tendrías el código en Git y los datos en DVC, pero ningún vínculo auditable que diga: "El modelo con F1=0.92 se entrenó con la versión abc123 del dataset, usando C=1.0 y max_features=2000, ejecutado el 12/05/2024". MLflow cierra el círculo de trazabilidad MLOps.

________________________________________

***"Cambiamos C=1.0 a C=0.1 y volvemos a correr el script. ¿Cómo sabemos si el nuevo modelo es realmente mejor o solo tuvo suerte con el split de test?"***
🧠 Razonamiento de la respuesta:  
MLflow nos da comparación estructurada, pero para responder "suerte vs mejora real" debemos integrar validación robusta (que veremos en la siguiente fase). Con MLflow solo:  
1.	Vemos dos run_id en el dashboard.
2.	Comparamos métricas lado a lado.
3.	Si F1 sube de 0.91 a 0.93, MLflow nos dice que mejoró en este split.
4.	Para descartar "suerte", necesitamos:
o	cross_val_score o múltiples seeds
o	Tests de significancia estadística (que MLflow no hace por defecto, pero podemos loguear la varianza)
o	Registro de std_dev de métricas en validación cruzada
MLflow no valida la robustez, pero la hace rastreable. La decisión de promover un modelo a producción debe basarse en métricas estables, no en un único run.

***"¿Por qué logueamos precision y recall por separado si f1_score ya los combina? ¿Qué decisión de negocio podríamos tomar equivocada si solo guardáramos f1?"***  
🧠 Razonamiento de la respuesta:  
F1 es un promedio armónico útil, pero oculta el trade-off. En un filtro de spam:
•	Alta precision (0.98) + baja recall (0.60) → El modelo bloquea muy poco spam, pero casi nunca se equivoca con correos legítimos. Costo: Melissa sigue perdiendo tiempo revisando spam.  
•	Baja precision (0.70) + alta recall (0.95) → Atrapa casi todo el spam, pero bloquea muchos correos válidos. Costo: Airis pierde ventas o comunicaciones críticas.  
Si solo logueamos F1, podríamos elegir un modelo con F1=0.85 que en realidad tiene precision=0.65 (inaceptable para negocio). Al registrar precision y recall por separado en MLflow:
1.	Podemos ajustar el umbral de decisión post-entrenamiento sin reentrenar.
2.	Podemos alinear la métrica con el costo real de error (FP vs FN).
3.	Podemos auditar: "¿Por qué promovimos este modelo? Porque priorizamos precision sobre recall según SLA del equipo de soporte."
F1 resume; precision y recall explican. MLOps exige transparencia en la decisión, no solo un número bonito.

*"Si mañana me piden revertir al modelo de ayer, ¿qué haría paso a paso?"*  
 

# 🤖 FASE 5: Selección de Algoritmo (No es magia, es criterio)
### Objetivo:
Que entienda que elegir algoritmo es un ejercicio de restricciones, no de popularidad.

🎯 Preguntas para plantear:  
🗣️ "Tenemos 50,000 correos con 10,000 features (palabras). 
    ¿Qué algoritmos podrían sufrir con esta dimensionalidad? ¿Cuáles la manejan bien?"

🗣️ "Si necesitamos que el equipo legal explique por qué un correo fue marcado como spam, 
    ¿nos conviene un modelo 'caja negra' como una red neuronal profunda, 
    o algo más interpretable como un árbol de decisión?"
•	"Si el equipo legal pregunta '¿por qué este correo fue bloqueado?', ¿podemos explicarlo?" Interpretability  Qué tan fácil es entender por qué el modelo tomó una decisión. 

🗣️ "¿Qué pasa si nuestro dataset crece a 10 millones de correos? 
    ¿El algoritmo que elegimos hoy escala linealmente, cuadráticamente, o qué?" 
•	"¿El algoritmo puede procesar 10K correos/hora sin volverse lento o caro?" Scalability Cómo se comporta el modelo cuando crecen los datos o las peticiones

🗣️ "¿Necesitamos que el modelo aprenda nuevas formas de spam sin reentrenar desde cero? 
    ¿Eso descarta algún tipo de algoritmo?"

💡 Lo que buscas que ellas descubran:  
•	El trade-off entre interpretabilidad vs. rendimiento.  
•	La importancia de la complejidad computacional.  
•	Que no existe "el mejor algoritmo", existe "el más adecuado para estas restricciones".

Primer modelo simple que sirve como punto de comparación Baseline Model
Qué tan 'sofisticado' es un modelo: desde reglas simples hasta redes profundas Model Complexity
"Un modelo muy simple no detecta spam nuevo; uno muy complejo 'memoriza' spam viejo" Bias-Variance Tradeoff Equilibrio entre simplificar demasiado (subajuste) o memorizar (sobreajuste)
________________________________________
## Code

Aquí cerramos el ciclo de "entrenar" y entramos al ciclo de "aprobar para producción". Sin gates, no hay MLOps; solo experimentos en notebooks.

> 
```bash
pip install pytest
```

un test verifica que una función devuelva el resultado esperado. En ML, el modelo siempre tendrá error; lo que nos importa es que ese error esté dentro de límites aceptables para el negocio. pytest es el estándar industrial porque permite:  
•	Parametrizar casos de prueba (ej: distintos tipos de correos)  
•	Integrarse nativamente en pipelines CI/CD (pytest tests/) Sin tests automáticos, no hay Integración Continua. Sin CI, no hay forma de garantizar que un nuevo commit o un nuevo dataset no rompa el modelo en producción.

> 
```python
# Validación Cruzada + Logging de Estabilidad (src/fase_05_cv_validation.py)
import pandas as pd
import mlflow
from sklearn.model_selection import cross_validate
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# 1. Reconstruir pipeline idéntico al entrenado en Fase 3
pipeline = Pipeline([
    ("preprocessor", ColumnTransformer([
        ("text", TfidfVectorizer(stop_words="english", max_features=2000, ngram_range=(1,2)), "message"),
        ("numeric", StandardScaler(), ["msg_length", "num_exclamations"])
    ])),
    ("classifier", LogisticRegression(random_state=42, max_iter=1000, C=1.0))
])

# 2. Cargar datos de entrenamiento
X = pd.read_csv("data/processed/X_train.csv")
y = pd.read_csv("data/processed/y_train.csv").squeeze()

# 3. Configurar métricas de negocio + técnicas
scoring = {
    "accuracy": "accuracy",
    "precision": "precision",
    "recall": "recall",
    "f1": "f1"
}

mlflow.set_experiment("spam_filter_cv_stability")

# 4. Ejecutar validación cruzada (5 folds)
cv_results = cross_validate(pipeline, X, y, cv=5, scoring=scoring, n_jobs=-1)

# 5. Loguear media y desviación estándar en MLflow
with mlflow.start_run(run_name="cv_baseline_logreg_v1"):
    for metric in scoring.keys():
        mean_val = cv_results[f"test_{metric}"].mean()
        std_val  = cv_results[f"test_{metric}"].std()
        mlflow.log_metric(f"{metric}_mean", mean_val)
        mlflow.log_metric(f"{metric}_std", std_val)
        
    mlflow.log_param("cv_folds", 5)
    mlflow.log_param("model_type", "LogisticRegression")
    
    print("✅ Validación cruzada completada.")
    print(f"   F1 mean: {cv_results['test_f1'].mean():.3f} ± {cv_results['test_f1'].std():.3f}")
```    

> 
```python
# Tests Automatizados como Gate de Calidad (tests/test_pipeline.py)
import pytest
import pandas as pd
import joblib
import numpy as np
from sklearn.metrics import f1_score, precision_score

MODEL_PATH = "artifacts/pipeline_v1.joblib"
X_TEST_PATH = "data/processed/X_test.csv"
Y_TEST_PATH = "data/processed/y_test.csv"

@pytest.fixture
def model():
    return joblib.load(MODEL_PATH)

@pytest.fixture
def test_data():
    X = pd.read_csv(X_TEST_PATH)
    y = pd.read_csv(Y_TEST_PATH).squeeze()
    return X, y

# 🔹 Test 1: Integridad del artefacto
def test_model_loads_successfully(model):
    assert model is not None
    assert hasattr(model, "predict")
    assert hasattr(model, "predict_proba")

# 🔹 Test 2: Schema de entrada robusto
def test_pipeline_handles_valid_input(model, test_data):
    X_test, _ = test_data
    preds = model.predict(X_test)
    assert len(preds) == len(X_test)
    assert set(np.unique(preds)).issubset({0, 1})

# 🔹 Test 3: Gate de negocio (SI esto falla, el CI rechaza el deploy)
def test_f1_meets_deployment_threshold(model, test_data):
    X_test, y_test = test_data
    y_pred = model.predict(X_test)
    f1 = f1_score(y_test, y_pred)
    
    MIN_F1_GATE = 0.85
    assert f1 >= MIN_F1_GATE, (
        f"❌ F1 score {f1:.3f} está por debajo del umbral de despliegue ({MIN_F1_GATE}). "
        f"Revisar drift de datos, feature engineering o reentrenar con más datos."
    )
```
________________________________________

***"Si el test_split ya nos dio un accuracy=0.92, ¿por qué necesitamos validación cruzada? ¿Qué nos revela la std (desviación estándar) que la métrica única oculta?"***  
🔍 Razonamiento esperado:  
Un único split es una foto instantánea; puede ser favorable o desfavorable por azar. La validación cruzada toma 5 fotos distintas del mismo dataset y calcula el promedio y la variabilidad.  
La std nos dice qué tan estable es el modelo frente a variaciones naturales de los datos:  
•	F1 = 0.91 ± 0.01 → Modelo robusto. Confiable para producción.  
•	F1 = 0.91 ± 0.12 → Modelo inestable. Depende críticamente de qué ejemplos caen en train/test. En producción, su rendimiento será impredecible.  
En MLOps, la estabilidad importa más que el pico de rendimiento. Un modelo con F1=0.88 ± 0.02 suele preferirse sobre uno con F1=0.93 ± 0.15.  

***"En pytest, ¿por qué escribimos assert f1 >= 0.85 en lugar de solo verificar que el script 'corre sin errores'? ¿Qué diferencia conceptual hay entre un test de software tradicional y un 'gate' de ML?"***  
🔍 Razonamiento esperado:  
•	Software tradicional: La función sum(a,b) siempre debe devolver a+b. El test valida determinismo. Si falla, hay un bug de código.  
•	Machine Learning: El modelo es probabilístico y estocástico. Siempre tendrá error. El test no valida que "funcione", valida que cumpla un Acuerdo de Nivel de Servicio (SLA) de negocio.  
El assert f1 >= 0.85 es un gate de calidad automatizado. Si el modelo corre pero su F1 es 0.70, el CI debe rechazar el despliegue automáticamente, no porque haya un crash, sino porque no cumple el umbral acordado con el área de negocio.  
Esto cambia la mentalidad: en ML, correr ≠ listo. Correr + cumplir gate ≠ listo. Solo entonces se aprueba para staging.  

***"Si el CI falla porque F1 = 0.78 (por debajo del gate), ¿cómo sabes si el problema es: a) código roto, b) datos cambiados, o c) hiperparámetros subóptimos? ¿Cómo usarías MLflow para diagnosticarlo sin adivinar?"***
🔍 Razonamiento esperado:
El fallo del CI es una señal de alerta, no un diagnóstico. MLflow cierra el ciclo de observabilidad:
1.	Comparar run_id actual vs run_id anterior exitoso en el dashboard.
2.	Si params (C, max_features, seed) son idénticos → el código no cambió. Probablemente los datos cambiaron (drift o nueva versión del dataset).
3.	Si data_version o hash de X_train.csv es distinto → data drift. Revisar EDA de la nueva versión.
4.	Si params cambiaron → hiperparámetros subóptimos. Revisar experimentos cercanos o lanzar búsqueda automática.
5.	Si el ## Code_version (git hash) cambió pero los datos/params son iguales → bug en preprocessing o lógica de entrenamiento.
En MLOps, nunca se debuggea a ciegas. MLflow + CI proporcionan el rastro forense exacto: qué cambió, cuándo, y qué impacto tuvo. El diagnóstico deja de ser intuitivo y se vuelve sistemático.

 
# 🧪 FASE 6: Entrenamiento y Trazabilidad con MLFlow
### Objetivo: 
Que surja la necesidad de MLFlow como respuesta al caos experimental.

🎯 Preguntas para plantear:
🗣️ "Corriste 15 experimentos hoy con distintas combinaciones de features y hiperparámetros. 
    Mañana te pregunto: '¿Cuál fue el que usó TF-IDF con n-gramas de 2 y C=0.1 en el SVM?'. 
    ¿Dónde buscas esa información?"

🗣️ "Si el modelo que está en producción empieza a fallar, ¿cómo sabemos 
    exactamente con qué datos y configuración fue entrenado?"
•	"Como un cuaderno de laboratorio: fecha, ingredientes, temperatura, resultado" "Experimento #42: SVM + TF-IDF 2-grams + C=0.1 → F1=0.91, tiempo=3.2min" Experiment Tracking Registrar sistemáticamente cada intento: parámetros, datos, resultados
•	"No estudiar solo con un tipo de pregunta; practicar con varios exámenes de prueba", "Dividir datos en 5 folds: entrenar en 4, validar en 1, rotar y promediar resultados" Cross-Validation, Técnica para evaluar el modelo usando múltiples particiones de los datos
•	"Como una biblioteca: cada libro tiene título, autor, edición y estante asignado"; "Modelo 'spam-filter': v1.0 (staging), v1.1 (production), v2.0 (archived)" Model Registry, Catálogo organizado de modelos: versiones, estado, metadatos
•	"Como la etiqueta de un medicamento: dosis, vía de administración, efectos"; "Input: dict con 'subject', 'body', 'sender'; Output: {'label': 'spam', 'confidence': 0.94}"; Model Signature, Definición clara de qué espera el modelo (inputs) y qué devuelve (outputs)

🗣️ "¿Qué información mínima necesitarías guardar de cada experimento 
    para poder 'replicar' o 'mejorar' ese resultado en el futuro?"
•	"Como la temperatura y tiempo del horno: no son ingredientes, pero afectan el resultado" Hyperparameter, Configuración del algoritmo que ajustamos antes de entrenar

🗣️ "Si quieres comparar visualmente la curva de aprendizaje de 3 modelos, 
    ¿lo haces con prints en consola o hay una forma más sistemática?"

💡 Lo que buscas que ellas descubran:
•	Que MLFlow Tracking responde a la necesidad de reproducibilidad.
•	La diferencia entre loggear y monitorear.
•	Que la trazabilidad es un requisito para el mantenimiento, no un "nice-to-have".
________________________________________
## Code

Aquí unimos código, datos, tests y modelo en un flujo que se ejecuta solo, decide solo y protege producción. Sin automatización, MLOps es solo documentación.  
En la máquina local o en el runner del CI:

> 
```bash
pip install -r requirements.txt
pip install dvc[gs]  # Soporte para Google Cloud Storage
pip install mlflow
pip install pytest
```

En MLOps, no se confía en entornos locales. Cada desarrollador tiene versiones distintas de Python, librerías o rutas. GitHub Actions crea un entenedor efímero y limpio (ubuntu-latest) donde:
1.	Se instala Python desde cero
2.	Se ejecuta pip install -r requirements.txt → garantiza que todos los runs usan exactamente las mismas dependencias
3.	Se descargan datos con dvc pull → asegura que los tests corren sobre la versión real del dataset
4.	Se ejecutan pytest → valida gates de calidad
5.	Si todo pasa, se promueve el modelo a Staging en MLflow Registry → habilita despliegue seguro
Esto transforma "funciona en mi laptop" en "funciona en cualquier entorno, siempre".

> 
```yaml
# Configuración CI/CD  .github/workflows/mlops_pipeline.yml
name: MLOps CI/CD Pipeline
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  validate-and-promote:
    runs-on: ubuntu-latest
    env:
      DVC_GCS_TOKEN: ${{ secrets.DVC_GCS_TOKEN }}
      MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
          
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt
          
      - name: Pull data with DVC
        run: dvc pull
        env:
          GOOGLE_APPLICATION_CREDENTIALS: ${{ secrets.GCP_SA_KEY }}
          
      - name: Run tests & validation gates
        run: pytest tests/ -v --tb=short
        
      - name: Promote to MLflow Registry (if tests pass)
        if: success()
        run: python src/fase_06_registry.py
        env:
          MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
```

> 
```python
# Creamos src/fase_06_registry.py
import os
import mlflow
from mlflow.tracking import MlflowClient

def promote_best_model_to_staging():
    client = MlflowClient()
    experiment_name = "spam_filter_mlops"
    experiment = client.get_experiment_by_name(experiment_name)
    
    # Obtener el run más reciente exitoso
    runs = client.search_runs(
        experiment_ids=[experiment.experiment_id],
        order_by=["start_time DESC"],
        max_results=1
    )
    
    if not runs:
        raise ValueError("No se encontraron runs en MLflow.")
        
    latest_run = runs[0]
    model_uri = f"runs:/{latest_run.info.run_id}/spam_pipeline"
    model_name = "spam_filter_pipeline"
    
    # Registrar o actualizar en MLflow Model Registry
    try:
        client.create_registered_model(model_name)
    except mlflow.exceptions.MlflowException:
        pass  # Ya existe
        
    # Transición automática a Staging si los gates pasaron
    client.transition_model_version_stage(
        name=model_name,
        version=latest_run.data.tags.get("mlflow.runName", "latest"),
        stage="Staging",
        archive_existing_versions=True
    )
    
    print(f"✅ Modelo {model_name} promovido a Staging (Run: {latest_run.info.run_id})")

if __name__ == "__main__":
    promote_best_model_to_staging()
```
________________________________________
***"¿Por qué ejecutamos dvc pull dentro del CI en lugar de incluir los datos directamente en el repositorio o usarlos locales?"***
🔍 Razonamiento esperado:
Incluir datasets en Git rompe el versionado (archivos >100MB generan historiales inmanejables). Usar datos locales rompe la reproducibilidad: el CI runner es una máquina nueva cada vez. dvc pull en el CI garantiza que:
1.	El mismo hash de datos se usa en desarrollo, testing y producción.
2.	El pipeline es agnóstico a la infraestructura: funciona en GitHub, GitLab, Vertex AI Pipelines o on-premise.
3.	Si el dataset cambia en GCS, el CI automáticamente usa la nueva versión y los tests revelan si el modelo se degrada.
En MLOps, los datos son parte del código de construcción. Sin dvc pull en CI, no hay garantía de que lo que se prueba es lo que se despliega.

***"Si pytest falla en el CI, el pipeline se detiene. ¿Qué gana el equipo al bloquear el merge automáticamente en lugar de solo enviar un warning?"***  
🔍 Razonamiento esperado:  
Un warning se ignora; un gate se respeta. En ML, los errores son silenciosos: un modelo con F1=0.60 puede "correr" perfectamente en producción y generar costos de negocio reales (clientes perdidos, alertas falsas, desgaste operativo).
Bloquear el merge automáticamente:  
1.	Invierte la carga de prueba: no es "demostrar que funciona", es "el CI demuestra que no cumple el SLA".  
2.	Elimina el sesgo humano: nadie presiona "merge anyway" bajo presión de entrega.  
3.	Crea un contrato de calidad: el equipo acuerda upfront qué métricas son innegociables (precision >= 0.90, F1 >= 0.85).
En MLOps, la automatización protege al negocio de la urgencia. Un CI que bloquea es un CI que cumple su función.

***"¿Por qué promovemos a Staging y no directamente a Production si los tests pasaron? ¿Qué riesgo cubre esa etapa intermedia?"***  
🔍 Razonamiento esperado:  
Los tests de CI validan calidad técnica sobre datos históricos. Pero producción tiene:  
•	Tráfico real con patrones no vistos  
•	Latencia y concurrencia distintas  
•	Integraciones con otros sistemas (APIs, colas, BDs)  
•	Usuarios que interactúan de forma impredecible  
Staging es un sandbox de validación operativa:
1.	Se despliega en paralelo al modelo actual (shadow mode)
2.	Se monitorea latencia, tasa de error, drift de features
3.	Se valida que las métricas de negocio se mantienen en vivo
4.	Solo tras 24-72h de estabilidad se promueve a Production
En MLOps, ningún modelo salta de CI a producción sin validación en entorno espejo. Staging es el amortiguador entre "funciona en pruebas" y "funciona en el mundo real".

***"¿Qué pasaría si un desarrollador cambia requirements.txt añadiendo una versión incompatible de scikit-learn? ¿Cómo lo detecta el CI antes de que llegue a producción?"***  
🔍 Razonamiento esperado:  
El CI ejecuta pip install -r requirements.txt en un entorno limpio. Si hay incompatibilidad:
1.	La instalación falla → el job se detiene inmediatamente
2.	Si pasa la instalación pero hay API breaking changes, pytest fallará en los tests de schema o predicción
3.	El modelo no se registra en MLflow → no hay promoción accidental
Además, en flujos maduros se añade pip-audit o safety para detectar vulnerabilidades, y pip freeze > requirements.txt se bloquea con pre-commit hooks.
En MLOps, el CI es el primer firewall. Un entorno aislado + tests estrictos + gates automáticos crean un sistema donde los errores se atrapan antes de costar dinero.  


# 🔄 FASE 7: CI/CD para ML (No es lo mismo que software tradicional)
### Objetivo:
Entender las particularidades del testing en ML.

🎯 Preguntas para plantear:
🗣️ "En software tradicional, un test unitario verifica que una función devuelva el valor esperado. 
    En ML, ¿qué verificamos? ¿Que el modelo tenga accuracy > 90%? ¿Eso es suficiente?"

🗣️ "Si cambiamos una línea en el preprocessing, ¿debemos correr:
    a) Solo tests de código, b) Solo reentrenar el modelo, o c) Ambas cosas? ¿Por qué?"

🗣️ "¿Cómo automatizamos la validación de que un nuevo modelo es 'mejor' que el actual? 
    ¿Qué métricas y umbrales usarías como 'gate' para un deployment?"

🗣️ "¿Qué pasa si el modelo pasa todos los tests en CI, pero en producción 
    los datos de entrada tienen una distribución distinta? ¿Cómo detectamos eso temprano?"

💡 Lo que buscas que ellas descubran:  
•	Que en ML el testing es multinivel: código, datos, modelo, desempeño en producción.  
•	La necesidad de shadow deployment o canary releases para modelos.  
•	Que el CI/CD de ML incluye validación de drift y calidad de datos.  

"Cada push a main: linting + tests unitarios + validación de schema de datos" CI (Continuous Integration), Integrar y validar cambios de código frecuentemente con tests automáticos  
"Si el nuevo modelo supera F1 > 0.90 en validación → se despliega a staging automáticamente"; CD (Continuous Delivery/Deployment) Automatizar el despliegue de modelos a entornos de prueba o producción  
"Tests: accuracy > 0.95, FP rate < 0.01, sin sesgo por dominio de email"; Model Testing,  Validar no solo el código, sino el comportamiento del modelo: métricas, fairness, drift  
"Desplegar v1.2 al 5% de los correos, monitorear 24h, luego escalar", Canary Deployment  
"El modelo nuevo clasifica correos 'en silencio'; comparamos sus decisiones con el modelo actual", Shadow Mode, Ejecutar el nuevo modelo en paralelo sin que afecte al usuario, para comparar  
________________________________________
## Code

Aquí cerramos el ciclo MLOps: un modelo desplegado no es un punto final, es un sistema vivo que decae. Monitorear es anticipar; automatizar el reentrenamiento es sobrevivir.  

> 
```bash
pip install evidently
```

En CI/CD se valida que el modelo funcione sobre datos históricos. En producción, los datos cambian con el tiempo. evidently es la librería estándar open-source para monitoreo de ML porque:
•	Calcula drift estadístico (Kolmogorov-Smirnov, PSI, Jensen-Shannon) sin necesidad de etiquetas reales.
•	Genera reportes HTML/JSON listos para dashboards o alertas.
•	Define tests programáticos (assert drift_score < 0.1) que pueden disparar pipelines automáticos.
En GCP, esta lógica se traduce nativamente a Vertex AI Model Monitoring, pero evidently permite entender el qué y por qué antes de delegarlo a servicios gestionados. MLOps exige saber qué se mide antes de automatizarlo.

> 
```python
# Detección de Drift + Trigger de Reentrenamiento (src/fase_07_monitoring.py)
import pandas as pd
import json
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
from evidently.metrics import ColumnDriftMetric
from evidently.test_suite import TestSuite
from evidently.tests import TestValueDrift

# 1. Cargar referencia (datos de entrenamiento) y producción (batch reciente)
REF_PATH = "data/processed/X_train.csv"
PROD_PATH = "data/processed/X_prod_batch_latest.csv"  # Simulación de logs de producción

ref_data = pd.read_csv(REF_PATH)
prod_data = pd.read_csv(PROD_PATH)

# 2. Configurar métricas de drift
# Columnas numéricas: msg_length, num_exclamations
# Columnas de texto: message (se convierte a longitud promedio o embedding similarity en producción real)
report = Report(metrics=[
    ColumnDriftMetric(column_name="msg_length"),
    ColumnDriftMetric(column_name="num_exclamations")
])

# 3. Ejecutar análisis
report.run(reference_data=ref_data, current_data=prod_data)
drift_json = report.json()

# 4. Extraer decisión de drift
drift_results = json.loads(drift_json)
threshold_drift = 0.1  # Umbral de negocio: si >10% de features derivan, reentrenar
features_with_drift = [
    m["result"]["column_name"] 
    for m in drift_results["metrics"] 
    if m["result"]["drift_score"] > threshold_drift
]

print(f"📊 Drift detectado en: {features_with_drift}")

# 5. Trigger condicional de reentrenamiento
if len(features_with_drift) > 0:
    print("⚠️ Drift significativo. Disparando pipeline de reentrenamiento...")
    # En GCP: publicar mensaje en Pub/Sub → Cloud Function → Vertex AI Training Job
    trigger_payload = {
        "trigger": "data_drift",
        "features_drifted": features_with_drift,
        "threshold": threshold_drift,
        "timestamp": pd.Timestamp.now().isoformat()
    }
    with open("artifacts/retrain_trigger.json", "w") as f:
        json.dump(trigger_payload, f)
else:
    print("✅ Distribución estable. Modelo en producción sigue siendo válido.")
```

| COMPONENTE EN CÓDIGO | EQUIVALENTE NATIVO EN GCP | PROPÓSITO |
| :--- | :---: | :--- |
| EVIDENTLY + DATADRIFTPRESET | Vertex AI Model Monitoring | Monitoreo nativo de drift en features/predicciones sin Código|  
| RETRAIN_TRIGGER.JSON | Pub/Sub + Cloud Scheduler | Canal de eventos para orquestar reentrenamiento|  
| PYTHON TRIGGER SCRIPT | Cloud Run / Cloud Functions | Ejecuta lógica de decisión o notifica equipos|  
| VERTEX AI TRAINING | Vertex AI Pipelines + Kubeflow | Reentrena automáticamente con nuevos datos |  
| MLFLOW REGISTRY | Vertex AI Model Registry | Versionado y promoción automática a Staging |  

________________________________________

***"¿Qué diferencia hay entre Data Drift y Concept Drift? ¿Cuál de los dos podemos detectar sin tener etiquetas reales en producción?"***  
🔍 Razonamiento esperado:  
•	Data Drift: La distribución de las features cambia. Ej: antes los correos promediaban 120 caracteres, ahora promedian 450. Los spammers usan mensajes más largos. → Detectable sin etiquetas (comparamos distribución actual vs referencia).  
•	Concept Drift: La relación entre features y target cambia. Ej: antes "¡GRATIS!" era spam; ahora es newsletter legítima de una tienda. El modelo sigue viendo la misma distribución, pero su mapeo a spam/ham ya no es válido. → Solo detectable con feedback real o labels retrasadas.  
En MLOps, monitoreamos ambos: Data Drift con Evidently/Vertex AI, Concept Drift con métricas de negocio (tasa de corrección de usuarios, precision en batch con labels retrasadas).  
________________________________________
***"Si el CI pasó con F1=0.92, ¿por qué el modelo puede degradarse en producción sin que el código haya cambiado? ¿Qué asunción oculta rompemos al desplegar?"***  
🔍 Razonamiento esperado:  
El CI asume estación temporal: que el futuro se parece al pasado. En producción, esa asunción se rompe por:  
•	Cambios externos (nuevas tácticas de spam, estacionalidad, campañas de marketing)  
•	Cambios internos (nuevas reglas de filtrado en el servidor, integraciones con otros sistemas)  
•	Degradación de infraestructura (latencia alta → timeouts → pérdida de context window)  
Monitorear no es "ver si el modelo sigue corriendo", es ver si el modelo sigue siendo válido para el problema actual. En MLOps, correr ≠ resolver.  
________________________________________
***"¿Por qué usamos un umbral de 0.1 para drift en lugar de 0.05 o 0.2? ¿Quién debería definir ese número y con qué criterio?"***  
🔍 Razonamiento esperado:  
El umbral no es técnico, es de negocio + operacional. Definirlo implica:  
1.	Costo de reentrenamiento: si es alto (GPU, ingeniería, validación), el umbral sube (0.15-0.2).  
2.	Costo de error en producción: si es alto (clientes perdidos, multas), el umbral baja (0.05-0.1).  
3.	Velocidad de cambio del dominio: spam cambia rápido → umbral bajo. Datos médicos estables → umbral alto.  
En MLOps, los umbrales se documentan, versionan y revisan trimestralmente. No se hard## Codean; se parametrizan en un config file o Feature Store.  
________________________________________
***"Si decidimos reentrenar automáticamente cada vez que haya drift, ¿qué riesgo introducimos? ¿Cómo evitamos un ciclo infinito de reentrenamiento con datos ruidosos?"***  
🔍 Razonamiento esperado:  
El reentrenamiento automático ciego crea inestabilidad operativa:  
•	Datos ruidosos o atípicos → modelo se sobreajusta a anomalías → nuevo drift → reentrena de nuevo.  
•	Degradación progresiva por acumulación de errores de etiquetado automático.
La solución MLOps es human-in-the-loop + gates de calidad:
1.	Drift detectado → alerta al equipo + trigger a Staging
2.	Se reentrena, pero solo se promueve a Production si pasa CI/CD con métricas ≥ umbral
3.	Se aplica shadow mode 48h antes de activar
4.	Si el modelo nuevo degrada, rollback automático a versión anterior
La automatización acelera; los gates protegen.

 
# 📈 FASE 8: Métricas y Evaluación (Más allá de la Accuracy)
### Objetivo: 
Que entienda que la métrica correcta depende del costo de error.

| Concepto| Definición Simple| Fórmula (opcional)| Conexión Spam Filter |
| :--- | :--- | :--- | :--- |
| Accuracy | Porcentaje de predicciones correctas sobre el total | `(TP+TN) / Total` | "Engañosa si hay desbalance: 95% accuracy puede ser solo predecir siempre 'ham'" |
| Precision | De los que predije como spam, ¿cuántos realmente lo eran? | `TP / (TP+FP)` | "Alta precisión = pocos correos legítimos bloqueados por error" |
| Recall (Sensitivity) | De los spam reales, ¿cuántos logré detectar? | `TP / (TP+FN)` | "Alto recall = pocos spams se escapan a la bandeja de entrada" |
| F1-Score | Promedio armónico de precisión y recall: balance entre ambos | `2 * (P*R)/(P+R)` | "Útil cuando necesitamos equilibrar FP y FN; nuestro 'número mágico' de calidad" |
| Confusion Matrix | Tabla que muestra cuántos aciertos y errores de cada tipo cometió el modelo | Matriz 2x2: [TN, FP; FN, TP] | "Nos permite ver visualmente: ¿estamos fallando más en FP o en FN?" |
| ROC-AUC | Capacidad del modelo para distinguir entre clases, sin importar el umbral | Área bajo la curva TPR vs FPR | "Un AUC de 0.95 significa que el modelo 'ordena bien' spam vs ham en general" |
| Threshold Tuning | Ajustar el punto de corte para decidir cuándo predecir 'spam' | Mover el umbral de probabilidad (ej: de 0.5 a 0.7) | "Si queremos menos FP, subimos el umbral: solo marcamos como spam si estamos muy seguros" |

🎯 Preguntas para plantear:
🗣️ "Nuestro dataset tiene 95% ham, 5% spam. Un modelo que siempre predice 'ham' 
    tiene 95% de accuracy. ¿Es un buen modelo? ¿Por qué sí o por qué no?"

🗣️ "En nuestro contexto, ¿qué es más costoso:
    a) Que un spam llegue a la bandeja de entrada, o 
    b) Que un correo legítimo vaya a spam? 
    ¿Cómo se refleja eso en la métrica que elegimos?"

🗣️ "Si te digo que el modelo tiene F1-score de 0.85, ¿qué me estás diciendo realmente? 
    ¿Podrías explicármelo sin usar la fórmula?"

🗣️ "¿Cuándo usarías RMSE vs. MAE? ¿Y en un problema de clasificación como este, 
    por qué no aplican?"

💡 Lo que buscas que ellas descubran:
•	Que Accuracy es engañosa con clases desbalanceadas.
•	La relación entre Precisión, Recall y F1 en términos de negocio.
•	Que las métricas deben alinearse con los costos de error del dominio.


| Concepto | Definición Simple | Analogía | Conexión Spam Filter |
| :--- | :--- | :--- | :--- |
| Model Serving | Poner el modelo a disposición para que reciba peticiones y devuelva predicciones | "Como abrir el restaurante: la cocina ya está lista para recibir órdenes" | "API REST en Cloud Run: POST /predict con correo → devuelve {'label': 'spam'}" |
| Latency / Throughput | Tiempo de respuesta y cantidad de peticiones que el modelo puede atender | "Cuánto tarda en salir un plato y cuántos comensales puede atender por hora" | "¿El filtro responde en <200ms? ¿Puede procesar 100 correos/minuto sin colapsar?" |
| Data Drift | Cuando la distribución de los datos de entrada cambia con el tiempo | "Los gustos de los comensales cambian: hoy piden más vegano, ayer era todo carne" | "Los spammers empiezan a usar 'G@n@r' en lugar de 'Ganar' → el modelo no lo reconoce" |
| Concept Drift | Cuando la relación entre features y target cambia (la definición de 'spam' evoluciona) | "Antes 'oferta' era spam; hoy muchas newsletters legítimas usan esa palabra" | "Lo que era spam en 2024 puede no serlo en 2026; el modelo debe adaptarse" |
| Monitoring Dashboard | Visualización en tiempo real de métricas de modelo, datos y sistema | "El tablero de control de un avión: velocidad, altitud, combustible, alertas" | "Gráficas: % spam detectado, tasa de FP, latencia p95, volumen de correos/hora" |    
| Alerting | Notificaciones automáticas cuando algo sale de lo esperado | "Como la alarma de humo: te avisa antes de que el fuego se propague" | "Si la tasa de FP sube >2% en 1 hora → alerta a Slack + rollback automático" |
| Feedback Loop | Mecanismo para capturar correcciones de usuarios y reentrenar el modelo | "Como un chef que pregunta '¿cómo estuvo?' y ajusta la receta para la próxima" | "Cuando se marca un correo como 'no es spam', ese ejemplo se guarda para el próximo entrenamiento" |
| Model Retraining Strategy | Cuándo y cómo actualizar el modelo: schedule, trigger por drift, o manual | "¿Cocinar cada día con receta fija, o ajustar según los ingredientes disponibles?" | "Reentrenar semanalmente con nuevos datos + validación automática antes de desplegar" |

________________________________________
## Code
Aquí cerramos el ciclo: pasamos de "modelo que funciona" a "sistema gobernado, reutilizable y rentable". Sin gobernanza, MLOps escala el caos.

> 
```bash
pip install feast
```

Hasta ahora, calculamos features (msg_length, num_exclamations) en el script de entrenamiento y las recalculamos manualmente en el endpoint de inferencia. Esto genera duplicación, inconsistencia y riesgo de drift silencioso. feast (Feature Store) introduce un catálogo centralizado y versionado de features:
•	Define una vez, sirve en batch (para entrenamiento) y online (para inferencia en tiempo real).
•	Garantiza consistencia absoluta: el modelo ve exactamente la misma distribución y lógica en dev y producción.
•	Habilita reutilización cross-modelo: si otro equipo necesita msg_length, no vuelve a escribirla; la consume desde el store.

> 
```python
pip install pandera
```

Los tests de pytest validan que el código funciona. pandera valida que los datos que entran al pipeline cumplen contratos explícitos: tipos, rangos, valores nulos, restricciones de negocio. En gobernanza de ML, la calidad de datos no es opcional; es un requisito de compliance. Sin validación runtime, un correo mal formateado o un pico de spam silencioso rompe el modelo sin que el CI lo detecte.

> 
```python
pip install python-dotenv
```

Hardcodear rutas, URIs o credenciales rompe el principio de infraestructura inmutable. python-dotenv permite gestionar configuraciones por entorno (dev, staging, prod) sin tocar el código. En MLOps maduro, el mismo artefacto se despliega en todos los entornos; solo cambian las variables de entorno. Esto elimina errores de "funcionó en staging, falló en prod por una ruta distinta".

> 
```python
# gobernanza + Feature Definition + Multi-Env (src/fase_08_governance.py)
import os
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series
from dotenv import load_dotenv
from feast import FeatureView, Entity, Field
from feast.types import Float32, Int64, String

# 1. Cargar configuración por entorno
load_dotenv(f".env.{os.getenv('ENVIRONMENT', 'dev')}")
MLFLOW_URI = os.getenv("MLFLOW_TRACKING_URI")
FEATURE_STORE_PROJECT = os.getenv("FEATURE_STORE_PROJECT")

# 2. Contrato de datos (Schema Validation)
class EmailFeaturesSchema(pa.SchemaModel):
    message: Series[String] = pa.Field(nullable=False, str_length={"min_value": 1})
    msg_length: Series[Int64] = pa.Field(ge=0, le=5000)
    num_exclamations: Series[Int64] = pa.Field(ge=0, le=50)
    target: Series[Int64] = pa.Field(isin=[0, 1])

    class Config:
        coerce = True
        strict = True

# 3. Definición de Feature Store (conceptual)
email_entity = Entity(name="email_id", join_keys=["email_id"])
email_feature_view = FeatureView(
    name="spam_email_features",
    entities=[email_entity],
    schema=[
        Field(name="msg_length", dtype=Int64),
        Field(name="num_exclamations", dtype=Int64),
        Field(name="tfidf_spam_score", dtype=Float32)
    ],
    description="Features estandarizadas para clasificación de spam"
)

# 4. Validación runtime antes de ingestión
def validate_ingestion(df: pd.DataFrame) -> pd.DataFrame:
    try:
        validated_df = EmailFeaturesSchema.validate(df)
        print("✅ Contrato de datos cumplido. Ingestión segura.")
        return validated_df
    except pa.errors.SchemaError as e:
        print(f"🚨 Violación de gobernanza: {e}")
        raise

# Simulación de uso
if __name__ == "__main__":
    sample = pd.DataFrame({
        "email_id": ["msg_001"],
        "message": ["¡Gana 1000 USD ya!!!"],
        "msg_length": [22],
        "num_exclamations": [3],
        "target": [1]
    })
    validate_ingestion(sample)
```
________________________________________

***"¿Por qué invertir tiempo en un Feature Store si podemos simplemente guardar processed_data.parquet y leerlo cuando necesitemos?"***  
🔍 Razonamiento esperado:  
Un .parquet es una foto estática. Un Feature Store es un sistema vivo que resuelve 3 problemas críticos:  
1.	Consistencia online/batch: En inferencia en tiempo real, no puedes cargar un parquet de 10GB. El Feature Store sirve features individuales vía API con latencia <50ms, usando la misma lógica que se usó para entrenar.  
2.	Versionado temporal: ¿Qué features vio el modelo el 12/03/2024 a las 14:30? Un Feature Store guarda el point-in-time correcto. Un parquet mezcla datos viejos y nuevos, causando data leakage retrospectivo.  
3.	Reutilización y costo: 5 equipos recalculando msg_length = 5x costo de computación + 5 riesgos de inconsistencia. Un store = 1 definición, 5 consumidores.  
En MLOps, la gobernanza empieza por evitar duplicación. El Feature Store no es lujo; es infraestructura de escala.

***"Si ya tenemos pytest y validación de métricas, ¿qué aporta pandera que no cubran los tests unitarios?"***  
🔍 Razonamiento esperado:  
•	pytest valida comportamiento del código (¿la función devuelve lo esperado?).  
•	pandera valida integridad de los datos en runtime (¿el input cumple el contrato antes de entrar al pipeline?).  
Un test unitario pasa si el código está bien, pero falla silenciosamente si los datos cambian fuera de rango. pandera actúa como un firewall de datos: si un spammer envía mensajes de 50,000 caracteres, el pipeline rechaza la entrada antes de que el modelo genere predicciones erróneas o consuma memoria innecesaria.  
En gobernanza, los datos son tan críticos como el código. Validar ambos cierra el ciclo de calidad.

***"Si usamos el mismo código en dev, staging y prod, ¿cómo evitamos que un error en dev rompa staging o que se filtren credenciales de prod a un notebook local?"***  
🔍 Razonamiento esperado:  
La respuesta está en aislamiento por diseño:  
1.	Variables de entorno + .env por capa: El código nunca hard## Codea URIs. Lee os.getenv(). Cada entorno inyecta sus propios valores en despliegue.  
2.	Secretos gestionados: Credenciales de GCS, MLflow, BDs viven en Secret Manager (GCP), no en .env commitados.  
3.	Permisos por IAM: El SA de dev no tiene acceso a buckets de prod. Un commit en develop no puede escribir en registry de producción.  
4.	Promoción de artefactos, no de código: El mismo .joblib y .parquet se mueven entre entornos. No se recompila.  
En MLOps, la seguridad no es un add-on; es una propiedad del pipeline. La separación estricta de entornos + gestión centralizada de secretos elimina la mayoría de incidentes de producción.

***"El negocio pregunta: '¿Cuánto nos cuesta mantener todo este MLOps? ¿Vale la pena?'. ¿Cómo calculamos el ROI sin caer en tecnicismos?"***
🔍 Razonamiento esperado:
El ROI de MLOps no se mide en "accuracy +2%". Se mide en reducción de costo operativo + aceleración de valor:
1.	Time-to-Market: Sin MLOps, un nuevo modelo tarda 3 semanas en desplegarse (pruebas manuales, config, rollback). Con CI/CD + registry: 2 horas. (3 semanas - 2h) × valor/hora del equipo.
2.	Costo de incidentes: Un modelo degradado no detectado por 48h puede generar 10K falsos positivos. MLOps con drift + gates lo detecta en <2h. Ahorro = (tiempo sin detectar × costo por error).
3.	Reutilización: Feature Store + pipelines estandarizados evitan que 3 ingenieros reconstruyan la misma lógica. Ahorro = horas evitadas × costo/hora.
4.	Infraestructura optimizada: Monitoreo evita provisionar GPUs innecesarias o reentrenar sin motivo.
En MLOps, la métrica de éxito es predictibilidad, no perfección. Un sistema que falla rápido, se recupera solo y audita cada decisión vale más que un modelo "preciso" que nadie confía en tocar.

| COMPONENTE EN CÓDIGO | EQUIVALENTE NATIVO EN GCP | PROPÓSITO |
| :--- | :--- | :--- |
FEAST + FEATUREVIEW | Vertex AI Feature Store | Servir features online/batch con consistencia garantizada |
| PANDERA SCHEMA | Dataform + BigQuery Assertions o Cloud Run pre-flight checks | Validación de calidad de datos en ingestión |
| PYTHON-DOTENV + ENV VARS | Cloud Run Environment Variables + Secret Manager | Gestión segura de config multi-ambiente |
VALIDATE_INGESTION() | Eventarc + Pub/Sub + Cloud Functions | Gate de calidad antes de entrar a pipeline de training |
| ROI TRACKING | Cloud Billing Export + Vertex AI Cost Dashboard | Atribución de costo por modelo/ambiente/equipo |



# Algoritmos de ML
## 📐 1. [ Regresion Lineal ](../algoritmos/Supervised_Learning-Regresion_Lineal.md)
🧠 *Concepto Clave:* Predice un valor numérico continuo ajustando una línea recta que minimiza el error respecto a los datos.  
⚙️ *¿Cómo funciona?* Busca la combinación de pesos para cada feature que hace que ŷ = w₁x₁ + w₂x₂ + ... + b se acerque lo más posible al valor real. Usa mínimos cuadrados.  
🎯 *¿Cuándo elegirlo?* Forecasting, tendencias, variables continuas (precio, temperatura, tiempo).  
✅ Extremadamente rápido, interpretable, baseline sólido.  
❌ Asume relación lineal, sensible a outliers, no sirve para clasificación.  

## 🎲 2. [ Regresión Logística ](../algoritmos/Supervised_Learning-Regresion_Logistica.md)
🧠 *Concepto Clave:* Extensión de la regresión lineal diseñada para clasificación binaria. Predice probabilidades.  
⚙️ *¿Cómo funciona?* Aplica la función sigmoide (1 / (1 + e⁻ᶻ)) a la salida lineal para comprimirla entre 0 y 1. Si P ≥ 0.5 → clase positiva.  
🎯 *¿Cuándo elegirlo?* Clasificación binaria/multiclase, necesidad de probabilidades calibradas, baseline interpretable.  
✅ Rápido, escalable, entrega probabilidades, fácil de debuggear.  
❌ Línea de decisión lineal; lucha con patrones no lineales complejos.  

## 🌳 3. [ Árboles de Decisión ](../algoritmos/Supervised_Learning-Arboles_de_Decision.md)
🧠 *Concepto Clave:* Modelo que toma decisiones mediante reglas SI-ENTONCES anidadas, dividiendo los datos recursivamente.  
⚙️ *¿Cómo funciona?* En cada nodo elige la feature y umbral que maximiza la "pureza" (Gini o Entropía) de los subconjuntos resultantes.  
🎯 *¿Cuándo elegirlo?* Necesidad de reglas explicables, datos mixtos (numéricos + categóricos), relaciones no lineales.  
✅ No requiere escalado, muy interpretable, maneja interacciones complejas.  
❌ Propenso a sobreajuste, inestable (pequeños cambios en datos → árbol distinto).  

## 🌲🌲🌲 4. [ Random Forest ](../algoritmos/Supervised_Learning-Random_Forest.md)
🧠 *Concepto Clave:* Ensemble de cientos de árboles de decisión que votan colectivamente para reducir varianza y sobreajuste.  
⚙️ *¿Cómo funciona?* Entrena cada árbol con un subconjunto aleatorio de datos (bagging) y features. La predicción final es la mayoría de votos (clasificación) o promedio (regresión).  
🎯 *¿Cuándo elegirlo?* Alta precisión requerida, datos ruidosos, importancia de features, robustez en producción.  
✅ Muy preciso, robusto a overfitting, entrega feature importance, maneja no-linealidad.  
❌ Menos interpretable que un solo árbol, mayor consumo de RAM/CPU, serving más lento.  

## 📏 5. [ Máquinas de Vectores de Soporte (SVM) ](../algoritmos/Supervised_Learning-SVM.md)
🧠 *Concepto Clave:* Encuentra el hiperplano que maximiza el margen de separación entre clases.  
⚙️ *¿Cómo funciona?* Usa solo los puntos más cercanos al borde ("vectores de soporte") para definir la frontera. Con kernels (lineal, RBF, polinomial) puede separar datos no lineales proyectándolos a dimensiones superiores.  
🎯 *¿Cuándo elegirlo?* Datos de alta dimensionalidad (texto, embeddings), margen de separación claro, clasificación precisa.  
✅ Muy efectivo en espacios de alta dimensión, robusto a overfitting (con buen C/gamma), histórico en NLP.  
❌ Costoso en datasets >100K muestras, difícil de interpretar, sensible a escalado y hiperparámetros.  

## 📧 6. [ Naive Bayes ](../algoritmos/Supervised_Learning-Naive_Bayes.md)
🧠 *Concepto Clave:* Clasificador probabilístico basado en el Teorema de Bayes, asumiendo independencia entre features.  
⚙️ *¿Cómo funciona?* Calcula P(Spam | palabras) ∝ P(Spam) × ∏ P(palabra | Spam). Aunque la independencia es "ingenua", funciona sorprendentemente bien en texto.  
🎯 *¿Cuándo elegirlo?* Clasificación de texto, entrenamiento ultra-rápido, baseline NLP, recursos limitados.  
✅ Extremadamente rápido, escala bien a millones de features, tolera missing data, simple de implementar.  
❌ Asume independencia (las palabras en un correo no son independientes), puede calibrar mal probabilidades.  

## 📍 7. [ K-Nearest Neighbors (KNN) ](../algoritmos/Supervised_Learning-KNN.md)
🧠 *Concepto Clave:* Clasifica un ejemplo nuevo basándose en la mayoría de sus K vecinos más cercanos en el espacio de features.  
⚙️ *¿Cómo funciona?* No entrena un modelo explícito. Al predecir, calcula distancias (euclidiana, manhattan, coseno) a todos los puntos de entrenamiento y vota.  
🎯 *¿Cuándo elegirlo?* Datasets pequeños, relaciones no paramétricas, necesidad de adaptación instantánea a nuevos datos.  
✅ Sin fase de entrenamiento, simple, se adapta a fronteras complejas.  
❌ Predicción lenta (O(N)), sensible a escala y dimensionalidad, alto consumo de memoria.  
________________________________________
## 🔍 8. [ Análisis de Componentes Principales (PCA) ](../algoritmos/Unsupervised_Learning-PCA.md)
🧠 *Concepto Clave:* Reducción de dimensionalidad no supervisada. Encuentra las direcciones de máxima varianza y proyecta los datos en un espacio más pequeño.  
⚙️ *¿Cómo funciona?* Calcula componentes ortogonales (autovectores de la matriz de covarianza) y retiene solo los que explican la mayor variabilidad.  
🎯 *¿Cuándo elegirlo?* Datos con cientos/miles de features, ruido alto, necesidad de visualización o acelerar modelos posteriores.  
✅ Rápido, elimina redundancia, mejora estabilidad numérica.  
❌ Pierde interpretabilidad (los componentes no son features originales), asume relaciones lineales.  

## 🧩 9. [ K-Means Clustering ](../algoritmos/Unsupervised_Learning-K_Means.md)
🧠 *Concepto Clave:* Agrupamiento no supervisado que partitiona datos en K grupos basándose en distancia a centroides.  
⚙️ *¿Cómo funciona?* Inicializa K centroides → asigna cada punto al centroide más cercano → recalcula centroides → repite hasta convergencia.  
🎯 *¿Cuándo elegirlo?* Segmentación, detección de patrones ocultos, reducción de datos antes de modelado supervisado.  
✅ Simple, escalable (O(N·K·d)), fácil de paralelizar.  
❌ Requiere definir K, sensible a escala e inicialización, asume clusters esféricos y de tamaño similar.  

## 🌿 10. [ Agrupamiento Jerárquico (Hierarchical Clustering) ](../algoritmos/Unsupervised_Learning-Hierarchical_Clustering.md)
🧠 *Concepto Clave:* Construye una jerarquía de clusters (dendrograma) sin requerir K predefinido.  
⚙️ *¿Cómo funciona?* Versión aglomerativa: cada punto inicia como cluster → se fusionan los dos más cercanos iterativamente → se detiene al cortar el dendrograma.  
🎯 *¿Cuándo elegirlo?* Exploración de estructura natural de datos, datasets pequeños/medianos, necesidad de niveles de granularidad.  
✅ No requiere K, visualmente interpretable, captura relaciones anidadas.  
❌ Complejidad O(N²) o O(N³), sensible a ruido, difícil de actualizar incrementalmente.  

## 🎮 11. [ Q-Learning (Reinforcement Learning) ](../algoritmos/Reinforcement_Learning-QLearning.md)
🧠 *Concepto Clave:* Aprendizaje por refuerzo que optimiza decisiones secuenciales maximizando recompensa acumulada.  
⚙️ *¿Cómo funciona?* Actualiza una tabla o red de valores Q(s,a) usando la ecuación de Bellman: Q ← Q + α[r + γ·max Q(s',a') - Q]. Balancea exploración vs explotación.  
🎯 *¿Cuándo elegirlo?* Entornos dinámicos, decisiones en cadena, sistemas adaptativos con feedback retardado.  
✅ Aprende sin modelo del entorno, maneja recompensas diferidas, se adapta en tiempo real.  
❌ Inestable con espacios grandes, requiere simulación o entorno seguro, difícil de debuggear.  

## 🖼️ 12. [ Redes Neuronales Convolucionales (CNN) ](../algoritmos/Deep_Learning-CNN.md)
🧠 *Concepto Clave:* Arquitectura deep learning optimizada para datos con estructura espacial o local (imágenes, señales, texto 1D).  
⚙️ *¿Cómo funciona?* Aplica filtros deslizantes que detectan patrones locales → pooling reduce dimensionalidad → capas profundas combinan features jerárquicamente.  
🎯 *¿Cuándo elegirlo?* Reconocimiento visual, procesamiento de señales, extracción de patrones locales en secuencias.  
✅ Invariante a traslación, excelente en patrones locales, altamente paralelizable en GPU.  
❌ Requiere muchos datos, computacionalmente costoso, caja negra difícil de auditar.  

## 🔁 13. [ Redes Neuronales Recurrentes (RNN / LSTM / GRU) ](../algoritmos/Deep_Learning-RNN_LSTM_GRU.md)
🧠 *Concepto Clave:* Redes con memoria interna que procesan secuencias manteniendo un estado oculto paso a paso.  
⚙️ *¿Cómo funciona?* h_t = f(W·h_{t-1} + U·x_t + b). LSTM/GRU añaden compuertas para retener/olvidar información a largo plazo y evitar vanishing gradients.  
🎯 *¿Cuándo elegirlo?* Datos secuenciales: texto, series de tiempo, audio, donde el orden importa.  
✅ Captura dependencias temporales, flexible en longitud de secuencia.  
❌ Entrenamiento lento, propenso a desvanecimiento de gradientes (RNN base), mayormente reemplazado por Transformers.  

## 🕸️ 14. [ Perceptrón Multicapa (MLP) ](../algoritmos/Deep_Learning-MLP.md)
🧠 *Concepto Clave:* Red neuronal feedforward con capas ocultas y activaciones no lineales. Aproximador universal.  
⚙️ *¿Cómo funciona?* Propaga datos hacia adelante: z = W·x + b → a = σ(z). Entrena con backpropagation y optimizadores (Adam, SGD).  
🎯 *¿Cuándo elegirlo?* Datos tabulares complejos, relaciones no lineales fuertes, baseline deep learning.  
✅ Flexible, captura interacciones complejas, compatible con features numéricas/categóricas.  
❌ Propenso a overfitting, requiere regularización/dropout, menos interpretable, sensible a escalado.  
