import pyttsx3   #lib used for text to speech
import PyPDF2    #extract text from pdf

book = open('poem.pdf', 'rb')           #opening pdf

pdfReader = PyPDF2.PdfFileReader(book)  #read file
pages =pdfReader.numPages               #check no. of pages
print("No. Pages in the PDF : ",pages)  #print no. of pages

speck = pyttsx3.init()                  #initialing TTS

speck.setProperty('rate', 125)          #rate of speech | tempo

voices = speck.getProperty('voices')     
speck.setProperty('voice', voices[1].id)  #change voice  
page = pdfReader.getPage(17)              #read text at page no. 18
text =page.extractText()                  #extract text
speck.say(text)                           #speck out the extracted text
speck.runAndWait()                        #run
