# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""""
*****************************************
Program Name: AudioBook
Presented By: 1DS19EC414 & 1DS19EC408
# used variables in this program
pdfReader   - read pdf file
speak       - speak what is readen
readPage    - read page number
pageNumber - get page number from start to end
readSpeed   - set speed rate
voices      - change voices
*****************************************
"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
"""
****************************************************************************


# used variables in this program
pdfFile     - open file in read & binary mode
pdfReader   - read pdf file
speak       - speak what is readen
readPage    - read page number
pageNumber  - get page number from start to end
readSpeed   - set speed rate
voices      - change voices
*****************************************************************************
"""

#   importing pyttsx3 for speak sentances from pdf
import pyttsx3

#   importing PyPDF2 for handling pdf file
import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename


#   opening pdf file in read mode and binary mode
pdfFile = open('What is InfyTQ.pdf', 'rb')

#   reading pdf file
pdfReader = PyPDF2.PdfFileReader(pdfFile)

#   initializing pyttsx3 for make it ready to speak
speak = pyttsx3.init()

#   change voice
voices = speak.getProperty('voices')

# changing index, changes voices. o for male
# speak.setProperty('voice', voices[0].id)

# changing index, changes voices. 1 for female
speak.setProperty('voice', voices[1].id)

#   set speak speed
rate = speak.getProperty('rate')
speak.setProperty('rate', rate - 1)

"""
#   speak what is inside say function
speak.say('speak now')

#   showing number of ages in a pdf file
print(pdfReader.numPages)
"""

#   getting page number from start to end
for pageNumber in range(0, pdfReader.numPages):
    #   read from a specific page
    readPage = pdfReader.getPage(pageNumber)

    #   read page and extract text into a variable
    readText = readPage.extractText()

    #   speak what is in the pdf file
    speak.say(readText)

    #   save text as mp3 file
    speak.save_to_file(readText, 'mypdf.mp3')

    #   make speak function work
    speak.runAndWait()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
