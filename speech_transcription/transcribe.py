#!/usr/bin/python3
import speech_recognition as sr
import os

def get_audio_files(folder):
        """ Retrieves Video files to be processed from hot folder """
        return [os.path.join(folder, f) for f in os.listdir(folder)
                if re.match(r'.*\.(mp4|avi|wav|mov|ASF)', f, flags=re.I)]

AUDIO_FILES = get_audio_files("data")
for AF in AUDIO_FILES:
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)

    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
