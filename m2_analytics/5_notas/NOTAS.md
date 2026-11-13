Clasificación Parte 2: Framework y Evaluación

Proceso de Clasificación
El framework estándar para llevar un modelo desde los datos hasta el mundo real sigue estos pasos:

    • Datos de entrenamiento y etiquetas: Recolectar datos históricos donde ya conocemos el resultado ($Y$) para cada entrada ($X$).
    • Entrenar un algoritmo de clasificación: El modelo ajusta sus parámetros internos para encontrar la relación entre las características y las etiquetas.
    • Evaluar en un dataset de validación: Probar el modelo con datos que no usó para estudiar para medir su desempeño real.
    • Poner el modelo en producción: Implementar el modelo final para que clasifique nuevos datos en tiempo real.



Tarea de mapear set $x$χ a una clase $y$ψ
Esta es la definición formal de lo que hace un Modelo de Clasificación. Se basa en transformar datos de entrada en una respuesta categórica.
    Componentes del Proceso
    El flujo de trabajo se divide en tres partes fundamentales, tal como muestra el diagrama:
        ○ Input (Conjunto de Atributos $x$): Son las variables independientes o características del objeto.
            § Ejemplo: Si queremos detectar spam, los atributos serían las palabras del correo, el remitente y la hora de envío.
        ○ Modelo de Clasificación: Es la "caja negra" (algoritmo) que ha sido entrenada para reconocer patrones. Su función es encontrar una función matemática $f(x)$ que relacione los atributos con una categoría.
        ○ Output (Etiqueta de la clase $y$): Es el resultado final o variable dependiente. Debe ser una clase discreta.
            § Ejemplo: "Spam" o "No Spam"; "Sano" o "Enfermo".
    Clasificación como Aprendizaje Supervisado
    En Machine Learning, este proceso se considera estrictamente un enfoque de aprendizaje supervisado.
        ○ ¿Por qué?: Porque para que el modelo aprenda a realizar este mapeo de $x$ a $y$, requiere datos etiquetados.
        ○ La Lógica: No podemos esperar que el modelo adivine qué es "Enfermo" si antes no le mostramos miles de ejemplos de sets $x$ que resultaron en la etiqueta $y = \text{Enfermo}$.
Nota Técnica: A diferencia de la regresión (que predice números continuos como el precio de una casa), la tarea de mapear a una clase $y$ siempre busca un resultado categórico o nominal.

Machine Learning vs. Data Mining
Aunque ambos campos utilizan técnicas similares, el objetivo final cuando hacemos clasificación es lo que los diferencia:
    Machine Learning (Enfoque en Automatización)
    En Machine Learning, el objetivo principal es la predicción y ejecución autónoma.
        ○ Propósito: Queremos que la máquina aprenda a realizar una tarea por sí misma basándose en la experiencia (datos).
        ○ Ejemplo del slide: Reconocer rostros en imágenes de forma automática sin intervención humana.
        ○ Palabra clave: Automatizar.
    Data Mining (Enfoque en Descubrimiento)
    En Data Mining (Minería de Datos), el objetivo es la comprensión y el análisis.
        ○ Propósito: Queremos encontrar un patrón oculto en los datos. No solo predecir, sino entender cómo se relaciona $x$ con $y$ a través de un modelo.
        ○ Ejemplo del slide: Usar un modelo predictivo para extraer conocimiento útil que nos ayude a tomar decisiones.
        ○ Palabra clave: Entender / Encontrar patrones.
    Resumen de diferencias
    Campo	Objetivo Principal	Resultado esperado
    Machine Learning	Automatizar una tarea.	Un modelo que actúe solo.
    Data Mining	Encontrar un patrón.	Conocimiento/Insights sobre los datos.

¿Cómo saber si un modelo es bueno o no?
Para determinar la calidad de un modelo de Machine Learning, no basta con que responda bien a lo que ya conoce; la clave es su comportamiento ante lo desconocido.
    5.1. Capacidad Predictiva y Generalización
        ○ Capacidad Predictiva: Es el factor más importante. Se refiere a qué tan acertadas son las predicciones del modelo.
        ○ El engaño de los datos de entrenamiento: Hacer predicciones correctas sobre los mismos datos que se usaron para entrenar no es suficiente. El modelo podría estar simplemente memorizando (Overfitting).
        ○ Generalización: Es la verdadera prueba de fuego. El modelo debe ser capaz de realizar predicciones correctas en datos distintos a los de entrenamiento.
    5.2. Otros factores de éxito
    Además de acertar, un buen modelo debe ser:
        ○ Interpretable: Que podamos entender por qué tomó esa decisión.
        ○ Eficiente: Que no consuma recursos excesivos (tiempo/memoria) para dar una respuesta.

¿Cómo saber si un modelo es bueno? (Proceso de Evaluación)
Para medir esa "bondad" de forma científica, seguimos un proceso de experimentación:
    • Métricas de desempeño: Resumimos la capacidad del modelo mediante números (performance metrics).
    • Contraste: Estas métricas se calculan comparando los valores predichos por la IA versus los valores reales (la verdad) de la variable objetivo.
    • Uso de datos "Invisibles": Este contraste SIEMPRE debe hacerse con datos que no fueron usados durante el entrenamiento para asegurar que el modelo generaliza.
    • Diseño de experimentos: No nos quedamos con el primer resultado. Comparamos las métricas de varios modelos distintos y seleccionamos el que demuestre el mejor desempeño global.

