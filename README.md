# Text2Speech using OpenAI

This is a very simple sample program demonstrating how to feed text files to OpenAI's
Text-to-Speech API and save the outputs as MP3 files.

The concept is pretty simple:

* You prepare a text file (`script.txt`) that has the text you want synthesized.
* The text file is broken up into sections.  Each section starts with a line of the format `# Name / Voice'.
  * The name is whatever you want to call the section
  * The voice is one of the following:  `alloy`, `echo`, `fable`, `onyx`, `nova`, or `shimmer`. There are samples of the voices on OpenAI's web site.
* When you run the app, it will either generate a single section or all of them, based upon how you respond to a prompt
* The output is placed in the outputs directory as an MP3 file with the name a combination of the name of the section and a time stamp.

There's a sample script.txt provided in the repository to run with.

To run the application, you'll need an OpenAI API Key and to have set the environment variable OPENAI_API_KEY to its value (`sk-...`)

## Notes

The OpenAI TTS interface is very primative, and there's no way to insert explicit instructions
into the text to inflect the generated voice.  The best I've found is the careful use of
punctuation, spacing, and blank lines can get it to better speak your text.
