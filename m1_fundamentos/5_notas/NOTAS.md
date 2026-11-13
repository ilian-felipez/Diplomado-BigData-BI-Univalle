# Módulo 1: Transformación digital y fundamentos de Big Data

Notas de estudio del diplomado, Univalle, gestión 2026.
El objetivo es conectar un problema organizacional con datos, análisis y decisiones.
La ruta de clases procede del [programa analítico](../2_recursos/01%20PROGRAMA%20ANALITICO%20POSTGRADO%20MARCELO%20PINTO.pdf); no sustituye las grabaciones.

## 1. Mapa del módulo

- 03/03: economía digital, plataformas y madurez digital; [tendencias globales](../2_recursos/Tendencias%20Globales%20y%20Transformaci%C3%B3n%20Digital.pdf).
- 05/03: 5V, tipos de datos y ciclo del dato; [fundamentos de Big Data](../2_recursos/Fundamentos%20de%20Big%20Data.pdf).
- 10/03: carga de datos y exploración inicial con Python; [práctica de exploración](../3_tareas/Actividad%203%20Exploraci%C3%B3n%20y%20An%C3%A1lisis%20de%20un%20Dataset%20con%20Python.ipynb).
- 12/03: limpieza, agrupaciones y gráficos; [análisis exploratorio](../3_tareas/Actividad%204/Exploratory_Data_Analysis_Ilian_Felipez.ipynb).
- 17/03: organizaciones orientadas a datos, gobierno y KPIs; [programa](../2_recursos/01%20PROGRAMA%20ANALITICO%20POSTGRADO%20MARCELO%20PINTO.pdf).
- 19/03: innovación ágil, cultura y gestión del cambio; [ecosistema y arquitecturas](../2_recursos/Ecosistema%20Big%20Data%20y%20Arquitecturas%20Modernas.pdf).
- 24/03: Data Lake, Data Warehouse y ETL/ELT; [ecosistema y arquitecturas](../2_recursos/Ecosistema%20Big%20Data%20y%20Arquitecturas%20Modernas.pdf).
- 26/03: integración de diagnóstico, indicadores y propuesta; [proyecto de nacimientos](../4_proyecto/analisis_nacimientos_bolivia_2009_2015_Ilian_Felipez.ipynb).
- Actividad 1: aplicación del [modelo de plataforma digital](../3_tareas/Actividad%201%20Aplicaci%C3%B3n%20del%20Modelo%20de%20Plataforma%20Digital.docx).
- Actividad 2: [diagnóstico de madurez digital](../3_tareas/Actividad%202%20Diagn%C3%B3stico%20de%20Madurez%20Digital.docx).

## 2. Conceptos clave

### Digitalización y transformación digital

Digitalizar convierte información o tareas a un soporte digital.
Transformar modifica procesos, capacidades y la manera de crear valor.
La diferencia importa porque instalar una herramienta no garantiza mejores decisiones.
Fuente: [tendencias globales](../2_recursos/Tendencias%20Globales%20y%20Transformaci%C3%B3n%20Digital.pdf) y [arquitecturas](../2_recursos/Ecosistema%20Big%20Data%20y%20Arquitecturas%20Modernas.pdf).

### Plataforma digital

Una plataforma conecta participantes y facilita interacciones mediante una infraestructura común.
El análisis debe identificar quién participa, qué intercambia y dónde aparece el valor.
Esto permite explicar el modelo de negocio antes de elegir una tecnología.
Fuente de aplicación: [actividad de plataforma digital](../3_tareas/Actividad%201%20Aplicaci%C3%B3n%20del%20Modelo%20de%20Plataforma%20Digital.docx).

### Madurez digital

Un diagnóstico de madurez examina la preparación de la organización para trabajar digitalmente.
Debe considerar capacidades y prácticas, además de disponibilidad de herramientas.
Sirve para ordenar mejoras viables y reconocer las barreras organizacionales.
Fuente de aplicación: [actividad de madurez digital](../3_tareas/Actividad%202%20Diagn%C3%B3stico%20de%20Madurez%20Digital.docx).

### Big Data y las 5V

Big Data implica gestionar y analizar datos cuya escala, ritmo o diversidad desafían los medios habituales.
Las 5V permiten describir el problema desde varias dimensiones:

- **Volumen:** cantidad de datos que se almacena y procesa.
- **Velocidad:** ritmo de generación y necesidad de procesamiento.
- **Variedad:** coexistencia de estructuras y formatos diferentes.
- **Veracidad:** confiabilidad y calidad de la información.
- **Valor:** utilidad del análisis para tomar decisiones.

