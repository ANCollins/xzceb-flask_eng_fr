"""Module providing Function translating English and French."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
langT = LanguageTranslatorV3(
    version='2022-12-23',
    authenticator=authenticator
)
langT.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/c09dabd6-4b24-47ea-906e-8967de86b340')

langT.set_disable_ssl_verification(True)

def english_to_french(english_text):
    ''' Function to translate English to French. '''
    translation = langT.translate(
        text = english_text,
        model_id = 'en-fr'
        ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    ''' Function to translate French to English '''
    translation = langT.translate(
        text = french_text,
        model_id = 'fr-en'
        ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
