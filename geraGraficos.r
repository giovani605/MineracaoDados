library("ggplot2")

dados <- read.csv("tabelaTuplas.csv")


dados$ordem <- dados$month + (dados$year*2)

field0 <- subset(dados,field == 0,select = c(field,month,year,production,age,ordem,tempo))


agregadoProdAge <-aggregate(dados$production,by = list(dados$age),mean)
agregadoProdField <-aggregate(dados$production,by = list(dados$field),mean)



ggplot(agregadoProdAge,aes(x=agregadoProdAge$Group.1,y = agregadoProdAge$x)) + geom_line() + labs(x= "Idade" , y = "Produção")

ggplot(field0,aes(x=field0$ordem,y=field0$production)) + geom_smooth()