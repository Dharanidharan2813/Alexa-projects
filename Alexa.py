import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener=sr.Recognizer()
engine=pyttsx3.init()

voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_commands():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voices=listener.listen(source)
            command=listener.recognize_google(voices)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
                return command
    except sr.UnknownValueError:
        engine_talk("Sorry, I did not understand that.")
    except sr.RequestError:
        engine_talk("Sorry, my speech service is down.")
    return ""
def run_alexa():
    command=take_commands()
    print(command)
    if 'play' in command:
        song=command.replace('play',' ')
        talk('Playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime("%I:%M %f")
        talk('curren time'+time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'how to make a ' in command:
        cook=command.replace('how to make a','')
        pywhatkit.playonyt(cook)
    elif 'about' in command:
        kovil=command.replace('kovil','')
        pywhatkit.search(kovil)
        print(kovil)
        talk(kovil)
    elif 'best place to visit in' in command:
        tour=command.replace('best place to visit in','')
        pywhatkit.search(tour)
        print(tour)
        talk(tour)
        
run_alexa()
