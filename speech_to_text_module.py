import speech_recognition as sr   # This is speech to text module which uses google library to convert
                                  # your speech to text.

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")             
    audio = r.listen(source)
 

try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Speech Recognition service; {0}".format(e))
