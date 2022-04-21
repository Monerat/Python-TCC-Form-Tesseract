import cv2
import pytesseract
import numpy as np
import difflib as dl
from matplotlib import pyplot as plt
from transform import cropTransformIMG

pytesseract.pytesseract.tesseract_cmd="C:\Program Files\Tesseract-OCR\Tesseract.exe"

def aplicarOCR(enderecoForm,blurKernel,divideScale,threshAny,threshMax,kernelAnchor1,kernelAnchor2,dilateIterations,enderecoResultado):

    #Carrega a img em memoria
    img = cv2.imread(enderecoForm)
    original = img.copy()

    #Recorta a imagem
    img = cropTransformIMG(img)

    #transforma em escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #faz uma copia da da img em preto e branco para a mascara
    mask = np.ones(gray.shape, dtype=np.uint8) * 255

    #aplicando um blur
    blur = cv2.GaussianBlur(gray,(blurKernel,blurKernel),0)

    #divide 
    divide = cv2.divide(gray, blur, scale=divideScale)

    #aplicando um threshold 
    thresh = cv2.threshold(divide, threshAny, threshMax,cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)[1]

    #operação morphologica
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernelAnchor1,kernelAnchor2))

    #expessar a linha
    dilate = cv2.dilate(thresh,kernel, iterations=dilateIterations)

    #afinar a linha
    erode = cv2.erode(dilate, kernel, cv2.BORDER_REFLECT) 

    #encontrar os contornos
    cnts = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        mask[y:y+h, x:x+w] = gray[y:y+h, x:x+w]

    TextOCR = pytesseract.image_to_string(mask, lang="por")
    TextOCR.strip()
    with open("Python-TCC-Form-Tesseract/Resultados/Output.txt", "w",encoding='utf-8') as txt_file:
        txt_file.write(TextOCR)
    with open(enderecoResultado, "r",encoding='utf-8') as leitor:
        TextReferencia = leitor.read()

    test = dl.SequenceMatcher(None,TextReferencia, TextOCR)

    return test.ratio()*100