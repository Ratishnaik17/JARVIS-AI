import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import json
import google.generativeai as genai

recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "47cac49e0eb746e1b2d1eb49dbc8abb1"
def aiprocess(command):
    try:
    # Configure the API key
        genai.configure(api_key="AIzaSyBGIVpoBoqBAgiRbEEJAof9XMrxk-ZJ14g")

    # Create a model instance
        model = genai.GenerativeModel('gemini-2.0-flash')

    # Generate the response
        response = model.generate_content(command)

    # Print the response
        return response.text

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    if "open google" in c.lower():
        speak("Opening google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        speak("Opening facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        speak("Opening linkedin")
        webbrowser.open("https://www.linkedin.com")
    elif "open bmw picture" in c.lower():
        speak("Opening bmw picture")
        webbrowser.open("https://www.bing.com/images/search?q=bmw+m+series+cars&form=HDRSC3&first=1")
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link= musiclibrary.music[song]  
        webbrowser.open(link) 
    elif "news" in c.lower():
        speak("Opening news")
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=47cac49e0eb746e1b2d1eb49dbc8abb1")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    # --- Chatbot Capabilities ---
    elif any(greet in c.lower() for greet in ["hello", "hi", "hey"]):
        speak("Hello! How can I help you today?")
    elif "how are you" in c.lower():
        speak("I'm just a bunch of code, but I'm doing great! How can I assist you?")
    elif "tell me a joke" in c.lower():
        speak("Why did the computer show up at work late? It had a hard drive!")
    elif "who are you" in c.lower():
        speak("I'm Jarvis, your personal AI assistant.")
    elif "thank you" in c.lower():
        speak("You're welcome!")
    # --- End Chatbot Capabilities ---
    else:
        #let openai handle the request
        output=aiprocess(c)
        print(output)
        speak(output)


    
    
if __name__ == "__main__":
    speak("Initializing Jarvis")    
    #listen for wake word jarvis
    #obtain audio from the microphone
    while True:

# Initialize recognizer
     r = sr.Recognizer()

# Use microphone as the audio source
    
     print("recognizing...")
     try:
         with sr.Microphone() as source:
            print("Listening")
            audio = r.listen(source,timeout=2,phrase_time_limit=1)
         word = r.recognize_google(audio)
         if(word.lower() == "jarvis"):
             speak("Ya")
             with sr.Microphone() as source:
                print("jarvis active")
                audio = r.listen(source)
                command = r.recognize_google(audio)
               
                processcommand(command)
     except Exception as e:
         print(f"Error:{e}".format(e))