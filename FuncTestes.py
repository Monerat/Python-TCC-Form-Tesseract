from unittest import result
from OCRtestes import aplicarOCR
import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
import pathlib


def testePrecisaoAlgoritmo(nomeForm):
    #difinições iniciais das variaveis
    enderecoForm ="Python-TCC-Form-Tesseract/Userforms/Formularios/"+nomeForm+".png"
    enderecoResultado = "Python-TCC-Form-Tesseract/Userforms/Resultados/"+nomeForm+".txt"
    pathlib.Path("Python-TCC-Form-Tesseract/Resultados/Testes/"+nomeForm).mkdir(parents=True, exist_ok=True)
    blurKernel = 7
    divideScale = 255
    threshAny = 0
    threshMax = 255
    kernelAnchor1 = 3
    kernelAnchor2 = 13
    dilateIterations = 2

    mimTaxAcerto = 0

    ordemTest = random.sample(range(7), 7)
    '''
    blurKernel = 0
    divideScale = 1
    threshAny = 2
    threshMax = 3
    kernelAnchor1 = 4
    kernelAnchor2 = 5
    dilateIterations = 6
    '''
    for i in ordemTest:
        match i:
            case 0:
                blurKernelResultados = []
                blurKernelvalor = []
                for i in range(1,151,2):
                    blurKernel = i
                    resultado = aplicarOCR(enderecoForm,blurKernel,divideScale,threshAny,threshMax,kernelAnchor1,kernelAnchor2,dilateIterations,enderecoResultado)
                    blurKernelvalor.append(i)
                    blurKernelResultados.append(resultado)

                daf = pd.DataFrame({'BlurKernel':blurKernelvalor,'Taxa_de_acerto':blurKernelResultados })
                daf = daf[daf.Taxa_de_acerto > mimTaxAcerto]
                max = daf.Taxa_de_acerto.idxmax()
                blurKernel = daf.BlurKernel[max]
                plt.figure(1)
                plt.plot(daf.BlurKernel,daf.Taxa_de_acerto)
                text= "BlurKernel={:d}, Taxa de Acerto={:.2f}".format(daf.BlurKernel[max], daf.Taxa_de_acerto[max])
                plt.annotate(text, xy=(daf.BlurKernel[max], daf.Taxa_de_acerto[max]), xytext=(daf.BlurKernel[max]+4, daf.Taxa_de_acerto[max]+0.05),arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))
                plt.title('Teste do Blur')
                plt.xlabel('BlurKernel')
                plt.ylabel('Taxa de Acerto')
                plt.savefig('Python-TCC-Form-Tesseract/Resultados/Testes/'+nomeForm+'/01_Teste_do_Blur.png')
                plt.close(fig=1)
                
            case 1:
                divideScaleResultados = []
                divideScaleValor = []
                for i in range(0,255,1):
                    divideScale = i
                    resultado = aplicarOCR(enderecoForm,blurKernel,divideScale,threshAny,threshMax,kernelAnchor1,kernelAnchor2,dilateIterations,enderecoResultado)
                    divideScaleResultados.append(resultado)
                    divideScaleValor.append(i)

                daf = pd.DataFrame({'DivideScale':divideScaleValor,'Taxa_de_acerto':divideScaleResultados })
                daf = daf[daf.Taxa_de_acerto > mimTaxAcerto]
                max = daf.Taxa_de_acerto.idxmax()
                divideScale = daf.DivideScale[max]
                plt.figure(2)
                plt.plot(daf.DivideScale,daf.Taxa_de_acerto)
                text= "DivideScale={:d}, Taxa de Acerto={:.2f}".format(daf.DivideScale[max], daf.Taxa_de_acerto[max])
                plt.annotate(text, xy=(daf.DivideScale[max], daf.Taxa_de_acerto[max]), xytext=(daf.DivideScale[max]+4, daf.Taxa_de_acerto[max]+0.05),arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))
                plt.title('Teste do Divide')
                plt.xlabel('DivideScale')
                plt.ylabel('Taxa de Acerto')
                plt.savefig('Python-TCC-Form-Tesseract/Resultados/Testes/'+nomeForm+'/02_Teste_do_Divide.png')
                plt.close(fig=2)
                
            case 2:
                threshAnyResultados = []
                threshAnyValor = []
                for i in range(0,255,1):
                    threshAny = i
                    resultado = aplicarOCR(enderecoForm,blurKernel,divideScale,threshAny,threshMax,kernelAnchor1,kernelAnchor2,dilateIterations,enderecoResultado)
                    threshAnyResultados.append(resultado)
                    threshAnyValor.append(i)

                daf = pd.DataFrame({'ThreshAny':threshAnyValor,'Taxa_de_acerto':threshAnyResultados})
                daf = daf[daf.Taxa_de_acerto > mimTaxAcerto]
                max = daf.Taxa_de_acerto.idxmax()
                threshAny = daf.ThreshAny[max]
                plt.figure(3)
                plt.plot(daf.ThreshAny,daf.Taxa_de_acerto)
                text= "ThreshAny={:d}, Taxa de Acerto={:.2f}".format(daf.ThreshAny[max], daf.Taxa_de_acerto[max])
                plt.annotate(text, xy=(daf.ThreshAny[max], daf.Taxa_de_acerto[max]), xytext=(daf.ThreshAny[max]+4, daf.Taxa_de_acerto[max]+0.05),arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))
                plt.title('Teste do ThreshAny')
                plt.xlabel('ThreshAny')
                plt.ylabel('Taxa de Acerto')
                plt.savefig('Python-TCC-Form-Tesseract/Resultados/Testes/'+nomeForm+'/03_Teste_do_ThreshAny.png')
                plt.close(fig=3)
            
            case 3:
                threshMaxResultados = []
                threshMaxValor = []
                for i in range(0,255,1):
                    threshMax = i
                    resultado = aplicarOCR(enderecoForm,blurKernel,divideScale,threshAny,threshMax,kernelAnchor1,kernelAnchor2,dilateIterations,enderecoResultado)
                    threshMaxResultados.append(resultado)
                    threshMaxValor.append(i)

                daf = pd.DataFrame({'ThreshMax':threshMaxValor,'Taxa_de_acerto':threshMaxResultados})
                daf = daf[daf.Taxa_de_acerto > mimTaxAcerto]
                max = daf.Taxa_de_acerto.idxmax()
                threshMax = daf.ThreshMax[max]
                plt.figure(4)
                plt.plot(daf.ThreshMax,daf.Taxa_de_acerto)
                text= "ThreshMax={:d}, Taxa de Acerto={:.2f}".format(daf.ThreshMax[max], daf.Taxa_de_acerto[max])
                plt.annotate(text, xy=(daf.ThreshMax[max], daf.Taxa_de_acerto[max]), xytext=(daf.ThreshMax[max]+4, daf.Taxa_de_acerto[max]+0.05),arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))
                plt.title('Teste do ThreshMax')
                plt.xlabel('ThreshMax')
                plt.ylabel('Taxa de Acerto')
                plt.savefig('Python-TCC-Form-Tesseract/Resultados/Testes/'+nomeForm+'/04_Teste_do_ThreshMax.png')
                plt.close(fig=4)

            case 4:
                kernelAnchor1Resultados = []
                kernelAnchor1Valor = []
                for i in range(1,50,1): 
                    kernelAnchor1 = i
                    resultado = aplicarOCR(enderecoForm,blurKernel,divideScale,threshAny,threshMax,kernelAnchor1,kernelAnchor2,dilateIterations,enderecoResultado)
                    kernelAnchor1Resultados.append(resultado)
                    kernelAnchor1Valor.append(i)

                daf = pd.DataFrame({'kernel_Anchor_1':kernelAnchor1Valor,'Taxa_de_acerto':kernelAnchor1Resultados})
                daf = daf[daf.Taxa_de_acerto > mimTaxAcerto]
                max = daf.Taxa_de_acerto.idxmax()
                kernelAnchor1 = daf.kernel_Anchor_1[max]
                plt.figure(5)
                plt.plot(daf.kernel_Anchor_1,daf.Taxa_de_acerto)
                text= "kernel_Anchor_1={:d}, Taxa de Acerto={:.2f}".format(daf.kernel_Anchor_1[max], daf.Taxa_de_acerto[max])
                plt.annotate(text, xy=(daf.kernel_Anchor_1[max], daf.Taxa_de_acerto[max]), xytext=(daf.kernel_Anchor_1[max]+4, daf.Taxa_de_acerto[max]+0.05),arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))
                plt.title('Teste do kernel_Anchor_1')
                plt.xlabel('kernel_Anchor_1')
                plt.ylabel('Taxa de Acerto')
                plt.savefig('Python-TCC-Form-Tesseract/Resultados/Testes/'+nomeForm+'/05_Teste_do_kernel_Anchor_1.png')
                plt.close(fig=5)

            case 5:
                kernelAnchor2Resultados = []
                kernelAnchor2Valor = []
                for i in range(1,50,1):
                    kernelAnchor2 = i
                    resultado = aplicarOCR(enderecoForm,blurKernel,divideScale,threshAny,threshMax,kernelAnchor1,kernelAnchor2,dilateIterations,enderecoResultado)
                    kernelAnchor2Resultados.append(resultado)
                    kernelAnchor2Valor.append(i)

                daf = pd.DataFrame({'kernel_Anchor_2':kernelAnchor2Valor,'Taxa_de_acerto':kernelAnchor2Resultados})
                daf = daf[daf.Taxa_de_acerto > mimTaxAcerto]
                max = daf.Taxa_de_acerto.idxmax()
                kernelAnchor2 = daf.kernel_Anchor_2[max]
                plt.figure(6)
                plt.plot(daf.kernel_Anchor_2,daf.Taxa_de_acerto)
                text= "kernel_Anchor_2={:d}, Taxa de Acerto={:.2f}".format(daf.kernel_Anchor_2[max], daf.Taxa_de_acerto[max])
                plt.annotate(text, xy=(daf.kernel_Anchor_2[max], daf.Taxa_de_acerto[max]), xytext=(daf.kernel_Anchor_2[max]+4, daf.Taxa_de_acerto[max]+0.05),arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))
                plt.title('Teste do kernel_Anchor_2')
                plt.xlabel('kernel_Anchor_2')
                plt.ylabel('Taxa de Acerto')
                plt.savefig('Python-TCC-Form-Tesseract/Resultados/Testes/'+nomeForm+'/06_Teste_do_kernel_Anchor_2.png')
                plt.close(fig=6)

            case 6:
                dilateResultados = []
                dilateValor = []
                for i in range(0,50,1):
                    dilateIterations = i
                    resultado = aplicarOCR(enderecoForm,blurKernel,divideScale,threshAny,threshMax,kernelAnchor1,kernelAnchor2,dilateIterations,enderecoResultado)
                    dilateResultados.append(resultado)
                    dilateValor.append(i)

                daf = pd.DataFrame({'Dilate_Iterations':dilateValor,'Taxa_de_acerto':dilateResultados})
                daf = daf[daf.Taxa_de_acerto > mimTaxAcerto]
                max = daf.Taxa_de_acerto.idxmax()
                dilateIterations = daf.Dilate_Iterations[max]
                plt.figure(7)
                plt.plot(daf.Dilate_Iterations,daf.Taxa_de_acerto)
                text= "Dilate_Iterations={:d}, Taxa de Acerto={:.2f}".format(daf.Dilate_Iterations[max], daf.Taxa_de_acerto[max])
                plt.annotate(text, xy=(daf.Dilate_Iterations[max], daf.Taxa_de_acerto[max]), xytext=(daf.Dilate_Iterations[max]+4, daf.Taxa_de_acerto[max]+0.05),arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60"))
                plt.title('Teste do Dilate_Iterations')
                plt.xlabel('Dilate_Iterations')
                plt.ylabel('Taxa de Acerto')
                plt.savefig('Python-TCC-Form-Tesseract/Resultados/Testes/'+nomeForm+'/07_Teste_do_Dilate_Iterations.png')
                plt.close(fig=7)

            case _:
                print("valor ainda nao implementado")

    with open("Python-TCC-Form-Tesseract/Resultados/Testes/"+nomeForm+"/Testes.csv", 'w',encoding='utf-8', newline='') as csvfile:
        wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        w = csv.writer(csvfile)
        
        w.writerow(["OrdemTestes"])
        wr.writerow(ordemTest)

        w.writerow(["blurKernel",blurKernel])
        w.writerow(["divideScale",divideScale])
        w.writerow(["threshAny",threshAny])
        w.writerow(["threshMax",threshMax])
        w.writerow(["kernelAnchor1",kernelAnchor1])
        w.writerow(["kernelAnchor2",kernelAnchor2])
        w.writerow(["dilateIterations",dilateIterations])

        w.writerow(["blurKernelValor"])
        wr.writerow(blurKernelvalor)
        w.writerow(["blurKernelResultados"])
        wr.writerow(blurKernelResultados)
        
        w.writerow(["divideScaleValor"])
        wr.writerow(divideScaleValor)
        w.writerow(["divideScaleResultados"])
        wr.writerow(divideScaleResultados)
        
        w.writerow(["threshAnyValor"])
        wr.writerow(threshAnyValor)
        w.writerow(["threshAnyResultados"])
        wr.writerow(threshAnyResultados)
        
        w.writerow(["threshMaxValor"])
        wr.writerow(threshMaxValor)
        w.writerow(["threshMaxResultados"])
        wr.writerow(threshMaxResultados)
        
        w.writerow(["kernelAnchor1Valor"])
        wr.writerow(kernelAnchor1Valor)
        w.writerow(["kernelAnchor1Resultados"])
        wr.writerow(kernelAnchor1Resultados)

        w.writerow(["kernelAnchor2Valor"])
        wr.writerow(kernelAnchor2Valor)
        w.writerow(["kernelAnchor2Resultados"])
        wr.writerow(kernelAnchor2Resultados)

        w.writerow(["dilateValor"])
        wr.writerow(dilateValor)
        w.writerow(["dilateResultados"])
        wr.writerow(dilateResultados)