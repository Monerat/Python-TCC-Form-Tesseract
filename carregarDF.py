import pandas as pd

def carregarDF(pathForm,pasta,formulario):

    df = pd.read_csv("Resultados/Testes/"+pathForm+"/Testes.csv",sep=";",decimal=',')

    ordemTeste = df.iloc[0]['OrdemTestes']

    melhorResultado = df.iloc[1:8]
    melhorResultado = melhorResultado['OrdemTestes'].str.split(',', expand=True)
    melhorResultado.columns = ['Parametro', 'Valor']

    blurKernel = df.iloc[[9,11]]
    blurKernel = blurKernel['OrdemTestes'].str.split(',', expand=True)
    blurKernel = blurKernel.T
    blurKernel.columns = ['BlurKernelValor','BlurKernelResultado']
    blurKernel["Teste"] = pasta
    blurKernel["Formulario"] = formulario
    blurKernel["OrdemTeste"] = ordemTeste
    blurKernel = blurKernel.replace('"', '', regex=True)

    divideScale = df.iloc[[13,15]]
    divideScale = divideScale['OrdemTestes'].str.split(',', expand=True)
    divideScale = divideScale.T
    divideScale.columns = ['DivideScaleValor','DivideScaleResultado']
    divideScale["Teste"] = pasta
    divideScale["Formulario"] = formulario
    divideScale["OrdemTeste"] = ordemTeste
    divideScale = divideScale.replace('"', '', regex=True)

    threshAny = df.iloc[[17,19]]
    threshAny = threshAny['OrdemTestes'].str.split(',', expand=True)
    threshAny = threshAny.T
    threshAny.columns = ['threshAnyValor','threshAnyResultado']
    threshAny["Teste"] = pasta
    threshAny["Formulario"] = formulario
    threshAny["OrdemTeste"] = ordemTeste
    threshAny = threshAny.replace('"', '', regex=True)

    threshMax = df.iloc[[21,23]]
    threshMax = threshMax['OrdemTestes'].str.split(',', expand=True)
    threshMax = threshMax.T
    threshMax.columns = ['threshMaxValor','threshMaxResultado']
    threshMax["Teste"] = pasta
    threshMax["Formulario"] = formulario
    threshMax["OrdemTeste"] = ordemTeste
    threshMax = threshMax.replace('"', '', regex=True)

    kernelAnchor1 = df.iloc[[25,27]]
    kernelAnchor1 = kernelAnchor1['OrdemTestes'].str.split(',', expand=True)
    kernelAnchor1 = kernelAnchor1.T
    kernelAnchor1.columns = ['kernelAnchor1Valor','kernelAnchor1Resultado']
    kernelAnchor1["Teste"] = pasta
    kernelAnchor1["Formulario"] = formulario
    kernelAnchor1["OrdemTeste"] = ordemTeste
    kernelAnchor1 = kernelAnchor1.replace('"', '', regex=True)

    kernelAnchor2 = df.iloc[[29,31]]
    kernelAnchor2 = kernelAnchor2['OrdemTestes'].str.split(',', expand=True)
    kernelAnchor2 = kernelAnchor2.T
    kernelAnchor2.columns = ['kernelAnchor2Valor','kernelAnchor2Resultado']
    kernelAnchor2["Teste"] = pasta
    kernelAnchor2["Formulario"] = formulario
    kernelAnchor2["OrdemTeste"] = ordemTeste
    kernelAnchor2 = kernelAnchor2.replace('"', '', regex=True)

    dilate = df.iloc[[33,35]]
    dilate = dilate['OrdemTestes'].str.split(',', expand=True)
    dilate = dilate.T
    dilate.columns = ['dilateValor','dilateResultado']
    dilate["Teste"] = pasta
    dilate["Formulario"] = formulario
    dilate["OrdemTeste"] = ordemTeste
    dilate = dilate.replace('"', '', regex=True)
    
    return blurKernel, divideScale, threshAny, threshMax, kernelAnchor1, kernelAnchor2, dilate

