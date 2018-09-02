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

def salvarTupla(tabela,field,year,month,production,age):
    linha = {}
    linha[fields[0]] = field
    linha[fields[1]] = month
    linha[fields[2]] = year
    linha[fields[3]] = production
    linha[fields[4]] = age
    linha[fields[5]] = str(month)+"/"+str(year)
    print(linha)
    csv_writer.writerow(linha)


fields = ['field','month','year','production','age','tempo']


tabela = open('tabelaTuplas.csv','w')
csv_writer = csv.DictWriter(tabela, fieldnames=fields, delimiter=',')
csv_writer.writeheader()


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
    for d in dictField:
        # procurar o match com meu teste
        if comparar(dado,d):
            salvarTupla(tabela,dado["field"],dado["harvest_year"],dado["harvest_month"],dado["production"],dado["age"])
            print(" ")
          #  print(dictField.fieldnames)
            ## criar uma nova entrada no dict


