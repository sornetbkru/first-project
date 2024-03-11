import pyttsx4

import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

engige = pyttsx4.init()
engige.say('Привет, Макс!')
engige.runAndWait(" Hi ")