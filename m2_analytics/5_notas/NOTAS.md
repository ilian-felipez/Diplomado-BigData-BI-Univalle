# Módulo 2: Analytics y aprendizaje automático

Notas de estudio del diplomado, Univalle, gestión 2026.
La ruta sigue los cuadernos disponibles y el proyecto de canciones de Spotify.
La numeración de recursos no se interpreta como un calendario de clases confirmado.

## 1. Mapa del módulo

- 3.1.1: definición de funciones, argumentos y expresiones [lambda](../3_tareas/notebooks/3.1.1%20Funciones%2C%20Argumentos%20y%20Expresiones%20Lambda%20v2.ipynb).
- 3.1.2: lectura de archivos, CSV y manejo de [excepciones](../3_tareas/notebooks/3.1.2%20Manejo%20de%20archivos%2C%20CSV%20y%20Manejo%20de%20Errores%20%26%20Excepciones%20v2.ipynb).
- 3.1.3: clases, objetos, métodos y módulos en [POO](../3_tareas/notebooks/3.1.3%20Programacion%20Orientada%20a%20Objetos%20%28POO%29%20v2.ipynb).
- 3.2.1: figuras, ejes y tipos de gráficos en [Matplotlib](../3_tareas/notebooks/3.2.1%20Matplotlib.ipynb).
- 3.2.2: creación de arreglos, operaciones y álgebra con [NumPy](../3_tareas/notebooks/3.2.2%20Numpy.ipynb).
- 3.3.1: Series, DataFrame, carga y agrupación con [pandas](../3_tareas/notebooks/3.3.1%20Pandas.ipynb).
- 3.3.2: arreglos, operaciones, álgebra y faltantes con [NumPy](../3_tareas/notebooks/3.3.2%20Numpy%202.ipynb).
- 4.2: regresión simple y múltiple aplicada a [publicidad](../3_tareas/notebooks/4.2.%20IA-RegresionLineal.ipynb).
- 4.3: precios de viviendas, partición y [regresión polinomial](../3_tareas/notebooks/4.3.%20IA-RegresionLineal_2.ipynb).
- 5.1: clasificación probabilística, Iris y spam con [Naive Bayes](../3_tareas/notebooks/5.1.%20IA-Clasificacion_Naives_Bayes.ipynb).
- 5.3: distancias, vecinos y validación cruzada con [KNN](../3_tareas/notebooks/5.3.%20IA-Clasificaci%C3%B3n_knn.ipynb).
- 5.4: pureza, entropía, sobreajuste y [árboles de decisión](../3_tareas/notebooks/5.4.%20IA-Clasificacion_ArbolesDecision.ipynb).
- 6.1: reducción de dimensionalidad mediante [PCA](../3_tareas/notebooks/6.1.%20IA-AprendizajeNoSupervisado_1.ipynb).
- 6.2: K-Means, escalado y método del codo en [dígitos y vinos](../3_tareas/notebooks/6.2.%20IA-AprendizajeNoSupervisado_2.ipynb).
- 6.3: jerarquías, dendrogramas, DBSCAN y [métricas externas](../3_tareas/notebooks/6.3.%20IA-AprendizajeNoSupervisado_3.ipynb).
- Proyecto: limpieza y selección de [variables acústicas](../4_proyecto/notebooks/02_preprocesamiento.ipynb).
- Proyecto: [muestreo y escalado](../4_proyecto/notebooks/04_muestreo_escalado.ipynb), [K-Means](../4_proyecto/notebooks/05_K-Means.ipynb) y [DBSCAN](../4_proyecto/notebooks/06_DBSCAN.ipynb).

## 2. Conceptos clave

### Funciones, arreglos y tablas

Una función encapsula una operación reutilizable con entradas y un resultado.
Un arreglo NumPy facilita operaciones numéricas; pandas añade columnas e índices con significado.
Separar preparación y cálculo ayuda a reproducir el análisis y localizar errores.
Fuentes: [funciones](../3_tareas/notebooks/3.1.1%20Funciones%2C%20Argumentos%20y%20Expresiones%20Lambda%20v2.ipynb), [NumPy](../3_tareas/notebooks/3.3.2%20Numpy%202.ipynb) y [pandas](../3_tareas/notebooks/3.3.1%20Pandas.ipynb).

