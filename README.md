# Convertidor de Audio a Texto

Este proyecto es una aplicación GUI desarrollada en Python que permite convertir archivos de audio a formato WAV, limpiar el ruido de fondo del audio y convertir el audio a texto, además de traducir el texto reconocido al español.

## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes bibliotecas de Python:

- tkinter
- pydub
- speech_recognition
- googletrans
- noisereduce
- numpy
- scipy

Puedes instalarlas usando `pip`:

```bash
pip install tkinter pydub speechrecognition googletrans==4.0.0-rc1 noisereduce numpy scipy
demás, debes tener instalado ffmpeg para permitir la conversión de archivos de audio. Puedes instalar ffmpeg desde su sitio web o usando un gestor de paquetes como apt

sudo apt install ffmpeg

git clone https://github.com/javierfevidaho/audio_to_text.git
cd audio_to_text

python main.py


Descripción del Código
El archivo principal del proyecto incluye las siguientes funcionalidades:

Convertir Audio a WAV: Selecciona un archivo de audio y lo convierte a formato WAV.
Limpiar Ruido de Audio: Reduce el ruido de fondo del archivo de audio.
Convertir Audio a Texto: Usa el servicio de reconocimiento de Google para convertir el audio a texto y lo traduce al español.
Funciones Principales
convert_to_wav(): Convierte el archivo de audio seleccionado a formato WAV.
clean_audio(file_path): Limpia el ruido de fondo del archivo de audio.
save_text_to_file(text): Guarda el texto reconocido y traducido en un archivo de texto.
convert_audio_to_text(): Convierte el archivo de audio a texto, lo traduce al español y guarda el resultado en un archivo de texto.
Interfaz Gráfica
La interfaz gráfica está construida usando tkinter y contiene dos botones:

Seleccionar y convertir audio a WAV: Abre un cuadro de diálogo para seleccionar un archivo de audio y lo convierte a WAV.
Convertir audio a texto y traducirlo: Abre un cuadro de diálogo para seleccionar un archivo de audio en formato WAV, lo limpia, lo convierte a texto, lo traduce al español y guarda el resultado en un archivo de texto.
Ejemplo de Uso
Ejecuta la aplicación.
Haz clic en el botón "Seleccionar y convertir audio a WAV" para seleccionar un archivo de audio y convertirlo a formato WAV.
Haz clic en el botón "Convertir audio a texto y traducirlo" para seleccionar un archivo WAV, limpiar el ruido de fondo, convertir el audio a texto y traducir el texto al español.
Contribuciones
Las contribuciones son bienvenidas. Por favor, crea un issue o un pull request para contribuir.

Licencia
Este proyecto está licenciado bajo la MIT License.

