from flask import Flask, render_template, request, jsonify
from azure_speech_handler import init_speech
from openai_handler import get_response_from_model
from voice_Syncronized import display_and_speak

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Interfaz básica para tu asistente virtual

@app.route('/get_response', methods=['POST'])
def get_virtual_response():
    # Realiza el reconocimiento de voz
    user_input = init_speech()

    if user_input:
        # Obtiene la respuesta desde el modelo OpenAI
        assistant_response = get_response_from_model(user_input)

        # Muestra y reproduce la respuesta en la consola y voz
        display_and_speak(assistant_response)

        return jsonify({"response": assistant_response})
    else:
        return jsonify({"response": "No se detectó voz o input incorrecto."})


if __name__ == '__main__':
    app.run(debug=True)

