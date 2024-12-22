from azure_speech_handler import *
from openai_handler import *
from voice_Syncronized import *

while True:
    text = init_speech()
    if text.lower() == 'detener.':
        break 
    else:
        answer = get_response_from_model(text)
        display_and_speak(answer)
# save_to_file(answer)





