from flask import Flask, request, jsonify
from azure_speech_handler import init_speech
from openai_handler import get_response_from_model
from voice_Syncronized import display_and_speak
import os

# Inicializar Flask
app = Flask(__name__)

# Endpoint de prueba
@app.route('/', methods=['GET'])
def home():
    return "Asistente Virtual Desplegado en Azure - API Activa", 200

# Endpoint para procesar voz cargada (archivo de audio)
@app.route('/process_audio', methods=['POST'])
def process_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No se recibió un archivo de audio."}), 400

    audio_file = request.files['audio']
    if audio_file.filename == '':
        return jsonify({"error": "El archivo no tiene un nombre válido."}), 400

    try:
        # Guardar temporalmente el archivo de audio
        audio_file_path = 'temp_audio.wav'
        audio_file.save(audio_file_path)

        # Convertir el audio en texto usando Azure Speech-to-Text
        user_text = init_speech(audio_file_path)

        if user_text:
            # Obtener respuesta desde OpenAI
            answer = get_response_from_model(user_text)

            # Hacer que el asistente hable la respuesta
            display_and_speak(answer)

            return jsonify({"response": answer}), 200
        else:
            return jsonify({"error": "No se pudo procesar el audio."}), 400
    except Exception as e:
        return jsonify({"error": f"Error al procesar el archivo: {str(e)}"}), 500

# Endpoint para procesar texto directamente
@app.route('/process_text', methods=['POST'])
def process_text():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "No se recibió texto para procesar."}), 400

    try:
        # Obtener respuesta desde OpenAI
        user_text = data['text']
        answer = get_response_from_model(user_text)

        # Hacer que el asistente hable la respuesta
        display_and_speak(answer)

        return jsonify({"response": answer}), 200
    except Exception as e:
        return jsonify({"error": f"Error al procesar el texto: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
