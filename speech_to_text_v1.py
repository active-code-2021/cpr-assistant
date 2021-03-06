import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
import threading
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator("nKrI3BBoFjUeKgZ40Mjd4Wf8dIFf0f7z36WD7hP7Tl4_")
authenticator.set_disable_ssl_verification(True)
service = SpeechToTextV1(authenticator=authenticator)
service.set_service_url(
    'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/b9125aa5-b317-4650-b4d2-3bcd6b48e521'
)
service.set_disable_ssl_verification(True)

def spt():
    with open(join(dirname(__file__), './speech.wav'), 'rb') as audio_file:
        result = service.recognize(audio=audio_file,
        content_type='audio/wav').get_result()
        return result["results"][0]["alternatives"][0]["transcript"]

# def sptxt():
#       with open(join(dirname(__file__), './speech.wav'),
#               'rb') as audio_file:
#          result = service.recognize(
#             audio=audio_file,
#         content_type='audio/wav').get_result()
#       # print(json.dumps(result, indent=2))
#        return result["results"][0]["alternatives"][0]["transcript"]
print(spt())
# # Example using websockets
# class MyRecognizeCallback(RecognizeCallback):
#     def __init__(self):
#         RecognizeCallback.__init__(self)

#     def on_transcription(self, transcript):
#         print(transcript)

#     def on_connected(self):
#         print('Connection was successful')

#     def on_error(self, error):
#         print('Error received: {}'.format(error))

#     def on_inactivity_timeout(self, error):
#         print('Inactivity timeout: {}'.format(error))

#     def on_listening(self):
#         print('Service is listening')

#     def on_hypothesis(self, hypothesis):
#         print(hypothesis)

#     def on_data(self, data):
#         print(data)

# # Example using threads in a non-blocking way
# mycallback = MyRecognizeCallback()
# audio_file = open(join(dirname(__file__), './speech.wav'), 'rb')
# audio_source = AudioSource(audio_file)
# recognize_thread = threading.Thread(
#     target=service.recognize_using_websocket,
#     args=(audio_source, "audio/l16; rate=44100", mycallback))
# recognize_thread.start()
