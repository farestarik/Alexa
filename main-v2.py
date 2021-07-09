import io
import time
import speech_recognition as sr
import webbrowser
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

def calc_age(age : int):
    age = int(age)

    months = age * 12
    weeks = months * 4
    days = age * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60 

    print("You lived For: ")
    print(f"Years : {age} Years.")
    print(f"Months : {months} Months.")
    print(f"Weeks : {weeks:,} Weeks.")
    print(f"Days : {days:,} Days.")
    print(f"Hours : {hours:,} Hours.")
    print(f"Minutes : {minutes:,} Minutes.")
    print(f"Seconds : {seconds:,} Seconds.")
    
    talk("You lived For: ")
    talk(f"Years : {age} Years.")
    talk(f"Months : {months} Months.")
    talk(f"Weeks : {weeks:,} Weeks.")
    talk(f"Days : {days:,} Days.")
    talk(f"Hours : {hours:,} Hours.")
    talk(f"Minutes : {minutes:,} Minutes.")
    talk(f"Seconds : {seconds:,} Seconds.")

def take_command():
    try:
        command = ''
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
    if(command == ''):
        print("No Keywords Applied.. Try Again With Keywords".center(80,">"))
        exit()
    if 'play' in command:
        song = command.replace('play', ' ').replace('song',' ').strip()
        talk('Playing' + str(song) + '..')
        print(song)
        pywhatkit.playonyt(song)
    elif 'youtube' in command:
        keywords = command.replace('youtube', '').strip()
        keywords.replace(' ', '+')
        print(f"Searching for {keywords} ...")      
        webbrowser.open(f'https://www.youtube.com/results?search_query={keywords}', new=2)
    elif 'clock' in command:
            time = datetime.datetime.now().strftime('%H:%M %p')
            print(time)
            talk('Its ' + time)
    elif ('who' and ' is ' in command) or ('من هو' in command):
        person = command.replace('who', ' ').replace(' is ', ' ').replace('من هو', ' ').strip()
        wikipedia.set_lang("ar")
        print(person)
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info,"ar")
    elif 'calc my age' in command or 'calculate my age' in command:
        age = command.replace('calc my age', '').replace('calculate my age', '').strip()
        print(age)
        calc_age(int(age))    
    elif 'are you single' in command:
        talk('Iam in relationship with ommak')
    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)    
    elif 'thanks' or 'thank you' in command:
        talk("You're Welcome Babe")        

run_alexa()