### Aprendizaje supervisado

Se aprende una relación entre atributos $X$ y una respuesta conocida $y$.
Regresión estima una cantidad, como ventas o precio de vivienda.
Clasificación asigna una categoría, como especie o correo basura.
La distinción determina los modelos y las métricas que corresponde usar.
Fuentes: [publicidad](../3_tareas/notebooks/4.2.%20IA-RegresionLineal.ipynb), [viviendas](../3_tareas/notebooks/4.3.%20IA-RegresionLineal_2.ipynb) y [Naive Bayes](../3_tareas/notebooks/5.1.%20IA-Clasificacion_Naives_Bayes.ipynb).

### Regresión lineal y polinomial

La regresión lineal estima una combinación de atributos para explicar la respuesta.
En publicidad se usan `TV`, `Radio` y `Newspaper` para modelar `Sales`.
Agregar potencias permite ajustar curvas, pero un grado alto puede sobreajustar.
Un buen ajuste sobre entrenamiento no garantiza buenas predicciones en datos nuevos.
Fuentes: [regresión lineal](../3_tareas/notebooks/4.2.%20IA-RegresionLineal.ipynb) y [experimento polinomial](../3_tareas/notebooks/4.3.%20IA-RegresionLineal_2.ipynb).

### Naive Bayes, KNN y árboles

Naive Bayes combina probabilidades y una hipótesis de independencia condicional.
KNN decide según las etiquetas de vecinos cercanos; por eso la escala de atributos importa.
Un árbol divide los datos mediante reglas que buscan aumentar la pureza de los grupos.
Son enfoques distintos para una misma tarea de clasificación y deben evaluarse con datos separados.
Fuentes: [Bayes](../3_tareas/notebooks/5.1.%20IA-Clasificacion_Naives_Bayes.ipynb), [KNN](../3_tareas/notebooks/5.3.%20IA-Clasificaci%C3%B3n_knn.ipynb) y [árboles](../3_tareas/notebooks/5.4.%20IA-Clasificacion_ArbolesDecision.ipynb).

### Validación y sobreajuste

La partición entrenamiento/prueba separa aprendizaje y evaluación.
La validación cruzada repite particiones para comparar configuraciones dentro del entrenamiento.
Elegir complejidad solo por el resultado sobre datos usados para ajustar favorece el sobreajuste.
Fuentes: [viviendas](../3_tareas/notebooks/4.3.%20IA-RegresionLineal_2.ipynb) y selección de vecinos con [validación cruzada](../3_tareas/notebooks/5.3.%20IA-Clasificaci%C3%B3n_knn.ipynb).

### Aprendizaje no supervisado

El agrupamiento busca estructura sin una etiqueta objetivo de referencia.
En Spotify se describen perfiles mediante atributos como energía, valencia y bailabilidad.
Los nombres asignados a grupos son interpretaciones de sus perfiles medios.
No son géneros musicales certificados ni etiquetas verdaderas del dataset.
Fuente: interpretación de perfiles del [proyecto K-Means](../4_proyecto/notebooks/05_K-Means.ipynb).

### Escalado y PCA

Estandarizar evita que una variable de gran magnitud domine las distancias.
PCA representa variabilidad en un número menor de componentes.
En K-Means se emplea PCA para visualizar; el cuaderno DBSCAN también lo usa antes de agrupar.
Esta diferencia modifica el espacio de trabajo y limita comparaciones directas de métricas.
Fuentes: [muestreo y escalado](../4_proyecto/notebooks/04_muestreo_escalado.ipynb), [PCA](../3_tareas/notebooks/6.1.%20IA-AprendizajeNoSupervisado_1.ipynb), [K-Means](../4_proyecto/notebooks/05_K-Means.ipynb) y [DBSCAN](../4_proyecto/notebooks/06_DBSCAN.ipynb).

### K-Means y DBSCAN

K-Means asigna observaciones a $k$ centroides y minimiza dispersión interna.
DBSCAN forma grupos por densidad con `eps` y `min_samples`, e identifica ruido con `-1`.
El primer método requiere elegir $k$; el segundo exige justificar vecindad y densidad.
Fuentes: experimentos del [cuaderno K-Means](../4_proyecto/notebooks/05_K-Means.ipynb) y [cuaderno DBSCAN](../4_proyecto/notebooks/06_DBSCAN.ipynb).

