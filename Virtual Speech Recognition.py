import speech_recognition as sr # to recognise speech
import playsound #to play an audio
import random
from gtts import gTTS # google text to speech
import webbrowser #open browser
import ssl
import certifi
import time
import os #remove the audio files
import subprocess
from PIL import Image
import pyautogui#screenshot 
import pyttsx3
import bs4 as bs
import urllib.request

class person:
      name=''
      def setName(self,name):
          self.name=name

class asis:
      name=''     
      def setName(self,name):
          self.name=name
      
def there_exists(terms):
    for term in terms:
        if term in value_data:
           return True

def engine_speak(text):
    text= str(text)
    engine.say(text)
    engine.runAndWait()

r=sr.recognizer()#intialise the recognizer 
#listen for audio and convert it to text

def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio=r.listen(source , 5 ,5) # listen for audio via source
        print("done listening")
        voice_data=""
        try:
            voice_data=r.recognise_google(ausio)# convert audio to text
        except sr.UnknownValueError: # error : recogniser does not understand 
            engine_speak("Sorry,i did not get that")
        except sr.RequestError:
            engine_speak:("Sorry the server is down")# error the recogniser is not connected 
            print(">>",voice_data.lower())#print what the user said
            return voice_data.lower()

#get string and make a audio file to be played 
def engine_speak(audio_string):
    audio_string= str(audio_string)
    tts= gTTS(text=audio_string, lang = 'en')#text to speech
    r= random.randint(1,20000000)
    audio_file='audio' +str(r) + '.mp3'
    tts.save(audio_file)#save as mp3
    playsound.playsound(audio_file) #help us to play the audio
    print(asis_obj.name+ ":", audio_string)#print what app said 
    os.remove(audio_file)#Remove audio file

def repond(voice_data):
    #1) greeting
    if there_exists(['hello','hi','hey']):
        greetings=['hey, how can i help you'+ person_obj.name,'how can i help you'+ person_obj.name,'hello'+ person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    #2) name
    if there_exists(["what is your name","tell me your name",]):
         if person_obj.name:
             engine_speak("i don't know my name , please give my name by saying command your name should be ,,,, what is your name ")   
    else:
         engine_speak("what's you name")

    if there_exists(["my name is"]):
        person_name=voice_data.split("is")[-1].strip()
        engine_speak("okay sir i'll remember that your name is "+person_name())
        person_obj.setName(person_name)# remember name in person object

    if there_exists(["your name should be"]):
         asis_name=ce_data.split("be")[-1].strip()
         engine_speak("okay i'll remember that my name is "+asis_name)
         asis_obj.setName(asis_name)# remember name is asis object 

    #3) greetings
    if there_exists(["how are you doing"]):
         engine_speak("e'm very well, thanks for asking"+person_obj.name)

    #4) time
    if there_exists(["what's the time","tell me the time"]):
         time=ctime().split("")[3].split(":")[0:2]
         if time[0]=="00":
             hours='12'
         else:
              hours=time[0]
              minutes=time[1]
              time = hours+"hours and" + minutes + "minutes"
              engine_speak(time)    

    #5) search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
         search_term= voice_data.split("for")[-1]
         url="http://google.com/search?q"+ search_term 
         webbrowser.get().open(url)
         engine_speak("Here is what i found for") + search_term

    #6) search youtube
    if there_exists(["youtube"]):
         search_term = voice_data.split("for")[-1]
         url="http://www.youtube.com/results?search_query="+search_term
         webbrowser.get().open(url)
         engine_speak("Here is what i found for"+ search_term+ "on youtube")

    #7) get to know the stock price
    if there_exists(["price of"]):
         search_term=voice_data.split("for")[-1]
         url="http;//google.com/search?q"+search_term
         webbrowser.get().open(url)
         engine_speak("here is what i found for"+search_term+ "on google")
    # search for music 
    if there_exists(["play music"]):
         saerch_term= voice_data.split("for")[-1]
         url="http://open.spotify.com/search/"+search_term
         webbrowser.get().open(url)
         engine_speak("You are listening to"+ search_term +"enjoy")
    # search for amazon.com
    if there_exists(["amazon.com"]):
        search_term = voice_data.split("for")[-1]
        url="http://www.amazon.in"+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i founnd for"+ search_term + "on amazon.com")

    #make a note
    if there_exists(["make a note"]):
         search_term=voice_data.split("for")[-1]
         url="http://keep.google.com/#home"
         webbrowser.get().open(url)
         engine_speak("Here you can make notes")

    #open instagram
    if there_exists(["open instagram","want to have some fun time"]):
        search_term=voice_data.split("for")[-1]
        url="http://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")

    #open twitter  
    if there_exists(["open twitter"]):
        search_term=voice_data.split("for")[-1]
        url="http://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")     
    #8 time table
    if there_exists(["show my time table"]):
         im = Image.open(r"D:\Whatsapp Image 2019-12-26 at 10.51.10 AM.jpeg")         
         im.show()

    #9 open gmail
    if there_exists(["open my gmail","gmail","check my email"]):
        search_term = voice_data.split("for")[-1]
        url = "http://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")

    #calc
    if there_exists(["plus","minues","multiply","divide","power","+","-","*","/"]):
         opr = voice_data.split()[1]

         if opr == '+':
              engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
         elif opr =='-':
              engine_speak(int(voice_data.split()[0] - int(voice_data.split)[2]))
         elif opr =='multiply':
              engine_speak(int(voice_data.slpit()[0]) * int(voice_data.split()[2]))
         elif opr =='divide':
              engine_speak(int(voice_data.slpit()[0]) / int(voice_data.split()[2]))
         elif opr =='power':
              engine_speak(int(voice_data.slpit()[0]) ** int(voice_data.split()[2])) 
         else:
            engine_speak("Wong operator")  
    #screenshot
    if there_exists(["capture","screenshot","my screen"]):
         myScreenshot=pyautogui.screenshot()
         myScreenshot.save('')


    if there_exists(["exit","quit","goodbye"]):
         engine_speak("we could continue more,but.,,.,,,,.,,,,, bye")
         exit()


time.sleep(1)
asis_obj= asis()
person_obj=person()
asis_obj.name='Kim'
engine=pyttsx3.init()

while(1):
    voice_data = record_audio("Recording") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond