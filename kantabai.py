import speech_recognition as sr
import pyttsx3
import smtplib
from email.message import EmailMessage
import time
from tqdm import tqdm
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
from googlesearch import search
import os, urllib, sys
import webbrowser


listener = sr.Recognizer()
    
def talk(text,x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[x].id)
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            return info.lower()
    except Exception as e:
        print(e)

def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('Type Email id here','XXXXXXXXXXXXXXXX')
    email = EmailMessage()
    email['From'] = 'XXXXXXXXXXXXXXXXXX'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)

    server.send_message(email)
    for i in tqdm([1,2,3,4,5]):
        time.sleep(0.3)

    #   Partials 
take = 'xyz'
new = False 
email_dict = {
    # type details of email here as an object
} 
web = {
    'chrome':""
}


def fun(x):
    if 'tell me my name' in x:
        global new
        if(new==False):
            talk('I dont know the exactly but i think hear you voice! can you please tell me your name! Just say your name only',0)
            y = get_info()
            talk(f'IS this your name dear! {y}! If not just say yes or no',0)
            print(f'Your name is {y}')
            correct = get_info()
            if(correct == 'no'):
                talk('Ok! Then you can type your name here below',0)
                global take
                take = input("Type here .. ")
                # global new
                new = True
                talk(f'Ok! You are {take}! i have remembered your name',0)  
            else:
                talk("Ok i got it! You can ask any other thing you want",0)      
        else:
            talk(f'I know your name! you are {take}',0)
    if 'email' in x:
        talk("ok! You wanna send an email! i am calling my son parichay!! who will help you in sending an email! Please wait for 2 or 3 seconds",0)
        for i in tqdm([1,2,3,4,5]):
            import time
            time.sleep(0.5)   
        talk("Hello dear! I am parichay !! i can send an email very quickly! You can try this",1)
        talk('What you gonna have to do is! to say that to whom you wanna send an email! just say only the reciver name ',1)
        name = get_info()
        talk('Is this receiver name correct see this ! just say yes or no',1)
        print(f"Receiver name = {name}")
        correct = get_info()
        if(correct == 'no'):
            talk('Ok! then you can type the email here',1)
            x = input('Type here :')
            talk('Ok!!Then what is the subject! of your email dear?',1)
            subject = get_info()
            print(f'Emm! Your subject is: {subject}')
            talk('Sounds good ! Now tell me the body of your email?',1)
            message = get_info()
            print(f'Ok Ok! Your message is : {message}')
            talk(f"ok! Now see your email details below:",1)
            print(f"\nTo: {x}\nSubject: {subject}\nMessage: {message}")
            import time
            time.sleep(2)
            talk("Is this correct? If not just say no! if yes just say yes",1)
            verify = get_info()
            if verify=="no":
                talk("Ok! now tell me which part is wrong! like subject or message or both! just say subject or message or both only",1)
                ss = get_info()
                if ss =="subject":
                    talk("Ok! then type the exact subject below",1)
                    xx = input("Type here ..")
                    subject = xx
                elif ss == "message":
                    talk("Ok! then type the exact message below",1)
                    xx = input("Type here ..")
                    message = xx
                else:
                    talk("Ok! all are wrong! sorry for that my dear! type both correct below",1)
                    xx = input("Type subject:")
                    yy= input("Type message:")
                    subject = xx
                    message = yy
            talk("Ok! i am sending your email to your receiver! please wait for few seconds! its on way",1)
            send_email(x,subject,message)
            talk("Your email has sent successfully! congratulation",1)
            print("\n Your email has sent successfully")
        else:     
            receiver = email_dict[name]
            print(f'Ok! Your reciever is:{name}=> {receiver}')
            talk('Ok!!Then what is the subject! of your email dear?',1)
            subject = get_info()
            print(f'Emm! Your subject is: {subject}')
            talk('Sounds good ! Now tell me the body of your email?',1)
            message = get_info()
            print(f'Ok Ok! Your message is : {message}')

            talk(f"ok! Now see your email details below:",1)
            print(f"\nTo: {receiver}\nSubject: {subject}\nMessage: {message}")
            import time
            time.sleep(2)
            talk("Is this correct? If not just say no! if yes just say yes",1)
            verify = get_info()
            if verify=="no":
                talk("Ok! now tell me which part is wrong! like subject or message or both! just say subject or message or both only",1)
                ss = get_info()
                if ss =="subject":
                    talk("Ok! then type the exact subject below",1)
                    xx = input("Type here ..")
                    subject = xx
                elif ss == "message":
                    talk("Ok! then type the exact message below",1)
                    xx = input("Type here ..")
                    message = xx
                else:
                    talk("Ok! all are wrong! sorry for that my dear! type both correct below",1)
                    xx = input("Type subject :")
                    yy= input("Type message :")
                    subject = xx
                    message = yy
            
            talk("Ok! i am sending your email to your receiver! please wait for few seconds! its on way",1)
            send_email(receiver,subject,message)
   
            print("\n Your email has sent successfully")
            talk("Your email has sent successfully! congratulation",1)
    if 'music' in x:
        talk("Ok! Do you wanna catch yup some music! Then tell the music or a song name only! to play for you ",0)
        song = get_info()
        talk("ok! I got it! i am gonna play it for you, I am getting back from youtube !enjoy",0)
        pywhatkit.playonyt(song)
        input("Press any key to continue")

    if 'song' in x:
        talk("Do you wana hear a song! Then tell the song name only! to play for you ",0)
        song = get_info()
        talk("I got it! i am gonna play it for you, I have found something from youtube !enjoy",0)
        pywhatkit.playonyt(song)
        input("Press any key to continue")
        
    # if 'play' in x:
    #     talk("Please tell me the exact song title name! such that i can find it for you ",0)
    #     song = get_info()
    #     talk("I got it! i am gonna play it for you, your favourite song is here !enjoy",0)
    #     pywhatkit.playonyt(song)
    #     import time
    #     time.sleep(10)
    if 'time' in x:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'It is {time} in my clock',0)
    if 'who is' in x:
        y = x.replace('who is','')
        info = wikipedia.summary(y,1)
        talk(f'Ok! i have found something from web',0)
        print(f"Short summary=>\n{info}")
        talk(info,0)
    if 'what is' in x:
        y = x.replace('what is','')
        info = wikipedia.summary(y,1)
        talk(f'Ok! i have found something from web',0)
        print(f"Short summary=>\n{info}")
        talk(info,0)
    if 'joke' in x:
        talk("Ok! i can throw a bad joke for you! listen",0)
        talk(pyjokes.get_joke(language="en", category="neutral"),0)
    if 'tongue' in x:
        talk("Ok! one tongue twister is for you",0)
        talk(pyjokes.get_joke(language="de", category="twister"),0)
    if 'how are you' in x:
        talk("I am fine dear! what about you",0)
    if 'i am good' in x:
        talk("God bless you dear! Tell me what can i help you",0)
    if 'i am fine' in x:
        talk("God bless you dear! Tell me what can i help you",0)
    if 'who are you' in x:
        talk("I am your personal assistant my friend! tell me what can i help you",0)    
    if 'hell' in x:
        talk("Hey! Dont use these types of words here! My mon is also here",1)
    if 'fuck' in x:
        talk("Hey! Dont use these types of words here! My mom is also here",1)
    if 'your age' in x:
        talk('I am thousand year old!',0)
    if 'your name' in x:
        talk("I am your personal assistant Manju ",0)    
    if 'love' in x:
        talk('I love you 2 to infinity in a loop',0)
    if 'get lost' in x:
        talk("How dare you to talk it like with my mother! Stay in your limit! get lost",1)
        return    
    if 'bye' in x:
        talk("Bye Bye dear! See you later",0)
        return
    if 'are you single' in x:
        talk("I am relationship with internet! when it dies ! i as well",0) 
    if 'chrome' in x:
        talk("opening chrome",0)
        # subprocess.Popen("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe") 
    if 'youtube' in x:
        talk("Opening youtube",0)    
        webbrowser.open("https://www.youtube.com/")
        input("Press any key to continue")


    # if 'search' in x:
        
    #     filename = 'http://www.google.com/search?' + urllib.urlencode({'q': ' '.join(sys.argv[1:]) })
    #     cmd = os.popen("lynx -dump %s" % filename)
    #     output = cmd.read()
    #     cmd.close()
    #     print(output)    
  

def getinfo():
    print("****************Hello! Manju Sethi is here! Your personal assistant***********************\n")
    talk("Hello! i am manju, Your personal assistant! What can i help you",0)
    while True:
        command = get_info()
        if command==None:
            # exit
            talk("i cant hear it correctly! Can you please repeat it again",0)
            command = get_info()    
        fun(command)
        if 'bye' in command:
            break
        if 'get lost' in command:
            break  
    print("Bye! see you later")    

getinfo()    