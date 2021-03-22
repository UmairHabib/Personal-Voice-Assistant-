import pyttsx3,datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os,random
import smtplib

'''First of all wish you with respect to time,
speaks a string,
convert voice to string,
speaks data by getting from wikipedia,
opens google, youtube, stackoverflow,
runs music from directory randomly,
speaks current time,
opens a software i.e. mozilla,
email to user,
quits software'''

engine=pyttsx3.init('sapi5') #used to get inbuilt voice both male and female
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) #male voice 0, female voice 1

senderEmail='UmairHabib000@gmail.com'
recieverEmail= 'UmairHabib000@gmail.com'
passwordOfSender='password'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(senderEmail,passwordOfSender)
    server.sendmail(senderEmail,to,content)


def wishMe(): #used to wish in start of program
    hour= int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak('Good Morning')
    elif hour>=12 and hour<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak("I am Umair's personal assistant. Please tell me how can I help you?")


#open a ppf account
#TERM LIFE
#

def takeCommand():
    '''it takes  voice input and returns string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1 #pause between voice
        audio= r.listen(source) #it will listen audio here


        try:
            print('Recognizing... ')
            query=r.recognize_google(audio,language='en-in') #convert audio to english using Google Cloud
            print(f'User Said: {query}\n')


        except Exception as e:
            print(e)
            print("Say that again please ...")
            return "None"
        return query


if __name__=='__main__':
    print('Voice Assistant Starter')
    wishMe()

    while True:
        query= takeCommand().lower()
        try:
            if 'wikipedia' in query:
                speak('Searching wikipedia...')
                query=query.replace('wikipedia',"")
                results= wikipedia.summary(query,sentences=2)
                speak("According to Wikipedia ")
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open('youtube.com')

            elif 'open google' in query:
                webbrowser.open('google.com')

            elif 'open stack overflow' in query:
                webbrowser.open('stackoverflow.com')

            elif 'play music' in query:
                musicDir= 'F:\\NFAK\\' #paste your music directory path here
                songs= os.listdir(musicDir)
                os.startfile(os.path.join(musicDir,random.choice(songs)))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                speak(f'Sir the time is {strTime}')
            elif 'open mozilla' in query:
                codePath= "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                os.startfile(codePath)
            elif 'quit' in query:
                speak('Personal Assistant is Shutting Down. Good Bye Umair Habib')
                print('Personal Assistant is Shutting Down...!')
                break
            elif 'email to' in query:
                speak('What should I say?')
                content=takeCommand()
                sendEmail(recieverEmail,content)
                speak("Email has been sent")
        except Exception as e:
            print("Error Occured")


