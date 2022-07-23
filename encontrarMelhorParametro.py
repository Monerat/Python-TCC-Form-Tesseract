import pandas as pd

df = pd.read_excel('Resultados\Testes\ResultadoFinal\ValoresVariaveisDiv.xlsx', index_col=0)

df2 = df.loc[df.groupby('Formulario')['Resultado'].nlargest(5).reset_index(0).index]

df2.to_excel("Resultados/Testes/ResultadoFinal/50topValoresPorFormPorVar.xlsx")