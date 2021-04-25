#import library
import speech_recognition as sr
from keys import GOOGLE_CLOUD_API_KEY

print(GOOGLE_CLOUD_API_KEY)
def somethingwecopiedonline(file_name):
    r = sr.Recognizer()

    with sr.AudioFile(file_name) as source:
        audio = r.listen(source)

    try:
        # print("Google Cloud Speech thinks you said " + r.recognize_google(audio))
        result = r.recognize_google(audio)
        return result
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))


def somethingelse():
    return 23
