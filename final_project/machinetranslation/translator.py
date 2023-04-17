from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
API_KEY = "HGFc5awcNaXIXa6Kpd8AlPTd4i6TRsIytLlZ0qBwNQGs"
API_URL = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/1c125d7a-1833-4d04-9b31-b76e087465fb"
#model_id = 'en-it'
#text_to_translate = 'Your content you want translate here'

# Prepare the Authenticator
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(API_URL)

# Translate
def english_to_french(englishtext):
    if englishtext == "":
        return ""
    #print(f"English :{englishText}")
    frenchtext = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    #print(f"look:{frenchText}")
    frenchtext = frenchtext['translations'][0]['translation']
    return frenchtext

def french_to_english(frenchtext):
    if frenchtext == "":
        return ""
    englishtext = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    englishtext = englishtext['translations'][0]['translation']
    return englishtext

# Print results
#print(englishToFrench("Hello"))
#print(frenchToEnglish("Bonjour"))

