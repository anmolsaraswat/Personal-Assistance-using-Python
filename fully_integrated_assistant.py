import speech_recognition as sr
from time import ctime
import time
import os
import webbrowser
import sys
import pyttsx3
import subprocess
import win32gui
import win32con
from os import getpid, system
from threading import Timer
import os , win32com.client
import win32com.client as comclt

def speak(audioString):                # speak function will convert your text to speech. The 
   engine = pyttsx3.init()             #  text is passed as audioString variable.
   engine.say(audioString)             #  It uses pyttsx3 libraray which is python text to speech library.
   engine.runAndWait()                 #  runAndWAit - blocks while processing all currently queued commands.

 
def recordAudio():                     #  The recordAudio function will take speech from your microphone and will convert into speech.
    
    r = sr.Recognizer()                
    with sr.Microphone() as source:
        audio = r.listen(source)       # It listens to the microphone for the speech.
    
    data = ""
    try:
        data = r.recognize_google(audio)  # It uses google library to convert your speech to text and saves the text into variable 'data'.
        speak("You said: " + data)
        print ("You said: " + data)
    except sr.UnknownValueError:
        speak("could not understand audio say it clearly ") # Error if voice is not clear or some error.
    except sr.RequestError as e:
        speak("Could not request results from Speech Recognition service; {0}".format(e))
 
    return data    #returns the text 
 
def personalassistant(data):

    if "how are you" in data:          # if the text is "how are you " it will reply with "I am fine".
        speak("I am fine")
    elif "time" in data:
        speak(ctime())                 # If you ask the time it will return the present time.
    elif "open student login" in data:          # You can also set a particular website to a particular keyword in this case if you ask to open student login it will open the
        speak("Hold on, I will open student login")                        # particular website who URL is given.
        webbrowser.open_new_tab('https://academicscc.vit.ac.in/student/stud_login.asp')
    elif "student" in data:
        speak("Hold on, I will open student login")
        webbrowser.open_new_tab('https://academicscc.vit.ac.in/student/stud_login.asp')
    elif "open Media player" in data:     # You can also open a installed app in your system you have to provide path for the exe file for that application. 
        speak("Hold on, I will open media player")
        os.startfile('C:\Program Files (x86)\Windows Media Player\wmplayer.exe', 'open')
    elif "notes" in data:                 # You can also open documents. 
        os.startfile('E:\VIT\Cryptography.pdf', 'open')
    elif "moodle" in data:
        speak("Hold on, I will open moodle login")
        webbrowser.open_new_tab('http://moodlecc.vit.ac.in/my/') 
    elif "quora" in data:
        speak("Hold on, I will open quora")
        webbrowser.open_new_tab('https://www.quora.com/')
    elif "where is" in data:           # You can also see the location you just have to speak the name of place it will serach in the google maps.
        data = data.split(" ")
        location = data[2]
        speak("Hold on, I will show you where " + location + " is.")
        webbrowser.open_new_tab('https://www.google.nl/maps/place/' + location + '/&amp;')
    elif "search for" in data:
        data = data.split(" ")
        searchfor = data[2]
        speak("Hold on, I will search for " + searchfor)
        webbrowser.open_new_tab('https://www.google.co.in/?gfe_rd=cr&ei=c5cTWLeuOqLnugSekrfQAw#q=' + searchfor) 
    elif "search" in data:
        data = data.split(" ")
        searchfor = data[1]
        speak("Hold on, I will search for " + searchfor)
        webbrowser.open_new_tab('https://www.google.co.in/?gfe_rd=cr&ei=c5cTWLeuOqLnugSekrfQAw#q=' + searchfor)
    elif "display off" in data:     # This function will off your display. 
        def runScreensaver():
          strComputer = "."
          objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
          objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
          colItems = objSWbemServices.ExecQuery("Select * from Win32_Desktop")
          for objItem in colItems:
             if objItem.ScreenSaverExecutable:
                os.system(objItem.ScreenSaverExecutable + " /start")
                break
    elif "lock" in data: 
        wsh= comclt.Dispatch("WScript.Shell")
        wsh.SendKeys("%({TAB})") # send the keys you want
  

while 1:
   speak("Hello Mr. Anmol what can i do for you?")
   data = recordAudio()
   personalassistant(data)

