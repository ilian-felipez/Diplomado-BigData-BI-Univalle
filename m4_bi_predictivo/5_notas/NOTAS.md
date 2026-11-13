# Módulo 4: Business Intelligence y analítica predictiva

Notas de estudio del diplomado, Univalle, gestión 2026.
El hilo conductor es transformar registros en indicadores, predicciones y decisiones comerciales.
Las prácticas reúnen ejemplos docentes y extensiones con datos de comercio electrónico.

## 1. Mapa del módulo

- A1: datos de negocio, métricas derivadas e insights de rentabilidad; [introducción a BI](../3_tareas/A1/Ejercicio_A1_FMNQ.ipynb).
- A2: extracción, limpieza, integridad y carga; [ETL, Data Warehouse y OLAP](../3_tareas/A2/Clase2_ETL_DW_OLAP.ipynb).
- A2: esquema estrella con ventas, clientes, productos, canal y tiempo; [práctica](../3_tareas/A2/Clase2_ETL_DW_OLAP.ipynb).
- A2: extensión de comercio electrónico y consultas SQLite; [Data Warehouse](../3_tareas/A2/Clase2_ETL_DW_OLAP.ipynb).
- A3: indicadores, evolución temporal y comparación de segmentos; [analítica descriptiva](../3_tareas/A3/Clase3_Modelos_Descriptivos_Analitica_Exploratoria.ipynb).
- A4: clasificación de compra y regresión del valor futuro; [modelos predictivos](../3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb).
- A4: priorización comercial mediante probabilidad y valor estimado; [campaña inteligente](../3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb).
- Proyecto: ETL, EDA, logística, Random Forest y validación de [Telco Churn](../4_proyecto/notebooks/Telco_Customer_Churn_Analysis.ipynb).
- Proyecto: alcance y entrega definidos en la [consigna del trabajo final](../4_proyecto/documents/INSTRUCCIONES%20DEL%20PROYECTO%20FINAL%20-%20M%C3%93DULO%20IV.pdf).

## 2. Conceptos clave

### BI orientado a decisiones

Business Intelligence integra y organiza datos para comprender el desempeño del negocio.
La práctica A1 construye indicadores y los interpreta como decisiones comerciales.
Importa distinguir ingreso, descuentos y costos: vender más no garantiza retener más margen.
Fuente: [métricas y rentabilidad por canal de A1](../3_tareas/A1/Ejercicio_A1_FMNQ.ipynb).

### ETL y calidad

Extracción obtiene las tablas; transformación corrige y estandariza; carga prepara su uso analítico.
A2 incorpora errores deliberados: duplicados, fechas inconsistentes y descuentos inválidos.
También revisa si las claves de ventas existen en las tablas de clientes y productos.
La calidad condiciona el indicador final, no solo la comodidad de programarlo.
Fuente: [proceso ETL de A2](../3_tareas/A2/Clase2_ETL_DW_OLAP.ipynb).

### Hechos, dimensiones y granularidad

La tabla de hechos representa el evento de negocio y sus medidas.
Las dimensiones describen sus perspectivas: cliente, producto, canal y tiempo.
La granularidad indica qué significa una fila y debe aclararse antes de contar tickets.
Un esquema estrella organiza esas relaciones para un análisis consistente.
Fuente: [construcción del Data Warehouse de A2](../3_tareas/A2/Clase2_ETL_DW_OLAP.ipynb).

### OLAP e indicadores descriptivos

OLAP permite analizar un mismo hecho desde distintas dimensiones.
Comparar canal, región, categoría o mes revela diferencias que el total puede esconder.
A3 añade contexto e interpretación: una tabla de ventas todavía necesita una pregunta de negocio.
Fuentes: [análisis OLAP](../3_tareas/A2/Clase2_ETL_DW_OLAP.ipynb) y [de la descripción al insight](../3_tareas/A3/Clase3_Modelos_Descriptivos_Analitica_Exploratoria.ipynb).

### Clasificación y regresión en una campaña

Clasificación estima si un cliente comprará; regresión estima una magnitud monetaria.
A4 compara algoritmos y combina probabilidad de compra con valor predicho.
Así se diferencia al cliente probable del cliente con mayor oportunidad económica.
Fuente: [caso de campaña inteligente](../3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb).

### Transformaciones y evaluación

Las prácticas usan escalado numérico y codificación de categorías en pipelines.
Los transformadores deben aprender de entrenamiento y aplicarse coherentemente a prueba.
La métrica elegida debe representar el error que importa a la decisión.
Fuente: [preparación y evaluación de A4](../3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb).

### Churn y acción comercial

Churn es el abandono del servicio, codificado como respuesta binaria en el proyecto Telco.
El proyecto compara regresión logística y Random Forest, con matriz de confusión y ROC-AUC.
El recall de fuga informa cuántos abandonos se detectan; la importancia de variables ayuda a explorar perfiles.
Una variable importante no demuestra por sí misma una causa del abandono.
Fuente: [análisis predictivo Telco](../4_proyecto/notebooks/Telco_Customer_Churn_Analysis.ipynb).

