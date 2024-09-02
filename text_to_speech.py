import pyttsx3

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate' , 'rate[[0].id')

def text_to_speech(text) :
    engine.say(text)
    print(text)
    engine.runAndWait()

if __name__ == "__main__" :
    text_to_speech("this is advance jarvis")

