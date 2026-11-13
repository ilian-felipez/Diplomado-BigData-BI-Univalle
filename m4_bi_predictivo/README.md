# Módulo 4. Business Intelligence y Modelos Predictivos

Transformar datos en información de negocio mediante ETL, almacenes de datos, análisis OLAP y modelos descriptivos y predictivos. Las prácticas conectan indicadores, estimación de compra y decisiones comerciales.

## Tareas

- [A1: notebook](3_tareas/A1/Ejercicio_A1_FMNQ.ipynb): introducción al análisis de negocio con BI.
- [A1: presentación](3_tareas/A1/Ejercicio_A1_FMNQ.pptx): presentación de la actividad.
- [A2](3_tareas/A2/Clase2_ETL_DW_OLAP.ipynb): extracción, transformación, carga y análisis OLAP.
- [A3](3_tareas/A3/Clase3_Modelos_Descriptivos_Analitica_Exploratoria.ipynb): modelos descriptivos, indicadores y análisis exploratorio.
- [A4](3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb): clasificación de probabilidad de compra y regresión del importe.

## Proyecto integrador

Análisis y predicción de fuga de clientes (*churn*) de Telco para orientar acciones de retención: limpieza, exploración, comparación de clasificadores e interpretación de variables.

- [Descripción](4_proyecto/README.md): contexto y organización del proyecto.
- [Notebook Telco](4_proyecto/notebooks/Telco_Customer_Churn_Analysis.ipynb): flujo de análisis y modelado.
- [Presentación PDF](4_proyecto/report_latex/main.pdf): presentación del proyecto.
- [Fuente LaTeX](4_proyecto/report_latex/main.tex): presentación Beamer.
- [Datos originales](4_proyecto/data/raw/): carpeta con los datos de entrada.
- [Consigna](4_proyecto/documents/INSTRUCCIONES%20DEL%20PROYECTO%20FINAL%20-%20M%C3%93DULO%20IV.pdf): requisitos del proyecto final.

## Recursos

- [Clase 1 - Fundamentos y Evolución de Business Intelligence](2_recursos/Clase%201%20-%20Fundamentos%20y%20Evoluci%C3%B3n%20de%20Business%20Intelligence) (carpeta de materiales).
- [Clase 2 - ETL, Datawarehouse y OLAP](2_recursos/Clase%202%20-%20ETL%2C%20Datawarehouse%20y%20OLAP) (carpeta de materiales).

## Ejecución

Usa [requirements de tareas](3_tareas/requirements.txt) para A1–A4 y [requirements del proyecto](4_proyecto/requirements.txt) para Telco. El material de la clase 1 tiene [dependencias propias](2_recursos/Clase%201%20-%20Fundamentos%20y%20Evoluci%C3%B3n%20de%20Business%20Intelligence/requirements.txt). Consulta la preparación de entornos en el índice del diplomado.

Ejecuta cada actividad desde su carpeta `3_tareas/A1/` a `A4/`. A2 regenera `ecommerce_datawarehouse.db`; esa base no está versionada. Revisa las celdas de creación y limpieza antes de ejecutar sobre una base local existente. Ejecuta Telco desde `4_proyecto/notebooks/` para resolver `../data/raw/`; su cargador también ofrece alternativas de carga y descarga si no encuentra el CSV. La ejecución completa no se ha validado.

## Apuntes

[Notas del módulo](5_notas/NOTAS.md) · [Índice del diplomado](../README.md)
