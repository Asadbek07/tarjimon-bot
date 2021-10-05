from googletrans import Translator

def translate_text(text):
	translator = Translator()
	if translator.detect(text).lang == 'uz':
		dest = 'en'
	else:
		dest = 'uz'

	translated_text = translator.translate(text, dest).text
	
	return translated_text



if __name__ == '__main__':
	print(translate_text('hello'))
	print(translate_text('salom'))


