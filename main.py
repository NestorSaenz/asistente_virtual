import os
import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION

# Asegurarse de que estamos en el directorio correcto
print(f"[DEBUG] Directorio de trabajo actual: {os.getcwd()}")
if os.getcwd() != "D:\\Asistente virtual":
    os.chdir("D:\\Asistente virtual")
    print(f"[INFO] Directorio cambiado a: {os.getcwd()}")

def save_to_file(text, filename="speech_output.txt"):
    try:
        print(f"[DEBUG] Intentando guardar el texto: {text}")
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text + "\n")
        print(f"[INFO] Texto guardado correctamente en {filename}")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")

def continuous_recognition():
    # Configuración de Azure Speech SDK
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    # Configurar el idioma del reconocimiento como español
    speech_config.speech_recognition_language = "es-ES"

    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("[INFO] Comienza el reconocimiento continuo (Ctrl+C para detener...)")
    partial_text = ""

    def speech_callback(evt):
        nonlocal partial_text
        if evt.result.text:
            print(f"[DEBUG] Texto reconocido: {evt.result.text}")
            partial_text += evt.result.text + " "
            if evt.result.text.endswith((".", "!", "?")):
                save_to_file(partial_text.strip())
                partial_text = ""

    recognizer.recognizing.connect(speech_callback)

    try:
        recognizer.start_continuous_recognition()
        input("[INFO] Mantén el script activo y presiona Enter para detener...")
    except KeyboardInterrupt:
        print("\n[INFO] Reconocimiento detenido manualmente.")
    recognizer.stop_continuous_recognition()

if __name__ == "__main__":
    continuous_recognition()
