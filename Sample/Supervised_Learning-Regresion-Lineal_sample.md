# Ejemplo Práctico: Regresión Lineal

# Caso de Uso: Real Estate Analytics

# Predicción con Regresión Lineal

Acompaña el proceso de creación de un modelo que estima el precio de una propiedad basándose en su
tamaño. Un flujo de trabajo desde el dato crudo hasta la toma de decisión financiera.

**Guía del Proyecto:** Haz clic en cada fase para ver las
tareas técnicas realizadas en este ejemplo de predicción inmobiliaria.

1

### Exploración (EDA)

Analizamos el dataset de 500 viviendas para confirmar si hay una
tendencia lineal evidente.

Creamos un gráfico de dispersión (scatter plot). Observamos que a medida que aumentan los m², el
precio sube de forma constante. La correlación es de 0.85, lo que valida el uso de una regresión
lineal.

Visualización de tendencia

Cálculo de correlación

Identificación de Outliers

2

### Preprocesamiento

Limpiamos los datos para que el modelo no se confunda con valores
nulos o escalas extrañas.

Eliminamos registros sin precio y aplicamos **Escalado Estándar**. Aunque la
regresión lineal simple no lo exige estrictamente, ayuda a la convergencia si usáramos gradiente
descendente.

Imputación de nulos

Estandarización de m²

División Train/Test (80/20)

3

### El Modelo

Planteamos la hipótesis: Precio = β₀ + β₁ \* (Metros Cuadrados).

Definimos que el "Precio" es nuestra variable objetivo ($Y$) y los "Metros Cuadrados" nuestra
característica ($X$). El modelo buscará cuánto vale cada metro cuadrado extra (β₁) y el precio
base (β₀).

Selección de Target

Configuración de Hipótesis

Inicialización de Pesos

4

### Ajuste (Fit)

El algoritmo ajusta la línea de mejor ajuste usando los datos de
entrenamiento.

Se aplica Mínimos Cuadrados Ordinarios (OLS). El algoritmo encuentra que β₀ = $50k y β₁ = $1.2k.
Esto significa que cada m² aumenta el valor en $1,200 sobre una base de $50,000.

Minimización de residuos

Cálculo de coeficientes

Optimización OLS

5

### Evaluación

Probamos el modelo con datos que nunca vio para medir su precisión
real.

Obtenemos un **R² de 0.82**. Esto indica que el tamaño de la casa explica el 82% de
la variación del precio. El error promedio (MAE) es de +/- $15,000.

R² Score: 0.82

MAE: $15k de error

Análisis de Residuos

6

### Supuestos

Verificamos que el modelo sea estadísticamente sólido y no sea fruto
del azar.

Comprobamos que los errores se distribuyen de forma normal y que no hay patrones extraños en los
residuos. Si hubiera "curvas" en los errores, el modelo lineal sería insuficiente.

Prueba de Homocedasticidad

Normalidad de Errores

Independencia

7

### Inferencia

¡Listo para usar! Predecimos el valor de una casa nueva en el mercado.

Entra una casa de 100m². El modelo calcula: $50k + ($1.2k \* 100) = **$170,000**.
Esta predicción ayuda a tasadores y compradores a tener un precio de referencia justo.

Predicción en tiempo real

Estimación de confianza

Valor añadido al negocio

## Conclusión del Ejemplo

La Regresión Lineal nos permitió convertir datos históricos en una herramienta de tasación
automática. Aunque simple, es la base para modelos más complejos (como añadir antigüedad, barrio o
número de baños).

Interpretable
Escalable
Predictivo

> [**Algoritmo - Regresion Lineal**](../Algoritmos/Supervised_Learning-Regresion_Lineal.md)
• 
> [**Codigo - Regresion Lineal**](../Code/Supervised_Learning-Regresion_Lineal.md)
• 
> [**Practica - Regresion Logistica**](Supervised_Learning-Regresion_Logistica.md)
---