Métricas de Desempeño (Performance Metrics)
Las métricas nos sirven para cuantificar qué tan bien está clasificando el modelo, basándonos en el conteo de predicciones correctas e incorrectas.
    Accuracy (Exactitud)
    Es la métrica más intuitiva: ¿Qué porcentaje del total de predicciones fue correcto?
        ○ Fórmulas:
            § Accuracy: Es el número de predicciones correctas sobre el número total de predicciones.
            Accuracy= (a+d)/(a+b+c+d)= (TP+TN)/(TP+TN+FP+FN)
            § Error Rate (Tasa de error): Es el número de predicciones incorrectas sobre el número total de predicciones.
            Error rate= (Number of wrong predictions)/(Total number of predictions)  =1 −Accuracy
    La Matriz de Confusión
    Para entender el Accuracy, usamos una tabla que cruza la Clase Real con la Clase Predicha:
        ○ TP (True Positive): Era (+) y predijo (+). ¡Acierto!
        ○ TN (True Negative): Era (-) y predijo (-). ¡Acierto!
        ○ FP (False Positive): Era (-) pero predijo (+). (Error Tipo I / Falsa Alarma).
        ○ FN (False Negative): Era (+) pero predijo (-). (Error Tipo II / Omisión).
        Predicción: Positivo (+)	Predicción: Negativo (-)
    Realidad: Positivo (+)	VP (Verdadero Positivo)	FN (Falso Negativo)
    Realidad: Negativo (-)	FP (Falso Positivo)	VN (Verdadero Negativo) 
    
    Falsos Positivos vs. Falsos Negativos
    No todos los errores son iguales. La imagen del médico lo explica perfecto:
        ○ Error Tipo I (Falso Positivo): Decirle a un hombre que está embarazado. Es una "falsa alarma".
        ○ Error Tipo II (Falso Negativo): Decirle a una mujer claramente embarazada que no lo está. Es una "omisión peligrosa".
            § Nota: En medicina o ciberseguridad, el Error Tipo II suele ser el más costoso y el que más queremos evitar.
    
    Limitaciones del Accuracy (El peligro del desbalance)
    El Accuracy es una pésima métrica cuando tienes clases desbalanceadas.
        ○ Ejemplo del slide: Tienes 10,000 datos. 9,990 son de "Clase 0" y solo 10 son de "Clase 1".
        ○ Si creas un modelo flojo que siempre responda "Clase 0", tendrá un 99.9% de Accuracy.
        ○ El problema: El modelo no aprendió nada y falló en detectar los 10 casos importantes (Clase 1). Por eso necesitamos métricas más finas.
    
    Precision y Recall (Calidad vs. Cantidad)
    Cuando definimos una clase positiva (el evento que nos interesa detectar), utilizamos estas dos métricas para evaluar el desempeño:
        ○ Precision (Precisión): Mide la calidad de las predicciones positivas. Responde a: de todos los que el modelo seleccionó como positivos, ¿cuántos eran realmente correctos?.
Precision= TP/(TP+FP)
        ○ Recall (Exhaustividad/Sensibilidad): Mide la capacidad de captura del modelo. Responde a: de todos los positivos que realmente existen en la realidad, ¿cuántos logró atrapar el modelo?.
        Recall= TP/(TP+FN)
        El Trade-off: Existe un equilibrio inverso; si aumentas la Precision (te vuelves más exigente para decir que algo es positivo), el Recall suele bajar porque se te escapan casos reales.
    
    F-measure: Media Armónica Ponderada
    La F-measure combina Precision ($P$) y Recall ($R$) en un solo valor. Se utiliza un promedio armónico porque es "conservador": si una de las dos métricas es muy baja, el resultado final se hunde, obligando al modelo a ser bueno en ambas.
        
        Versión con α (Alfa)
        Esta fórmula representa la media armónica ponderada clásica:
        F= 1/(α ∙ 1/P+(1 −α)∙1/R)
        
            § α (Alfa): Es el peso que se le asigna a la Precision.
            § Equilibrio (F_1): Se logra con α= 1/2  o (0.5), dándole igual importancia a ambas.
        
        Versión con β (Beta)
        Es la forma más utilizada en Machine Learning porque permite interpretar cuántas veces más importante es el Recall frente a la Precision:
            F= ((β^2  + 1)  ∙ P ∙ R)/(β^2  ∙ P + R)
            § β (Beta): Si β > 1$, das más peso al Recall. Si β < 1$, das más peso a la Precision.
            
            § Equilibrio (F_1): Se logra con β=1.
        
        Relación y Despejes (Pasar de β a α y viceversa)
        La relación fundamental entre ambos parámetros es:
        β^2= (1 −α )/α
            Para pasar de α a β:
            Si conoces el valor de alfa y quieres saber qué tan importante es el Recall respecto a la Precision:
            β=√((1−a)/a)
                □ Ejemplo: Si a=0.5, entonces β=√(0.5/0.5)=1.
            Para pasar de β a α: 
            Si sabes que el Recall es "el doble de importante" β=2 y necesitas hallar el alfa para la fórmula armónica:
            α=1/(b^2+1)
                □ Ejemplo: Si β=2, entonces α=1/(2^2+1)=1/5=0.2.
