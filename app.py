import gradio as gr
from gtts import gTTS
import os
from deep_translator import GoogleTranslator

# إعداد المترجم
def translate_text(text, src_lang, target_lang):
    translator = GoogleTranslator(source=src_lang, target=target_lang)
    return translator.translate(text)

def text_to_speech(text, lang):
    # تحويل النص إلى صوت
    tts = gTTS(text=text, lang=lang)
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

def translate_and_synthesize(input_text, input_lang):
    if input_lang == "English":
        # ترجمة من الإنجليزية إلى العربية
        translated_text = translate_text(input_text, src_lang='en', target_lang='ar')
        audio_original = text_to_speech(input_text, lang='en')  # الصوت باللغة الإنجليزية
        audio_translated = text_to_speech(translated_text, lang='ar')  # الصوت باللغة العربية
    else:  # إذا كان المدخل باللغة العربية
        # ترجمة من العربية إلى الإنجليزية
        translated_text = translate_text(input_text, src_lang='ar', target_lang='en')
        audio_original = text_to_speech(input_text, lang='ar')  # الصوت باللغة العربية
        audio_translated = text_to_speech(translated_text, lang='en')  # الصوت باللغة الإنجليزية
        
    return audio_original, audio_translated  # إرجاع الصوت الأصلي والصوت المترجم
