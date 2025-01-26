import speech_recognition as sr
import pyttsx3
import time
from transformers import pipeline

def record_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Say something...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Google Web Speech API
        print("You said: ", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return None



def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level
    engine.say(text)
    engine.runAndWait()



def tutor_system():
    print("Home Tutor is ready. Please speak a question or command.")
    
    while True:
        speech_text = record_speech()  # Record the question/command from the user
        if speech_text:
            # Process the speech and generate an appropriate response
            # For simplicity, let's say it always reads a description
            description = "This is a sample description for the tutor."
            
            # Use TTS to read back the description in your voice
            text_to_speech(description)
        
        time.sleep(2)  # Add a short delay before next round

# Run the tutor system
tutor_system()



def get_tutor_response(query):
    model = pipeline("text-generation", model="gpt2")  # Use a pre-trained model
    response = model(query, max_length=50, num_return_sequences=1)
    return response[0]["generated_text"]


