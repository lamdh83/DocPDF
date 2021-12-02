#pyttsx3==2.71
import pyttsx3
import PyPDF2

robot_mouth = pyttsx3.init()
voices = robot_mouth.getProperty("voices")
robot_mouth.setProperty("voice", voices[1].id)

def noi(s='A Bi xin chào cả nhà'):
    robot_mouth.say(s)
    robot_mouth.runAndWait()

sach = open("sach4.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(sach)
pages = pdfReader.numPages
# print(pages)
# noi("xin chào các bạn")
page = pdfReader.getPage(16)
text = page.extractText()
print(text)
noi(text)