Ejercicio Práctico: Reincidencia de Cáncer
    Consigna del problema
    Considerar un estudio con 286 mujeres sobre la reincidencia de cáncer después de 5 años:
        ○ Total (): 286
        ○ Clase Positiva (Sí reinciden): 85
        ○ Clase Negativa (No reinciden): 201
    Objetivo: Comparar dos modelos extremos (M1 y M2) mediante matrices de confusión y métricas (, , y ).
    
    Resolución Modelo 1 (M1): "Todas reinciden"
    Este modelo es "pesimista" o perezoso: predice siempre que la paciente tendrá reincidencia, sin importar sus datos.
    Matriz de Confusión M1:
    Clase Real \ Predicha	Positivo (Sí)	Negativo (No)
    Positivo (85)	85 (VP)	0 (FN)
    Negativo (201)	201 (FP)	0 (VN)
    
    Cálculo de Métricas M1:
        ○ Accuracy: (29.7%)
            § Interpretación: Muy bajo, falla en la mayoría de los casos negativos.
        ○ Precision: 
            § Interpretación: De todo lo que marcó como positivo, solo el 29% lo era realmente.
        ○ Recall: (100%)
            § Interpretación: Perfecto. No se le escapó ninguna enferma porque a todas las marcó como tal.
        ○ F1-Score: 

    Resolución Modelo 2 (M2): "Ninguna reincide"
    Este modelo es "optimista": predice siempre que la paciente está sana.
    Matriz de Confusión M2:
    Clase Real \ Predicha	Positivo (Sí)	Negativo (No)
    Positivo (85)	0 (VP)	85 (FN)
    Negativo (201)	0 (FP)	201 (VN)
    
    Cálculo de Métricas M2:
        ○ Accuracy: (70.3%)
            § Interpretación: Parece un buen número, pero es un engaño por el desbalance de los datos.
        ○ Precision: 
        ○ Recall: 
            § Interpretación: Peligroso. No detectó a ninguna sola persona que realmente iba a reincidir.
        ○ F1-Score: 

    Conclusión del Ejercicio
    Este ejercicio demuestra por qué el Accuracy no es suficiente.
        ○ El M2 tiene un Accuracy mucho mayor (70% vs 29%), pero es inútil en medicina porque su es 0.
        ○ En problemas de salud, preferimos modelos con alto Recall (como el M1) aunque tengan muchos Falsos Positivos, porque el costo de un Falso Negativo (dejar ir a un enfermo) es demasiado alto.
    
    Anexo: Métodos de Validación y Ajuste
    Para evitar modelos tan malos como M1 o M2, usamos:
        ○ Holdout: Particionar datos en Entrenamiento (usualmente 2/3) y Test (1/3).
            § Limitación: Si el set de test es muy pequeño, el no es confiable.
        ○ Balance entre Sesgo y Varianza: * Underfitting: Modelo muy simple (como una línea recta ), no entiende la tendencia.
            § Overfitting: Modelo muy complejo (), memoriza el ruido y los puntos exactos pero no generaliza bien.



Matriz de Costo y Evaluación Económica
En la vida real, no todos los errores tienen la misma gravedad ni todos los aciertos el mismo valor. La Matriz de Costo nos permite asignar un "peso" o penalización a cada celda de la matriz de confusión.
    Definición de la Matriz de Costo
    Se utiliza cuando sabemos explícitamente qué errores son más costosos y qué aciertos son más valiosos.
        ○ Notación $C(i|j)$: Representa el costo de clasificar un objeto como clase $j$ dado que pertenece realmente a la clase $i$.
        Clase Real \ Predicha	Clase = +	Clase = -
        Clase = +	$C(+	+)$ (Acierto)
        Clase = -	$C(+	-)$ (Error tipo I)
    Ejemplo Práctico: ¿Cuál modelo es mejor?
    Basándonos en el ejercicio comparativo del slide, analizamos dos modelos para decidir cuál implementar.
        Definición de Costos (Penalizaciones)
        El docente propone la siguiente matriz de costos:
            § Acierto positivo: $-1$ (Premio por detectar un positivo).
            § Falso Negativo (Error Grave): $100$ (Penalidad alta por no detectar un caso positivo).
            § Falso Positivo: $1$ (Penalidad baja por falsa alarma).
            § Acierto negativo: $0$.
        Comparación de Modelos
            i. Modelo 1 (M1):
                □ Accuracy: $0.8$ (80%).
                □ Cálculo de Costo: $(-1 \times 150) + (100 \times 40) + (1 \times 60) + (0 \times 250) = \mathbf{3910}$.
            ii. Modelo 2 (M2):
                □ Accuracy: $0.9$ (90%).
                □ Cálculo de Costo: $(-1 \times 250) + (100 \times 45) + (1 \times 5) + (0 \times 200) = \mathbf{4255}$.
    Conclusión: La Regla del Costo
    La regla de oro es: A mayor costo total, peor es el modelo.
        ○ Resultado: Aunque el Modelo 2 tiene un accuracy superior ($0.9$ vs $0.8$), el Modelo 1 es el ganador porque su costo total es menor ($3910$ vs $4255$).
        ○ Razón: El M2 cometió 5 errores de tipo "Falso Negativo" adicionales (45 vs 40), y como ese error es extremadamente caro ($100$ puntos c/u), arruinó su desempeño económico final.
Clasificación Multi-clase
Hasta ahora hemos visto problemas binarios (Sí/No), pero en la vida real es común tener $k$ etiquetas o categorías distintas.

    La Matriz de Confusión Multi-clase
    Cuando trabajamos con múltiples categorías, la matriz de confusión deja de ser de $2 \times 2$ para convertirse en una matriz de $k \times k$.
        ○ Estructura: Las filas representan la clase real y las columnas la clase asignada (predicha) por el modelo.
        ○ Interpretación de la Diagonal: Los valores que se encuentran en la diagonal principal de la matriz representan los aciertos para cada categoría específica.
        ○ Interpretación fuera de la diagonal: Cualquier valor fuera de la diagonal indica una confusión. Por ejemplo, en el slide se observa que 13 documentos que eran realmente del Reino Unido (True UK) fueron clasificados erróneamente como trigo (Assigned wheat).
    Visualización del Desempeño
    Esta matriz es la herramienta más poderosa para identificar qué clases específicas están "confundiendo" al modelo.
        ○ Si una columna tiene muchos números fuera de la diagonal, el modelo es demasiado "liberal" al asignar esa etiqueta.
        ○ Si una fila tiene muchos números fuera de la diagonal, el modelo no está logrando capturar bien esa categoría real.

