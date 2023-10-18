import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define the voice assistant function
def voice_assistant():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said: " + command)

            if "hello" in command:
                speak("Hello! How can I assist you today?")

            elif "what's the time" in command:
                import datetime
                time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {time}.")

            elif "fever" in command:
                speak("")
                exit()
            elif 'headache' in command:
                speak('Im not a doctor, but I can suggest a few general tips for dealing with a headache. You might want to try drinking water, resting in a dark and quiet room, or taking over-the-counter pain relievers. If the headache persists, its essential to consult a medical professional for proper advice.')
            elif 'cold' in command:
                speak('For a cold, its a good idea to rest, drink plenty of fluids, and use over-the-counter cold medications as needed. If your symptoms worsen or persist, consult a doctor for further guidance.')
            elif 'fever' in command:
                speak('If you have a fever, its important to monitor your temperature and stay hydrated. You may consider taking fever-reducing medication, but if the fever persists or worsens, seek medical advice.')
            elif 'injury' in command:
                speak('In case of an injury, the severity and necessary actions depend on the type of injury. Its crucial to clean and disinfect any open wounds and, if necessary, seek immediate medical attention. Please provide more details about the injury for specific advice.')
            elif 'obesity' in command:
                speak('Obesity is a complex health issue that requires a holistic approach. Its advisable to consult a healthcare professional for a personalized plan that may include dietary changes, exercise, and other lifestyle modifications.')
            elif 'diabetes' in command:
                speak('Diabetes management involves monitoring blood sugar levels, a balanced diet, regular exercise, and medication as prescribed by a healthcare provider. If you have diabetes or suspect you do, consult a doctor for guidance.')
            elif 'chronic respiratory diseases' in command:
                speak('Chronic respiratory diseases such as asthma, COPD, or bronchitis require careful management. Ensure you follow your prescribed treatment plan, avoid triggers, and consult your healthcare provider for any worsening symptoms.')

            else:
                speak("I'm sorry, I don't understand that command.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand your command.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Main loop
if _name_ == "_main_":
    speak("Hello! I'm your voice assistant.")
    while True:
        voice_assistant()
