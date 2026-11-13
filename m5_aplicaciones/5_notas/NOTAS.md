# Módulo 5: Aplicaciones de Big Data en entornos digitales

Notas de estudio del diplomado, Univalle, gestión 2026.
El módulo conecta evidencia de usuarios, procesos y mercados con acciones de negocio.
El mapa distingue casos efectivamente trabajados y consignas de diseño de ecosistemas.

## 1. Mapa del módulo

- Análisis de conversaciones: temas, tono y severidad por reglas; [script de análisis cualitativo](../3_tareas/1/main.py).
- Caso 1: embudo web, rebote, dispositivos y fricciones previas a la compra; [script](../3_tareas/caso1/main.py).
- Caso 2: rutas, tiempos, retrabajo, segmentos y coordinación; [consigna de procesos](../3_tareas/caso2/APBIG%20Clase%203%20Casos%20de%20estudio%20%E2%80%93%20Parte%202.pdf).
- Caso 2: eventos y duración por tipo de solicitud y aceptación; [implementación](../3_tareas/caso2/main.py).
- Caso 3: calidad, canales, campañas y perfiles de clientes; [consigna comercial](../3_tareas/caso3/APBIG%20Clase%203%20Casos%20de%20estudio%20%E2%80%93%20Parte%203.pdf).
- Caso 3: preparación, respuesta y segmentación gasto/frecuencia; [notebook de marketing](../3_tareas/caso3/main.ipynb).
- Caso 4: evolución de ingresos físicos y digitales de música; [notebook](../3_tareas/caso4/main.ipynb).
- Clase 5: ecosistemas ELT para retail, telecomunicaciones y salud; [casos de diseño](../3_tareas/clase5/APBIG%20Clase%205%20Casos%20de%20estudio.pdf).
- Clase 5: pandas, DuckDB, SQL sobre Parquet y puente a Spark; [práctica de taxis](../3_tareas/clase5/Curso3_Big_data_visualizations.ipynb).

## 2. Conceptos clave

### Del comentario a una señal de fricción

Un texto puede agruparse por tema, tono o severidad para apoyar un diagnóstico.
El script clasifica severidad mediante palabras críticas y palabras de apariencia estética.
La etiqueta resultante depende de esa regla y necesita revisión del contexto.
Sirve para priorizar lectura; no equivale a una clasificación validada del estado del usuario.
Fuente: `clasificar_severidad` del [análisis de conversaciones](../3_tareas/1/main.py).

### Embudo y abandono

El embudo ordena etapas como ver productos, agregar al carrito, iniciar checkout y comprar.
Comparar etapas ayuda a localizar dónde se pierde continuidad.
La pérdida relativa debe acompañarse del número de sesiones afectadas.
La práctica también segmenta por dispositivo para detectar comportamientos distintos.
Fuente: [análisis del caso 1](../3_tareas/caso1/main.py).

### Evento, caso y trayectoria

Un evento registra una actividad; un caso reúne eventos del mismo proceso.
La trayectoria reconstruye su secuencia y puede revelar variantes, repeticiones o demoras.
Para analizar tiempo hay que ordenar y convertir las marcas temporales.
La granularidad importa: cien eventos no representan necesariamente cien solicitudes.
Fuentes: [consigna del caso 2](../3_tareas/caso2/APBIG%20Clase%203%20Casos%20de%20estudio%20%E2%80%93%20Parte%202.pdf) y [script de segmentación](../3_tareas/caso2/main.py).

### Fricción y segmentación de procesos

El caso compara objetivos de préstamo, tipos de solicitud y aceptación.
Usa cantidad de eventos y duración para describir complejidad y posible fricción.
Tener muchos eventos no prueba por sí solo que todo el proceso sea ineficiente.
La consigna pide interpretar retrabajo, interrupciones y coordinación, además de contar.
Fuentes: [caso 2](../3_tareas/caso2/APBIG%20Clase%203%20Casos%20de%20estudio%20%E2%80%93%20Parte%202.pdf) e [implementación](../3_tareas/caso2/main.py).

### Cliente, canal y campaña

El caso comercial compara compras web, catálogo y tienda con perfiles y respuesta.
Una campaña eficaz para un segmento puede rendir poco en otro.
El notebook imputa ingresos faltantes con mediana y calcula gasto por categorías.
Cada transformación debe conservar el significado de negocio de las variables.
Fuentes: [consigna del caso 3](../3_tareas/caso3/APBIG%20Clase%203%20Casos%20de%20estudio%20%E2%80%93%20Parte%203.pdf) y [análisis de marketing](../3_tareas/caso3/main.ipynb).

### Segmentación por gasto y frecuencia