Métricas de Desempeño por Clase
Cuando trabajamos con clasificación multi-clase ($k > 2$), las métricas se calculan de manera individual para cada categoría. Esto permite identificar exactamente en qué etiquetas el modelo es fuerte y en cuáles falla.
    Recall (Exhaustividad) por clase
    Mide la capacidad del modelo para encontrar todos los ejemplos de la clase real $i$.
        ○ Definición: Fracción de ejemplos de la clase $i$ correctamente clasificados.
        ○ Cálculo: Es el valor de la celda en la diagonal ($c_{ii}$) dividido por la suma de toda su fila ($\sum_{j} c_{ij}$).
        ○ Pregunta clave: De todos los que son realmente de la clase $i$, ¿cuántos atrapó el modelo?
    Precision (Precisión) por clase
    Mide la calidad de la predicción del modelo para la clase $i$.
        ○ Definición: Fracción de ejemplos asignados a la clase $i$ que realmente pertenecen a dicha clase.
        ○ Cálculo: Es el valor de la celda en la diagonal ($c_{ii}$) dividido por la suma de toda su columna ($\sum_{j} c_{ji}$).
        ○ Pregunta clave: De todos los que el modelo dijo que eran de la clase $i$, ¿cuántos eran correctos?
    Accuracy Global (Exactitud)
    Es la métrica general del modelo para todas las categorías.
        ○ Definición: Fracción total de ejemplos correctamente clasificados en todo el conjunto de datos ($1 - \text{error rate}$).
        ○ Cálculo: Es la suma de toda la diagonal principal dividida por la suma de todos los elementos de la matriz:
$$\text{Accuracy} = \frac{\sum_{i} c_{ii}}{\sum_{j} \sum_{i} c_{ij}}$$

Micro-averaging vs. Macro-averaging
Cuando trabajas con múltiples clases (por ejemplo: perro, gato, pájaro), obtienes métricas individuales para cada una. El desafío es cómo combinar esos resultados en un solo número para evaluar el desempeño global del modelo.
Existen dos estrategias principales para promediar:
    Macro-averaging (Promedio por clase)
    Esta técnica trata a todas las clases por igual, sin importar cuántos ejemplos tenga cada una.
        ○ Procedimiento: Calculas la métrica (como Precision o Recall) para cada clase de forma independiente y luego sacas el promedio aritmético simple de esos resultados.
        ○ Cuándo usarlo: Es ideal cuando quieres que las clases pequeñas (con pocos datos) tengan la misma importancia que las clases grandes.
    Micro-averaging (Promedio global)
    Esta técnica se enfoca en el rendimiento total del sistema, tratando cada instancia de dato como igual.
        ○ Procedimiento: Primero sumas todos los VP, FP, FN y VN de todas las clases para crear una "gran matriz de confusión binaria" combinada. Luego, calculas la métrica sobre esos totales.
        ○ Cuándo usarlo: Es mejor cuando tienes clases muy desbalanceadas y te interesa saber qué tan bien le va al modelo en el conteo total de casos.

Ejemplo Completo: Micro vs. Macro Averaging (Spam)
Este método se usa para evaluar el desempeño global cuando tenemos varias clases. El proceso se divide en:
    Análisis por Clases Individuales
    Primero, el sistema se evalúa como si fueran 3 problemas binarios distintos.
    Clase	Matriz 2x2	Cálculo de Precision	Resultado
    1. Urgent	VP=8, FP=11	P_1=8/(8+11)	0.42
    2. Normal	VP=60, FP=55	P_2=60/(60+55)	0.52
    3. Spam	VP=200, FP=33	P_3=200/(200+33)	0.86
    
    Macro-average: El promedio de clases
    Se calcula promediando los resultados finales de cada tabla anterior. Trata a todas las clases por igual.
    macroaverage precision=(0.42+0.52+0.86)/3=0.60
        ○ Nota clave: Este valor es bajo porque las clases con pocos datos (como Urgent) tienen el mismo peso que las grandes.
    
    Micro-average (Pooled): El promedio de instancias
    Se crea una cuarta tabla llamada "Pooled" (agrupada) sumando los valores de las tres anteriores. Trata a todos los documentos por igual.
        ○ Suma de VP (yes): 8+60+200=268
        ○ Suma de FP (no): 11+55+33=99
    microaverage precision=268/(268+99)=0.73
        ○ Nota clave: Este valor es más alto porque el éxito en la clase Spam (que es la más frecuente) domina el resultado.
    
    Conclusiones del Docente (Puntos clave)
        ○ Dominio del Micro-promedio: Los resultados micro son dominados por las clases más frecuentes (en este caso, Spam). Si te va bien en lo que más hay, tu micro será alto.
        ○ Sesgo del Macro-promedio: Los macro pueden sobre-representar a clases minoritarias. Si fallas en una clase pequeña, el macro bajará drásticamente aunque el resto del sistema sea casi perfecto.

Factores que Afectan el Desempeño
Antes de medir, hay que entender que el éxito de un modelo no solo depende del algoritmo, sino de las condiciones externas.
    • Distribución de las clases: Si una clase tiene muchos más datos que otra (desbalance), las métricas como el Accuracy pueden engañarte.
    • Costo de clasificaciones erróneas: No todos los errores valen lo mismo (visto en la sección de Matriz de Costo).
    • Tamaño de los datos: Un dataset muy pequeño no permite al modelo aprender bien el patrón.
        ○ Curva de Aprendizaje: A medida que aumenta el tamaño de la muestra (Sample Size), el Accuracy suele subir y estabilizarse. Si la curva es muy plana, añadir más datos podría no ayudar más.

