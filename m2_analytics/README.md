# Módulo 2. Data Analytics: Procesos y Técnicas

Aplicar procesos y técnicas de análisis de datos mediante Python: preparación, exploración, visualización y modelos de aprendizaje supervisado y no supervisado. Los ejercicios disponibles cubren las herramientas y métodos que se enumeran a continuación.

## Tareas

- [3.1.1 Funciones, Argumentos y Expresiones Lambda v2](3_tareas/notebooks/3.1.1%20Funciones%2C%20Argumentos%20y%20Expresiones%20Lambda%20v2.ipynb): definición de funciones, argumentos y expresiones lambda.
- [3.1.2 Manejo de archivos, CSV y Manejo de Errores & Excepciones v2](3_tareas/notebooks/3.1.2%20Manejo%20de%20archivos%2C%20CSV%20y%20Manejo%20de%20Errores%20%26%20Excepciones%20v2.ipynb): lectura de archivos CSV y tratamiento de excepciones.
- [3.1.3 Programacion Orientada a Objetos (POO) v2](3_tareas/notebooks/3.1.3%20Programacion%20Orientada%20a%20Objetos%20%28POO%29%20v2.ipynb): clases y programación orientada a objetos.
- [3.2.1 Matplotlib](3_tareas/notebooks/3.2.1%20Matplotlib.ipynb): gráficos con Matplotlib.
- [3.2.2 Numpy](3_tareas/notebooks/3.2.2%20Numpy.ipynb): operaciones con arreglos NumPy.
- [3.3.1 Pandas](3_tareas/notebooks/3.3.1%20Pandas.ipynb): manipulación de tablas con pandas.
- [3.3.2 Numpy 2](3_tareas/notebooks/3.3.2%20Numpy%202.ipynb): segunda práctica de NumPy.
- [4.2. IA-RegresionLineal](3_tareas/notebooks/4.2.%20IA-RegresionLineal.ipynb): introducción a regresión lineal.
- [4.3. IA-RegresionLineal_2](3_tareas/notebooks/4.3.%20IA-RegresionLineal_2.ipynb): segunda práctica de regresión lineal.
- [5.1. IA-Clasificacion_Naives_Bayes](3_tareas/notebooks/5.1.%20IA-Clasificacion_Naives_Bayes.ipynb): clasificación con Naive Bayes.
- [5.3. IA-Clasificación_knn](3_tareas/notebooks/5.3.%20IA-Clasificaci%C3%B3n_knn.ipynb): clasificación con vecinos más cercanos.
- [5.4. IA-Clasificacion_ArbolesDecision](3_tareas/notebooks/5.4.%20IA-Clasificacion_ArbolesDecision.ipynb): clasificación con árboles de decisión.
- [6.1. IA-AprendizajeNoSupervisado_1](3_tareas/notebooks/6.1.%20IA-AprendizajeNoSupervisado_1.ipynb): reducción de dimensionalidad mediante PCA.
- [6.2. IA-AprendizajeNoSupervisado_2](3_tareas/notebooks/6.2.%20IA-AprendizajeNoSupervisado_2.ipynb): agrupamiento no supervisado.
- [6.3. IA-AprendizajeNoSupervisado_3](3_tareas/notebooks/6.3.%20IA-AprendizajeNoSupervisado_3.ipynb): agrupamiento jerárquico.

Los datos de los ejercicios se describen en [datasets/README.md](3_tareas/datasets/README.md).

## Proyecto integrador

Agrupamiento de perfiles musicales de Spotify con K-Means y DBSCAN. Consulta la [descripción del proyecto](4_proyecto/README.md) y la [guía de datos originales y partes](4_proyecto/data/raw/README.md).

- [01_adquisicion_dataset](4_proyecto/notebooks/01_adquisicion_dataset.ipynb): adquisición de datos.
- [02_preprocesamiento](4_proyecto/notebooks/02_preprocesamiento.ipynb): preprocesamiento.
- [03_eda](4_proyecto/notebooks/03_eda.ipynb): análisis exploratorio.
- [04_muestreo_escalado](4_proyecto/notebooks/04_muestreo_escalado.ipynb): muestreo y escalado.
- [05_K-Means](4_proyecto/notebooks/05_K-Means.ipynb): agrupamiento K-Means.
- [06_DBSCAN](4_proyecto/notebooks/06_DBSCAN.ipynb): agrupamiento DBSCAN.

Informe: [PDF](4_proyecto/docs/main.pdf) y [fuente LaTeX](4_proyecto/docs/main.tex).

## Recursos

La carpeta `2_recursos/` no contiene archivos actualmente. Los materiales asociados a ejercicios se enlazan en las tareas.

## Ejecución

Usa [requirements de tareas](3_tareas/requirements.txt) o [requirements del proyecto](4_proyecto/requirements.txt) en entornos separados, según el trabajo (véase la preparación en el índice del diplomado). Ejecuta las tareas desde `3_tareas/notebooks/` y el proyecto desde `4_proyecto/notebooks/`; las rutas `../datasets/` y `../data/` dependen de ello. Sigue el orden 01–06 para el proyecto.

El preprocesamiento puede leer las partes de Spotify; el notebook 01 todavía apunta al CSV completo. `05_K-Means.ipynb` lee `spotify_features_only.csv`, que no está disponible: hay que proporcionar ese archivo o adaptar su entrada antes de ejecutarlo. No se garantiza la ejecución completa con los archivos actuales.

## Apuntes

[Notas del módulo](5_notas/NOTAS.md) · [Índice del diplomado](../README.md)
