import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("I.A Kata:")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)