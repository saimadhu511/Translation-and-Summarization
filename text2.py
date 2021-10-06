# importing library sys
import sys

from googletrans import Translator

# User enters the input text(any language) 
Text=str(input("Enter:"))
translator = Translator()

# Translating to English Language
out=translator.translate(Text,dest='en')

# Translated text to save is translated.txt file
sys.stdout = open("translated.txt", "w")
print(out.text)
sys.stdout.close()
