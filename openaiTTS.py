import openai
from TTS import TTS
from openai import OpenAI

class OpenaiTTS(TTS):
    def __init__(self):
        super()

    def speechify(self, text, filename, model='echo'):
        client = OpenAI()


        response = client.audio.speech.create(
            model="tts-1-hd",
            voice=model,
            input=text,
        )

        response.stream_to_file(filename)


