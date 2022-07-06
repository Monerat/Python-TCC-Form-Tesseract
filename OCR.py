import cv2
import pytesseract
import numpy as np
import difflib as dl
from matplotlib import pyplot as plt
from transform import cropTransformIMG

pytesseract.pytesseract.tesseract_cmd="C:\Program Files\Tesseract-OCR\Tesseract.exe"

folder = r"C:\Users\gmone\Desktop\IdentificacaoCode\Python-TCC-Form-Tesseract\Resultados\logo"

#Carrega a img em memoria
#img = cv2.imread(r"C:\Users\gmone\Desktop\IdentificacaoCode\Python-TCC-Form-Tesseract\Resultados\fotos para o word\UERJ-LOGO-400.png")
img = cv2.imread(r"C:\Users\gmone\Desktop\IdentificacaoCode\Python-TCC-Form-Tesseract\Resultados\fotos para o word\UERJ-LOGO-400.png")
original = img.copy()

#Recorta a imagem
cv2.imwrite(folder+"01_Original.png",original)
img = cropTransformIMG(img)

cv2.imwrite(folder+"02_Imagem_Depois_Crop.png",img)

#transforma em escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(folder+"03_Imagem_escala_Cinza.png",gray)
mask = np.ones(gray.shape, dtype=np.uint8) * 255
plt.hist(gray.ravel(),256,[0,256])
plt.title('Histograma de uma imagem em tons de cinza')
plt.xlabel('Valor do Cinza')
plt.ylabel('Contagem de pixels')
plt.savefig(folder+"12_histogram_blur.png")
#aplicando um blur
blur = cv2.GaussianBlur(gray,(7,7),0)
cv2.imwrite(folder+"04_Imagem_blur.png",blur)

#divide
divide = cv2.divide(gray, blur, scale=255)
cv2.imwrite(folder+"11_Imagem_divide.png",divide)

#aplicando um threshold
thresh = cv2.threshold(divide, 0, 255,cv2.THRESH_BINARY_INV +cv2.THRESH_OTSU)[1]
cv2.imwrite(folder+"05_Imagem_thresh.png",thresh)

#operação morfologica
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,13))
cv2.imwrite(folder+"06_Imagem_kernel.png",kernel)
kernel2 = np.ones((3,3), np.uint8)

dilate = cv2.dilate(thresh,kernel, iterations=2)
cv2.imwrite(folder+"07_Imagem_dilate.png",dilate)

erode = cv2.erode(dilate, kernel, cv2.BORDER_REFLECT) 
cv2.imwrite(folder+"10_Imagem_Erode.png",erode)

cnts = cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    mask[y:y+h, x:x+w] = gray[y:y+h, x:x+w]
    cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)

cv2.imwrite(folder+"08_BB.png",img)
cv2.imwrite(folder+"09_Somente_Img_BB.png",mask)
TextOCR = pytesseract.image_to_string(mask, lang="por")
TextOCR.strip()
cv2

with open(folder+"Output.txt", "w",encoding='utf-8') as txt_file:
    txt_file.write(TextOCR)
with open(r"C:\Users\gmone\Desktop\IdentificacaoCode\Python-TCC-Form-Tesseract\Resultados\alo\resultado.txt", "r",encoding='utf-8') as leitor:
    TextReferencia = leitor.read()

test = dl.SequenceMatcher(None,TextReferencia, TextOCR)
print(test.ratio()*100)