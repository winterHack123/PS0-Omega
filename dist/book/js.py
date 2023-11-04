import pyttsx3
import PyPDF2
book=open('js.pdf','rb')
pdfReader = PyPDF2.PdfReader(book)
pages=len(pdfReader.pages)
print(pages)
speaker=pyttsx3.init()
page=pdfReader.pages[11]
text=page.extract_text()
speaker.say(text)
speaker.runAndWait()