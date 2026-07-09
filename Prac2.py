#installing an external module and perform tasks using it in the code
import pyttsx3
engine=pyttsx3.init()
engine.say("I will peak this text. Hello Shine! How are you?")
engine.runAndWait()
import pyjokes
joke=pyjokes.get_joke()
print(joke)
