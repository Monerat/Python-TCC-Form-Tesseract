from cv2 import blur
from carregarDF import carregarDF
import pandas as pd
import matplotlib.pyplot as plt

pastas = ["TEST1","TEST2","TEST3","TEST4","TEST5","TEST6"]
forms = ["form1","form2","form3","form4","form5","form6","form7","form8","form9","form10"]

#pastas = ["TEST1","TEST2"]
#forms = ["form1","form2"]


BlurKernel, divideScale, threshAny, threshMax, kernelAnchor1, kernelAnchor2, dilate = carregarDF("TEST7/form1","TEST7","form")
trBlurKernel, trDivideScale, trThreshAny, trThreshMax, trKernelAnchor1, trKernelAnchor2, trDilate = carregarDF("TEST7/form1","TEST7","form")

tamTR = 5

for pasta in pastas:
    for formulario in forms:
        parametro = pasta+"/"+formulario
        a,b,c,d,e,f,g = carregarDF(parametro,pasta,formulario)
        BlurKernel = pd.concat([BlurKernel,a], ignore_index=True)
        divideScale = pd.concat([divideScale,b], ignore_index=True)
        threshAny = pd.concat([threshAny,c], ignore_index=True)
        threshMax = pd.concat([threshMax,d], ignore_index=True)  
        kernelAnchor1 = pd.concat([kernelAnchor1,e], ignore_index=True)
        kernelAnchor2 = pd.concat([kernelAnchor2,f], ignore_index=True)
        dilate = pd.concat([dilate,g], ignore_index=True)

BlurKernel.drop([0], axis=0, inplace=True)
BlurKernel.BlurKernelResultado = BlurKernel.BlurKernelResultado.astype(float)
for form in forms:
    temp = BlurKernel
    temp = temp[temp.Formulario == form]
    temp = temp.nlargest(n=tamTR, columns=['BlurKernelResultado'])
    trBlurKernel = pd.concat([trBlurKernel,temp], ignore_index=True)
    
divideScale.drop([0], axis=0, inplace=True)
divideScale.DivideScaleResultado = divideScale.DivideScaleResultado.astype(float)
for form in forms:
    temp = divideScale
    temp = temp[temp.Formulario == form]
    temp = temp.nlargest(n=tamTR, columns=['DivideScaleResultado'])
    trDivideScale = pd.concat([trDivideScale,temp], ignore_index=True)
    
threshAny.drop([0], axis=0, inplace=True)
threshAny.threshAnyResultado = threshAny.threshAnyResultado.astype(float)
for form in forms:
    temp = threshAny
    temp = temp[temp.Formulario == form]
    temp = temp.nlargest(n=tamTR, columns=['threshAnyResultado'])
    trThreshAny = pd.concat([trThreshAny,temp], ignore_index=True)

threshMax.drop([0], axis=0, inplace=True)
threshMax.threshMaxResultado = threshMax.threshMaxResultado.astype(float)
for form in forms:
    temp = threshMax
    temp = temp[temp.Formulario == form]
    temp = temp.nlargest(n=tamTR, columns=['threshMaxResultado'])
    trThreshMax = pd.concat([trThreshMax,temp], ignore_index=True)

kernelAnchor1.drop([0], axis=0, inplace=True)
kernelAnchor1.kernelAnchor1Resultado = kernelAnchor1.kernelAnchor1Resultado.astype(float)
for form in forms:
    temp = kernelAnchor1
    temp = temp[temp.Formulario == form]
    temp = temp.nlargest(n=tamTR, columns=['kernelAnchor1Resultado'])
    trKernelAnchor1 = pd.concat([trKernelAnchor1,temp], ignore_index=True)

kernelAnchor2.drop([0], axis=0, inplace=True)
kernelAnchor2.kernelAnchor2Resultado = kernelAnchor2.kernelAnchor2Resultado.astype(float)
for form in forms:
    temp = kernelAnchor2
    temp = temp[temp.Formulario == form]
    temp = temp.nlargest(n=tamTR, columns=['kernelAnchor2Resultado'])
    trKernelAnchor2 = pd.concat([trKernelAnchor2,temp], ignore_index=True)

