import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather
import wikipedia
import os
import subprocess
import cv2
from requests import get

def Action (data):
    user_data = data.lower()


    if "what is your name" in user_data :
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"

    elif "hello" in user_data or "hye" in user_data :
        text_to_speech.text_to_speech("hey , sir how i help you")
        return "hey , sir how i help you"

    elif "good morning" in user_data :
        text_to_speech.text_to_speech("good morning sir")
        return "good morning sir"

    elif "time now" in user_data :
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :" , (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time

    elif "shutdown" in user_data :
        text_to_speech.text_to_speech("ok sir")
        return "ok sir"
    
    elif "play music" in user_data :
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_to_speech("gaana.com is now ready for you") 
        return "gaana.com is now ready for you"

    elif "youtube" in user_data :
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"

    elif "open google" in user_data :
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")
        return "google.com is now ready for you"


    elif "weather" in user_data :
      ans = weather.weather()
      text_to_speech.text_to_speech(ans)
      return ans
    

    elif "search wikipedia" in user_data:
        try:
            search_query = user_data.replace("search wikipedia for", "").strip()
            summary = wikipedia.summary(search_query, sentences=2)  # Get a brief summary of the topic
            text_to_speech.text_to_speech(summary)
            return summary
        except wikipedia.exceptions.DisambiguationError as e:
            response = "There are multiple results for this search. Please be more specific."
            text_to_speech.text_to_speech(response)
            return response
        except wikipedia.exceptions.PageError:
            response = "Sorry, I couldn't find any results for that topic."
            text_to_speech.text_to_speech(response)
            return response
        
    elif "take screenshot" in user_data:
        response = "Taking a screenshot."
        text_to_speech.text_to_speech(response)
        if os.name == 'nt':  # For Windows
            os.system("snippingtool /clip")

        return response 
           
    elif "run command" in user_data:
        command = user_data.replace("run command", "").strip()
        response = f"Running command: {command}"
        text_to_speech.text_to_speech(response)
        os.system(command)
        return response
    

    elif "open camera" in user_data:
        response = "opening camera."
        text_to_speech.text_to_speech(response)
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k==27:
                break;
        cap.release()
        cv2.destroyAllWindows()
        return response
    
    elif "ip address" in user_data:
        ip = get("https://api.ipify.org").text
        text_to_speech.text_to_speech(f"your IP address is {ip}")


    else :
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"