Un volumen alto con baja veracidad puede producir conclusiones poco confiables.
Fuente de estas definiciones: [fundamentos de Big Data](../2_recursos/Fundamentos%20de%20Big%20Data.pdf).

### Niveles de análisis

La analítica descriptiva resume qué ocurrió; la diagnóstica busca explicar patrones.
La predictiva estima resultados futuros y la prescriptiva orienta acciones.
Distinguirlas evita llamar predicción a una simple tendencia histórica.
Fuente: [fundamentos](../2_recursos/Fundamentos%20de%20Big%20Data.pdf) y [programa analítico](../2_recursos/01%20PROGRAMA%20ANALITICO%20POSTGRADO%20MARCELO%20PINTO.pdf).

### Ciclo del dato y arquitectura

Capturar, almacenar, preparar y analizar datos son pasos conectados con su uso en decisiones.
Un Data Lake admite datos diversos; un Data Warehouse organiza datos para análisis consistente.
ETL transforma antes de cargar; ELT carga antes de transformar en el destino.
Estas decisiones importan porque condicionan calidad, integración y reutilización.
Fuente: [ecosistema y arquitecturas modernas](../2_recursos/Ecosistema%20Big%20Data%20y%20Arquitecturas%20Modernas.pdf).

### Exploración y segmentación

Explorar combina estructura, calidad, estadística y visualización.
En la práctica de ejercicio se comparan pulsaciones por `kind` y `diet`.
Agrupar permite detectar diferencias que el promedio global puede ocultar.
Una diferencia entre grupos debe interpretarse junto con el diseño y la unidad de observación.
Fuente: [práctica con Python](../3_tareas/Actividad%203%20Exploraci%C3%B3n%20y%20An%C3%A1lisis%20de%20un%20Dataset%20con%20Python.ipynb).

### KPI y gobierno de datos

Un KPI conecta una medida con un objetivo y una decisión.
El proyecto de nacimientos propone cobertura, mortalidad registrada y brecha institucional.
El gobierno de datos exige definiciones y validaciones comunes para compararlos.
Importa comprobar la calidad del registro antes de atribuir diferencias a la atención sanitaria.
Fuente: [proyecto integrador](../4_proyecto/analisis_nacimientos_bolivia_2009_2015_Ilian_Felipez.ipynb).

## 3. Fórmulas y métricas

### Media y comparación entre grupos

La media de $n$ observaciones es $\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i$.
En la práctica, $x_i$ es `pulse`; se calcula globalmente y por tipo de ejercicio.
La diferencia entre medias grupales extremas es $D=\max_g\bar{x}_g-\min_g\bar{x}_g$.
Esta diferencia describe separación; por sí sola no establece causalidad.
Fuente: cálculos de `mean_pulse` e `impacto_ejercicio` en la [práctica](../3_tareas/Actividad%203%20Exploraci%C3%B3n%20y%20An%C3%A1lisis%20de%20un%20Dataset%20con%20Python.ipynb).

### Indicadores del proyecto de nacimientos

Las siguientes expresiones conservan las definiciones del [notebook del proyecto](../4_proyecto/analisis_nacimientos_bolivia_2009_2015_Ilian_Felipez.ipynb).
Son indicadores del registro analizado, no estimaciones clínicas validadas externamente.

$PAPE=\frac{\text{Nacidos vivos atendidos por personal de salud}}{\text{Total de nacidos vivos}}\times100$.

Mide cobertura registrada de atención al parto.
El numerador y el denominador deben corresponder al mismo territorio y período.

$TMFR=\frac{\text{Nacidos muertos}}{\text{Total general de nacimientos}}\times1000$.

Expresa nacidos muertos por cada mil nacimientos registrados.
No se debe leer como porcentaje: el factor de escala es mil.

$IBC=\frac{\text{Total general}-\text{Nacidos vivos atendidos}}{\text{Total general}}\times100$.

Mide la brecha con la definición operativa usada en el proyecto.
PAPE e IBC no son complementos exactos si sus denominadores son distintos.

### Ejemplo numérico ilustrativo

Para practicar las fórmulas del proyecto, supongamos 1.000 nacidos vivos,
800 nacidos vivos atendidos y 20 nacidos muertos en el mismo período.
El total general sería $1.000+20=1.020$.