El notebook cruza dos medianas para construir cuatro perfiles.
Premium combina gasto y frecuencia superiores a sus medianas respectivas.
Los otros grupos separan alto gasto con baja frecuencia, el caso inverso y ambos bajos.
Es una tipología descriptiva dependiente de la muestra, no un modelo de valor de vida.
Fuente: `condiciones` y `etiquetas` del [notebook comercial](../3_tareas/caso3/main.ipynb).

### Composición y evolución temporal

El caso musical limpia importes monetarios y compara ingresos físicos y digitales.
El área apilada muestra composición y evolución del total a través del tiempo.
Una anotación histórica aporta contexto, pero no demuestra por sí sola una causa del cambio.
Fuente: [transformación de la industria musical](../3_tareas/caso4/main.ipynb).

### Ecosistema analítico y escala

Los casos de diseño integran fuentes operativas, transformación y consumo analítico mediante ELT.
La práctica de taxis muestra un motor SQL local, DuckDB, consultando archivos Parquet.
Spark introduce procesamiento distribuido cuando el problema supera una sola máquina.
La herramienta debe elegirse por volumen, memoria, consulta y necesidad de integración.
Fuentes: [diseño de ecosistema](../3_tareas/clase5/APBIG%20Clase%205%20Casos%20de%20estudio.pdf) y [práctica de taxis](../3_tareas/clase5/Curso3_Big_data_visualizations.ipynb).

## 3. Fórmulas y métricas

### Embudo

$Conversion=\frac{SesionesConCompra}{TotalSesiones}\times100$.
$Abandono_{k\to k+1}=\left(1-\frac{N_{k+1}}{N_k}\right)\times100$, con $N_k>0$.
La tasa de rebote se calcula como la proporción de filas con `Indicador_Rebote = 'Con rebote'`.
Las etapas deben ser compatibles y pertenecer a la misma población y período.
Fuente: [cálculos del embudo](../3_tareas/caso1/main.py).

### Duración y fricción por caso

$DuracionHoras=\frac{t_{ultimo}-t_{primero}}{3600}$ si la diferencia se expresa en segundos.
$Friccion=TotalEventos\times DuracionHoras$.
El producto es un indicador construido en el ejercicio, con unidades evento-hora.
No es un estándar universal de eficiencia y puede crecer tanto por actividad como por espera.
Fuente: `duracion_caso` y `Friccion` del [script de procesos](../3_tareas/caso2/main.py).

### Respuesta comercial y gasto

Para un indicador binario: $TasaRespuesta=\frac{\sum_i Response_i}{n}\times100$.
$TotalSpent=\sum_{j\in categorias}Mnt_j$.
$TotalPurchases=NumWebPurchases+NumCatalogPurchases+NumStorePurchases$.
No se suma `NumDealsPurchases` como un cuarto canal porque describe compras con descuento.
La diferencia entre perfiles es $\frac{MediaRespondedores-MediaNoRespondedores}{MediaNoRespondedores}\times100$.
El denominador debe ser distinto de cero y el redondeo debe aplicarse al final.
Fuente: comparación de perfiles del [notebook comercial](../3_tareas/caso3/main.ipynb).

### Proxy de conversión web

El notebook define $WebConversionRate=\frac{NumWebPurchases}{NumWebVisitsMonth+0,1}$.
El $0,1$ evita dividir por cero, pero modifica el cociente.
El indicador compara compras y visitas mensuales sin demostrar que comparten ventana temporal.
Por ello es una señal exploratoria de fricción, no una tasa de conversión de sesiones validada.
La regla de fricción identifica visitas mensuales $\ge5$ y compras web $\le1$.
Fuente: cálculo de `Web_Conversion_Rate` del [notebook de marketing](../3_tareas/caso3/main.ipynb).

### Participación digital e importe medio

$IngresoTotal=Physical+Digital$ y $ParticipacionDigital=\frac{Digital}{IngresoTotal}\times100$.
La participación cambia si crece el ingreso digital o cae el físico; hay que mirar ambas series.
Fuente: `Total` y `Digital_pct` del [caso musical](../3_tareas/caso4/main.ipynb).

En taxis, $TarifaMedia_h=\frac{\sum_{i:hora_i=h}fare_i}{n_h}$.
La consulta de propinas promedia cocientes individuales: $\frac{1}{n}\sum_i\frac{tip_i}{fare_i}$.
No es necesariamente igual a $\frac{\sum_i tip_i}{\sum_i fare_i}$.
La consulta filtra tarifas positivas y protege la división con `NULLIF`.
Fuente: consultas por hora y por distrito en la [práctica SQL](../3_tareas/clase5/Curso3_Big_data_visualizations.ipynb).

