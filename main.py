# Author : Imtiaz Adar
# Project : Translator
# Language : Python
import os
import deep_translator as deep_t
from_lang = input('Translate from : ')
to_lang = input('Translate to : ')
line = input('The line to be translated is : ')
translate = deep_t.GoogleTranslator(source=from_lang, target=to_lang)
translated_line = translate.translate(line)
print(translated_line)
os.system('pause')