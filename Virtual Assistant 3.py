import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes
import os
import socket
#from ecapture import ecapture as photo
import pyscreenshot as screenshot
import weather_forecast as wf
from calculator.simple import SimpleCalculator

#Intializing speechrecognizer and python text to speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=4,phrase_time_limit=5)

    try:
        print("Recognizing")
        command = r.recognize_google(audio,language='en-in')
        print(f"User said:{command}")

    except Exception as e:
        talk("Say the command again...")
        return "none"
    return command

    
#Greetings to the user.
def wish():
    a = int(datetime.datetime.now().hour)
    if a>=0 and a<=12:
	    talk("Good Morning")
    elif a>12 and a<16:
	    talk("Good Afternoon")
    else :
	    talk("Good Evening")
    talk("I am Selena How can I help you")

    
if __name__=="__main__":
    wish()
    while True:
        command = takecommand().lower()
        print(command)
    
        if 'play' in command:
        
            song = command.replace('play', ' ')
            talk('playing ' + song)
            kit.playonyt(song)
        
        elif 'time' in command:
        
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is ' + time)

        elif 'date' in command:
        
            x = datetime.datetime.now()
            x = x.strftime("%x")
            print(x)
            talk('Todays date is'+ x)

        elif 'who is' in command:
        
            person = command.replace('who is', '')
            info = wikipedia.summary(person,2)
            print(info)
            talk(info)

        elif 'what is' in command:
        
            something = command.replace('what is', '')
            info = wikipedia.summary(something, 2)
            print(info)
            talk(info)

        elif 'joke' in command:
        
            joke=pyjokes.get_joke()
            print(joke)
            talk(joke)
        
        elif 'open google' in command:
        
            url = "www.google.com"
            print("opening google")
            webbrowser.open(url)
            talk("opening google")
        
        elif 'chess game' in command:
        
            url = "https://gamesnacks.com/embed/games/chessclassic"
            print("opening chess")
            webbrowser.open(url)
            talk("opening chess")
        
        elif 'ludo game' in command:
        
            url = "https://gamesnacks.com/embed/games/ludolegend"
            print("opening ludo")
            webbrowser.open(url)
            talk("opening ludo")
        
        elif 'open cmd' in command:
        
            os.system("start /B start cmd.exe")
        
        elif 'open notepad' in command:
        
            os.system("start /B start notepad.exe")
        
        #elif 'photo' in command:
        
            #p = datetime.datetime.now().strftime('%M')
            #p = "photo" + p + ".png"
            #photo.delay_imcapture(0,"Camera",p,3)
        
        #elif 'video' in command:
        
            #v = datetime.datetime.now().strftime('%M')
            #v = "video" + v + ".avi"
            #photo.vidcapture(0,"Camera",v,"q")
        
        elif 'screenshot' in command:
        
            y = datetime.datetime.now().strftime('%M')
            y = "screenshot" + y + ".png"
            im = screenshot.grab()
            im.save(y)
        
        elif 'ip address' in command:
        
            host_name = socket.gethostname()
            ip_address = socket.gethostbyname(host_name)
            print("Host Name: ",host_name)
            print("Ip Address: ",ip_address)
        
        elif 'send a message' in command:
        
            message = command.replace('send a message', '')
            h = datetime.datetime.now()
            h = h.strftime("%H")
            h=int(h)
            n = datetime.datetime.now()
            mn = datetime.timedelta(minutes = 1)
            m = n + mn
            m=m.strftime('%M')
            m=int(m)
            kit.sendwhatmsg("+918125242465",message,h,m)
        
        elif 'weather' in command:
        
            d = datetime.datetime.now().strftime('%Y-%m-%d')
            t = datetime.datetime.now().strftime("%x")
            wf.forecast(place = "Hyderabad", time = t, date = d, forecast = "daliy")
        
        elif 'how much' in command:
        
            sc= command.replace('how much', ' ')
        
            if 'into' in sc:
                sc=sc.replace('into', ' * ')
            elif 'plus' in command:
                sc=sc.replace('plus', ' + ')
            elif 'divided by' in command:
                
                sc=sc.replace('divided by', ' / ')
            elif 'minus' in command:
                sc=sc.replace('minus', ' - ')
        
            c = SimpleCalculator()
            c.run(sc)
            print (c.log)
        
        elif 'exit' in command:
            talk("Thanks for using me..")
            exit()