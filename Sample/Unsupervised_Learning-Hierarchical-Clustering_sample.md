# Caso Práctico: Agrupamiento Jerárquico

# Caso Real: Taxonomía de Productos E-commerce

# Organización con Clustering Jerárquico

¿Cómo organizas un catálogo de 50,000 productos nuevos sin categorías previas? El agrupamiento
jerárquico conecta los artículos por similitud, creando una estructura de "padres e hijos" que permite
navegar desde lo general hasta lo específico.

**Guía de Negocio:** Haz clic en cada etapa para entender cómo
transformamos un inventario desordenado en una jerarquía lógica de navegación.

1

### Objetivo del Proyecto

Crear una estructura de navegación lógica (Categorías > Subcategorías)
para un catálogo masivo.

A diferencia de K-Means, aquí no queremos grupos aislados, sino entender la relación entre
ellos. Buscamos saber si "Zapatillas de Running" y "Zapatillas de Basket" pertenecen a un mismo
grupo "Calzado Deportivo" en un nivel superior.

Descubrimiento de jerarquías

Estructura Multilevel

Navegación intuitiva

2

### Variables de Similitud

Definimos qué hace que dos productos sean "parientes" cercanos.

Analizamos descripciones de texto, precio, material y departamento de origen. Usamos técnicas de
NLP para convertir palabras en números, permitiendo que el algoritmo mida la "distancia"
semántica entre un sofá y un sillón.

Similitud de Texto (TF-IDF)

Rangos de Precio

Especificaciones Técnicas

3

### El Proceso de Unión

El algoritmo comienza con cada producto solo y empieza a fusionar los
más parecidos.

Es un enfoque "Bottom-Up". Primero une un martillo con un mazo. Luego une ese grupo con los
destornilladores para formar "Herramientas". El proceso continúa hasta que todo el catálogo está
conectado en una sola raíz.

Fusión por cercanía

Método de Ward (Varianza)

Construcción de ramas

4

### El Dendrograma

Visualizamos el historial completo de agrupamiento en un diagrama de
árbol.

Este gráfico nos muestra a qué distancia se unió cada par de grupos. Si la línea vertical es muy
larga, significa que los grupos fusionados eran muy diferentes, lo que nos ayuda a identificar
dónde termina una categoría real.

Registro de fusiones

Identificación de niveles

Transparencia visual

5

### Corte de Granularidad

Decidimos en qué nivel del árbol cortar para obtener el número de
categorías deseado.

Si cortamos el árbol muy arriba, tendremos solo 5 departamentos grandes (ej. Hogar,
Electrónica). Si cortamos más abajo, tendremos 500 subcategorías muy específicas (ej. Lámparas
de Mesa LED). Esta flexibilidad es la mayor ventaja del algoritmo.

Ajuste de Profundidad

Definición de K flexible

Equilibrio de catálogo

6

### Interpretación

Analizamos el contenido de cada cluster para asignarle un nombre
comercial.

Al revisar un grupo, vemos que contiene "Cámaras", "Lentes" y "Trípodes". Lo nombramos
automáticamente como "Fotografía". Este paso valida que la inteligencia del algoritmo coincide
con la lógica del cliente final.

Naming de categorías

Validación de expertos

Refinamiento de catálogo

7

### Impacto en UX

El catálogo queda listo para ser navegado por el usuario final de
forma lógica.

Gracias a esta jerarquía, el buscador puede ofrecer filtros inteligentes. Si el usuario busca
"Herramientas", el sistema ya sabe que debe mostrar subcategorías de "Manuales" y "Eléctricas",
mejorando la conversión en un 18%.

Filtros inteligentes

Mejora en buscadores (SEO)

Automatización de carga

## El Orden Natural de los Datos

El Agrupamiento Jerárquico es la herramienta definitiva para la **Investigación de
Estructuras**. Permite que el negocio no solo agrupe, sino que comprenda la anatomía de
su oferta, descubriendo nichos y familias de productos que antes estaban ocultos.

Taxonómico
Sin K
Predefinido
Descriptivo

> [**Algoritmos - Agrupamiento Jerárquico**](../Algoritmos/Unsupervised_Learning-Hierarchical-Clustering.md)
• 
> [**Codigo - Agrupamiento Jerárquico**](../Code/Unsupervised_Learning-Hierarchical-Clustering.md)
• 
> [**Practica - Q-Learning**](Reinforcement_Learning-Q-Learning.md)
---