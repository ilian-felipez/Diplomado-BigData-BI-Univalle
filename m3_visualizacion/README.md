# Módulo 3. Visualización de Datos y Data Discovery

Analizar, explorar y comunicar información mediante visualizaciones efectivas, herramientas de BI y técnicas de Data Discovery para apoyar decisiones estratégicas. El plan incluye percepción visual, dashboards, indicadores y narrativa con datos.

## Tareas

- [Tarea 1](3_tareas/1/1.pbix): archivo de trabajo de Power BI.
- [Tarea 2: gráfico honesto](3_tareas/2/notebook.ipynb): representación del presupuesto de marketing por canal.
- [Tarea 2: gráfico engañoso](3_tareas/2/notebook%20copy.ipynb): ejemplo de decisiones visuales que alteran la percepción.
- [Tarea 2: versión final](3_tareas/2/notebook%20final.ipynb): gráficos comparativos del presupuesto por canal y trimestre.

## Proyecto integrador

Dashboard integrado NOC/SOC para explorar telemetría de red e identificar patrones y anomalías en un entorno controlado.

- [Dashboard Power BI](4_proyecto/UNIVALLE_Postgrado_BigData_Felipez.pbix): informe interactivo.
- [Informe PDF](4_proyecto/LaTeX/main.pdf): documentación técnica del dashboard.
- [Fuente LaTeX](4_proyecto/LaTeX/main.tex): fuente del informe.
- [Datos y actualización](4_proyecto/README.md): instrucciones para las partes de Dataset_completo y su carga.

## Recursos

- [Clase 1](2_recursos/Clase%201.pdf).
- [Plan de asignatura - Clase 1](2_recursos/Plan%20de%20asignatura%20-%20Clase%201.pdf).
- [Unidad 1](2_recursos/Unidad%201.pdf).
- [Unidad 2 - P1](2_recursos/Unidad%202%20-%20P1.pdf).
- [Unidad 4](2_recursos/Unidad%204.pdf).

## Ejecución

Abre los `.pbix` con Power BI Desktop en Windows. Para actualizar el proyecto, usa **Obtener datos > Carpeta** (Get Data > Folder), selecciona `4_proyecto/` y filtra `Dataset_completo.part-*.csv` antes de combinar; sigue la guía de datos enlazada arriba para sustituir el origen anterior y verificar columnas y filas.

Los notebooks de la tarea 2 generan sus datos en el código y usan pandas, NumPy y Matplotlib; no hay `requirements.txt` propio. Ejecútalos desde `3_tareas/2/` con un kernel que tenga esas bibliotecas. No se ha validado aquí la ejecución ni la actualización de los PBIX.

## Apuntes

[Notas del módulo](5_notas/NOTAS.md) · [Índice del diplomado](../README.md)
