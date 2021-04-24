#import library
import speech_recognition as sr

user_choice = input("Enter speech :")
if(user_choice == "microphone"):

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            # using google speech recognition
            print("Text: "+r.recognize_google(audio_text))
        except:
            print("Sorry, I did not get that")
elif(user_choice == "recorded"):
    r = sr.Recognizer()

    with sr.AudioFile('audio.wav') as source:
        audio_text = r.listen(source)
        try:
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print(text)
        except:
            print('Sorry.. run again...')
