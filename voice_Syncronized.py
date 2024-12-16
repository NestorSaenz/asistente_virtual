import time
import azure.cognitiveservices.speech as speechsdk
from openai_handler import get_response_from_model
from azure_speech_handler import *
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION

import time
import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION

# def display_and_speak(text, delay=0.03):
#     """
#     Muestra texto carácter por carácter y lo reproduce en voz a medida que se imprime.
#     """
#     # Configuración del sintetizador de voz
#     speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
#     audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
#     synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

#     current_sentence = ""
#     buffer = ""

#     for char in text:
#         print(char, end="", flush=True)  # Imprime el texto carácter por carácter
#         buffer += char  # Acumula en un buffer temporal
#         time.sleep(delay)  # Añade un retraso entre caracteres

#         # Cuando encuentra un delimitador de frase, sintetiza el buffer y reinicia
#         if char in ".!?":
#             current_sentence += buffer
#             synthesizer.speak_text_async(current_sentence).get()  # Reproduce la frase actual
#             buffer = ""  # Reinicia el buffer
#             current_sentence = ""  # Reinicia la construcción de la frase

#     # Reproduce cualquier texto que haya quedado pendiente
#     if buffer.strip():
#         synthesizer.speak_text_async(buffer).get()

#     print()  # Salto de línea final


import time
import threading
import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION

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



