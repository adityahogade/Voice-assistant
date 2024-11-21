import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import  pyjokes
import string
import cv2
import numpy as np
import main as m
import pywhatkit as pw
def sptext():                        #it use to catch speech
    reconiser=sr.Recognizer()
    with sr.Microphone() as source:
        print('listning....')
        reconiser.adjust_for_ambient_noise(source) #it is use to remove source noise
        audio=reconiser.listen(source)
        try:
            print('recognising')
            data=reconiser.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print('Not understand')
def speechtx(x):
    engine =pyttsx3.init()
    voices =engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()
speechtx("please speaK passward")
if __name__ == '__main__':

    if sptext().__str__().lower() == 'hello':
        speechtx('hello. welcome to my project . what is your name ')
        a=input(sptext())
        speechtx("hello",a)


       speechtx('my name is john')
        while True:
            data1= sptext().__str__().lower()

            if "your name" in data1:
                 name= 'my name is john'
                 speechtx(name)
            elif "old are you" in data1:
                 age="i am four month old"
                 speechtx(age)
            elif 'time' in data1:
                 time = datetime.datetime.now().strftime("%I%M%p")  #now():-it returns live date and time
                 speechtx(time)
         elif 'youtube' in data1:
               webbrowser.open("https://www.youtube.com/c/GateSmashers")
           elif 'gmail' in data1:
               webbrowser.open("https://mail.google.com/mail/u/0/")
           elif 'joke' in data1:
               joke1=pyjokes.get_joke(language='en',category='neutral')
                print(joke1)
               speechtx(joke1)
           

           elif 'whatsapp message' in data1:
               speechtx("for sending message please enter following details ")
               pno = input("pno+91....=")
               msg = input('enter message:-')
               th = int(input('time in hour'))
               tm = int(input('time in minute:='))
               pw.sendwhatmsg(pno, msg, th, tm)
           elif 'exit' in data1:
               speechtx("thank you for visit voice assistant project")
               break
      else:
         print('thanks')

