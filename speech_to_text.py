import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=10)
    try:
        print("Recognizing...")
        voice_data= ""
        voice_data = r.recognize_google(audio)
        print(f"user said: {voice_data}")
        return voice_data
    except Exception as e:
        speech_to_text("say that agaib please...")
        return "none"
   
if __name__ == "__main__":
    speech_to_text()

