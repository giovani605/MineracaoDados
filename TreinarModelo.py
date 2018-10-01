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
    astep =0.01;
    limite = 3;
    while alpha < limite:
        #print("Alpha " + str(alpha))
        clf = linear_model.Lasso(alpha=alpha)

        clf.fit(X, Y)
        #print(clf.coef_)
        #print(clf.intercept_)
        #print("Score")
       # print(clf.score(X,Y))
        scores = cross_val_score(
            clf, dadosX, dadosY, scoring='neg_mean_absolute_error', cv=5)
        if((math.fabs(np.mean(scores)) <  bestScore) ):
            bestScore = math.fabs(clf.score(X, Y))
            bestAlpha = alpha
        alpha += astep
    print("Mlehor alpha e score " + str(bestAlpha) + " " + str(bestScore))
    return bestAlpha

def selecionarBestFeatures(df, vetorMelhores):
    novoDf = None;
    a = 0;
    while a < vetorMelhores.size:
        if vetorMelhores[a] == 1:
            if novoDf is None:
                novoDf = pd.concat([df.iloc[:,a]], axis=1)
            else:
                novoDf = pd.concat([novoDf,df.iloc[:,a]], axis=1)
          #  print(novoDf)
        a+=1
    return novoDf

#TODO
def testGrid(X,Y):
    bestNFeatures = 1
    bestScore = 1
    vetorMelhores = []
    bestAlpha = 0;

    alpha = 0.0001;
    astep = 0.0001;
    limite = 0.01;
    melhores = {}
    while alpha < limite:
        print("Alpha " + str(alpha))
        clf = linear_model.Lasso(alpha=alpha)
        clf.fit(X,Y)
        scores = selecionarMelhorQtdFeatures(X, Y, clf,alpha)
        print("alpha : " + str(alpha) + " BestScore " + str(bestScore) + " Novo Best  " + str(scores["bestScore"]))
        if scores["bestScore"] < bestScore:
            bestScore = scores["bestScore"]
            melhores = scores
            bestAlpha = alpha

        alpha += astep
    print("Melhor combinacao")
    print(melhores)
    return melhores






def selecionarMelhorQtdFeatures(X,Y,clf,alpha):
    bestNFeatures = 1
    bestScore = 1
    vetorMelhores = {}
    for a in range(1,len(X.columns)):
        rfe = RFE(estimator=clf, n_features_to_select=a, step=1)
        rfe.fit(X, Y)
        selecionados = selecionarBestFeatures(X,rfe.ranking_)
        scores = cross_val_score(
            clf, selecionados, dadosY, scoring='neg_mean_absolute_error', cv=10)

        print(" Teste a = " + str(a) + " bestScore " + str(bestScore) + " Novo score  " + str(math.fabs(np.mean(scores))))
        if ((math.fabs(np.mean(scores)) < bestScore)):
            bestScore = math.fabs(np.mean(scores))
            bestNFeatures = a
            vetorMelhores = rfe.ranking_

    print("melhor n feature  " + str(bestNFeatures) + " score " + str(bestScore) )
    return {"nfeatures" :bestNFeatures,
            "vetorVelhores" : vetorMelhores,
            "bestScore" : bestScore,
            "bestAlpha" : alpha}





reg = linear_model.LinearRegression()
## mudar a tabela base
dados = pd.read_csv("tabelaTuplas.csv")

## concateno as colunas em um novo dataframe
#dadosX = pd.concat([dados["temperature"], dados["solo"],dados["Precipitation"], dados["age"],dados["month"]], axis=1)
dadosX = dados.drop(columns=["production","Id"])
#print(dadosX)
dadosY = dados["production"]
Melhores = testGrid(dadosX,dadosY)


#alpha = testeMelhorAlpha(dadosX,dadosY)
#alpha = 0.2
clf = linear_model.Lasso(alpha=Melhores["bestAlpha"])
clf.fit(dadosX, dadosY)
print(clf.coef_)
print(clf.intercept_)
print("Score")
print(clf.score(dadosX,dadosY)) ## quero q este score fique mais eprto de 0
## ja sei como selecionar minha features
#rfe = RFE(estimator=clf, n_features_to_select=1, step=1)
#rfe.fit(dadosX, dadosY)
#print("imporntancia das features " + str(rfe.ranking_))
#print("cross validataion")
#scores = cross_val_score(
#    clf, dadosX, dadosY, scoring='neg_mean_absolute_error',cv=10)
#print((scores))
#print(np.mean(scores))

#Melhores = selecionarMelhorQtdFeatures(dadosX,dadosY,clf)
#print(Melhores)
#selecionarBestFeatures(dadosX,rfe.ranking_)
#reg.fit(dadosX, dadosY)
#print(clf.feature_importances_ )






def escreverSubmissao(classificador):
    print("iniciar predicao")
    dadosValidar = pd.read_csv("tabelaTuplasValidar.csv")
    dades = selecionarBestFeatures(dadosX, Melhores["vetorVelhores"])
    print("dados Treino")
    print(dades)
    dadosVal = dadosValidar[list(dades.columns.values)]
    print("dados Validar")
    print(dadosVal)
    classificador = linear_model.Lasso(alpha=Melhores["bestAlpha"])
    classificador.fit(dades, dadosY)


    predicao = classificador.predict(dadosVal)

    arrayId = dadosValidar["Id"]

    datasetResultado = pd.DataFrame({"Id": arrayId})

    datasetResultado["production"] = predicao
    print(datasetResultado)
    datasetResultado.to_csv("submission.csv")

escreverSubmissao(clf)