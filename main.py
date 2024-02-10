from datetime import datetime as dt
from collections import OrderedDict
from TTS import TTS
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

    def speechify(self, engine:TTS, which):

        name = list(self.sections.keys())[which]
        text = self.sections[name]
        voice = self.voices[which]

        suffix = dt.now().strftime("%Y-%m-%d-%H-%M-%S")

        engine.speechify(text, f"outputs/{name}-{suffix}.mp3", voice)





if __name__ == "__main__":

    engine = OpenaiTTS()

    script = Script("script.txt")

    print('Which section to covert?')

    sections = script.get_sections()

    for i,n in enumerate(sections):
        print(f'{i+1:2}: {n}')

    which = input('Enter a number or all to process all sections: ')

    if which == 'all':
        for i,k in enumerate(sections):
            print(f'Processing section {k}')
            script.speechify(engine, i)
    else:
        script.speechify(engine, int(which)-1)

    print('Finished.')