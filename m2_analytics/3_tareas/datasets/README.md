# CSV dividido en partes

Para Python 3 (Windows, Linux o macOS), desde esta carpeta. Las partes `enron_spam.part-NN.csv` conservan el orden y repiten la cabecera; cada archivo ocupa menos de 45.000.000 bytes. No se deben concatenar como texto sin quitar las cabeceras repetidas.

Para reconstruir `enron_spam.csv`, con pandas instalado, ejecuta esta línea en Python:

```python
import glob, pandas as pd; pd.concat((pd.read_csv(f) for f in sorted(glob.glob("enron_spam.part-*.csv"))), ignore_index=True).to_csv("enron_spam.csv", index=False)
```

Alternativa desde la terminal, solo con la biblioteca estándar (conserva los campos como texto, incluidas comillas y saltos de línea):

```sh
python -c "import csv,glob; from contextlib import ExitStack; csv.field_size_limit(2147483647); s=ExitStack(); files=sorted(glob.glob('enron_spam.part-*.csv')); assert files, 'No se encontraron partes'; readers=[csv.reader(s.enter_context(open(f, encoding='utf-8', newline=''))) for f in files]; headers=[next(r) for r in readers]; assert all(h==headers[0] for h in headers); w=csv.writer(s.enter_context(open('enron_spam.csv','w',encoding='utf-8',newline=''))); w.writerow(headers[0]); [w.writerows(r) for r in readers]; s.close()"
```

La reconstrucción sobrescribe el CSV de destino si existe; las partes se conservan. El archivo reconstruido puede superar el límite de GitHub: úsalo localmente y conserva las partes para versionar.
