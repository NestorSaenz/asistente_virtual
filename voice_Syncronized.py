import time
import azure.cognitiveservices.speech as speechsdk
import threading
from azure_speech_handler import *
from config import *

def text_to_speech_worker(text, synthesizer):
    """
    Hilo para reproducir el texto en voz.
    """
    synthesizer.speak_text_async(text).get()  # Reproduce todo el texto en un solo hilo

def display_text_worker(text, delay):
    """
    Hilo para mostrar el texto en consola carácter por carácter o palabra por palabra.
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)  # Retraso para simular el efecto de tipeo
    print()  # Salto de línea al final

def display_and_speak(text, delay = 0.08):
    """
    Maneja la impresión y la síntesis de voz en hilos separados.
    """
    # Configuración del sintetizador de voz
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
    speech_config.speech_synthesis_voice_name = "es-CO-GonzaloNeural"  # Voz masculina colombiana
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    
    # Crear hilos para la impresión y la síntesis de voz
    display_thread = threading.Thread(target=display_text_worker, args=(text, delay))
    speech_thread = threading.Thread(target=text_to_speech_worker, args=(text, synthesizer))

    # Iniciar ambos hilos
    display_thread.start()
    speech_thread.start()

    # Esperar a que ambos hilos terminen
    display_thread.join()
    speech_thread.join()



