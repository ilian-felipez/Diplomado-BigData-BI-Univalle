# Módulo 3: Visualización de datos y Data Discovery

Notas de estudio del diplomado, Univalle, gestión 2026.
La finalidad es interpretar y comunicar datos con gráficos que sostengan una decisión.
Las referencias corresponden a las unidades y trabajos disponibles en el módulo.

## 1. Mapa del módulo

- Clase 1: importancia, tipos de datos y elección de gráficos; [fundamentos](../2_recursos/Clase%201.pdf).
- Unidad 1: Gestalt, percepción, Tufte y errores de diseño; [material de la unidad](../2_recursos/Unidad%201.pdf).
- Unidad 2, parte 1: Data Discovery, EDA, patrones y métricas; [material de la unidad](../2_recursos/Unidad%202%20-%20P1.pdf).
- Tarea 2: comparación de un [gráfico honesto](../3_tareas/2/notebook.ipynb) y una [versión engañosa](../3_tareas/2/notebook%20copy.ipynb).
- Tarea 2, versión final: barras agrupadas, ranking y tendencias; [notebook final](../3_tareas/2/notebook%20final.ipynb).
- Unidad 4: contexto, datos clave, insight y acción; [Data Storytelling](../2_recursos/Unidad%204.pdf).
- Proyecto: dashboard Power BI NOC/SOC y medidas DAX; [informe de telemetría](../4_proyecto/LaTeX/main.tex).

## 2. Conceptos clave

### Tipo de dato y pregunta visual

Los datos cuantitativos expresan magnitudes; los categóricos distinguen grupos.
Los temporales describen evolución y los geográficos incluyen ubicación.
La elección del gráfico debe responder a la pregunta y a estas propiedades.
Un histograma muestra distribución; las barras comparan categorías y las líneas evolución.
Fuente: [clase de fundamentos](../2_recursos/Clase%201.pdf).

### Percepción y Gestalt

Comparar posiciones sobre una escala común suele ser más preciso que comparar áreas o ángulos.
La proximidad agrupa elementos; la similitud relaciona objetos con apariencia semejante.
La continuidad facilita seguir una serie; figura-fondo permite distinguir lo importante.
Estos principios explican por qué una composición facilita o dificulta una lectura.
Fuente: [Unidad 1](../2_recursos/Unidad%201.pdf).

### Color y jerarquía

El color dirige la atención y puede asociar categorías.
Debe mantener un significado coherente y acompañarse de rótulos o formas cuando sea necesario.
Resaltar solo un canal puede cambiar la impresión del lector sin cambiar los datos.
La tarea contrasta un color uniforme con un énfasis selectivo sobre Influencers.
Fuentes: [Unidad 1](../2_recursos/Unidad%201.pdf) y [versión engañosa](../3_tareas/2/notebook%20copy.ipynb).

### Escala honesta y ruido visual

En barras, la longitud codifica magnitud y necesita una base coherente para comparar.
Sombras, volumen aparente o elementos decorativos pueden distraer del dato.
El principio de dato-tinta propone dedicar la mayor parte del diseño a información útil.
Fuente: [fundamentos](../2_recursos/Clase%201.pdf) y [Unidad 1](../2_recursos/Unidad%201.pdf).

### Data Discovery y EDA

Data Discovery conecta fuentes, explora datos, visualiza patrones y apoya acciones.
EDA combina estadísticas, distribuciones, relaciones y revisión de calidad.
El cuarteto de Anscombe muestra que estadísticas similares pueden ocultar formas distintas.
Por eso una media o correlación debe complementarse con una inspección gráfica.
Fuente: [Unidad 2](../2_recursos/Unidad%202%20-%20P1.pdf).

### Patrones y anomalías

Una tendencia describe dirección general; la estacionalidad se repite con periodicidad.
Un ciclo puede fluctuar sin una frecuencia fija y un outlier se aparta del patrón habitual.
Una anomalía visual es una señal para investigar, no una explicación suficiente.
Fuente: [Unidad 2](../2_recursos/Unidad%202%20-%20P1.pdf).

### Data Storytelling

Una historia con datos articula evidencia, narrativa y visualización.
Su secuencia de trabajo es contexto, datos clave, insight y acción.
Un insight debe explicar la relevancia del hallazgo para la audiencia.
Una recomendación debe corresponder a la evidencia y señalar qué queda por confirmar.
Fuente: [Unidad 4](../2_recursos/Unidad%204.pdf).

### Dashboard NOC/SOC

El proyecto separa una vista operativa de tráfico y una de anomalías y seguridad.
Comparte datos, pero cambia la pregunta: actividad de red frente a investigación de amenazas.
El informe describe datos de un entorno controlado con ataques simulados.
La composición de ese dataset no representa automáticamente la frecuencia de ataques de una red real.
Fuente: [informe del proyecto](../4_proyecto/LaTeX/main.tex).

## 3. Fórmulas y métricas

### Participación del presupuesto

$Total=\sum_c Presupuesto_c$ y $Participacion_c=\frac{Presupuesto_c}{Total}\times100$.
El [notebook honesto](../3_tareas/2/notebook.ipynb) usa 205, 327, 75, 410, 135 y 120 miles de USD.
El total es $205+327+75+410+135+120=1.272$ miles de USD.
TV representa $410/1.272\times100\approx32,23\%$.
Influencers representa $120/1.272\times100\approx9,43\%$.
Los porcentajes ayudan a comparar composición sin ocultar el valor absoluto.

### Variación temporal y diferencia absoluta