Entonces $PAPE=800/1.000\times100=80\%$.
La tasa registrada sería $TMFR=20/1.020\times1000\approx19,61$ por mil.
Finalmente, $IBC=(1.020-800)/1.020\times100\approx21,57\%$.
Estos números son didácticos; no son resultados del dataset de Bolivia.
La diferencia entre $100-PAPE$ e IBC se explica por sus denominadores.
Fuente de las definiciones aplicadas: [proyecto integrador](../4_proyecto/analisis_nacimientos_bolivia_2009_2015_Ilian_Felipez.ipynb).

## 4. Código esencial

Fragmentos adaptados de las tareas; ejecutar con Python y pandas en el notebook indicado.
`df` debe ser el DataFrame ya cargado en la práctica; no se descargan datos aquí.
Las rutas y la preparación completa están en el [notebook de exploración](../3_tareas/Actividad%203%20Exploraci%C3%B3n%20y%20An%C3%A1lisis%20de%20un%20Dataset%20con%20Python.ipynb).

```python
import pandas as pd

# Inspección antes de interpretar.
df.head()
df.info()
df.isnull().sum()
df.duplicated().sum()
```

La inspección identifica estructura, faltantes y filas repetidas.
No elimina automáticamente ningún registro.
Fuente: etapas de exploración y calidad de la [práctica](../3_tareas/Actividad%203%20Exploraci%C3%B3n%20y%20An%C3%A1lisis%20de%20un%20Dataset%20con%20Python.ipynb).

```python
mean_pulse = df['pulse'].mean()
group_kind = df.groupby('kind')['pulse'].mean().sort_values(ascending=False)
impacto_ejercicio = group_kind.max() - group_kind.min()
```

La comparación conserva las unidades de `pulse`.
No conviene comparar diferencias sin revisar qué representan `kind` y `diet`.
Fuente: análisis por grupos de la [práctica](../3_tareas/Actividad%203%20Exploraci%C3%B3n%20y%20An%C3%A1lisis%20de%20un%20Dataset%20con%20Python.ipynb).

En el proyecto, `df_total` es la tabla consolidada después de limpiar los años.
Este fragmento requiere haber ejecutado esa preparación en el [proyecto](../4_proyecto/analisis_nacimientos_bolivia_2009_2015_Ilian_Felipez.ipynb).

```python
nacidos_por_anio = (
    df_total.groupby('anio')['nacidos_vivos'].sum().reset_index()
)
```

La agrupación suma nacidos vivos por año; no cuenta simplemente filas.
Antes de reutilizarla se debe comprobar la granularidad municipal de los registros.
Fuente: sección de tendencia de nacidos vivos del [proyecto](../4_proyecto/analisis_nacimientos_bolivia_2009_2015_Ilian_Felipez.ipynb).

## 5. Errores comunes

- Confundir transformación digital con compra de herramientas; revisar procesos y cultura.
- Describir solo volumen y olvidar veracidad o valor al caracterizar Big Data.
- Interpretar faltantes como ceros sin justificar qué significa la ausencia.
- Contar filas cuando la variable de interés requiere sumar nacimientos.
- Promediar porcentajes territoriales sin revisar sus denominadores.
- Interpretar una anomalía de registro como prueba de un fenómeno sanitario.
- Presentar una asociación por grupos como una relación causal demostrada.
- Reutilizar semáforos del proyecto como umbrales clínicos universales.

Base de estas precauciones: [fundamentos](../2_recursos/Fundamentos%20de%20Big%20Data.pdf), [práctica](../3_tareas/Actividad%203%20Exploraci%C3%B3n%20y%20An%C3%A1lisis%20de%20un%20Dataset%20con%20Python.ipynb)
y problemas de calidad identificados en el [proyecto](../4_proyecto/analisis_nacimientos_bolivia_2009_2015_Ilian_Felipez.ipynb).

## 6. Preguntas de repaso

1. ¿Qué cambio organizacional diferencia digitalizar de transformar?
2. ¿Cómo describirías las cinco V en un registro de nacimientos?
3. ¿Qué revisarías antes de confiar en una media de pulsaciones?
4. ¿Por qué `groupby(...).sum()` y contar filas responden preguntas distintas?
5. ¿Qué diferencia hay entre PAPE, TMFR e IBC y sus denominadores?
6. ¿Cómo detectarías una cobertura registrada mayor que el total disponible?
7. ¿Cuándo usarías un Data Warehouse y qué papel tendría ETL?
8. ¿Qué decisión concreta puede respaldar un KPI y qué límite debe comunicarse?
