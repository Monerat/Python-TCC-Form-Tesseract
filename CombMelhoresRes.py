import cv2
import pytesseract
import numpy as np
import difflib as dl
from matplotlib import pyplot as plt
from OCRtestes import aplicarOCR
from transform import cropTransformIMG
import pathlib
import itertools
import pandas as pd
import csv

formulariosParaTestes = ["form1","form2","form3","form4","form5","form6","form7","form8","form9","form10"]
pathlib.Path("Resultados/Testes/ResultadoFinal/").mkdir(parents=True, exist_ok=True)
enderecoForm=[]
enderecoResultado=[]
for form in formulariosParaTestes:
    enderecoForm.append("Userforms/Formularios/"+form+".png")
    enderecoResultado.append("Userforms/Resultados/"+form+".txt")
    

blurKernel = [7,9,3,11,5]
divideScale = [5,6,7,3,0]
threshAny = [0,1,2,3,4]  #threshMax = [1,2,3,4,5]
kernelAnchor1 = [3,2,4,1,5]
kernelAnchor2 = [13,15,9,11,17]
dilateIteration = [2,1,3,4,5]
listaMelhoresResults=[]
resultadoOCR=[]
variaveisUsadas=[]
formularioAplicado=[]
listaMelhoresResults.append(blurKernel)
listaMelhoresResults.append(divideScale)
listaMelhoresResults.append(threshAny)
listaMelhoresResults.append(kernelAnchor1)
listaMelhoresResults.append(kernelAnchor2)
listaMelhoresResults.append(dilateIteration)
combinacosPossiveis = list(itertools.product(*listaMelhoresResults))

#test = [(1,2,3,4,5,6),(7,8,9,10,11,12)]
for i in range(len(enderecoForm)):
    for listaResultado in combinacosPossiveis:
        resultado = aplicarOCR(enderecoForm[i],listaResultado[0],listaResultado[1],listaResultado[2],listaResultado[2]+1,listaResultado[3],listaResultado[4],listaResultado[5],enderecoResultado[i])
        resultadoOCR.append(resultado)
        variaveisUsadas.append(listaResultado)
        formularioAplicado.append(formulariosParaTestes[i])
        print(listaResultado)

juncaoListas = {'variaveis usadas':variaveisUsadas,'Formulario':formularioAplicado,'Resultado':resultadoOCR}
df = pd.DataFrame(juncaoListas)
df.to_excel("Resultados/Testes/ResultadoFinal/Valores.xlsx")  
