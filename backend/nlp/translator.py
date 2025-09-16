from transformers import MarianMTModel, MarianTokenizer

src_lang = "hi"  # Hindi
tgt_lang = "en"  # English

model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_to_english(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
