import pyaudio
import speech_recognition as sr
import ITHANKe as th
mic = sr.Microphone(1)
mic
recog = sr.Recognizer()
recog
i=0
with mic as source:
    for i in range(10):
        print("listening")
        audio = recog.listen(source)
        try:
            Speech=recog.recognize_google(audio,language='th')
            print("you said: ",Speech)
            th.ChatBot(Speech)
        except:
            pass