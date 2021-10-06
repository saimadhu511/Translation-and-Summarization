from googletrans import Translator

# User enters the input text(any language)
Text=str(input("Enter:"))
translator = Translator()

# Translates to destination English Language
out=translator.translate(Text,dest='en')
print(out.text)