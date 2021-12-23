import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
import pyjokes
import cv2


r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def jokes():
    Text = pyjokes.get_joke(language="en", category= "all")
    myobj = gTTS(text=Text, lang = "en", slow = False)
    myobj.save("Joke.mp3")
    os.system("start Joke.mp3")
    os.close("Joke.mp3")

def repeat(MyText):
    myobj = gTTS(text=MyText, lang = "en", slow = False)
    myobj.save("New.mp3")
    os.system("start New.mp3")

def camera():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Capture Image")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Capture Image", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "Image_Captured_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you said " + MyText)
            if MyText == "tell me a joke":
                jokes()
                continue
            if MyText == "take my picture":
                camera()
                continue
            if MyText == "quit":
                print("Made by Mayank Sharma")
                print("Follow me at Github : www.github.com/mayanksharma61099")
                print("Connect with me on LinkedIn: www.linkedin.com/in/mayank-sharma-ab9784121/")
                print("Send me an email: mayanksharma61099")
                break
            else:
                repeat(MyText)
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown Error Occured")
