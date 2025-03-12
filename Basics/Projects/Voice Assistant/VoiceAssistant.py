import pyttsx3 
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

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
    engine.setProperty("voice", voices[1].id)  # Female voice
    engine.setProperty('rate', 150)  # Adjust speed
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    data = txt_speech()

    if "your name" in data or "what is your name" in data:
        name = "My name is Elon Musk, I am Billionaire from all over the world."
        speech_txt(name)


    
  # if txt_speech().lower() == "hey Ali":
  #   print("test")
  # else:
  #   print("Thanks, But not recognize")