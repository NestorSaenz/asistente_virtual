import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION


def save_to_file(text, filename="speech_output.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text + "\n")
        print(f"[INFO] Texto guardado correctamente en {filename}")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")

def init_speech():
    
    print("[INFO] Inicia el reconocimiento de voz. Habla algo...")
    
    # Configuración de Azure Speech SDK
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    # Configurar detección automática de idioma
    auto_language_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=["es-ES", "en-US"])

    # Crear el reconocedor con detección automática de idioma
    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config,
        auto_detect_source_language_config=auto_language_config,
    )

    
    # Inicia el reconocimiento y espera a que termine después de detectar el final del habla
    result = recognizer.recognize_once()

    # Procesar el resultado
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        language = result.properties[speechsdk.PropertyId.SpeechServiceConnection_AutoDetectSourceLanguageResult]
        print(f"[INFO] Idioma detectado: {language} | Texto reconocido: {result.text}")
        save_to_file(f"[{language}] {result.text}")
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("[INFO] No se detectó habla.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"[ERROR] Reconocimiento cancelado: {cancellation_details.reason}")
        if cancellation_details.error_details:
            print(f"[ERROR] Detalles: {cancellation_details.error_details}")
    
    return result.text

   