### Ejemplo numérico ilustrativo: ponderación por eventos

Supongamos dos casos del mismo segmento: A tiene 2 eventos y dura 1 hora;
B tiene 8 eventos y dura 9 horas.
La media por caso es $(1+9)/2=5$ horas.
Si se repite la duración en cada evento y se promedia, resulta $(2\times1+8\times9)/10=7,4$ horas.
La segunda cifra pondera por cantidad de eventos y responde otra pregunta.
Este ejemplo explica un riesgo del `merge` seguido de medias del [script de procesos](../3_tareas/caso2/main.py).
Son datos didácticos, no resultados calculados sobre BPI 2017.

## 4. Código esencial

Fragmentos adaptados de las tareas; requieren las variables ya preparadas en el archivo citado.
No se descargan datos ni se escriben datasets desde estas notas.

En [caso 2](../3_tareas/caso2/main.py), `df` es el log de eventos cargado.
El bloque resume fechas a nivel de caso antes de medir duración.

```python
import pandas as pd

df['time:timestamp'] = pd.to_datetime(df['time:timestamp'], format='ISO8601')
duracion_caso = df.groupby('case:concept:name').agg(
    Fecha_Inicio=('time:timestamp', 'min'),
    Fecha_Fin=('time:timestamp', 'max'),
)
duracion_caso['Duracion_Horas'] = (
    duracion_caso['Fecha_Fin'] - duracion_caso['Fecha_Inicio']
).dt.total_seconds() / 3600
```

`format='ISO8601'` requiere una versión de pandas que lo admita, como la serie 2.x.
Las fechas deben ser compatibles en zona horaria para que la resta tenga sentido.

En [marketing](../3_tareas/caso3/main.ipynb), `df` es la tabla de clientes limpia.
Se adaptan las operaciones de gasto y respuesta por educación.

```python
mnt_cols = [
    'MntWines', 'MntFruits', 'MntMeatProducts',
    'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
]
df['TotalSpent'] = df[mnt_cols].sum(axis=1)
resp_educacion = (df.groupby('Education')['Response'].mean() * 100).sort_values(
    ascending=False
)
```

En la [práctica de taxis](../3_tareas/clase5/Curso3_Big_data_visualizations.ipynb), `trips` es una vista de DuckDB creada previamente sobre Parquet.
La consulta se ejecuta en esa conexión SQL; no corresponde a un archivo CSV de marketing.

```sql
SELECT EXTRACT(hour FROM tpep_pickup_datetime) AS hour,
       AVG(fare_amount) AS avg_fare
FROM trips
GROUP BY hour
ORDER BY hour;
```

La consulta agrupa horas de todos los días; no identifica por sí sola una tendencia diaria.

## 5. Errores comunes

- Tratar severidad por palabras clave como una etiqueta validada sin leer los textos.
- Usar número de eventos como si fuera número de casos o clientes.
- Promediar duración repetida tras una unión y omitir la ponderación por eventos.
- Unir varias decisiones de aceptación por caso y multiplicar filas sin comprobar unicidad.
- Interpretar el proxy de conversión web como una probabilidad o un porcentaje de sesiones.
- Confundir respuesta observada a campañas con efecto incremental demostrado.
- Presentar la coincidencia temporal del cambio musical como causalidad ya comprobada.
- Comparar motores con diferentes meses, filtros, resultados o costos de materialización.

Fuentes: [reglas cualitativas](../3_tareas/1/main.py), [proceso](../3_tareas/caso2/main.py), [marketing](../3_tareas/caso3/main.ipynb),
[música](../3_tareas/caso4/main.ipynb) y [benchmark pandas/DuckDB](../3_tareas/clase5/Curso3_Big_data_visualizations.ipynb).
El benchmark filtra un DataFrame en pandas y cuenta filas en DuckDB: no materializa el mismo resultado.
Sus tiempos deben interpretarse bajo esas operaciones concretas y no como una ventaja universal.

## 6. Preguntas de repaso

1. ¿Qué diferencia existe entre un evento, una sesión, un caso y un cliente?
2. ¿Cómo localizarías la mayor fricción del embudo sin mirar solo porcentajes?
3. ¿Por qué el promedio por evento puede diferir del promedio por caso?
4. ¿Qué limitación introduce el denominador `NumWebVisitsMonth + 0.1`?
5. ¿Cómo se construyen los cuatro perfiles de gasto y frecuencia?
6. ¿Qué diferencia hay entre promedio de ratios y ratio de totales?
7. ¿Qué tendría que mantenerse igual para comparar pandas y DuckDB?
8. ¿Qué fuentes y componentes integrarías en una arquitectura ELT de retail?
