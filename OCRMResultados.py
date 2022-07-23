import cv2
import pytesseract
import numpy as np
import difflib as dl
from matplotlib import pyplot as plt
from transform import cropTransformIMG
import pathlib
import pandas as pd

pytesseract.pytesseract.tesseract_cmd="C:\Program Files\Tesseract-OCR\Tesseract.exe"

def aplicarOCRcomIMG(enderecoForm,blurKernel,divideScale,threshAny,threshMax,kernelAnchor1,kernelAnchor2,dilateIterations,enderecoResultado):
    folder = "Resultados/Testes/ResultadoFinal/MelhorVar/"+enderecoForm+"/"
    pathlib.Path(folder).mkdir(parents=True, exist_ok=True)

    #Carrega a img em memoria
    img = cv2.imread(enderecoForm)
    original = img.copy()
    cv2.imwrite(folder+"01_Original.png",original)

    #Recorta a imagem
    img = cropTransformIMG(img)
    cv2.imwrite(folder+"02_Imagem_Depois_Crop.png",img)

    #transforma em escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(folder+"03_Imagem_escala_Cinza.png",gray)

    #faz uma copia da da img em preto e branco para a mascara
    mask = np.ones(gray.shape, dtype=np.uint8) * 255

    #aplicando um blur
    blur = cv2.GaussianBlur(gray,(blurKernel,blurKernel),0)
    cv2.imwrite(folder+"04_Imagem_blur.png",blur)

    #divide(Aplica uma divisão para refinar o blur gaussiano) 
    divide = cv2.divide(gray, blur, scale=divideScale)
    cv2.imwrite(folder+"11_Imagem_divide.png",divide)

    #aplicando um threshold 
    thresh = cv2.threshold(divide, threshAny, threshMax,cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)[1]
    cv2.imwrite(folder+"05_Imagem_thresh.png",thresh)

    #operação morphologica
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernelAnchor1,kernelAnchor2))
    cv2.imwrite(folder+"06_Imagem_kernel.png",kernel)

    #expessar a linha
    dilate = cv2.dilate(thresh,kernel, iterations=dilateIterations)
    cv2.imwrite(folder+"07_Imagem_dilate.png",dilate)

    #afinar a linha
    erode = cv2.erode(dilate, kernel, cv2.BORDER_REFLECT)
    cv2.imwrite(folder+"08_Imagem_Erode.png",erode) 

    #encontrar os contornos
    cnts = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        mask[y:y+h, x:x+w] = gray[y:y+h, x:x+w]

    cv2.imwrite(folder+"09_BB.png",img)
    cv2.imwrite(folder+"10_Somente_Img_BB.png",mask)
    TextOCR = pytesseract.image_to_string(mask, lang="por")
    TextOCR.strip()
    OriginTextOCR = pytesseract.image_to_string(original, lang="por")
    TextOCR.strip()
    GrayTextOCR = pytesseract.image_to_string(gray, lang="por")
    TextOCR.strip()

    with open(enderecoResultado, "r",encoding='utf-8') as leitor:
        TextReferencia = leitor.read()

    test = dl.SequenceMatcher(None,TextReferencia, TextOCR)
    testSemTratamento = dl.SequenceMatcher(None,TextReferencia, OriginTextOCR)
    testGray = dl.SequenceMatcher(None,TextReferencia, GrayTextOCR)

    return test.ratio()*100,testSemTratamento.ratio()*100,testGray.ratio()*100

formulariosParaTestes = ["form1","form2","form3","form4","form5","form6","form7","form8","form9","form10"]
pathlib.Path("Resultados/Testes/ResultadoFinal/MelhorVar").mkdir(parents=True, exist_ok=True)
enderecoForm=[]
enderecoResultado=[]
for form in formulariosParaTestes:
    enderecoForm.append("Userforms/Formularios/"+form+".png")
    enderecoResultado.append("Userforms/Resultados/"+form+".txt")

resultadoProcessamento=[]
resultadoIMGOriginal=[]
resultadoIMGGray=[]
for i in range(len(enderecoForm)):
    resultados = aplicarOCRcomIMG(enderecoForm[i],9,3,0,1,3,9,2,enderecoResultado[i])
    resultadoProcessamento.append(resultados[0])
    resultadoIMGOriginal.append(resultados[1])
    resultadoIMGGray.append(resultados[2])

juncaoListas = {'Imagem Original':resultadoIMGOriginal,'Só filtro de Cinza':resultadoIMGGray,'Aplicados os filtros':resultadoProcessamento}
df = pd.DataFrame(juncaoListas)
df['Imagem Original'] = df['Imagem Original'].astype(float).map(lambda n: '{:.2%}'.format(n/100))
df['Imagem Original'] = df['Imagem Original'].astype(str).map(lambda x: str(x.replace('.',',')))
df['Só filtro de Cinza'] = df['Só filtro de Cinza'].astype(float).map(lambda n: '{:.2%}'.format(n/100))
df['Só filtro de Cinza'] = df['Só filtro de Cinza'].astype(str).map(lambda x: str(x.replace('.',',')))
df['Aplicados os filtros'] = df['Aplicados os filtros'].astype(float).map(lambda n: '{:.2%}'.format(n/100))
df['Aplicados os filtros'] = df['Aplicados os filtros'].astype(str).map(lambda x: str(x.replace('.',',')))
#BlurKernel['BlurKernelResultado'] = BlurKernel['BlurKernelResultado'].astype(str).map(lambda x: str(x.replace('.',',')))
df.to_excel("Resultados/Testes/ResultadoFinal/MelhorVar/Resultadosfinais.xlsx")