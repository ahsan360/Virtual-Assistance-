from logging import root
from socket import IPV6_PKTINFO
from tkinter.tix import Tree
import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
import os.path
import smtplib
from tkinter import *
import tkinter as tk




listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

def talk(text):
 engine.say(text)
 engine.runAndWait()
talk("Hello sir, what can i do for you sir")
def take_command():
    try:
     with sr.Microphone() as source:
      print("listeninig...")
      voice = listener.listen(source)
      command = listener.recognize_google(voice)
      #command = command.lower()
      #if'alexa' in command:
      command = command.replace('alexa','')
     return command
    except: pass
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ahsanhabib462@gmail.com','pasword')
    server.sendmail('ahsanhabib462@gmail.com', to, content)
    server.close()   
def search(key):
    try:
     from jarvis import search
    except ImportError:
     print("No module named 'google' found")
    query = "Geeksforgeeks"
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
     print(j)

def run():
    command = take_command()
    print(command)
    if 'play' in command:
         song = command.replace('play','')
         talk('plying'+song)
         print("playing.."+song)
         pywhatkit.playonyt(song)
    elif  'how are you' in command:
         print("I am fine sir . how about you?")
         talk('I am fine sir . how about you?')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' +time)
        print(time)
    elif 'who is' in command :
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        if info :
            print(info)
            talk(info)
        else : talk('nothing is found')

    elif 'open google' in command :
         webbrowser.open("google.com")
    elif 'open youtube' in command :
         webbrowser.open("youtube.com") 
    elif 'email to'  in command :
         talk("to whom")
         var =   take_command() 
         print(var)
         to = "harryyourEmail@gmail.com"
         talk("what text to send")
         text = take_command()
         print(text)
         sendEmail(to,text)
         talk("email has been sent")
         
    else : 
        talk("Sorry sir I can not get It")

root = Tk()
root.title('Button')
root.geometry("500x500")
def click ():
     run()
mybutton = Button(root,text ="Say Something" ,command= click ,padx=50,pady=10)
mybutton.pack()
label = tk.Label(text="Hello, Tkinter", background="#34A2FE")
root.mainloop()
