import csv
from sklearn import linear_model
import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.model_selection import cross_val_score


import numpy as np
import math
def testeMelhorAlpha(X,Y):

    bestScore = 1;
    bestAlpha = 0;
    alpha = 0.1;
    astep =0.1;
    limite = 10;
    while alpha < limite:
        print("Alpha " + str(alpha))
        clf = linear_model.Lasso(alpha=alpha)

        clf.fit(X, Y)
        print(clf.coef_)
        print(clf.intercept_)
        print("Score")
        print(clf.score(X,Y))
        scores = cross_val_score(
            clf, dadosX, dadosY, scoring='neg_mean_absolute_error', cv=5)
        if((math.fabs(np.mean(scores)) <  bestScore) ):
            bestScore = math.fabs(clf.score(X, Y))
            bestAlpha = alpha
        alpha += astep
    print("Mlehor alpha e score " + str(bestAlpha) + " " + str(bestScore))
    return bestAlpha


reg = linear_model.LinearRegression()
## mudar a tabela base
dados = pd.read_csv("tabelaTuplas.csv")

## concateno as colunas em um novo dataframe
#dadosX = pd.concat([dados["temperature"], dados["solo"],dados["Precipitation"], dados["age"],dados["month"]], axis=1)
dadosX = dados.drop(columns="production")
print(dadosX)
dadosY = dados["production"]
alpha = testeMelhorAlpha(dadosX,dadosY)
#alpha = 0.2
clf = linear_model.Lasso(alpha=alpha)
clf.fit(dadosX, dadosY)
print(clf.coef_)
print(clf.intercept_)
print("Score")
print(clf.score(dadosX,dadosY)) ## quero q este score fique mais eprto de 0
## ja sei como selecionar minha features
rfe = RFE(estimator=clf, n_features_to_select=1, step=1)
rfe.fit(dadosX, dadosY)
print("imporntancia das features " + str(rfe.ranking_))
print("cross validataion")
scores = cross_val_score(
    clf, dadosX, dadosY, scoring='neg_mean_absolute_error',cv=10)
print((scores))
print(np.mean(scores))


#reg.fit(dadosX, dadosY)
#print(clf.feature_importances_ )






def escreverSubmissao(classificador):
    print("iniciar predicao")
    dadosValidar = pd.read_csv("tabelaTuplasValidar.csv")
    dadosVal = pd.concat([dadosValidar["temperature"], dadosValidar["solo"],dadosValidar["Precipitation"],dadosValidar["age"],dadosValidar["month"]],axis=1)

    predicao = classificador.predict(dadosVal)

    arrayId = dadosValidar["Id"]

    datasetResultado = pd.DataFrame({"Id": arrayId})

    datasetResultado["production"] = predicao
    print(datasetResultado)
    datasetResultado.to_csv("submission.csv")

#escreverSubmissao(clf)