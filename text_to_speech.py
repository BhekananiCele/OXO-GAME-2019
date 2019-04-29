import pyttsx3

def text_to_speech(my_message):
    Fred = pyttsx3.init()
    rate = Fred.getProperty('rate')
    Fred.setProperty('rate', rate-30)
    Fred.say('{}'.format(my_message))
    Fred.runAndWait()
