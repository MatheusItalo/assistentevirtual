import pyttsx3 

speak = pyttsx3.init('sapi5')

speak.setProperty('voice', b'brazil')

def speaker(text):
	speak.say(text)
	speak.runAndWait()
