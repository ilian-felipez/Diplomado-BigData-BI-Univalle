# Big Data, Analytics y Business Intelligence V1

Documentación personal del diplomado de la Universidad Privada del Valle (Univalle), Bolivia, gestión 2026. Reúne tareas, notebooks, datos, informes y apuntes para consulta y revisión académica.

[Plan de estudios](Big%20Data%2C%20Analytics%20y%20Business%20Intelligence%20V1.pdf). El orden de los módulos corresponde a las carpetas del repositorio.

## Módulos

| Carpeta | Módulo | Temas principales | Proyecto |
|---|---|---|---|
| [m1_fundamentos](m1_fundamentos/README.md) | 1. Transformación Digital y Fundamentos de Big Data | Transformación digital, madurez, ciclo del dato y Python | Diagnóstico del registro de nacimientos en Bolivia (2009–2015) |
| [m2_analytics](m2_analytics/README.md) | 2. Data Analytics: Procesos y Técnicas | Python, análisis exploratorio, regresión, clasificación y agrupamiento | Agrupamiento de perfiles musicales de Spotify |
| [m3_visualizacion](m3_visualizacion/README.md) | 3. Visualización de Datos y Data Discovery | Percepción visual, exploración, dashboards y narrativa con datos | Dashboard NOC/SOC de telemetría y amenazas de red |
| [m4_bi_predictivo](m4_bi_predictivo/README.md) | 4. Business Intelligence y Modelos Predictivos | ETL, almacenes de datos, OLAP y predicción | Análisis y predicción de fuga de clientes Telco |
| [m5_aplicaciones](m5_aplicaciones/README.md) | 5. Aplicaciones de Big Data en Entornos Digitales | Comportamiento de usuarios, estrategia comercial y procesamiento de datos | Sin entregables de proyecto integrador en la carpeta |

## Estructura

Cada módulo sigue esta organización; algunas carpetas todavía están vacías:

```text
mN_nombre/
  README.md       Índice del módulo
  1_clases/       Grabaciones locales, excluidas de Git
  2_recursos/     Material del docente
  3_tareas/       Ejercicios y entregas
  4_proyecto/     Proyecto integrador y sus datos e informes
  5_notas/
    NOTAS.md      Apuntes personales
```

Las grabaciones no se incluyen en el repositorio. Los archivos Power BI requieren Power BI Desktop; los notebooks requieren Python y un editor con soporte de Jupyter. No hay un entorno Python único ni una versión de Python fijada para todo el diplomado.

## Preparación de entornos

En Windows, crea un entorno separado para la tarea o el proyecto y selecciona ese intérprete como kernel del notebook. Estos son los seis archivos de dependencias disponibles:

- [m2_analytics/3_tareas/requirements.txt](m2_analytics/3_tareas/requirements.txt)
- [m2_analytics/4_proyecto/requirements.txt](m2_analytics/4_proyecto/requirements.txt)
- [m4_bi_predictivo/2_recursos/Clase 1 - Fundamentos y Evolución de Business Intelligence/requirements.txt](m4_bi_predictivo/2_recursos/Clase%201%20-%20Fundamentos%20y%20Evoluci%C3%B3n%20de%20Business%20Intelligence/requirements.txt)
- [m4_bi_predictivo/3_tareas/requirements.txt](m4_bi_predictivo/3_tareas/requirements.txt)
- [m4_bi_predictivo/4_proyecto/requirements.txt](m4_bi_predictivo/4_proyecto/requirements.txt)
- [m5_aplicaciones/3_tareas/requirements.txt](m5_aplicaciones/3_tareas/requirements.txt)

Ejemplo para las tareas de M2, desde la raíz del repositorio (comandos de instalación; no se han verificado instalando un entorno nuevo):

```powershell
python -m venv m2_analytics/3_tareas/.venv
m2_analytics/3_tareas/.venv/Scripts/python.exe -m pip install -r m2_analytics/3_tareas/requirements.txt
```

Usa el archivo correspondiente a cada trabajo y consulta su README para el directorio de ejecución. Los requisitos no siempre incluyen todas las dependencias de todos los notebooks; M1 y M3 no tienen un `requirements.txt` propio. Las versiones de las herramientas y la ejecución completa de los análisis no se han validado conjuntamente.

## Datasets y archivos grandes

No se deben versionar archivos mayores de 50 MB. Los CSV grandes se guardan como `<nombre>.part-NN.csv`, con cabecera repetida y partes menores de 45.000.000 bytes. Carga las partes en orden con pandas; no las concatenes directamente como texto.

Ejemplo de lectura desde la raíz, con pandas instalado:

```python
from pathlib import Path
import pandas as pd

carpeta = Path("m2_analytics/3_tareas/datasets")
partes = sorted(carpeta.glob("enron_spam.part-*.csv"))
assert partes, "No se encontraron partes del dataset"
df = pd.concat([pd.read_csv(p) for p in partes], ignore_index=True)
```

La utilidad [tools/split_csv.py](tools/split_csv.py) divide y valida los registros. Ejemplo ilustrativo desde la raíz; sustituye la ruta por un CSV UTF-8 existente y sin partes previas:

```powershell
python tools/split_csv.py "ruta/al/dataset.csv"
```

El límite predeterminado es exclusivo: 45.000.000 bytes por parte; `--max-bytes` lo cambia. El comando conserva el original y rechaza partes ya existentes. No uses `--delete-source` sin autorización del propietario.

Consulta las instrucciones específicas de [Enron](m2_analytics/3_tareas/datasets/README.md), [Spotify](m2_analytics/4_proyecto/data/raw/README.md) y [telemetría de red y actualización de Power BI](m3_visualizacion/4_proyecto/README.md). Los archivos reconstruidos grandes son para uso local.