Métodos para Evaluar la Generalización
La meta es saber qué tan bien funcionará el modelo con datos que nunca ha visto. Para eso usamos estas técnicas de partición:
    Holdout
    Es el método más básico: divides tus datos etiquetados en dos grupos.
        ○ Proporción común: $2/3$ para entrenamiento (training) y $1/3$ para evaluación (testing).
        ○ Limitaciones: Si el set de entrenamiento es muy pequeño, el modelo sale sesgado; si el de test es muy pequeño, el Accuracy no es confiable.
    Random Subsampling (Submuestreo aleatorio)
    Es como repetir el método Holdout varias veces con diferentes particiones aleatorias.
        ○ Ventaja: Permite obtener una distribución de los errores para ver qué tan estable es el modelo.
        ○ Riesgo: Algunos datos podrían usarse siempre para entrenar y nunca para evaluar, o viceversa.
    Cross-validation (Validación Cruzada)
    Es el estándar de la industria para aprovechar todos los datos.
        ○ Proceso: El dataset se divide en $k$ conjuntos o "folds".
        ○ Iteración: Se entrena $k$ veces. En cada vez, se usa un fold distinto para test y los $k-1$ restantes para entrenar.
        ○ Variante extrema: Leave-one-out ($k=n$), donde se entrena con todos los datos menos uno, y se repite para cada dato del dataset.

Problemas Prácticos en la Clasificación
Al final, los errores que comete el modelo suelen caer en estas dos categorías:
    1. Errores de entrenamiento: Ocurren cuando el modelo es demasiado simple y no tiene capacidad de aprender el patrón (Underfitting).
    2. Errores de generalización: Ocurren cuando el modelo se hace demasiado específico a los datos de entrenamiento y falla con datos nuevos (Overfitting).

18. Capacidad de Aprendizaje: Flexibilidad del Modelo
Para que un modelo sea útil, debe ser capaz de aprender la estructura de los datos sin ser tan rígido que ignore el patrón, ni tan flexible que memorice el ruido. En regresión, esto se controla con el orden del polinomio ($M$).
18.1. Underfitting (Subajuste)
Ocurre cuando el modelo es demasiado simple para los datos.
    • $M = 0$ y $M = 1$: El modelo intenta explicar una curva usando una línea recta.
    • Resultado: Error alto tanto en entrenamiento como en test. El modelo "no se entera" de qué trata el problema.

18.2. Ajuste Óptimo (Generalización)
Es el punto de equilibrio donde el modelo captura la esencia del patrón.
    • $M = 3$: La curva roja (modelo) se solapa casi perfectamente con la verde (realidad).
    • Resultado: Error bajo en todos los escenarios. El modelo ha generalizado correctamente.

18.3. Overfitting (Sobreajuste)
Ocurre cuando el modelo es demasiado complejo y tiene "demasiada memoria".
    • $M = 9$: El modelo se esfuerza por pasar por cada punto azul, creando oscilaciones absurdas que no existen en el patrón real.
    • Resultado: Error cero en entrenamiento, pero error masivo en datos nuevos. El modelo memorizó el ruido.




1. Diferencias entre Aprendizaje Supervisado y No Supervisado
Este apartado es fundamental para entender cómo las máquinas procesan la información y qué resultados esperamos de ellas.
1.1. Aprendizaje Supervisado (The Master-Student Model)
Se basa en la idea de que el desarrollador actúa como un guía o maestro para el algoritmo.
    • Concepto clave: La salida o respuesta del algoritmo ya es conocida de antemano.
    • Datos Etiquetados: Se entrena al modelo con datos que incluyen la "respuesta correcta".
        ○ Ejemplo: Para clasificar animales, usamos imágenes que ya vienen marcadas como "perro", "gato", etc..
    • Algoritmos comunes:
        ○ Regresión lineal y logística.
        ○ Clasificación de clases múltiples.
        ○ Máquinas de vectores de soporte (SVM).
1.2. Aprendizaje No Supervisado (Self-Discovery Model)
Está más alineado con la Inteligencia Artificial pura, ya que la computadora debe identificar procesos y patrones complejos sin intervención humana.
    • Concepto clave: No hay respuestas correctas ni incorrectas predefinidas. El algoritmo busca una "verdad objetiva" basada en la estructura de los datos .
    • Datos NO Etiquetados: Se entra al problema de manera "ciega". El algoritmo agrupa elementos que comparten características similares sin saber cómo se llaman.
        ○ Ejemplo: Puede agrupar figuras de 4 lados sin saber que se llaman "cuadrados", simplemente porque detecta que son similares entre sí [03:44].
    • Algoritmos comunes:
        ○ Clustering o agrupamiento (como K-means).
        ○ Reglas de asociación [01:55].
1.3. Cuadro Comparativo de Enfoque (Ejemplo Geométrico)
Características	Supervisado	No Supervisado
Entrada	Formas geométricas de colores.	Formas geométricas de colores
Instrucción	"4 lados es un cuadrado, píxel rojo es color rojo".	"Ordena estas figuras en grupos lógicos".
Resultado	Grupos con nombres específicos (Cuadrado Azul).	Grupos basados en similitud (Grupo A, Grupo B).
Fortaleza	Precisión en tareas conocidas.	Capacidad de resolver problemas complejos sin guía.

1.4. ¿Cuál elegir?
La elección depende de dos factores [04:21]:
    1. Estructura y volumen de los datos: ¿Están etiquetados o son datos brutos?
    2. Objetivo del problema: ¿Necesitas predecir un valor específico o descubrir relaciones ocultas?
    Nota para el examen: Muchos problemas reales utilizan ambos tipos de algoritmos para construir modelos predictivos robustos.

Referencia extra: 
DIFERENCIA ENTRE APRENDIZAJE SUPERVISADO Y NO SUPERVISADO



