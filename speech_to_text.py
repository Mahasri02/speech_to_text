import speech_recognition as src
import pyaudio

regconizer = src.Recognizer()
print("speak...")
with src.Microphone() as source: #it setup the audio input as the speech recognization
    regconizer.adjust_for_ambient_noise(source)#it adjust the input
    audio = regconizer.listen(source)#it gets the input as audio

try:
    print("regconizing")
    text = regconizer.recognize_google(audio)#it converts the audio into text using the google speech recognization api
    print(text)
except src.unknownerror:  #occurs due to the unclear voice
    print("the voice is not regconizable please try again")
except src.error as e:   #occurs due to the cancellation in the requests
    print("there is an issue in the network or api")