import speech_recognition as sr
import pyttsx3
import webbrowser
import OpenAITest
import datetime
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Speak now!")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing.......")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return "None"
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return query


if __name__ == '__main__':
    print('hello Piyush')
    say("Hello I am Your Personal Assistant")
    while True:
        print("Listening.........")
        text = takeCommand()
        sites = [["Youtube","https://www.youtube.com/"],
                 ["Whatsapp","https://web.whatsapp.com/"],
                 ["Google","https://www.google.com/"],
                 ["Instagram","https://www.instagram.com/?hl=en"],
                 ["Hotstar","https://www.hotstar.com/in/home"]]
        for site in sites:
            if "open" in text.lower() and site[0].lower() in text.lower():
                say(f"Opening {site[0]} sir.....")
                webbrowser.open(site[1])
           
        if "the time" in text.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")



        
        
         

   

