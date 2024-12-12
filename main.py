import os
import azure.cognitiveservices.speech as speechsdk
from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION

def save_to_file(text, filename="speech_output.txt"):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text + "\n")
        print(f"[INFO] Texto guardado correctamente en {filename}")
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo: {e}")

def recognize_and_stop_on_silence():
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

    print("[INFO] Inicia el reconocimiento de voz. Habla algo...")

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

if __name__ == "__main__":
    recognize_and_stop_on_silence()








# import os
# import azure.cognitiveservices.speech as speechsdk
# from config import AZURE_SPEECH_KEY, AZURE_SPEECH_REGION

# def save_to_file(text, filename="speech_output.txt"):
#     try:
#         print(f"[DEBUG] Intentando guardar el texto: {text}")
#         with open(filename, "a", encoding="utf-8") as file:
#             file.write(text + "\n")
#         print(f"[INFO] Texto guardado correctamente en {filename}")
#     except Exception as e:
#         print(f"[ERROR] No se pudo guardar el archivo: {e}")

# def continuous_recognition():
#     # Configuración de Azure Speech SDK
#     speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_SPEECH_REGION)
#     audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

#     # Configurar el idioma del reconocimiento como español
#     speech_config.speech_recognition_language = "es-ES"

#     recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

#     print("[INFO] Comienza el reconocimiento continuo (Ctrl+C para detener...)")
#     partial_text = ""

#     def speech_callback(evt):
#         nonlocal partial_text
#         if evt.result.text:
#             print(f"[DEBUG] Texto reconocido: {evt.result.text}")
#             partial_text += evt.result.text + " "
#             if evt.result.text.endswith((".", "!", "?")):
#                 save_to_file(partial_text.strip())
#                 partial_text = ""

#     recognizer.recognizing.connect(speech_callback)

#     try:
#         recognizer.start_continuous_recognition()
#         input("[INFO] Mantén el script activo y presiona Enter para detener...")
#     except KeyboardInterrupt:
#         print("\n[INFO] Reconocimiento detenido manualmente.")
#     recognizer.stop_continuous_recognition()

# if __name__ == "__main__":
#     continuous_recognition()
