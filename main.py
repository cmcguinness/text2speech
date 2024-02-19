"""

# main.py
The "user interface" to the program

## Tasks

* Get the name of the text file holding the script
* Read it in via the Script class
* Present the list of sections
* Ask the user which section to convert to speach (or all of them)
* Trigger the conversion

"""

from script import Script


if __name__ == "__main__":

    # Default to script.txt because that's the same I provide!
    sname = input('Script name [script.txt]: ')
    if sname == '':
        sname = 'script.txt'

    # See script.py for a discussion on the file format
    script = Script(sname)

    print('Which section to covert?')

    sections = script.get_sections()

    for i,n in enumerate(sections):
        print(f'{i+1:2}: {n}')

    which = input('Enter a number or all to process all sections: ')

    quality = input('High/Low TTS quality? [h/L]')

    if which == 'all':
        for i,k in enumerate(sections):
            print(f'Processing section {k}')
            script.speechify(i, quality)
    else:
        script.speechify(int(which)-1, quality)

    print('Finished.')