import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION

def init_speech():
    """
    Inicializa y configura el reconocimiento de voz de Azure.
    """
    # Configuración del Speech SDK de Azure
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    # Configuración del idioma del reconocimiento a español
    speech_config.speech_recognition_language = "es-ES"

    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    return recognizer

