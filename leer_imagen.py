"""Extrae el texto de una imagen y lo imprime en la terminal.

Uso:
    python3 leer_imagen.py foto.png
    python3 leer_imagen.py            (si no pasas archivo, te lo pide)
"""
import sys

from PIL import Image
import pytesseract


def main():
    # 1. Obtener la ruta: del argumento, o preguntándola si no hay
    if len(sys.argv) > 1:
        ruta = sys.argv[1]
    else:
        ruta = input("Ruta de la imagen: ").strip().strip("'\"")

    # 2. Abrir la imagen
    try:
        imagen = Image.open(ruta)
    except (FileNotFoundError, OSError):
        print(f"No pude abrir la imagen: {ruta}")
        sys.exit(1)

    # 3. Extraer el texto (español + inglés)
    try:
        texto = pytesseract.image_to_string(imagen, lang="spa+eng")
    except pytesseract.TesseractError as error:
        print(f"Error de Tesseract (¿falta el idioma instalado?): {error}")
        sys.exit(1)

    # 4. Mostrarlo
    print(texto)


main()

