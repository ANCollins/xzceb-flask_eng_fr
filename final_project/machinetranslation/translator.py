import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('{apikey}')
langT = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)
langT.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

"""
Function to translate English to French
"""
def englishToFrench(englishText):

    # This is to check for Null or empty text field.
    if englishText == "":
        return "Enter English Text"
    
    # We can proceed with the rest of the code if Null check passes.
    else:
        
        # Translates the english text to french text.
        translation = langT.translate(
            text = englishText,
            model_id = 'en-fr'
            ).get_result()

        frenchText = translation['translations'][0]['translation']
        return frenchText

"""
Function to translate French to English
"""
def frenchToEnglish(frenchText):

    # This is to check for Null or empty text field.
    if frenchText == "":
        return "Enter French Text"

    else:

        # Translates the english text to french text.
        translation = langT.translate(
            text = frenchText,
            model_id = 'fr-en'
            ).get_result()

        englishText = translation['translations'][0]['translation']
        return englishText

