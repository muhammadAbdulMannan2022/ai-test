import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
engine.say("hello muhammad! what i can do for you")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def talk_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "py" in command:
                # print(command)
                command = command.replace('py', '')
                print(command)
            
    except:
        pass
    return command
def run_ai():
    command = talk_command()
    if "play" in command:
        command = command.replace('play', '')
        talk('playing ' + command)
        pywhatkit.playonyt(command)
        print('playing ...')
    elif "time" and "what's" in command:
        command = command.replace('time', '')
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("current time is "+time)
    elif "your" and "boyfriend" in command:
        talk("I love muhammad abdul mannan but He don't care about my fillings")
    else:
        talk("say again. I don't heard you.")
while True:
    run_ai()