dilate.drop([0], axis=0, inplace=True)
dilate.dilateResultado = dilate.dilateResultado.astype(float)
for form in forms:
    temp = dilate
    temp = temp[temp.Formulario == form]
    temp = temp.nlargest(n=tamTR, columns=['dilateResultado'])
    trDilate = pd.concat([trDilate,temp], ignore_index=True)

trBlurKernel.to_excel("Resultados/Testes/Dataframes/Tr-BlurKernel.xlsx")
trDivideScale.to_excel("Resultados/Testes/Dataframes/Tr-divideScale.xlsx")
trThreshAny.to_excel("Resultados/Testes/Dataframes/Tr-threshAny.xlsx")
trThreshMax.to_excel("Resultados/Testes/Dataframes/Tr-threshMax.xlsx")
trKernelAnchor1.to_excel("Resultados/Testes/Dataframes/Tr-kernelAnchor1.xlsx")
trKernelAnchor2.to_excel("Resultados/Testes/Dataframes/Tr-kernelAnchor2.xlsx")
trDilate.to_excel("Resultados/Testes/Dataframes/Tr-dilate.xlsx")
                        
'''
BlurKernel['BlurKernelResultado'] = BlurKernel['BlurKernelResultado'].astype(float).map(lambda n: '{:.2%}'.format(n/100))
BlurKernel['BlurKernelResultado'] = BlurKernel['BlurKernelResultado'].astype(str).map(lambda x: str(x.replace('.',',')))

divideScale.drop([0], axis=0, inplace=True)
divideScale['DivideScaleResultado'] = divideScale['DivideScaleResultado'].astype(float).map(lambda n: '{:.2%}'.format(n/100))

threshAny.drop([0], axis=0, inplace=True)
threshAny['threshAnyResultado'] = threshAny['threshAnyResultado'].astype(float).map(lambda n: '{:.2%}'.format(n/100))

threshMax.drop([0], axis=0, inplace=True)
threshMax['threshMaxResultado'] = threshMax['threshMaxResultado'].astype(float).map(lambda n: '{:.2%}'.format(n/100))

kernelAnchor1.drop([0], axis=0, inplace=True)
kernelAnchor1['kernelAnchor1Resultado'] = kernelAnchor1['kernelAnchor1Resultado'].astype(float).map(lambda n: '{:.2%}'.format(n/100))

kernelAnchor2.drop([0], axis=0, inplace=True)
kernelAnchor2['kernelAnchor2Resultado'] = kernelAnchor2['kernelAnchor2Resultado'].astype(float).map(lambda n: '{:.2%}'.format(n/100))

dilate.drop([0], axis=0, inplace=True)
dilate['dilateResultado'] = dilate['dilateResultado'].astype(float).map(lambda n: '{:.2%}'.format(n/100))



for pasta in pasta:
    for form in forms:
        bkplot = BlurKernel
        bkplot = bkplot[ bkplot.Formulario == form, bkplot.Teste == pasta]
        print(bkplot)
        #plt.hist(bkplot.BlurKernelResultado)
        #plt.show()


BlurKernel.to_excel("Resultados/Testes/Dataframes/BlurKernel.xlsx")
divideScale.to_excel("Resultados/Testes/Dataframes/divideScale.xlsx")
threshAny.to_excel("Resultados/Testes/Dataframes/threshAny.xlsx")
threshMax.to_excel("Resultados/Testes/Dataframes/threshMax.xlsx")
kernelAnchor1.to_excel("Resultados/Testes/Dataframes/kernelAnchor1.xlsx")
kernelAnchor2.to_excel("Resultados/Testes/Dataframes/kernelAnchor2.xlsx")
dilate.to_excel("Resultados/Testes/Dataframes/dilate.xlsx")
'''