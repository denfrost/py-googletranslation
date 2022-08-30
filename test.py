from pygoogletranslation import Translator

translator = Translator()
text = 'Good Morning'
dest='th'
translated = translator.translate(text, dest=dest)
print(type(translated))
print('Translat text : ' +text)
print('Translated on ['+dest+']: ' +translated.text)
print('Transcription : '+translated.pronunciation)