# CSV dividido en partes

Para Python 3 (Windows, Linux o macOS), desde esta carpeta. Las partes `Dataset_completo.part-NN.csv` conservan el orden y repiten la cabecera; cada archivo ocupa menos de 45.000.000 bytes. No se deben concatenar como texto sin quitar las cabeceras repetidas.

Para reconstruir `Dataset_completo.csv`, con pandas instalado, ejecuta esta línea en Python:

```python
import glob, pandas as pd; pd.concat((pd.read_csv(f) for f in sorted(glob.glob("Dataset_completo.part-*.csv"))), ignore_index=True).to_csv("Dataset_completo.csv", index=False)
```

Alternativa desde la terminal, solo con la biblioteca estándar (conserva los campos como texto, incluidas comillas y saltos de línea):

```sh
python -c "import csv,glob; from contextlib import ExitStack; csv.field_size_limit(2147483647); s=ExitStack(); files=sorted(glob.glob('Dataset_completo.part-*.csv')); assert files, 'No se encontraron partes'; readers=[csv.reader(s.enter_context(open(f, encoding='utf-8', newline=''))) for f in files]; headers=[next(r) for r in readers]; assert all(h==headers[0] for h in headers); w=csv.writer(s.enter_context(open('Dataset_completo.csv','w',encoding='utf-8',newline=''))); w.writerow(headers[0]); [w.writerows(r) for r in readers]; s.close()"
```

La reconstrucción sobrescribe el CSV de destino si existe; las partes se conservan. El archivo reconstruido puede superar el límite de GitHub: úsalo localmente y conserva las partes para versionar.

## Power BI

En Power BI Desktop, cambia el origen del PBIX a **Obtener datos > Carpeta** (Get Data > Folder) y selecciona esta carpeta. Filtra los nombres `Dataset_completo.part-*.csv` antes de combinar los archivos; cada parte tiene su propia cabecera. Elimina el paso que apunte al antiguo CSV y comprueba las columnas y el número total de filas después de actualizar.

También puedes reconstruir `Dataset_completo.csv` con el comando anterior y mantener el origen de archivo del PBIX. Para volver a dividirlo desde la raíz del repositorio, ejecuta `python tools/split_csv.py m3_visualizacion/4_proyecto/Dataset_completo.csv`; mueve primero las partes existentes, porque el script no las sobrescribe. El script divide y valida; el comando `python -c` anterior reconstruye.
