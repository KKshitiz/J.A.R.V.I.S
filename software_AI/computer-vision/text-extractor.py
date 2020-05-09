import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd='‪C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img=cv2.imread('C:\\Users\\skili\\Documents\\GitHub\\J.A.R.V.I.S\\software_AI\\computer-vision\\news.png')
text=pytesseract.image_to_string(img)
print(text)