Bases de datos desbalanciadas 
Diapositiva 20
Ensamble: Random Forest (Bagging) 🌲🌲🌲
Mejora la precisión combinando múltiples árboles de decisión independientes. Su fuerza reside en la diversidad y el paralelismo.
¿Cómo funciona?
    • Bootstrapping (Muestreo con Reemplazo): Cada árbol se entrena con un subconjunto aleatorio del dataset. Al ser con reemplazo, un mismo dato puede repetirse en el mismo árbol, mientras que otros quedan fuera (datos Out-of-Bag). Esto reduce la varianza.
    • Agregación (Voting): Para clasificar, se toma la votación mayoritaria. La clase más frecuente entre todos los árboles es la ganadora.
    • Selección Aleatoria de Características: En cada división (split) del árbol, solo se considera un grupo al azar de columnas (features). Esto evita que un solo atributo dominante haga que todos los árboles sean iguales.
Control de Overfitting y Generalización:
    • Podado (Pruning): Se limita la profundidad máxima (max_depth) y el mínimo de muestras por hoja (min_samples_leaf) para que los árboles no memoricen el ruido.
    • Número de Árboles (n_estimators): A diferencia de otros modelos, agregar más árboles no suele causar sobreajuste, sino que estabiliza el error.

Gradient Boosting: Aprendizaje Secuencial 🚀
A diferencia de Random Forest, aquí los árboles se construyen uno tras otro para minimizar el error total.
¿Cómo funciona?
    • Estrategia Secuencial: Cada nuevo árbol tiene la misión específica de corregir los errores (residuos) del modelo anterior.
    • Aprender del Residuo: El modelo actual se entrena sobre la diferencia entre el valor real y la predicción previa. Así, cada paso "pule" el resultado final.
    • Suma Ponderada: El resultado final no es un promedio, sino la suma de las pequeñas correcciones de todos los árboles.
    • Gradiente Descendente: Utiliza el concepto matemático de gradiente para encontrar la dirección exacta en la que debe ajustar los pesos para minimizar la función de pérdida.
Control de Overfitting y Generalización:
    • Tasa de Aprendizaje (learning_rate): Determina qué tan fuerte es la corrección de cada árbol. Valores bajos (ej. 0.01) requieren más árboles pero logran una mejor generalización.
    • Early Stopping: Se detiene el entrenamiento automáticamente cuando el error en los datos de prueba deja de mejorar, evitando que el modelo se vuelva demasiado complejo.
    • Subsampling: Entrenar cada árbol con solo una fracción del dataset (ej. 80%) añade aleatoriedad y reduce el sesgo.

Clasificador KNN (K-Nearest Neighbors) 📍
Es uno de los algoritmos más simples e intuitivos. Se basa en la premisa: "Dime con quién andas y te diré quién eres".
Conceptos Clave:
    • Basado en Instancias: No construye un modelo matemático interno (como una ecuación). En su lugar, memoriza el dataset de entrenamiento y consulta los datos guardados cada vez que debe clasificar uno nuevo.
    • Algoritmo "Lazy" (Perezoso): Se le llama así porque no hace nada de "esfuerzo" durante la fase de entrenamiento. Todo el trabajo pesado (cálculo de distancias) ocurre recién en la fase de predicción.
    • El parámetro $k$: Es el número de vecinos que el algoritmo consultará.
        ○ Si $k=3$, mirará los 3 puntos más cercanos.
        ○ La predicción final se elige por mayoría de votos entre esos $k$ vecinos.
¿Cómo funciona?
    1. Calcula la distancia (generalmente Euclidiana) entre el punto nuevo y todos los demás puntos del dataset.
    2. Selecciona los $k$ puntos más cercanos.
    3. Asigna al punto nuevo la categoría más común entre esos $k$ vecinos.
Control de Overfitting y Generalización:
    • Valor de $k$ pequeño (ej. $k=1$): El modelo es muy sensible al ruido y tiende al overfitting.
    • Valor de $k$ grande: El modelo se vuelve más suave y generaliza mejor, pero si es demasiado grande, puede ignorar patrones locales importantes (underfitting).
    • Escalamiento de Datos: Es obligatorio normalizar o estandarizar los datos antes de usar KNN. Como se basa en distancias, si una variable tiene números muy grandes (ej. Salario) y otra pequeños (ej. Edad), la variable grande dominará injustamente la predicción.

Cuestionario: Aplicación de K-Nearest Neighbors (KNN)
    Opción 1: Predecir el tipo de flor según sus características
        ○ Respuesta: SÍ (Es aplicable).
        ○ Justificación: Es un problema de clasificación multiclase clásico. KNN funciona excelente aquí porque flores de la misma especie suelen tener medidas (pétalos/sépalos) similares, agrupándose en el espacio de características por cercanía geométrica.
    Opción 2: Predecir si una acción de la bolsa subirá o bajará
        ○ Respuesta: NO (No es el algoritmo ideal).
        ○ Justificación: Aunque parece una clasificación binaria (sube/baja), los datos bursátiles son series temporales. KNN es un algoritmo "perezoso" que no entiende la secuencia lógica ni la dependencia del tiempo; solo compara fotos fijas del pasado sin considerar el contexto de cuándo ocurrió cada movimiento.
    Opción 3: Predecir supervivencia en el Titanic
        ○ Respuesta: SÍ (Es aplicable).
        ○ Justificación: Es un problema de clasificación binaria. El algoritmo identifica "perfiles" de pasajeros similares (misma cabina, rango de edad, sexo) para determinar la probabilidad de supervivencia basada en los vecinos más cercanos del dataset histórico.

