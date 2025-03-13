import pyttsx3 
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os 
import random

def txt_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
            return text.lower()  # Convert to lowercase
        except sr.UnknownValueError:
            print("Sorry, I did not understand that")
            return ""
        except sr.RequestError as e:
            print(f"Error: {e}")
            return ""

def speech_txt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)  # Female voice
    engine.setProperty('rate', 150)  # Adjust speed
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    while True:
        data = txt_speech()

        if "your name" in data or "what is your name" in data:
            name = "My name is Elon Musk, I am Billionaire from all over the world."
            speech_txt(name)
        elif "old are you" in data:
            age = "i am 23 years old"
            speech_txt(age)
        elif "now time" in data or "tell me now time" in data:
            # I for hours, M for Minutes and p for am/pm
            time = datetime.datetime.now().strftime("%I%M%p")
            speech_txt(time)
        elif "chat gpt"in data:
            webbrowser.open("https://chatgpt.com/")
        elif "joke"in data:
            joke = pyjokes.get_joke(language="en", category='all')
            print(joke)
            speech_txt(joke)
        elif "song" in  data:
            add = r"A:\Songs\Songs\Arijit Singh\Songs"
            listSong = os.listdir(add)
            song = random.choice(listSong)
            print(listSong)
            os.startfile(os.path.join(add, song))
        elif "exit" in data:
            speech_txt("thank you, Mr. Ali")
            break