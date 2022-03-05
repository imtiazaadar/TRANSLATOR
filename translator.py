# Author : Imtiaz Adar
# Project : Translator
# Language : Python

import speech_recognition as speech_engine
import time, os
import pyttsx3 as tts_engine
import deep_translator as deep_t

class Translator_Adar:
    def __init__(self):
        self.text_to_speech = tts_engine.init()
        self.voices = self.text_to_speech.getProperty('voices')
        self.text_to_speech.setProperty('voice', self.voices[1].id)

    def listen(self):
        listener = speech_engine.Recognizer()
        self.talk('Translate from : ')
        with speech_engine.Microphone() as mic:
            print('Listening...')
            listener.adjust_for_ambient_noise(mic)
            my_voice = listener.listen(mic)
            try:
                from_command = listener.recognize_google(my_voice).lower()
                from_lang = from_command
                print(from_lang)
                self.talk(from_lang)
                self.talk('Translate to : ')
                print('Listening...')
                listener.adjust_for_ambient_noise(mic)
                my_voice1 = listener.listen(mic)
                try:
                    to_command = listener.recognize_google(my_voice1).lower()
                    to_lang = to_command
                    print(to_lang)
                    self.talk(to_lang)
                    self.talk('Say something : ')
                    print('Listening...')
                    listener.adjust_for_ambient_noise(mic)
                    my_voice2 = listener.listen(mic)
                    try:
                        line_command = listener.recognize_google(my_voice2).lower()
                        trans_line = line_command
                        print('The line to be translated is : ', trans_line)
                        self.talk(f'The line to be translated is : {trans_line}')
                        self.translate_(from_lang, to_lang, trans_line)
                        time.sleep(1)
                        self.talk('Thank you')
                    except Exception:
                        print('# Sorry #')

                except Exception:
                    print('# Sorry #')

            except Exception:
                print('# Sorry #')

    def translate_(self, from_lang, to_lang, line):
        translate__ = deep_t.GoogleTranslator(source=from_lang, target=to_lang)
        translated_line = translate__.translate(line)
        print(translated_line)
        self.talk(f'Translated line : {translated_line}')

    def talk(self, command):
        self.text_to_speech.say(command)
        self.text_to_speech.runAndWait()
        self.text_to_speech.stop()

if __name__ == "__main__":
    translate_class = Translator_Adar()
    print('Welcome To The Google Translator By Imtiaz Adar')
    translate_class.talk('Welcome To The Google Translator By Imtiaz Adar')
    running = True
    while running:
        translate_class.talk('Want to translate ?')
        want = input('Want to translate ? Y/ Yes  N/ No\n').lower()
        if want == 'y':
            translate_class.talk('yes')
            translate_class.listen()
        else:
            translate_class.talk('no')
            running = False
    os.system('pause')