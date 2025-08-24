from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from deep_translator import GoogleTranslator
load_dotenv()

def eng_to_ger(text):
    translated_text = GoogleTranslator(source='en', target='de').translate(text)
    return translated_text
def end_to_itly(text):
    translated_text = GoogleTranslator(source='en', target='it').translate(text)
    return translated_text
def eng_to_fren(text):
    translated_text = GoogleTranslator(source='en', target='fr').translate(text)
    return translated_text

