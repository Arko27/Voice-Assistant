import speech_recognition as sr
import pyttsx3
import time
import wikipedia
import webbrowser
import pywhatkit as kit
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-15)

def speak(word):

   engine.say(word)
   engine.runAndWait()
   
def wishBegin():

   engine = pyttsx3.init()
   lt = time.localtime()
   wish="";txt=""
   if (lt.tm_hour >= 4 and lt.tm_hour < 12):
      txt = "Good Morning"
   elif (lt.tm_hour == 12):
      txt = "Good Noon"
   elif (lt.tm_hour > 12 and lt.tm_hour <= 18):
      txt = "Good Afternoon"
   elif (lt.tm_hour > 18 and lt.tm_hour < 21):
      txt = "Good Evening"
   else:
      txt = "Good Night"
   wish = "Hi Sir, " + txt + ", this is Aryan. How can I help you sir?"
   speak(wish)

def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(query)
        return query

    except Exception as e:
       print("Say that again please...")
       return "None"

if __name__== "__main__":

   wishBegin()
   while True:
      #speak("What more can I do for you, sir?")
      query = takeCommand().lower()
      
## Wikipedia Search
      if ('wikipedia' in query):
         speak('Searching Wikipedia Sir...')
         query = (query[1:].split(" in" or " on"))[0]
         results = wikipedia.summary(query,sentences=2)
         speak("According to wikipedia")
         speak(results)
         speak("Sir, do you want me to open the website?")
         ans = takeCommand().lower()
         if ('yes' in ans):
            kit.search(results)

## Google Search            
      elif ('search' in query):
         speak('Searching Sir...')
         srch = (query.split("search"))[1:]
         kit.search(srch)

## YouTube Play Songs/Videos
      elif ('play' in query):
         speak("Playing Sir...")
         song = (query.split("play "))[1]
         kit.playonyt(song)

## Open a System File
      elif ('open' and 'system' and  'software' in query):
         try:
            speak("Which Application do you want to open, Sir?")
            app = takeCommand().lower()
            app = app.replace(" ","")
            path = "C:\WINDOWS\system32\\" + app +".exe"
            os.startfile(path)
         except Exception as e:
            print("Sorry, no such file found")
                
## Send e-mail
#       elif ('send' and 'email' in query):
#          try:
#             speak("Sir, could u please provide me with the receipient's e-mail address?")
#             rec_mail = input("Recepient's e-Mail here: ")
#             speak("Sir, could u please provide me with the content of the mail")
#             content = takeCommand().lower()
#             sendEmail(rec_mail,content)
#             speak("Sir, your e-mail has been sent successfully")

#          except Exception as e:
#             print(e)
#             speak("Sorry Sir, your e-mail could not be sent")

## Send e-mail
# def sendEmail(to,content):
#    server = smtplib.SMTP("smtp.gmail.com",587)
#    server.ehlo()
#    server.starttls()
#    server.login("sender's mail-id","pass")
#    server.sendmail("sender's mail-id",to,content)
#    server.close()

## Open a Website         
      elif ('open' in query):
         web = (query.split("open "))[1]
         web = web.replace(" ","")
         websrch = "https://www." +web +".com"
         webbrowser.register('chrome', None,
                             webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
         webbrowser.get('chrome').open_new(websrch)

## Terminate The Assistant
      elif ('sleep' in query):
         speak("Thank you sir .... Have a good day")
         sys.exit()

# Calculate some operations
      if ('add' or 'ad' in query):
         a = query.split()[1]
         b = query.split()[3]
         add = int(a) + int(b)
         speak(f"The summation is {add}")
      
      if ('subtract' in query):
         a = query.split()[1]
         b = query.split()[3]
         diff = int(b) - int(a)
         speak(f"The difference is {diff}")

else:
   pass