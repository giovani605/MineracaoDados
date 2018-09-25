import csv
from sklearn import linear_model
import pandas as pd
import numpy as np

reg = linear_model.LinearRegression()
## mudar a tabela base
dados = pd.read_csv("tabelaTuplas.csv")

## concateno as colunas em um novo dataframe
dadosX = pd.concat([dados["temperature"] , dados["solo"]],axis=1)

print(dadosX)
dadosY = dados["production"]

reg.fit(dadosX, dadosY)
print(reg.coef_)