Para comparar dos trimestres: $\Delta=x_f-x_i$ y $Variacion=\frac{x_f-x_i}{x_i}\times100$, si $x_i\ne0$.
Es una formalización de las comparaciones del [notebook final](../3_tareas/2/notebook%20final.ipynb).
Influencers pasa de 10 a 50 miles de USD: $\Delta=40$ y variación del $400\%$.
TV pasa de 120 a 85: $\Delta=-35$ y variación aproximada de $-29,17\%$.
Una subida relativa grande puede partir de una base pequeña.
El nivel anual y la tendencia responden preguntas distintas.

### Ejemplo: verificar la frase que acompaña al gráfico

El [notebook final](../3_tareas/2/notebook%20final.ipynb) afirma que TV, con 410, supera en más del doble a Google Ads, con 327.
La relación correcta es $410/327\approx1,254$, y la diferencia es $410-327=83$ miles de USD.
TV tiene aproximadamente un $25,38\%$ más, no más del doble.
El gráfico necesita una interpretación numérica consistente para que el mensaje sea confiable.
Este cálculo revisa la frase; no modifica los datos ni el cuaderno fuente.

### Indicadores de telemetría

Las medidas siguientes se derivan del DAX documentado en el [informe](../4_proyecto/LaTeX/main.tex).
$TotalFlows=N$, donde cada fila representa un flujo registrado.

$TasaAnomalias=\frac{\#\{filas:label=1\}}{TotalFlows}$.

La medida retorna una proporción; el formato porcentual multiplica visualmente por cien.
Con los conteos del informe: $336.735/368.017\times100\approx91,50\%$.
Esta tasa describe etiquetas del dataset; no mide exactitud de un detector.

$Throughput=\frac{\sum sbytes+\sum dbytes}{DuracionSegundos\times1024^2}$.

El informe rotula MB/s, pero el divisor $1024^2$ corresponde a MiB/s.
La duración usa el intervalo entre el inicio mínimo y el final máximo del contexto filtrado.
El código sustituye intervalos inválidos por un segundo; ese caso requiere revisar los tiempos.

$FlowsPorHora=\frac{TotalFlows}{DATEDIFF(inicio,fin,HOUR)+1}$.

Es la definición operativa del proyecto; no es un promedio de conteos por hora activa.
Por ello conviene revisar cómo cambian los extremos temporales al aplicar filtros.

## 4. Código esencial

Fragmentos adaptados de las tareas de presupuesto, con datos contenidos en el cuaderno.
El primer bloque es autónomo y requiere Python y pandas.
Fuente: [notebook honesto](../3_tareas/2/notebook.ipynb).

```python
import pandas as pd

df = pd.DataFrame({
    'Canal': ['Redes Sociales', 'Google Ads', 'Email', 'TV', 'Eventos', 'Influencers'],
    'Total': [205, 327, 75, 410, 135, 120],
})
total_general = df['Total'].sum()
df['Porcentaje'] = (df['Total'] / total_general) * 100
df_sorted = df.sort_values('Total', ascending=True)
```

Ordenar por magnitud facilita el ranking.
Mantener el total y su porcentaje evita perder la escala del presupuesto.

Continuación del bloque anterior; requiere Matplotlib.
Se adapta la barra horizontal del [notebook final](../3_tareas/2/notebook%20final.ipynb).

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(df_sorted['Canal'], df_sorted['Total'], color='steelblue')
ax.set_xlabel('Presupuesto total (miles USD)')
ax.set_ylabel('Canal')
ax.set_title('Presupuesto anual de marketing por canal')
ax.set_xlim(0, 450)
plt.tight_layout()
plt.show()
```

El proyecto utiliza DAX, no SQL, para estas medidas.
Se reproducen expresiones del [informe](../4_proyecto/LaTeX/main.tex); requieren la tabla `NetworkTraffic` en Power BI.

```dax
TotalFlows = COUNTROWS('NetworkTraffic')

TasaAnomalias =
VAR Anomalias = CALCULATE(COUNTROWS('NetworkTraffic'), 'NetworkTraffic'[label] = 1)
RETURN DIVIDE(Anomalias, [TotalFlows], 0)
```

## 5. Errores comunes

- Elegir un gráfico por decoración antes de definir qué comparación se necesita.
- Truncar la base de barras para exagerar diferencias.
- Destacar un canal mediante color, orden o separación sin explicar el criterio.
- Confundir el crecimiento de Influencers con el mayor presupuesto anual.
- Repetir conclusiones textuales sin contrastar cocientes y diferencias.
- Presentar la tasa de etiquetas maliciosas como una métrica de clasificación.
- Omitir unidades, filtros o intervalo temporal al mostrar throughput.
- Saturar una vista ejecutiva con métricas sin contexto ni acción.

Fuentes: [Unidad 1](../2_recursos/Unidad%201.pdf), [tarea comparativa](../3_tareas/2/notebook%20copy.ipynb), [notebook final](../3_tareas/2/notebook%20final.ipynb)
y [proyecto de telemetría](../4_proyecto/LaTeX/main.tex).
La [Unidad 4](../2_recursos/Unidad%204.pdf) recomienda 5–7 visualizaciones por vista y exige al menos ocho en el trabajo final.
Las dos indicaciones pueden organizarse en las dos pestañas requeridas por la misma consigna.

## 6. Preguntas de repaso

1. ¿Qué gráfico usarías para comparar canales y cuál para su evolución trimestral?
2. ¿Por qué las barras facilitan comparar magnitudes más que los ángulos de un pastel?
3. ¿Cómo puede el color manipular la lectura sin alterar los valores?
4. ¿Qué diferencia existe entre aumentar 40 miles de USD y crecer 400%?
5. ¿Qué cálculo contradice la frase «más del doble» en la tarea?
6. ¿Qué información falta cuando una tarjeta muestra solo una cifra?
7. ¿Por qué una tasa de anomalías del 91,5% no demuestra la calidad de un detector?
8. ¿Cómo convertirías un hallazgo del dashboard en una acción verificable?
