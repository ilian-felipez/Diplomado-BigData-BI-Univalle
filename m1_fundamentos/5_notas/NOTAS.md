Resumen
Introduccion a big data
    1.  Ejemplos Organizacionales
        1. Bases de Datos Tradicionales:
        Se usan en bancos para registrar transacciones de forma segura mediante tablas fijas, consultas SQL y un estricto control de integridad, aunque no permiten un análisis avanzado de clientes.
        2. Business Intelligence (BI):
        Las cadenas de supermercados analizan sus datos históricos usando reportes, dashboards y un Data Warehouse para entender sus ventas, limitándose solo a datos estructurados.
        3. Big Data:
        El comercio electrónico procesa masivamente clics y redes sociales para analizar datos no estructurados en tiempo real, enfrentando una alta complejidad en el manejo de la información.
        4. Analítica Avanzada
        Plataformas de streaming usan modelos predictivos, Machine Learning y sistemas de recomendaciones para optimizar su servicio, buscando siempre anticipar el comportamiento del usuario.
    2. 5 V del Big Data
        1. Volumen:
        La cantidad masiva de datos generados cada segundo.
            Almacenamiento Distribuido: Técnica que guarda datos en múltiples servidores (nodos) en lugar de uno solo. Permite escalar horizontalmente y evita que el sistema caiga si un equipo falla.
            Data Lake (Lago de Datos): Un repositorio central que almacena grandes cantidades de datos en su formato original (bruto), ya sean estructurados (tablas) o no estructurados (videos, logs).
            Hadoop: Es el marco de trabajo pionero para el almacenamiento y procesamiento masivo. Usa el sistema de archivos HDFS para repartir datos y MapReduce para procesarlos por lotes.
            Spark: Es un motor de procesamiento mucho más rápido que Hadoop porque trabaja en memoria (RAM). Se usa para análisis en tiempo real, Machine Learning y ráfagas rápidas de datos.
            
            
        2. Velocidad:
            La rapidez con la que se crean, procesan y analizan los datos en tiempo real.
            Que en tiempo Tiempo real y que no 
            Apache kafka
            Spark streaming
            flink
        3. Variedad:
        Los diferentes formatos de datos (fotos, videos, texto, bases de datos).
            No sql
            Data lakes
            Nlp
            Vision comptacional
        4. Veracidad:
        La calidad y confiabilidad de los datos obtenidos.
            Calidad de los datos
            Data governance
            Data quality management 
            Limpieza de datos
            Valiación automatica
        5. Valor:
        La utilidad de convertir esos datos en beneficios o decisiones para la organización.
        
    Los datos son n actrivo estrategico
    3 tipos de analitica
        Analitica descriptiva
            Que paso complejidad baja impacto en el control
            Cuantas ventas se realizaron el mes pasado
            Que produtos fueron lo mas vendidos?
            Cual fue el ingreso toatl de la empresa
            Cuantos clientes visitaron la plataforma 
            Preguntas del pasado?
            Usa herramientas como el dashboartd powee bi tableau sistemas de reportes corporativos
        Analitica predictiva
            Que pasara complejidad media impacia de anticipacion
            Futuro?
            Que clietne tiene mayor probabilidad de abandonar el servico?
            Cual sera la demanda del proxmio mes?
            Que productso podrian vender mas en la proxima temporada
            No predice el futo reduce la incertidumbre de la toma de desiciones
            
        Analitica prescriptiva
            Que deberia hacer es de complejidad alta imptao en la optimizacion 
            Uqe deberia hacer?
            Nivel mas avanzado
            Que estrategia de precio maximiza las ventas
            Como asignar recursos de forma efieciente
            Que cmapaan de marketin deberia ejecutarse 
            Que rutas logisticas minimizan costos
Combina predicciones reglas de negocio optimizacione simlaciones 