## 3. Fórmulas y métricas

### Indicadores comerciales

En A1 se utiliza $MargenOperativo=IngresoNeto-CostoEnvio$ al resumir canales.
Es una definición operativa del ejercicio: no incorpora todos los posibles costos empresariales.
Fuente: `rentabilidad_canal` de [A1](../3_tareas/A1/Ejercicio_A1_FMNQ.ipynb).

En A3: $TicketPromedio=\frac{VentasTotales}{NumeroDeTransacciones}$.
El número de transacciones debe corresponder a ventas distintas cuando hay varias filas por venta.
La tasa de conversión es $\frac{SesionesConvertidas}{TotalSesiones}\times100$.
Una media de `is_converted` binario produce la proporción de sesiones convertidas.
Fuente: indicadores de ventas y comercio electrónico de [A3](../3_tareas/A3/Clase3_Modelos_Descriptivos_Analitica_Exploratoria.ipynb).

### Métricas de clasificación

VP y VN son aciertos; FP son falsas alarmas y FN positivos no detectados.
$Accuracy=\frac{VP+VN}{VP+VN+FP+FN}$.
$Precision=\frac{VP}{VP+FP}$; $Recall=\frac{VP}{VP+FN}$.
Un modelo puede acertar muchos clientes que no abandonan y detectar pocas fugas.
ROC-AUC resume la discriminación a través de umbrales, usando probabilidades o puntuaciones.
No equivale a una tasa de conversión ni al beneficio de una campaña.
Fuentes: [evaluación de A4](../3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb) y [proyecto Telco](../4_proyecto/notebooks/Telco_Customer_Churn_Analysis.ipynb).

### Métricas de regresión

$MAE=\frac{1}{n}\sum_i|y_i-\hat y_i|$.
$RMSE=\sqrt{\frac{1}{n}\sum_i(y_i-\hat y_i)^2}$.
$R^2=1-\frac{\sum_i(y_i-\hat y_i)^2}{\sum_i(y_i-\bar y)^2}$.
MAE y RMSE mantienen las unidades de la respuesta; RMSE penaliza más los errores grandes.
$R^2$ compara contra predecir con la media y no se interpreta como exactitud de clasificación.
Fuente: [modelos de regresión de A4](../3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb).

### Valor esperado y priorización

A4 calcula $ValorEsperado=P(compra\mid X)\times ValorPredicho$.
Por ejemplo ilustrativo, si $P=0,60$ y el valor condicional estimado es 100€, resulta $60€$.
Un segundo cliente con $P=0,30$ y valor de 300€ tendría un valor esperado de $90€$.
El segundo puede priorizarse por oportunidad económica aunque tenga menor probabilidad de compra.
El cálculo no descuenta automáticamente costos ni mide beneficio incremental.
Para leerlo como esperanza monetaria, el valor debe representar el monto condicionado a comprar.
Si ya se predice gasto incondicional, multiplicar otra vez por probabilidad puede descontarlo dos veces.
Fuente de la regla y su aplicación: [priorización comercial de A4](../3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb).

### Ejemplo Numérico: Generación de Valor

Cuando procesamos y analizamos los datos, es cuando realmente aparece el valor económico. Para entender cómo se genera este impacto, supongamos que mediante un análisis de datos avanzado se logra identificar un segmento específico de **200 clientes** que presentan una probabilidad de conversión significativamente mayor que el resto.

Para resolver el beneficio de esta estrategia, primero se calculan los costes de ejecución: al lanzar una campaña focalizada exclusivamente en este grupo optimizado, con un coste de contacto de **2€ por cliente**, la inversión total requerida se reduce a **400€** ($200 \times 2€$). En lugar de malgastar recursos de manera masiva, los datos permiten apuntar con precisión.

A continuación, se determina el retorno financiero del segmento. Gracias a esa segmentación precisa, se alcanza una tasa esperada de compra del **20%**, lo que se traduce directamente en **40 compras efectivas** ($200 \times 20\%$). Sabiendo que cada uno de estos clientes genera un ingreso promedio de **50€**, el volumen de ventas proyectado alcanza un ingreso total de **2.000€** ($40 \times 50€$). Al restar los costes de campaña previamente calculados, el beneficio bruto obtenido es de **1.600€** ($2.000€ - 400€$).

La verdadera relevancia del análisis de datos se demuestra al comparar este resultado con el rendimiento del escenario tradicional sin analítica. Mientras que el caso base sin datos generaba apenas 500€ de beneficio debido a la falta de puntería en la campaña, la optimización estadística introduce una mejora neta de **1.100€** de valor incremental para el negocio ($1.600€ - 500€$).

