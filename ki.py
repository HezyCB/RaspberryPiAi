#!/usr/bin/python3

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
from shlex import quote
import re
import os

chatbot = ChatBot('Kira')
chatbot.set_trainer(ChatterBotCorpusTrainer)

r = sr.Recognizer()
mic = sr.Microphone()

voiceInput = ''

def speak(text):
    os.system('pico2wave -l de-DE -w buffer.wav "' + text + '" && aplay buffer.wav -q')

while True:

    confirmedInput = False
    while (confirmedInput == False):

        try:
            with mic as source:

                r.adjust_for_ambient_noise(source)
                print(' #Listening')
                audio = r.listen(source)

            voiceInput = r.recognize_google(audio, language='de-DE')
            confirmedInput = True
            print('Du: ' + voiceInput)

        except sr.UnknownValueError:
            print(' #Error')
            #speak('I do not understand')

    if voiceInput == 'Computer':

        print(' #Conversation Started')
        speak('I am listening')
        print('Neon: I am listening')

        isConversation = True

        while (isConversation == True):

            confirmedInput = False
            while (confirmedInput == False):

                try:
                    with mic as source:

                        r.adjust_for_ambient_noise(source)
                        print(' #Listening')
                        #speak('I am listening!')
                        audio = r.listen(source)
                        print(' I am understanding...')


                    voiceInput = r.recognize_google(audio, language='de-DE')
                    confirmedInput = True
                except sr.UnknownValueError:
                    print(' #Error')
                    speak('I did not understad that.')
                    print('Neon: I did not understad that.')

            print('Du: ' + voiceInput)

            if voiceInput == 'Quiet':
                isConversation = False
                speak('Ok. I am waiting.')
                print('Neon: Ok. I am waiting.')
                print(' #Coversation paused')

            else:
                answ = str(chatbot.get_response(voiceInput))

                print(str('Neon: ') + answ)
                speak(quote(answ))
