import io
import time
import speech_recognition as sr
import pyglet
import pywhatkit
import datetime
import wikipedia
import pyjokes
from gtts import gTTS



listener = sr.Recognizer()

pyglet.options["audio"] = ("pulse",)
TICK = .1

def talk(words: str, lang: str="en"):
    with io.BytesIO() as f:
        gTTS(text=words, lang=lang).write_to_fp(f)
        f.seek(0)
        sound = pyglet.media.load("_.mp3", file=f)
    player = sound.play()
    while player.playing:
        pyglet.app.platform_event_loop.dispatch_posted_events()
        pyglet.clock.tick()
        time.sleep(TICK)

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' or 'اليكسا' in command:
                command = command.replace('alexa', ' ').strip()
                print(command)
                print(50*'=')
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
    elif ('who' and 'is') or ('من هو') in command:
        person = command.replace('who', ' ').replace(' is ', ' ').replace('من هو', ' ').strip()
        wikipedia.set_lang("ar")
        print(person)
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info,"ar")
    elif 'are you single' in command:
        talk('Iam in relationship with ommak')
    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)    
    elif 'thanks' or 'thank you' in command:
        talk("You're Welcome Babe")        

run_alexa()