import pyttsx3
import PyPDF2

#Replace file.pdf' with path to your PDF file (i.e. /Desktop/Contracts/file.pdf)

pdfreader = PyPDF2.PdfReader(open('/Users/mac/Downloads/LouiseIzere_Enrollment_Letter.pdf','rb'))

reader = pyttsx3.init()

for page in range(pdfreader.numPages):   

    text = pdfreader.getPage(page).extractText()

    legible_text = text.strip().replace('\n',' ')

    print(legible_text)

    reader.say(legible_text)

    reader.save_to_file(legible_text,'file.mp3')

    reader.runAndWait()

reader.stop()