Text-to-Speech and Translation AI Project - README

Description:
This project is a system for converting text to speech with instant translation, supporting both Arabic and English languages. It allows users to input text in either language and converts it into an audio file, while also providing the audio translation of the text in another language. The project relies on open-source libraries such as Gradio for user interaction, gTTS for speech generation, and Deep-Translator for translation.

Requirements:
- Python 3.x: The programming language used for the project.
- Gradio: To create the interactive user interface.
- gTTS: For converting text to speech using Google Text-to-Speech service.
- Deep-Translator: For translating text between English and Arabic.
- Hugging Face: To utilize some available tools and models on the platform.

- Installation Instructions:
You can install all requirements through the requirements.txt file or manually as follows:
pip install gradio
pip install gtts
pip install deep-translator

1. To run the project, use the following Link:
(https://991bdf45fdd0e33eaa.gradio.live/)
or visit my page on hugging face link:
(https://huggingface.co/spaces/Menawer/text-to-speech)
3. Once the application is running, an interactive Gradio interface will automatically open in your browser. The interface allows you to input the text and select the language.
4. Choose the language you want to hear the audio in, either in the original language or in the translated language.
5. Click the "Submit" button, and an audio file will be generated for both the input text and the translated text.

6. Expected Output:
- Audio file in the original language entered by the user.
- Audio file in the translated language (depending on the user's selection for the translated language).
For example:
- If the user inputs text in English, they will receive an audio file in English and another audio file in the translation to Arabic.
- The reverse is true when entering text in Arabic.

- Code Explanation:
- text_to_speech: A function to convert text to speech using the gTTS library. It takes the text and language as input and produces an audio file.
- translate_and_synthesize: A function that translates the input text to another language using Deep-Translator and then converts the (original and translated) texts to audio files.
- Gradio Interface: An interactive interface to create a user-friendly experience for inputting text, selecting language, and listening to results.


Project Benefits:
- Language Learning: It helps users learn the pronunciation of texts in two different languages, contributing to language skills improvement.
- Global Accessibility: Supporting two major languages (Arabic and English) makes it useful for communication and translation across cultures.
- Ease of Use: The interactive Gradio interface makes it easy for any user to use the project without needing technical knowledge.

- Contribution:
Contributions to improve the project or add support for more languages or features are welcome. If you wish to contribute, please open an "Issue" or submit a "Pull Request" on GitHub.
