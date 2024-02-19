"""
# OpenaiTTS
Transform a block of text into an MP3 file

## Notes
There's probably no reason at the moment that this be a class, but the intent
is to grow this app in the future to include other TTS providers (e.g., Google)
and therefore having an abstract superclass allows callers to not care which
provider they're using (by being able to pass class instances whereas passing
function pointers is not pretty).

This assumes that the environment variable `OPENAI_API_KEY` is set to a valid
API key; that is needed when the code calls OpenAI().
"""
from openai import OpenAI

class OpenaiTTS:
    def __init__(self):
        pass

    def speechify(self, text, filename, voice='echo', quality="low"):
        if quality.lower().startswith('h'):
            model = 'tts-1-hd'
        else:
            model = 'tts-1'

        client = OpenAI()


        response = client.audio.speech.create(
            model=quality,
            voice=voice,
            input=text,
        )

        response.stream_to_file(filename)


