import csv
import json
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

def salvarTupla(tabela, objJson):

    print(objJson)
    csv_writer.writerow(objJson)

def mediaSolo(l1,l2,l3,l4):
    return (float(l1) + float(l2) + float(l3) + float(l4))/4



fields = [      "field",
                "harvest_year",
                "harvest_month",
                "production",
                "age",
                "temperature",
                "Precipitation","Soilwater_L3",
                "dewpoint",
                "Soilwater_L4",
                "windspeed",
                "Soilwater_L1",
                "Soilwater_L2"]


tabela = open('tabelaTuplas.csv','w')
csv_writer = csv.DictWriter(tabela, fieldnames=fields, delimiter=',')
csv_writer.writeheader()


dados = open("datasets/train.csv",'r')
dictDados = csv.DictReader(dados)
dadosSoil = open("datasets/soil_data.csv",'r')
dictSoil = csv.DictReader(dadosSoil)
for dado in dictDados:
    # carrega o dadso do field
    fieldcsv = open("datasets/field-"+dado["field"]+".csv",'r')
    dictField = csv.DictReader(fieldcsv)
    tupla = procurarTupla(dictSoil,dado["field"])
    dadosSoil = open("datasets/soil_data.csv", 'r')
    dictSoil = csv.DictReader(dadosSoil)
    for d in dictField:
        # procurar o match com meu teste
        # Dado vem do train.csv , d vem do field##.csv , clima
        #falta o soil data
        if comparar(dado,d):
            salvarTupla(tabela, {
                "field": dado["field"],
                "harvest_year": dado["harvest_year"],
                "harvest_month": dado["harvest_month"],
                "production": dado["production"],
                "age": dado["age"],
                "temperature": d['temperature'],
                "Precipitation": d['Precipitation'],
                "Soilwater_L3": d['Soilwater_L3'],
                "dewpoint": d['dewpoint'],
                "Soilwater_L4": d['Soilwater_L4'],
                "windspeed": d['windspeed'],
                "Soilwater_L1": d['Soilwater_L1'],
                "Soilwater_L2": d['Soilwater_L2']
            })
            print(" ")


