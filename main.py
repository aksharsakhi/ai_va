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

            elif "goodbye" in command:
                speak("Goodbye! Have a great day.")
                exit()

            else:
                speak("I'm sorry, I don't understand that command.")

        except sr.UnknownValueError:
            print("Sorry, I could not understand your command.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Main loop
if __name__ == "__main__":
    speak("Hello! I'm your voice assistant.")
    while True:
        voice_assistant()
