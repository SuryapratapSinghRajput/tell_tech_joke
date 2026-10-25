import pyjokes
import pyttsx3
def tell_tech_joke():
    # Pyjoke will give a random joke related to tech-themed world
     joke = pyjokes.get_joke()
     print(joke)
    # Give the script a voice so it can peform its own stand-up comedy!
     engine = pyttsx3.init()
     engine.say(joke)
     engine.runAndWait()
if __name__ == '__main__':
     tell_tech_joke()