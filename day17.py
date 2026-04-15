'''import pyttsx3
engine = pyttsx3.init()
def speech_text(text):
    engine.say(text)
    
speech_text("hello, I am janu")
speech_text("how are you")
engine.runAndWait()

import pyttsx3
engine = pyttsx3.init()
def speech_text(text):
    print(text)          
    engine.say(text)     
speech_text("Hello, I am Janu")
speech_text("How are you?")
engine.runAndWait()

'''
import pyttsx3
engine = pyttsx3.init()
def speech_text(text):
    engine.say(text)
user_text = input("Enter your message: ").lower()
name = "user"
if "my name is" in user_text:
    name = user_text.split("my name is")[-1].strip()
elif "name is" in user_text:
    name = user_text.split("name is")[-1].strip()
if user_text in["hi","hello","hola"]:
    resonse = "hello! how can i help you"
elif "name" in user_text:    
    response = f"hello {name},how can i help you?"
else:
    response = "sorry, I did not understand."
print(response)
speech_text(response)
engine.runAndWait()
    
