import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id) # Male
engine.setProperty('voice', 'english_rp+f4') # Female

engine.setProperty('volume',1.0)
engine.setProperty('rate', 145)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Hi I'm Alexa")
talk("How can i help you")

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', ' ').strip()
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', ' ').replace('song',' ').strip()
        talk('Playing' + str(song) + '..')
        print(song)
        pywhatkit.playonyt(song)
        
    elif 'clock' in command:
            time = datetime.datetime.now().strftime('%H:%M %p')
            print(time)
            talk('Its ' + time)
    elif 'who' and 'is' in command:
        person = command.replace('who', ' ').replace('is', ' ').strip()
        info = wikipedia.summary(person, 2)
        print(person + 'is ' + info)
        talk(person + 'is ' + info)
    elif 'are you single' in command:
        talk('Iam in relationship with ommak')
    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)    
    elif 'thanks' or 'thank you' in command:
        talk("You're Welcome Babe")

run_alexa()















###### Females Voices #######
# engine.setProperty('voice', 'english+f1')
# engine.setProperty('voice', 'english+f2')
# engine.setProperty('voice', 'english+f3')
# engine.setProperty('voice', 'english+f4')
# engine.setProperty('voice', 'english_rp+f3') #my preference
# engine.setProperty('voice', 'english_rp+f4')