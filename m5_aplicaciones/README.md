# Módulo 5. Aplicaciones de Big Data en Entornos Digitales

Aplicar analítica a problemas de entornos digitales: comportamiento de usuarios, procesos, clientes, canales y campañas. Los casos disponibles llevan desde la exploración de datos hasta recomendaciones de negocio y procesamiento con DuckDB y Spark.

## Tareas

- [Análisis ICUPE](3_tareas/1/main.ipynb): exploración y visualización del dataset Analisis_ICUPE_Enfoque1.
- [Caso 1](3_tareas/caso1/analizar_datos.py): análisis del embudo digital; la carpeta incluye otros scripts de exploración.
- [Caso 1: script inicial](3_tareas/caso1/main.py): lectura y revisión del embudo digital.
- [Caso 2](3_tareas/caso2/main.py): exploración del registro de eventos BPI 2017.
- [Caso 2: consigna](3_tareas/caso2/APBIG%20Clase%203%20Casos%20de%20estudio%20%E2%80%93%20Parte%202.pdf): trayectorias, patrones temporales y fricción del proceso.
- [Caso 3](3_tareas/caso3/main.ipynb): análisis de clientes, canales, gasto y respuesta a campañas.
- [Caso 3: consigna](3_tareas/caso3/APBIG%20Clase%203%20Casos%20de%20estudio%20%E2%80%93%20Parte%203.pdf): ajuste de estrategia comercial basado en evidencia.
- [Caso 3: presentación](3_tareas/caso3/presentaic%C3%B3n.pdf): presentación del análisis comercial.
- [Análisis comercial en la raíz de tareas](3_tareas/main.ipynb): otra copia del análisis de marketing con rutas relativas propias.
- [Caso 4](3_tareas/caso4/main.ipynb): evolución de ingresos físicos y digitales de la industria musical estadounidense.
- [Clase 5](3_tareas/clase5/Curso3_Big_data_visualizations.ipynb): consultas, comparación de pandas y DuckDB y práctica con Spark.

## Proyecto integrador

La carpeta `4_proyecto/` está vacía: no hay notebook, informe ni datos de un proyecto integrador disponibles. Los trabajos actuales se encuentran en `3_tareas/`.

## Recursos

La carpeta `2_recursos/` no contiene archivos actualmente. Los materiales asociados a ejercicios se enlazan en las tareas.

Material adicional de clase 5: [casos de estudio](3_tareas/clase5/APBIG%20Clase%205%20Casos%20de%20estudio.pdf) y [taxonomía de herramientas y plataformas](3_tareas/clase5/APBIG%20Clase%205%20Taxonom%C3%ADa%20de%20herramientas%20y%20plataformas%20de%20anal%C3%ADtica%20-%20Big%20Data.xlsx).

## Ejecución

El [requirements de tareas](3_tareas/requirements.txt) incluye pandas y NumPy, pero no todas las dependencias: varios notebooks importan Matplotlib y Seaborn. Revisa los imports antes de preparar el entorno; no hay una instalación completa validada.

- ICUPE: usa `3_tareas/1/` como directorio de trabajo; busca `data/Analisis_ICUPE_Enfoque1.csv`.
- Caso 1: revisa las rutas de cada script. `main.py` apunta a `2/digital_funnel_clean_ES.csv`, distinta de los datos disponibles en `caso1/data/raw/`; requiere adaptar la entrada.
- Caso 2: ejecuta desde `3_tareas/`, pues el script lee `caso2/bpi_2017_cleaned v2.csv`.
- Caso 3: ejecuta desde `3_tareas/caso3/` para resolver `data/raw/`, `data/processed/` y `output/`. La copia `3_tareas/main.ipynb` usa esas mismas rutas respecto de su directorio de trabajo; comprueba la ubicación de los datos antes de usarla.
- Caso 4: ejecuta desde `3_tareas/caso4/`; lee `data/raw/US_Music_Revenues.csv`.
- Clase 5: el notebook está preparado para Google Colab, utiliza `/content/nyc_taxi_data`, instala DuckDB y PySpark y descarga datos. Requiere conexión y ajustes de rutas para usarlo localmente.

## Apuntes

[Notas del módulo](5_notas/NOTAS.md) · [Índice del diplomado](../README.md)
