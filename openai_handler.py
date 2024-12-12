import openai
from config import OPENAI_API_KEY

# Configurar la clave API de OpenAI
openai.api_key = OPENAI_API_KEY

def openai_response(prompt):
    """
    Envía el texto a OpenAI y devuelve la respuesta.
    """
    try:
        # Realizar la solicitud a la API de OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Obtener la respuesta del texto generado por el modelo
        answer = response.choices[0].message['content'].strip()

        return answer

    except Exception as e:
        return f"[ERROR] No se pudo obtener respuesta de OpenAI: {str(e)}"
