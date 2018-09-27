import csv
from sklearn import linear_model
import pandas as pd
from sklearn.feature_selection import RFE



import numpy as np




reg = linear_model.LinearRegression()
## mudar a tabela base
dados = pd.read_csv("tabelaTuplas.csv")

## concateno as colunas em um novo dataframe
dadosX = pd.concat([dados["temperature"], dados["solo"],dados["Precipitation"], dados["age"]], axis=1)

#print(dadosX)
dadosY = dados["production"]

clf = linear_model.Lasso(alpha=0.1)
clf.fit(dadosX, dadosY)
print(clf.coef_)
print(clf.intercept_)
## ja sei como selecionar minha features
rfe = RFE(estimator=clf, n_features_to_select=1, step=1)
rfe.fit(dadosX, dadosY)
print("imporntancia das features " + str(rfe.ranking_))

#reg.fit(dadosX, dadosY)
#print(clf.feature_importances_ )






def escreverSubmissao(classificador):
    print("iniciar predicao")
    dadosValidar = pd.read_csv("tabelaTuplasValidar.csv")
    dadosVal = pd.concat([dadosValidar["temperature"], dadosValidar["solo"],dadosValidar["age"],dadosValidar["Precipitation"]],axis=1)

    predicao = classificador.predict(dadosVal)

    arrayId = dadosValidar["Id"]

    datasetResultado = pd.DataFrame({"Id": arrayId})

    datasetResultado["production"] = predicao
    print(datasetResultado)
    datasetResultado.to_csv("submission.csv")

#escreverSubmissao(clf)