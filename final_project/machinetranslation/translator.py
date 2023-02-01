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

langT.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')
