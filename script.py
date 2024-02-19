"""
# script.py
Read in, parse, and convert script text to speech

## Script file format
Script files are broken into a set of sections, of which there must be at least one.

The start of a section is indicated by a '#' being the first character of the line.
The # is followed by the name of the section.  It is optionally followed by a '/',
amd then the name of the voice you want the section to use.  This is probably an
unnecessary feature, but I like it for introductions (see script.txt for an example).

## Functionality

This class does three things:

1. It parses the script file (and retains the parsed version in instance variables)
2. It provides the UI (such as it is) information about the sections to drive the UI
3. It will call the TTS class (at the moment, just openaiTTS) to translate the text from a section to an MP3 file.

"""

from datetime import datetime as dt
from collections import OrderedDict
from openaiTTS import OpenaiTTS

class Script:

    def __init__(self, script_file, _default_voice = 'echo'):
        self.default_voice = _default_voice

        with open(script_file, 'r') as f:
            script = f.read()

        lines = script.split('\n')
        lines.append('# E-O-F')

        self.sections = OrderedDict()
        self.voices = []

        curname = 'Unnamed Section'
        curtext = ''

        for l in lines:
            if l.startswith('#'):
                if len(curtext) > 0:
                    self.sections[curname] = curtext
                curtext = ''
                l = l[1:].strip()
                if l.find('/') >= 0:
                    curname = l[:l.find('/')].strip()
                    self.voices.append(l[l.find('/')+1:].strip())
                else:
                    curname = l[1:].strip()
                    self.voices.append(self.default_voice)
                continue

            curtext += l + '\n'

    def get_sections(self):
        return self.sections.keys()

    def get_section(self, name):
        return self.sections[name]

    def speechify(self, which, quality):

        name = list(self.sections.keys())[which]
        text = self.sections[name]
        voice = self.voices[which]

        suffix = dt.now().strftime("%Y-%m-%d-%H-%M-%S")
        engine = OpenaiTTS()

        engine.speechify(text, f"outputs/{name}-{suffix}.mp3", voice, quality)
