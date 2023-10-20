# pip install kivy
# pip install SpeechRecognition
# pip install pyttsx3
# python voice_assistant.py
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import speech_recognition as sr
import pyttsx3

class VoiceAssistantApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="Voice Assistant: Initializing...")
        layout.add_widget(self.label)
        return layout

    def on_start(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Adjust speech rate as needed

        self.speak("Voice Assistant: Hello! I'm your voice assistant. How can I assist you today?")

        while True:
            self.voice_assistant()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def voice_assistant(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.label.text = "Voice Assistant: Listening..."
            audio = self.recognizer.listen(source)

            try:
                command = self.recognizer.recognize_google(audio).lower()
                print("You said: " + command)
                self.label.text = "Voice Assistant: You said: " + command

                if "hello" in command:
                    self.speak("Hello! How can I assist you today?")

                # Add more voice assistant commands and responses here.

                else:
                    self.speak("I'm sorry, I don't understand that command.")

            except sr.UnknownValueError:
                print("Sorry, I could not understand your command.")
                self.label.text = "Voice Assistant: Sorry, I could not understand your command."
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                self.label.text = "Voice Assistant: Could not request results; " + str(e)

if __name__ == "__main__":
    VoiceAssistantApp().run()
