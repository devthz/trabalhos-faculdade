#IMPORTAÇÃO DAS BIBLIOTECAS
import pandas as pd
#from google.colab import drive, files
from pandas_profiling import ProfileReport

#IMPORTANDO O ARQUIVO "STORES.csv"
#drive.mount('/content/drive')
df = pd.read_csv('/content/drive/MyDrive/stores.csv')

#RENOMEANDO TODAS AS COLUNAS DO ARQUIVO
dfRename = df.rename(columns={'Store_ID' : 'ID Loja', 'Store_Area':'Tamanho Loja', 'Items_Available' : 'Produtos Disponiveis', 'Daily_Customer_Count' :'Visitantes', 'Store_Sales' : 'Vendas'})
dfRename

#FAZENDO A MEDIA, VALOR MINIMO, VALOR MAXIMO E DESVIO PADRÃO DE COLUNAS ESPECIFICAS (PRODUTOS DISPONIVEIS, VISITANTES, VENDAS)

pd = dfRename ['Produtos Disponiveis']
vis = dfRename ['Visitantes']
vd = dfRename ['Vendas']

pdMedia = pd.mean()
pdMax = pd.max()
pdMin = pd.min()
pdDes = pd.std()

print(f'Produtos Disponiveis: \nValor Mínimo: {pdMin} \nValor Máximo: {pdMax} \nMédia: {pdMedia} \nDesvio padrão: {pdDes}')

visMedia = vis.mean()
visMax = vis.max()
visMin = vis.min()
visDes = vis.std()

print(f'\nVisitantes: \nValor Mínimo: {visMin} \nValor Máximo: {visMax} \nMédia: {visMedia} \nDesvio padrão: {visDes}')

vdMedia = vd.mean()
vdMax = vd.max()
vdMin = vd.min()
vdDes = vd.std()

print(f'\nVendas: \nValor Mínimo (EM US$): {vdMin} \nValor Máximo (EM US$): {vdMax} \nMédia (EM US$): {vdMedia} \nDesvio padrão: {vdDes}')

#MOSTRANDO A TABELA COM O NOME DAS COLUNAS ALTERADA
dfRename