import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

from voice1 import take_command

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def run_health_atm():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'headache' in command:
        talk('Im not a doctor, but I can suggest a few general tips for dealing with a headache. You might want to try drinking water, resting in a dark and quiet room, or taking over-the-counter pain relievers. If the headache persists, its essential to consult a medical professional for proper advice.')
    elif 'cold' in command:
        talk('For a cold, its a good idea to rest, drink plenty of fluids, and use over-the-counter cold medications as needed. If your symptoms worsen or persist, consult a doctor for further guidance')
    elif 'fever' in command:
        talk('If you have a fever, its important to monitor your temperature and stay hydrated. You may consider taking fever-reducing medication, but if the fever persists or worsens, seek medical advice.')
    elif 'injury' in command:
        talk('In case of an injury, the severity and necessary actions depend on the type of injury. Its crucial to clean and disinfect any open wounds and, if necessary, seek immediate medical attention. Please provide more details about the injury for specific advice.')
    elif 'obesity' in command:
        talk('Obesity is a complex health issue that requires a holistic approach. Its advisable to consult a healthcare professional for a personalized plan that may include dietary changes, exercise, and other lifestyle modifications.')
    elif 'diabetes' in command:
        talk('Diabetes management involves monitoring blood sugar levels, a balanced diet, regular exercise, and medication as prescribed by a healthcare provider. If you have diabetes or suspect you do, consult a doctor for guidance.')
    elif 'chronic respiratory diseases' in command:
        talk('Chronic respiratory diseases such as asthma, COPD, or bronchitis require careful management. Ensure you follow your prescribed treatment plan, avoid triggers, and consult your healthcare provider for any worsening symptoms.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

while True:
    run_health_atm()


