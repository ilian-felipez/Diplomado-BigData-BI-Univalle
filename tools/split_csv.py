"""Divide un CSV UTF-8 por registros, con cabecera en cada parte."""

import argparse
import csv
import hashlib
import io
from pathlib import Path


def split_csv(sources, target, max_bytes=45_000_000):
    """Combina fuentes en orden y valida antes de devolver las partes."""
    sources = [Path(p) for p in sources]
    target = Path(target)
    if max_bytes <= 0:
        raise ValueError("--max-bytes debe ser positivo")
    if list(target.parent.glob(f"{target.stem}.part-*.csv")):
        raise FileExistsError("Ya existen partes; muévalas antes de repetir")
    csv.field_size_limit(2**31 - 1)
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")

    def encode(row):
        buffer.seek(0)
        buffer.truncate(0)
        writer.writerow(row)
        return buffer.getvalue().encode("utf-8")

    parts, header, output = [], None, None
    count, size = 0, 0
    expected = hashlib.sha256()
    try:
        for source in sources:
            with source.open(encoding="utf-8-sig", newline="") as stream:
                rows = csv.reader(stream, strict=True)
                current = next(rows, None)
                if current is None:
                    raise ValueError(f"CSV vacío: {source}")
                if header is None:
                    header, header_bytes = current, encode(current)
                    if len(header_bytes) >= max_bytes:
                        raise ValueError("La cabecera excede el límite")
                elif current != header:
                    raise ValueError(f"Cabecera diferente: {source}")
                for row in rows:
                    if len(row) != len(header):
                        raise ValueError(f"Número de columnas incorrecto: {source}, registro {count + 1}")
                    data = encode(row)
                    if len(header_bytes) + len(data) >= max_bytes:
                        raise ValueError("Un registro con su cabecera excede el límite")
                    if output is None or size + len(data) >= max_bytes:
                        if output is not None:
                            output.close()
                        part = target.with_name(f"{target.stem}.part-{len(parts) + 1:02d}.csv")
                        output = part.open("xb")
                        parts.append(part)
                        output.write(header_bytes)
                        size = len(header_bytes)
                    output.write(data)
                    size += len(data)
                    expected.update(data)
                    count += 1
        # Un CSV con solo cabecera también produce una parte válida.
        if output is None:
            part = target.with_name(f"{target.stem}.part-01.csv")
            with part.open("xb") as stream:
                stream.write(header_bytes)
            parts.append(part)
        else:
            output.close()
        actual, checked = hashlib.sha256(), 0
        for part in parts:
            with part.open(encoding="utf-8", newline="") as stream:
                rows = csv.reader(stream, strict=True)
                if next(rows) != header:
                    raise ValueError(f"Cabecera inválida: {part}")
                for row in rows:
                    actual.update(encode(row))
                    checked += 1
            if part.stat().st_size >= max_bytes:
                raise ValueError(f"Parte demasiado grande: {part}")
        if checked != count or actual.digest() != expected.digest():
            raise ValueError("La validación de registros falló")
    except BaseException:
        if output is not None:
            output.close()
        # Solo se eliminan archivos creados por esta ejecución.
        for part in parts:
            part.unlink()
        raise
    for part in parts:
        print(f"{part}: {part.stat().st_size} bytes")
    print(f"Verificado: {count} registros, {len(header)} columnas")
    return parts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CSV UTF-8 de entrada")
    parser.add_argument("--max-bytes", type=int, default=45_000_000,
                        help="límite exclusivo por parte (predeterminado: 45000000)")
    parser.add_argument("--delete-source", action="store_true",
                        help="eliminar el original solo después de validar")
    args = parser.parse_args()
    try:
        split_csv([args.input], args.input, args.max_bytes)
        if args.delete_source:
            args.input.unlink()
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(1, f"Error: {error}\n")


if __name__ == "__main__":
    main()
