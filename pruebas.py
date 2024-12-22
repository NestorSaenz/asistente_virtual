def main():
    # Inicializar el reconocedor
    recognizer = sr.Recognizer()

    print("Bienvenido al asistente de voz. Diga 'salir' si desea terminar la conversación.")

    while True:
        # Usar el micrófono como fuente de audio
        with sr.Microphone() as source:
            print("Por favor, hable ahora...")

            # Ajustar el ruido ambiental
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            # Configurar el tiempo de pausa
            recognizer.pause_threshold = 2  # Tiempo de espera en segundos después de detectar silencio

            # Grabar el audio del micrófono
            try:
                audio = recognizer.listen(source)
                print("Procesando el audio...")

                # Convertir audio a texto usando el servicio de Google
                texto = recognizer.recognize_google(audio, language="es-ES")
                print("Texto reconocido:")
                print(texto)

                if texto.lower() == "salir":
                    print("Terminando la conversación...")
                    break

                # Guardar la transcripción
                with open("transcripcion.txt", "a", encoding="utf-8") as file:
                    file.write(f"Usuario: {texto}\n")

                # Llamar al chatbot
                ollama_chat(texto)

            except sr.UnknownValueError:
                print("No se pudo entender el audio.")
            except sr.RequestError as e:
                print(f"Error con el servicio de reconocimiento: {e}")

    # Eliminar el historial de conversación al finalizar
    if os.path.exists(HISTORIAL_PATH):
        os.remove(HISTORIAL_PATH)
    print("Gracias por usar el asistente de voz.")