### Agrupamiento jerárquico y comparación externa

El método aglomerativo comienza con observaciones separadas y fusiona grupos cercanos.
El enlace único usa la menor distancia entre miembros; el completo usa la mayor.
Un dendrograma representa la secuencia de fusiones y permite explorar cortes de la jerarquía.
NMI compara información compartida entre dos particiones; ARS compara asignaciones de pares ajustando por azar.
Estas métricas externas requieren una partición de referencia, a diferencia de Silhouette.
Los números asignados a clusters no tienen que coincidir con los códigos de las clases.
Fuente: [agrupamiento jerárquico y comparación de algoritmos](../3_tareas/notebooks/6.3.%20IA-AprendizajeNoSupervisado_3.ipynb).

## 3. Fórmulas y métricas

### Regresión y error

La predicción lineal es $\hat y=\beta_0+\sum_{j=1}^{p}\beta_jx_j$.
El error residual es $e_i=y_i-\hat y_i$ y la suma de cuadrados es $SSE=\sum_i e_i^2$.
Mínimos cuadrados selecciona coeficientes para reducir esa suma.
El coeficiente de determinación es $R^2=1-\frac{\sum_i(y_i-\hat y_i)^2}{\sum_i(y_i-\bar y)^2}$.
Un $R^2$ alto sobre entrenamiento debe contrastarse con datos de prueba.
Fuentes: [mínimos cuadrados en publicidad](../3_tareas/notebooks/4.2.%20IA-RegresionLineal.ipynb) y [evaluación de viviendas](../3_tareas/notebooks/4.3.%20IA-RegresionLineal_2.ipynb).

### Bayes y pureza de un árbol

Bayes actualiza una probabilidad: $P(C\mid X)=\frac{P(X\mid C)P(C)}{P(X)}$.
Naive Bayes aproxima $P(X\mid C)$ por el producto de probabilidades de atributos dado $C$.
La entropía de un nodo es $H=-\sum_c p_c\log_2p_c$, con $0\log_2 0=0$.
La ganancia de información resta a la entropía inicial la entropía ponderada tras dividir.
Estas expresiones explican por qué los algoritmos eligen una clase o una división.
Fuentes: [matemáticas de Naive Bayes](../3_tareas/notebooks/5.1.%20IA-Clasificacion_Naives_Bayes.ipynb) y [pureza y entropía](../3_tareas/notebooks/5.4.%20IA-Clasificacion_ArbolesDecision.ipynb).

### Clasificación

Para una clase positiva: VP son positivos correctos y VN negativos correctos.
FP son falsas alarmas y FN positivos que el modelo no detectó.

$Accuracy=\frac{VP+VN}{VP+VN+FP+FN}$.

$Precision=\frac{VP}{VP+FP}$; $Recall=\frac{VP}{VP+FN}$.

$F_1=2\frac{Precision\cdot Recall}{Precision+Recall}$.

La exactitud global no revela por sí sola qué clase se está confundiendo.
En multiclase se debe indicar el promedio usado, como macro o micro.
Fuentes: [métricas de clasificadores](../3_tareas/notebooks/5.1.%20IA-Clasificacion_Naives_Bayes.ipynb) y [evaluación de árboles](../3_tareas/notebooks/5.4.%20IA-Clasificacion_ArbolesDecision.ipynb).

### Distancias, escalado y agrupamiento

Distancia euclídea: $d(x,z)=\sqrt{\sum_j(x_j-z_j)^2}$.
Estandarización: $z_j=(x_j-\mu_j)/\sigma_j$ para atributos de desviación no nula.
Inercia de K-Means: $J=\sum_{k=1}^{K}\sum_{x_i\in C_k}\lVert x_i-\mu_k\rVert^2$.
Silhouette: $s(i)=\frac{b(i)-a(i)}{\max(a(i),b(i))}$.
Aquí $a(i)$ mide distancia media dentro del grupo y $b(i)$ al grupo alternativo más cercano.
Una Silhouette mayor favorece separación; Davies-Bouldin menor favorece grupos compactos y separados.
Calinski-Harabasz mayor favorece separación entre grupos respecto de la dispersión interna.
Fuentes: [distancias KNN](../3_tareas/notebooks/5.3.%20IA-Clasificaci%C3%B3n_knn.ipynb), [escalado](../4_proyecto/notebooks/04_muestreo_escalado.ipynb) y [evaluación del proyecto](../4_proyecto/notebooks/05_K-Means.ipynb).

