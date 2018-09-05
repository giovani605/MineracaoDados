library("ggplot2")
library("zoo")

dados$teste <- as.yearmon(paste(dados$year, dados$month), "%Y %m")
dados$ordem <- dados$month + (dados$year*2)



field0 <- subset(dados,field == 0,select = c(field,month,year,production,age,ordem,tempo))


agregadoProdAge <-aggregate(dados$production,by = list(dados$age),mean)
agregadoProdField <-aggregate(dados$production,by = list(dados$field),mean)



ggplot(agregadoProdAge,aes(x=agregadoProdAge$Group.1,y = agregadoProdAge$x)) + geom_line() + labs(x= "Idade" , y = "Produção")

ggplot(field0,aes(x=field0$ordem,y=field0$production)) + geom_smooth()

ggplot(agregadoProdField,aes(x=agregadoProdField$Group.1,y = agregadoProdField$x,colour =agregadoProdField$x),) + geom_bar(stat = "identity",aes(fill = agregadoProdField$x)) + labs(x= "Field" , y = "Produção") + labs(colour = "Produção")


