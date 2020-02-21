import speech_recognition as sr
import pyttsx3 as pt
import dialogflow
from google.api_core.exceptions import InvalidArgument

import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
import keyboard

while True:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'
    DIALOGFLOW_PROJECT_ID = 'sweety-6d440'
    DIALOGFLOW_LANGUAGE_CODE = 'en'
    SESSION_ID = 'session_test'

    r = sr.Recognizer()
    engine = pt.init()
    engine.setProperty('rate', 200)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[7].id)
    with sr.Microphone() as source:
        print("Waitiiiin voice input :")
        audio = r.listen(source)
        print("Got It :D")
    text_to_be_analyzed = r.recognize_google(audio)
    if text_to_be_analyzed != 'close':
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(
            DIALOGFLOW_PROJECT_ID, SESSION_ID)
        text_input = dialogflow.types.TextInput(
            text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
        query_input = dialogflow.types.QueryInput(text=text_input)
        try:
            response = session_client.detect_intent(
                session=session, query_input=query_input)
        except InvalidArgument:
            raise
        try:
            print("Text from Mic : "+r.recognize_google(audio))
            engine.say(response.query_result.fulfillment_text)
            engine.runAndWait()
        except:
            pass
    else:
        keyboard.send('ctrl+6')
