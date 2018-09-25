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

def salvarTupla(tabela,field,year,month,age,temperatura,Precipitation,medSolo,id):
    linha = {}
    linha[fields[0]] = field
    linha[fields[1]] = month
    linha[fields[2]] = year
    linha[fields[3]] = age
    linha[fields[4]] = str(month)+"/"+str(year)
    linha[fields[5]] = temperatura
    linha[fields[6]] = Precipitation
    linha[fields[7]] = medSolo
    linha[fields[8]] = id
    print(linha)
    csv_writer.writerow(linha)

def mediaSolo(l1,l2,l3,l4):
    return (float(l1) + float(l2) + float(l3) + float(l4))/4



fields = ['field','month','year','age','tempo', 'temperature','Precipitation','solo','Id']


tabela = open('tabelaTuplasValidar.csv','w')
csv_writer = csv.DictWriter(tabela, fieldnames=fields, delimiter=',')
csv_writer.writeheader()


dados = open("datasets/test.csv",'r')
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
        if comparar(dado,d):
            medSolo = mediaSolo(d['Soilwater_L1'],d['Soilwater_L2'],d['Soilwater_L3'],d['Soilwater_L4'])
            salvarTupla(tabela,dado["field"],dado["harvest_year"],dado["harvest_month"],dado["age"],d['temperature'],d['Precipitation'],medSolo,dado["Id"])
            print(" ")
          #  print(dictField.fieldnames)
            ## criar uma nova entrada no dict