Fundamentos de KNN: Métricas de Distancia y Escalado
El algoritmo KNN (K-Nearest Neighbors) basa sus decisiones en la cercanía geométrica entre puntos. Para que esta "cercanía" sea real y justa, debemos entender cómo se mide y cómo preparar los datos.
    1. Métricas de Distancia (¿Cómo mide el algoritmo?)
    Para calcular qué tan "lejos" está un punto de otro, KNN utiliza fórmulas matemáticas. La más versátil es la Distancia de Minkowski, que es una fórmula general:
    
    Dependiendo del valor que le demos a , obtenemos las dos métricas más utilizadas:
        ○  (Distancia de Manhattan): Mide la distancia siguiendo rutas en ángulos rectos (como caminar por las calles de una ciudad en cuadrícula). Es útil cuando los datos tienen muchísimas dimensiones.
        ○  (Distancia Euclidiana): Es la "línea recta" más corta entre dos puntos. Es la opción por defecto porque es la más intuitiva y funciona bien en la mayoría de los casos.
    ¿Por qué estas? Son eficientes de calcular y fáciles de interpretar, aunque existen otras (como Coseno para texto o Mahalanobis para datos correlacionados), Minkowski ofrece flexibilidad total.
    
    2. El Problema de las Escalas (Dominancia de Atributos)
    Sin una preparación previa, el algoritmo puede ser "engañado" por el tamaño de los números.
        ○ Ejemplo: Si comparas Edad (0-100) contra Ingreso ($150K - $10M), una pequeña variación en el dinero (ej. $1,000) tendrá un impacto matemático enorme, mientras que una diferencia de 20 años en edad no significará nada para la fórmula.
        ○ Resultado: El atributo con números más grandes "se traga" a los pequeños, volviéndolos irrelevantes.
    
    3. La Solución: Normalización (Min-Max Scaling)
    La normalización es el proceso de "democratizar" los datos. Consiste en transformar cada variable para que su valor mínimo sea 0, su máximo sea 1, y el resto quede en ese rango.
    ¿Qué logramos con el rango 0 a 1?
        a. Justicia: Todas las columnas compiten en igualdad de condiciones. Una diferencia de 0.2 en "Edad" ahora pesa lo mismo que una de 0.2 en "Salario".
        b. Precisión: La distancia euclidiana ahora compara proporciones reales y no magnitudes arbitrarias.
        c. Velocidad: El algoritmo procesa mucho más rápido números pequeños y controlados.
        Regla de Oro: Siempre que utilices algoritmos basados en distancias (KNN, K-Means, SVM), el escalado o normalización es obligatorio. Si no escalas, tu modelo está operando "a ciegas". ⚖️📏

Técnicas para Escalar Atributos
Como vimos, el escalado es vital. Dependiendo de la distribución de tus datos, elegirás una de estas dos fórmulas:
    1. Estandarización (Media Cero y Varianza Unitaria)
    También conocida como Z-Score Normalization. Transforma los datos para que tengan una media ($\mu$) de 0 y una desviación estándar ($\sigma$) de 1.
        ○ Fórmula:
$$z = \frac{x - \mu}{\sigma}$$
        ○ Cuándo usarla: Es ideal cuando tus datos siguen una distribución normal (campana de Gauss) o cuando tienes valores atípicos (outliers), ya que no confina los datos a un rango exacto, haciéndola más robusta ante valores extremos.
    2. Normalización (Rango entre 0 y 1)
    Llamada también Min-Max Scaling. Escala todos los valores de una columna al intervalo exacto $[0, 1]$.
        ○ Fórmula:
$$x_{norm} = \frac{x - min}{max - min}$$
        ○ Cuándo usarla: Es la mejor opción para algoritmos como KNN o Redes Neuronales, donde necesitas que todos los atributos tengan exactamente el mismo peso y rango. No es muy buena si tienes valores atípicos, porque estos "comprimirán" el resto de los datos en un rango muy pequeño.
    
    ⚠️ Regla de Oro: El "Leakage" de Datos
    El slide menciona algo fundamental: Aplica la misma transformación a training y testing.
        ○ El error común: Calcular el mínimo/máximo o la media por separado para cada grupo.
        ○ Lo correcto: Calculas los valores de normalización (min, max, media) solo con los datos de training y usas esos mismos valores para transformar el set de testing.
        ○ ¿Por qué? Porque en la vida real no conoces los datos futuros (testing). Si usas información del set de prueba para escalar, estarías haciendo "trampa" (Data Leakage) y los resultados de tu modelo no serían realistas.

Vectores Sparse y Selección de K en KNN 🧠
    1. Vectores Sparse (Vectores Dispersos)
    Un vector sparse es aquel donde la gran mayoría de sus elementos son cero. En lugar de almacenar miles de ceros (lo cual es un desperdicio de memoria), solo guardamos las posiciones que tienen datos reales.
        Analogía de la Lista de Compras: 🛒
            § Vector Normal: Anotas los 10,000 productos de un súper y pones "0" en lo que no compraste y "1" en lo que sí.
            § Vector Sparse: Solo anotas: "Compré leche en el pasillo 5 y pan en el pasillo 20". Ignoras el resto.
    ¿Para qué se usan?
        ○ NLP (Procesamiento de Lenguaje): En un vocabulario de 10,000 palabras, una frase como "El gato corre" solo activa 3 posiciones; las otras 9,997 son ceros.
        ○ Sistemas de Recomendación: Netflix tiene miles de películas, pero tú solo has visto 50. Tu vector de usuario está lleno de ceros en las películas no vistas.
        ○ Genética: Al analizar el ADN, solo unos pocos genes están "activos" o mutados entre miles de posibilidades.
    Similitud Coseno: La métrica ideal
    Para comparar vectores sparse, no usamos la distancia euclidiana (porque los ceros la confunden), usamos el Coseno del ángulo:
    $$\cos(\mathbf{x}, \mathbf{y}) = \frac{\mathbf{x} \cdot \mathbf{y}}{\|\mathbf{x}\| \|\mathbf{y}\|}$$
    Esta métrica se enfoca en la orientación. Si dos documentos tratan del mismo tema, sus vectores apuntarán en la misma dirección, sin importar cuántos ceros tengan por no usar el resto del diccionario.
    
    2. ¿Cómo elegir el valor de K en KNN? 📍
    Elegir K es como ajustar el enfoque de una cámara. Define qué tan "fino" o "grueso" será el aprendizaje:
        ○ Evita $K=1$ (Overfitting): El modelo se vuelve "nervioso". Cualquier dato ruidoso o error puntual hará que la predicción falle por seguir ciegamente al vecino más cercano.
        ○ Evita un K muy grande (Underfitting): Si el K es casi igual al total de datos, el modelo siempre dirá que la respuesta es la "clase mayoritaria", ignorando los patrones locales.
        ○ Usa siempre un número IMPAR: Esto evita empates (ej. 2 vs 2) en problemas de clasificación binaria.
        ○ Regla de la Raíz Cuadrada: Una técnica rápida de inicio es usar $K \approx \sqrt{n}$ (donde $n$ es el número total de datos).
    El Método Profesional: "Elbow Method" (Método del Codo)
    Consiste en entrenar el modelo con varios valores de K (ej. del 1 al 20) y graficar el error.
        a. El error bajará rápido al principio.
        b. Llegará un punto donde la mejora es mínima y la curva se estabiliza.
        c. El punto justo donde la curva se dobla (el "codo") es el valor de K ideal.

