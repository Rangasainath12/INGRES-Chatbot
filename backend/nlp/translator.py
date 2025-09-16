# Sarvam translation functions
from sarvamai import SarvamAI

client = SarvamAI(api_subscription_key="Saravam_API_KEY")

def translate_text_english(text):
    response = client.text.translate(
        input=text,
        source_language_code='auto',  # Auto-detect source language
        target_language_code="en-IN",  # Translate to English
        model='mayura:v1' # Using Mayura model for translation
    )
    return response.translated_text,response.source_language_code

def translate_text_hindi(text,detected_lang):
    response = client.text.translate(
        input=text,
        source_language_code='auto',  # Auto-detect source language
        target_language_code=detected_lang,  # Translate to Hindi
        model='mayura:v1' # Using Mayura model for translation
    )
    return response.translated_text
if __name__ == "__main__":
    translated,detected_lang=translate_text_english("नमस्ते, आप कैसे हैं?")
    print(f"Translated Text: {translated}, Detected Language: {detected_lang}")
