import speech_recognition as sr
#reconhecedor
r = sr.Recognizer()

#abrir mic
with sr.Microphone() as source:
    audio = r.listen(source) # define microfone como fonte de audio

    print(r.recognize_google(audio))