# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:09:37 2020

@author: Manas gupta
"""
import pyttsx3
import datetime
import speech_recognition as  sr
import os
import smtplib as s
import wikipedia
import webbrowser

complete = True

# VOICE Settings
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio) :
    engine.say(audio)
    engine.runAndWait()
    
def wishMe() :
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Hey Manas GOOOD MORNING !")
    elif hour>=12 and hour<16 :
        speak("Hey Manas How Was You Afternoon ?")
    elif hour>=16 and hour<20 :
        speak("Hey Manas Good Evening") 
    elif hour>=20 and hour<=24 :
        speak("Hey Manas its too late , Time to sleep !")
    else :
       speak("Hey Manas Hope you are having a good day ?")  
       
    speak("Its Jarvis ! How MAY I Help You ?")       
        
# Most important thing which will analyse what the user is trying to say
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"
    
    return query

def sendEmail(reciever,content) :
    server = s.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('manasgupta1820@gmail.com', 'your-password')
    server.sendmail('manasgupta1820@gmail.com',reciever, content)
    server.close()
 
def addFriend(name,email) :
    speak("adding "+name+" as your close friend")
    friends[name]=email
    speak('Successfuly added '+name+' as your friend')  
    

if __name__ == '__main__' :
    wishMe()
    while complete :
        
        query = takeCommand().lower()
        
        if 'shutdown' in query :
            speak("Jarvis signing off !") 
            os.system("shutdown /s /t 1")
        
        if 'send a email' in query :  
            try :
                speak("Can you please enter your friends email:")
                email=input()                  
                speak("Got that ! Can you tell the message please :")
                content = takeCommand()
                sendEmail(email,content)
                speak("Successfully sent the email to "+email)
            except Exception as e :
                print(e)
                speak("Sorry task was not completed , pls try saying that again")
                
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        if 'open google' in query:
            webbrowser.open("google.com")

        if 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"DuDE, the time is {strTime}")
            
        if 'shut up' in query :
           speak("Jarvis signing off !")  
           break;
           
                        
                    
                    
            
            
            
            
