import streamlit as st
from azure_speech_handler import init_speech
from openai_handler import get_response_from_model
from voice_Syncronized import display_and_speak

# Título de la aplicación
st.title("Asistente Virtual con Entrada de Voz")

# Instrucciones para el usuario
st.write("Presiona el botón para hablar con el asistente:")

# Botón para grabar audio
if st.button("Grabar voz"):
    st.info("Escuchando...")
    
    # Convertir voz a texto
    text_from_speech = init_speech()
    
    if text_from_speech:
        st.success(f"Consulta reconocida: {text_from_speech}")
        
        # Obtener respuesta del modelo
        answer = get_response_from_model(text_from_speech)
        
        # Mostrar respuesta en la interfaz
        st.write("Respuesta del Asistente:")
        st.success(answer)
        
        # Reproducir la respuesta
        display_and_speak(answer)
    else:
        st.warning("No se detectó ningún texto. Intenta nuevamente.")
