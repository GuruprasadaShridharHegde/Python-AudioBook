""""
*****************************************
Program Name : AudioBook
Presented By : 1DS19EC414 & 1DS19EC408
# used variables in this program
pdfReader   - read pdf file
speak       - speak what is readen
readPage    - read page number
pageNumber  - get page number from start to end
readSpeed   - set speed rate
voices      - change voices
*****************************************
"""
import pyttsx3  # pip install pyttsx3
import PyPDF2  # pip install pypdf2


def audio_book(book_name, start_page="1", gender="female"):
    book = open(book_name, 'rb')  # getting file name & opening pdf file in read mode and binary mode
    pdfReader = PyPDF2.PdfFileReader(book)  # reading pdf file
    pages = pdfReader.numPages  # counting number of pages

    engine = pyttsx3.init()  # starting engine

    for num in range(start_page, pages):  # loop through start_page to the end of the book
        page = pdfReader.getPage(num)  # Get single page according to the loop
        text = page.extractText()  # Extracting text from each page
        rate = engine.getProperty('rate')  # Getting text_speech rate property
        engine.setProperty('rate', rate - 1)  # Decreasing text_rate/min bcz it was too fast

        # Getting is gender male or not and setting the voice according to it
        if gender == "male" or gender[0] == "m":

            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)  # voice[0] means "male"
            engine.save_to_file(text, 'Page_no_' + str(num) + '.mp3')  # Saving that file in mp3 format
            engine.say(text)
            engine.runAndWait()
        else:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)  # voice[1] means "female"
            engine.save_to_file(text, 'Page_no_' + str(num) + '.mp3')  # Saving that file in mp3 format
            engine.say(text)
            engine.runAndWait()


if __name__ == "__main__":
    print("Welcome to the Python Audio Book !")
    try:
        book_name = input(
            "\nEnter the Location of the Book...\nAs Shown e.g\t (C:\\Book\\example.pdf)\n\nSo Enter the Address of the Pdf : ")
        start_page = int(input("Enter the Page Number to Start From : "))
        gender = input("Enter the Voice type (male/female) : ").lower()

        if start_page >= 1:
            audio_book(book_name, start_page, gender)
        else:
            print("Enter Valid Page Number Please.")

    except(IndexError):
        print("Please, Enter the Voice type want.\n ")
    except(ValueError):
        print("Please, Enter the Page Number to Start From.\n ")
    except(FileNotFoundError):
        print("Please, Enter the Valid Path for the File.\n")

