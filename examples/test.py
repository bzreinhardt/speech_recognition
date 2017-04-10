#!/usr/bin/env python3

from pprint import pprint
import imp

import os, sys, inspect
 # realpath() will make your script run, even if you symlink it :)
#cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
#if cmd_folder not in sys.path:
sys.path.insert(0, '/Users/Zaaron/Code/speech_recognition')
#sr = imp.load_source('speech_recognition', '/Users/Zaaron/Code/speech_recognition')
import speech_recognition as sr
print "speech recognition path  = %s"%sr.__file__

# obtain path to "english.wav" in the same folder as this script
from os import path
import json

FILE_NAME = "MobileAppCall"
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "%s.wav"%FILE_NAME)
TRANSCRIPT_FILE = path.join(path.dirname(path.realpath(__file__)), "%s.json"%FILE_NAME)
DURATION = 60
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source, duration=DURATION)  # read the entire audio file
"""
# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY", show_all=True)`
    # instead of `r.recognize_google(audio, show_all=True)`
    print("Google Speech Recognition results:")
    pprint(r.recognize_google(audio, show_all=True))  # pretty-print the recognition result
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = "INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"
try:
    print("Google Cloud Speech recognition results:")
    pprint(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, show_all=True))  # pretty-print the recognition result
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))

# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai recognition results:")
    pprint(r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True))  # pretty-print the recognition result
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "INSERT BING API KEY HERE"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Bing recognition results:")
    pprint(r.recognize_bing(audio, key=BING_KEY, show_all=True))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"  # Houndify client IDs are Base64-encoded strings
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"  # Houndify client keys are Base64-encoded strings
try:
    print("Houndify recognition results:")
    pprint(r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY, show_all=True))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))
"""
# recognize speech using IBM Speech to Text
with open("watson_credentials.json", 'r') as f:
    credentials = json.loads(f.read())
IBM_USERNAME = str(credentials['username'])  # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = str(credentials['password'])  # IBM Speech to Text passwords are mixed-case alphanumeric strings
print "credentials - \n username: %s \n password: %s"%(IBM_USERNAME, IBM_PASSWORD)
try:
    #print("IBM Speech to Text results:")
    transcript = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, show_all=True)
    with open(TRANSCRIPT_FILE, 'w') as f:
        f.write(json.dumps(transcript))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))
