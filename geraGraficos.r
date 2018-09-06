library("ggplot2")
library("zoo")

dados <- read.csv("tabelaTuplas.csv")

dados$teste <- as.yearmon(paste(dados$year, dados$month), "%Y %m")
dados$ordem <- dados$month + (dados$year*2)



field0 <- subset(dados,field == 0,select = c(field,month,year,production,age,ordem,tempo))


agregadoProdAge <-aggregate(dados$production,by = list(dados$age),mean)
agregadoProdField <-aggregate(dados$production,by = list(dados$field),mean)



ggplot(agregadoProdAge,aes(x=agregadoProdAge$Group.1,y = agregadoProdAge$x)) + geom_line() + labs(x= "Idade" , y = "Produção")

ggplot(field0,aes(x=field0$ordem,y=field0$production)) + geom_smooth()

ggplot(agregadoProdField,aes(x=agregadoProdField$Group.1,y = agregadoProdField$x,colour =agregadoProdField$x),) + geom_bar(stat = "identity",aes(fill = agregadoProdField$x)) + labs(x= "Field" , y = "Produção") + labs(colour = "Produção")

ggplot(dados,aes(x=dados$teste,y=dados$production)) + geom_smooth() + labs(x="Data",y="Produção")


ggplot(subset(dados,select = field < 5),aes(x = dados$teste,y=dados$production,color=dados$fator)) + geom_smooth()

ggplot(dados,aes(x = dados$teste,y=dados$production,color=dados$fator)) + geom_smooth(se = FALSE)

variosplots <- function (dados,plotPerPlot){
  a = 0;
  vetorPlot = c();
  while(a < 28){
    corte <- subset(dados,subset = field < 5)
    corte$fator <- factor(corte$field)
    ggplot(corte,aes(x = corte$teste,y=corte$production,color=corte$fator)) + geom_smooth(se = FALSE)
  }
}
variosplots(dados)


  