Como conclusión fundamental, este ejemplo demuestra que los datos por sí solos no generan ingresos de forma pasiva; el verdadero valor económico aparece únicamente cuando la información cruda se transforma de manera activa en segmentación, priorización de recursos y decisiones comerciales estratégicas.

**Lectura del ejemplo:** los 500€ del escenario base son un supuesto de comparación.
El «beneficio bruto» del ejemplo descuenta el contacto; no incluye otros costos no especificados.
Es una ilustración comercial conservada del material personal del módulo.
La relación entre segmentación, costos y decisión se trabaja también en [A1](../3_tareas/A1/Ejercicio_A1_FMNQ.ipynb) y [A4](../3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb).

## 4. Código esencial

Fragmentos adaptados de las tareas; ejecutar dentro de los cuadernos citados.
Las tablas y pipelines indicados deben estar preparados con las celdas previas.

En [A2](../3_tareas/A2/Clase2_ETL_DW_OLAP.ipynb), `fact_ventas` es la tabla de hechos ya construida.
Este resumen conserva las agregaciones del ejercicio.

```python
olap_canal = fact_ventas.groupby('canal_venta', as_index=False).agg(
    ventas_totales=('importe_total', 'sum'),
    unidades=('cantidad', 'sum'),
    tickets=('venta_id', 'count'),
)
```

`count` cuenta valores no nulos; revisa si cada fila equivale realmente a un ticket.
La sección de comercio electrónico de [A2](../3_tareas/A2/Clase2_ETL_DW_OLAP.ipynb) ejecuta esta consulta mediante SQLite.
Requiere las tablas `fact_purchases` y `dim_products` ya cargadas en la base.

```sql
SELECT p.category,
       SUM(f.total_amount) AS total_ventas,
       SUM(f.quantity) AS unidades_vendidas
FROM fact_purchases f
JOIN dim_products p ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_ventas DESC;
```

La dimensión debe tener una clave de producto única para evitar multiplicar ventas en la unión.

En [A4](../3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb), `base_scoring`, `features`, `mejor_clf` y `mejor_reg` proceden del ajuste previo.
El clasificador seleccionado debe disponer de `predict_proba` y clase positiva en la segunda columna.

```python
base_scoring['probabilidad_compra'] = mejor_clf.predict_proba(
    base_scoring[features]
)[:, 1]
base_scoring['valor_predicho'] = mejor_reg.predict(base_scoring[features])
base_scoring['valor_esperado'] = (
    base_scoring['probabilidad_compra'] * base_scoring['valor_predicho']
)
top_10 = base_scoring.sort_values('valor_esperado', ascending=False).head(10)
```

Es una regla de priorización del ejercicio, no una evaluación independiente del modelo.

## 5. Errores comunes

- Crear el dashboard antes de comprobar duplicados, tipos e integridad de claves.
- Unir dimensiones con claves repetidas y duplicar importes sin advertirlo.
- Llamar ticket a cada fila sin definir la granularidad de ventas.
- Confundir un margen calculado con ingreso neto menos envíos con rentabilidad completa.
- Elegir solo por accuracy cuando interesa detectar clientes que abandonan.
- Interpretar ROC-AUC como el porcentaje de clientes que responderán a la campaña.
- Reutilizar todo el scoring como evaluación aunque incluya filas usadas para entrenar.
- Confundir valor esperado con beneficio o mejora incremental demostrada.

Base de estas precauciones: [A1](../3_tareas/A1/Ejercicio_A1_FMNQ.ipynb), [integridad y OLAP de A2](../3_tareas/A2/Clase2_ETL_DW_OLAP.ipynb),
[comparación de modelos de A4](../3_tareas/A4/Clase4_Modelos_Predictivos_Clasificacion_Regresion.ipynb) y [evaluación Telco](../4_proyecto/notebooks/Telco_Customer_Churn_Analysis.ipynb).
En el proyecto Telco la imputación de `TotalCharges` ocurre antes de la partición.
Al evaluar una variante futura, esa mediana debería aprenderse solo con entrenamiento.
La codificación categórica y el escalado también deben revisarse dentro de la validación cruzada.
Fuente de esta secuencia: [preparación y validación del proyecto](../4_proyecto/notebooks/Telco_Customer_Churn_Analysis.ipynb).

## 6. Preguntas de repaso

1. ¿Cómo distinguirías una tabla de hechos de una dimensión en A2?
2. ¿Qué validación evita multiplicar ventas al unir productos?
3. ¿Qué diferencia hay entre ventas totales, tickets y ticket promedio?
4. ¿Cuándo un modelo con menor accuracy puede ser preferible para retención?
5. ¿Qué representan MAE y RMSE en una predicción monetaria?
6. ¿Qué condición necesita el valor predicho para multiplicarlo por probabilidad de compra?
7. ¿Cómo se obtienen los 1.100€ incrementales del ejemplo y qué costos faltan?
8. ¿Qué transformaciones deben aprenderse exclusivamente con entrenamiento?
