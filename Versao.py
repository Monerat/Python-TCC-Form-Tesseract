import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C:\Program Files\Tesseract-OCR\Tesseract.exe"

print (cv2.__version__)
print(pytesseract.get_tesseract_version())