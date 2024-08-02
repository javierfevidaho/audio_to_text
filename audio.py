import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment
import speech_recognition as sr
from googletrans import Translator
import noisereduce as nr
import numpy as np
import os
from scipy.io import wavfile

def convert_to_wav():
    # Abrir el cuadro de diálogo para seleccionar el archivo
    file_path = filedialog.askopenfilename(title="Seleccionar archivo de audio", filetypes=[("Audio Files", "*.mp3 *.m4a *.flac *.ogg *.wav")])
    if file_path:
        try:
            # Convertir el archivo seleccionado a formato WAV
            audio = AudioSegment.from_file(file_path)
            output_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
            if output_path:
                audio.export(output_path, format="wav")
                messagebox.showinfo("Éxito", "Archivo convertido y guardado como WAV.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir el archivo: {e}")

def clean_audio(file_path):
    try:
        # Leer el archivo de audio
        rate, data = wavfile.read(file_path)
        # Reducir el ruido
        reduced_noise = nr.reduce_noise(y=data, sr=rate)
        # Guardar el archivo limpio
        clean_path = os.path.splitext(file_path)[0] + "_clean.wav"
        wavfile.write(clean_path, rate, reduced_noise.astype(np.int16))
        return clean_path
    except Exception as e:
        messagebox.showerror("Error", f"Error al limpiar el archivo de audio: {e}")
        return None

def save_text_to_file(text):
    # Abrir el cuadro de diálogo para seleccionar la ubicación de guardado
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if save_path:
        try:
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write(text)
            messagebox.showinfo("Éxito", f"Texto guardado en {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el archivo: {e}")

def convert_audio_to_text():
    # Abrir el cuadro de diálogo para seleccionar el archivo
    file_path = filedialog.askopenfilename(title="Seleccionar archivo de audio", filetypes=[("Audio Files", "*.wav")])
    if file_path:
        clean_path = clean_audio(file_path)
        if clean_path:
            try:
                # Reconocer el texto del archivo de audio
                recognizer = sr.Recognizer()
                with sr.AudioFile(clean_path) as source:
                    print("Reconociendo el audio...")
                    audio_data = recognizer.record(source)
                    text = recognizer.recognize_google(audio_data, language="en-US")
                    print(f"Texto reconocido: {text}")

                # Traducir el texto al español
                translator = Translator()
                translated_text = translator.translate(text, src='en', dest='es').text
                print(f"Texto traducido: {translated_text}")

                # Guardar el texto reconocido y traducido en un archivo de texto
                full_text = f"Texto reconocido: {text}\n\nTexto traducido: {translated_text}"
                save_text_to_file(full_text)
                
                # Mostrar el texto traducido
                messagebox.showinfo("Texto traducido", translated_text)
            except sr.RequestError as e:
                messagebox.showerror("Error de solicitud", f"No se pudo solicitar resultados del servicio de reconocimiento de Google; {e}")
            except sr.UnknownValueError:
                messagebox.showerror("Error de reconocimiento", "No se pudo entender el audio")
            except Exception as e:
                messagebox.showerror("Error", f"Error al convertir el audio a texto: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Convertidor de audio a WAV y Texto")

# Botón para seleccionar y convertir el archivo a WAV
convert_button = tk.Button(root, text="Seleccionar y convertir audio a WAV", command=convert_to_wav)
convert_button.pack(pady=20)

# Botón para convertir el audio a texto y traducirlo
convert_text_button = tk.Button(root, text="Convertir audio a texto y traducirlo", command=convert_audio_to_text)
convert_text_button.pack(pady=20)

# Iniciar el loop de la interfaz gráfica
root.mainloop()