La Maldición de la Dimensionalidad 🌌⚠️
Este fenómeno ocurre cuando aumentamos el número de características (columnas) de un dataset. Aunque parece que "más información es mejor", en el aprendizaje automático esto genera problemas graves de rendimiento y precisión.
    ¿Por qué arruina el modelo?
        a. El espacio se vuelve "vacío" (Sparsity): A medida que agregas dimensiones, el volumen del espacio crece de forma exponencial. Los datos se quedan aislados y extremadamente lejos unos de otros.
            § En 1D: Los puntos están compactos en una línea.
            § En 2D: Se esparcen en un plano.
            § En 3D o más: La densidad baja tanto que el algoritmo ya no encuentra "vecinos" reales; todos parecen extraños entre sí.
        b. Las distancias pierden sentido: Es el problema más crítico para KNN. En alta dimensionalidad, la diferencia entre la distancia al vecino más cercano y al más lejano se vuelve casi cero. Si todos los puntos están "a la misma distancia", KNN no puede clasificar y termina eligiendo al azar.
        c. Overfitting (Sobreajuste): Con demasiadas variables, el modelo encuentra correlaciones por pura coincidencia (ruido) que no existen en la realidad. El algoritmo "memoriza" estas coincidencias en lugar de aprender el patrón real.
    ¿Cómo solucionarlo?
    Para mantener un modelo eficiente y generalizable, se aplican estas estrategias:
        ○ Selección de Atributos (Feature Selection): Eliminar manualmente las columnas que no aportan información relevante o que están repetidas.
        ○ Reducción de Dimensionalidad: Utilizar algoritmos como PCA (Principal Component_Analysis) para comprimir muchas variables en unas pocas que mantengan la mayor parte de la información.
        ○ Aumentar el Dataset: Para llenar el "vacío" de muchas dimensiones, se necesitaría una cantidad de datos astronómica, lo cual rara vez es posible.
        Resumen: En Machine Learning, "menos es más". Reducir las dimensiones ayuda a que los algoritmos de distancia (como KNN) funcionen correctamente y no se pierdan en el vacío matemático. 📉⚖️

Clasificación Basada en Naïve Bayes 🧠📊
Los clasificadores bayesianos son una familia de modelos basados en el Teorema de Bayes. Este teorema es una fórmula matemática que permite actualizar la probabilidad de una hipótesis a medida que aparece nueva evidencia.
    1. El Teorema de Bayes
    La fórmula fundamental para calcular la probabilidad es:
    $$P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}$$
        ○ $P(H|E)$ (Posterior): Es la probabilidad de que ocurra la hipótesis $H$ dado que hemos observado la evidencia $E$. Es lo que el modelo intenta predecir.
        ○ $P(E|H)$ (Likelihood/Verosimilitud): La probabilidad de observar la evidencia $E$ si la hipótesis $H$ fuera cierta.
        ○ $P(H)$ (Prior/Probabilidad Previa): La probabilidad inicial de la hipótesis antes de ver cualquier evidencia.
        ○ $P(E)$ (Evidencia): La probabilidad total de observar la evidencia bajo todas las hipótesis posibles.
    
    2. Clasificador Naïve Bayes (El "Ingenuo")
    Es la implementación más conocida de esta familia. Se le denomina "Naive" (Ingenuo) porque asume una independencia absoluta entre todas las características (atributos) del dataset. Aunque en la vida real los atributos suelen estar relacionados, esta simplificación permite realizar cálculos muy rápidos y eficientes.
        ○ ¿Para qué sirve? Es el estándar para la Clasificación de Texto, como la detección de SPAM o el análisis de sentimientos en redes sociales.
        ○ Ventajas:
            § Es extremadamente rápido para entrenar y realizar predicciones.
            § Funciona muy bien incluso con datasets pequeños.
            § A diferencia de KNN, no sufre tanto por la "maldición de la dimensionalidad".
        ○ Desventajas: Su precisión puede verse afectada si los atributos están altamente correlacionados, ya que rompen el supuesto de independencia.
    
    3. Variantes de Naïve Bayes según los datos
    Dependiendo de la naturaleza de tus atributos, existen diferentes versiones del modelo:
        ○ Gaussian Naïve Bayes: Se utiliza cuando los atributos son numéricos continuos y siguen una distribución normal (campana de Gauss).
        ○ Multinomial Naïve Bayes: Es el ideal para trabajar con frecuencias o conteos, como la cantidad de veces que aparece una palabra en un documento.
        ○ Bernoulli Naïve Bayes: Se usa para datos binarios, donde solo importa si una característica está presente o no (0 o 1).
    4. Otros Modelos Bayesianos
Además del clasificador Naïve, dentro de esta familia existen las Redes Bayesianas, que son modelos gráficos que sí permiten representar dependencias más complejas entre las variables.