### Ejemplo numérico ilustrativo

Aplicando las métricas de [clasificación](../3_tareas/notebooks/5.1.%20IA-Clasificacion_Naives_Bayes.ipynb), supongamos VP=30, FP=10, FN=20 y VN=40.
La exactitud es $(30+40)/100=70\%$ y la precisión es $30/40=75\%$.
El recall es $30/50=60\%$; por tanto $F_1\approx0,667$.
El modelo deja escapar 20 de 50 positivos aunque su exactitud sea del 70%.
Son cifras de práctica, no resultados de Iris ni de detección de spam.

## 4. Código esencial

Fragmentos adaptados de tareas; las variables deben prepararse en el cuaderno citado.
No se ejecutan descargas, entrenamientos ni escrituras de datasets desde estas notas.

En el cuaderno de [pandas](../3_tareas/notebooks/3.3.1%20Pandas.ipynb), `df` es el dataset COVID ya cargado.

```python
import pandas as pd

cb = df.groupby('region')
cb2 = df[df['recovered'] > 0].groupby('region')
```

`groupby` crea una agrupación; para obtener un resumen se requiere una agregación.
El segundo objeto agrupa solo las filas que cumplen el filtro.

En [publicidad](../3_tareas/notebooks/4.2.%20IA-RegresionLineal.ipynb), `data` contiene las columnas de Advertising.
Este fragmento reproduce el ajuste múltiple, no una evaluación independiente.

```python
from sklearn.linear_model import LinearRegression

atributos_cols = ['TV', 'Radio', 'Newspaper']
X = data[atributos_cols]
y = data.Sales
lm = LinearRegression()
lm.fit(X, y)
```

En el [proyecto K-Means](../4_proyecto/notebooks/05_K-Means.ipynb), `df_model` contiene solo atributos numéricos limpios.
`k=3` es una elección ilustrativa que debe contrastarse con la búsqueda de $k$ del cuaderno.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

X_scaled = StandardScaler().fit_transform(df_model)
k = 3
labels = KMeans(n_clusters=k, random_state=42, n_init=10).fit_predict(X_scaled)
```

No se debe incluir una etiqueta de cluster previa entre los atributos de un nuevo ajuste.
El proyecto también elimina faltantes y duplicados antes de estandarizar.

## 5. Errores comunes

- Usar exactitud de clasificación para evaluar un problema de regresión.
- Confundir precisión de la clase positiva con exactitud global.
- Escalar todo el dataset antes de separar entrenamiento y prueba en un experimento supervisado.
- Elegir un polinomio por ajuste visual sin evaluar generalización.
- Usar KNN o clustering con variables de escalas muy distintas sin revisarlas.
- Comparar Silhouette entre espacios o muestras diferentes como si fueran equivalentes.
- Contar `-1` de DBSCAN como un cluster ordinario al informar el número de grupos.
- Convertir nombres interpretativos de clusters en categorías verdaderas del problema.

Fuentes para revisar estas precauciones: [viviendas](../3_tareas/notebooks/4.3.%20IA-RegresionLineal_2.ipynb), [KNN](../3_tareas/notebooks/5.3.%20IA-Clasificaci%C3%B3n_knn.ipynb),
[métricas de clasificación](../3_tareas/notebooks/5.1.%20IA-Clasificacion_Naives_Bayes.ipynb) y [experimentos de clustering](../4_proyecto/notebooks/05_K-Means.ipynb).

## 6. Preguntas de repaso

1. ¿Cómo cambia $y$ entre regresión y clasificación?
2. ¿Qué representa cada coeficiente del modelo de publicidad?
3. ¿Por qué un polinomio de grado 15 puede generalizar peor?
4. ¿Cuándo resulta costoso un falso negativo y qué métrica lo refleja?
5. ¿Qué supone Naive Bayes sobre los atributos dado una clase?
6. ¿Cómo afectan las escalas a KNN y K-Means?
7. ¿Qué diferencia existe entre elegir $k$ y elegir `eps`?
8. ¿Qué debes igualar antes de comparar dos resultados de Silhouette?
