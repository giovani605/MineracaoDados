import csv
from sklearn import linear_model
import pandas as pd
import numpy as np

reg = linear_model.LinearRegression()
## mudar a tabela base
dados = pd.read_csv("tabelaTuplas.csv")

## concateno as colunas em um novo dataframe
dadosX = pd.concat([dados["temperature"] , dados["solo"],dados["age"],dados["Precipitation"]],axis=1)

#print(dadosX)
dadosY = dados["production"]

reg.fit(dadosX, dadosY)
print(reg.coef_)

print("iniciar predicao")
dadosValidar = pd.read_csv("tabelaTuplasValidar.csv")
dadosVal = pd.concat([dadosValidar["temperature"], dadosValidar["solo"],dadosValidar["age"],dadosValidar["Precipitation"]],axis=1)

predicao = reg.predict(dadosVal)

arrayId = dadosValidar["Id"]

datasetResultado = pd.DataFrame({"Id": arrayId})

datasetResultado["production"] = predicao
print(datasetResultado)
datasetResultado.to_csv("submission.csv")
