import openai
import pyttsx3
import time
from config import *

# Configura tu clave API y el endpoint de Azure
openai.api_key = OPENAI_API_KEY
openai.api_base = OPENAI_ENDPOINT
openai.api_type = 'azure'
openai.api_version = '2023-05-15'  # Asegúrate de usar una versión estable

# Nombre del modelo de OpenAI (debe ser uno compatible con Chat)
deployment_name = 'gpt-4o-mini'  # Cambia esto si estás usando otro modelo

# Función para interactuar con el modelo usando entradas dinámicas
def get_response_from_model(user_input):
    # Crear el historial de mensajes, empezando con una configuración inicial
    messages = [
        {"role": "system", "content": "Eres un asistente útil."},  # El sistema define el comportamiento del modelo
        {"role": "user", "content": "damelo en 30 palabras lo siguiente: " + user_input}  # El input del usuario
    ]
    
    # Enviar la solicitud a la API de OpenAI para obtener la respuesta
    response = openai.ChatCompletion.create(
        engine=deployment_name,  # El modelo que estás usando
        messages=messages,       # El historial de mensajes (usuario y sistema)
        max_tokens=200,          # Limita la longitud de la respuesta
        temperature=0.1,         # Controla la creatividad de las respuestas
        
    )
    
    # Obtiene el texto de la respuesta generada por el modelo
    text = response['choices'][0]['message']['content'].strip()
    #text_to_speech(text) 
    # for char in text:
    #     print(char, end="", flush=True)  # Imprime sin salto de línea y fuerza el refresco
    #     time.sleep(delay)  # Añade un pequeño retraso entre caracteres
       
    return text

