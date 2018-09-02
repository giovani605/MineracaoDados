import csv
# Esse scrpt cria uma tupla para cada dado

def comparar(teste,field):
    if teste["harvest_month"] != field["month"]:
        return False
    if teste["harvest_year"] != field["year"]:
        return False
    return True

def procurarTupla(dict,field):
    for entrada in dict:
        a = entrada["field"]
        if entrada["field"] == field:
            return entrada

dados = open("dados/train.csv",'r')
dictDados = csv.DictReader(dados)
dadosSoil = open("dados/soil_data.csv",'r')
dictSoil = csv.DictReader(dadosSoil)
for dado in dictDados:
    # carrega o dadso do field
    fieldcsv = open("dados/field-"+dado["field"]+".csv",'r')
    dictField = csv.DictReader(fieldcsv)
    tupla = procurarTupla(dictSoil,dado["field"])
    dadosSoil = open("dados/soil_data.csv", 'r')
    dictSoil = csv.DictReader(dadosSoil)
    print(tupla)
    for d in dictField:
        # procurar o match com meu teste
        if comparar(dado,d):
            print(" ")
          #  print(dictField.fieldnames)
            ## criar uma nova entrada no dict


