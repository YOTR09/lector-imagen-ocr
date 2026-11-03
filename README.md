# Lector de Texto en Imágenes (OCR por Consola)

Este programa toma una imagen (PNG, JPG, etc.) y extrae todo el texto visible para mostrarlo directamente en la terminal.

---

## ¿Cómo funciona por dentro?

Para entender el proyecto fácilmente, piensa en él como un equipo de dos piezas:

```
[ Tu Imagen ] 
      │
      ▼
[ leer_imagen.py ] (Python + Pillow)
  └─ Abre el archivo y valida la ruta.
      │
      ▼
[ pytesseract ] (El intermediario / Puente)
  └─ Le envía la imagen a Tesseract y le pide el resultado.
      │
      ▼
[ Tesseract OCR ] (El cerebro del sistema)
  └─ Analiza píxeles, reconoce caracteres y devuelve el texto.
      │
      ▼
[ Tu Terminal ] (Imprime el texto final)
```

1. **Python (`leer_imagen.py` + `pytesseract`):** Es solo el "puente". Python por sí solo no sabe leer letras dentro de imágenes; solo se encarga de recibir tu archivo, abrirlo y llamar a Tesseract.
2. **Tesseract OCR:** Es el motor real (creado por HP y mantenido por Google) que hace la "magia" de reconocer patrones de texto en imágenes.

---

## 1. Requisitos e Instalación

### Paso 1: Instalar el motor OCR en el sistema (Nobara / Fedora)
Como Tesseract es un programa a nivel de sistema operativo, debemos instalarlo con permisos de administrador:

```bash
sudo dnf install tesseract tesseract-langpack-spa
```

**¿Para qué sirve cada parte de este comando?**
* `sudo dnf install`: Usa el gestor de paquetes de Nobara/Fedora para instalar software en el sistema.
* `tesseract`: El motor OCR principal. Por defecto ya viene preparado para reconocer el alfabeto en **inglés**.
* `tesseract-langpack-spa`: El **paquete de idioma español**. Incluye los modelos entrenados para entender acentos (**á, é, í, ó, ú**), la **ñ**, diéresis (**ü**) y signos como **¿** y **¡**. Sin esto, confundiría esas letras.

---

### Paso 2: Entorno virtual y librerías de Python
*(Este paso ya está listo en tu carpeta, pero si necesitas rehacerlo alguna vez, es así)*:

```bash
# Crear el entorno virtual aislado
python3 -m venv .venv

# Instalar las librerías necesarias
.venv/bin/pip install pytesseract pillow
```

* `pillow`: Librería para abrir y manipular formatos de imagen.
* `pytesseract`: Conector en Python para hablar con Tesseract.

---

## 2. Formas de Uso

### Opción A: Pasándole la imagen como argumento directo
Ideal cuando ya sabes la ruta del archivo o quieres integrarlo con otros comandos:

```bash
.venv/bin/python leer_imagen.py /ruta/a/tu/imagen.png
```

### Opción B: Modo interactivo
Si ejecutas el script sin argumentos, te pedirá amablemente la ruta por pantalla:

```bash
.venv/bin/python leer_imagen.py
```
> Salida esperada:
> ```text
> Ruta de la imagen: /home/usuario/captura.png
> (Aquí saldrá el texto reconocido...)
> ```

---

## 3. Consejos para mejores resultados
* **Buena resolución:** Cuanto más nítido y grande sea el texto, mejor lo leerá.
* **Contraste:** Texto negro sobre fondo blanco funciona casi al 100%. Fondos con degradados o sombras pueden requerir limpiar la imagen previamente.
