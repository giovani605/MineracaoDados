library("ggplot2")
library("zoo")
library("grid")

dados <- read.csv("tabelaTuplas.csv")

dados$teste <- as.yearmon(paste(dados$year, dados$month), "%Y %m")
dados$ordem <- dados$month + (dados$year*2)

#Densidades
d <- density(dados$temperature) # densidade da temperatura
plot(d,xlab = "Temperatura",ylab = "Densidade",main="") # plota a densidade

dp <- density(dados$Precipitation) # densidade da temperatura
plot(dp,xlab = "Precipitação",ylab = "Densidade",main="") # plota a densidade

#agua no sllo
ds <- density(dados$solo) # densidade da temperatura
plot(ds,xlab = "Agua no solo(média entre as camadas) ",ylab = "Densidade",main="") # plota a densidade


# correlacao
cor(dados$Precipitation , dados$solo)

cor(dados$Precipitation , dados$production)

cor(dados$solo, dados$production)

cor(dados$age, dados$production)

cor(dados$temperature , dados$production)


#rename
dados$idade <- dados$age
dados$temperatura <- dados$temperature
dados$aguaSolo <- dados$solo
dados$precipitacao <- dados$Precipitation
## modelo 1
modelo <- lm(dados$production ~ dados$precipitacao + dados$aguaSolo + dados$temperatura + dados$idade)
summary(modelo)


summary(lm(dados$production ~ dados$Precipitation))
?lm

## criar uma corelação entre produção e temperatura


field0 <- subset(dados,field == 0,select = c(field,month,year,production,age,ordem,tempo))


agregadoProdAge <-aggregate(dados$production,by = list(dados$age),mean)
agregadoProdField <-aggregate(dados$production,by = list(dados$field),mean)



ggplot(agregadoProdAge,aes(x=agregadoProdAge$Group.1,y = agregadoProdAge$x)) + geom_line() + labs(x= "Idade" , y = "Produção")

ggplot(field0,aes(x=field0$ordem,y=field0$production)) + geom_smooth()

ggplot(agregadoProdField,aes(x=agregadoProdField$Group.1,y = agregadoProdField$x,colour =agregadoProdField$x),) + geom_bar(stat = "identity",aes(fill = agregadoProdField$x)) + labs(x= "Field" , y = "Produção") + labs(colour = "Produção")

ggplot(dados,aes(x=dados$teste,y=dados$production)) + geom_smooth() + labs(x="Data",y="Produção")


ggplot(subset(dados,select = field < 5),aes(x = dados$teste,y=dados$production,color=dados$fator)) + geom_smooth()

dados$fator <- factor(dados$field)
ggplot(dados,aes(x = dados$teste,y=dados$production,color=dados$fator))+
 geom_smooth(se = FALSE) 
geom_smooth(se = FALSE)
corte1 <- subset(dados,subset = dados$field < 7)
p1 <- ggplot(corte1,aes(x = corte1$teste,y=corte1$production,color=corte1$fator))+
 + labs(x="Field",y="Produção",colour="Field") 
+ geom_smooth(method = "lm",formula =corte1$production ~ corte1$temperature  )
p1
corte2 <- subset(dados,subset = dados$field >= 7 & dados$field < 14)
p2 <-ggplot(corte2,aes(x = corte2$teste,y=corte2$production,color=corte2$fator))+
  geom_smooth(se = FALSE) + labs(x="Field",y="Produção",colour="Field") 
p2
corte3 <- subset(dados,subset = dados$field >= 14 & dados$field < 21)
p3 <-ggplot(corte3,aes(x = corte3$teste,y=corte3$production,color=corte3$fator))+
  geom_smooth(se = FALSE) + labs(x="Field",y="Produção",colour="Field") 
p3
corte4 <- subset(dados,subset = dados$field >= 21 & dados$field < 28)
p4 <-ggplot(corte4,aes(x = corte4$teste,y=corte4$production,color=corte4$fator))+
  geom_smooth(se = FALSE) + labs(x="Field",y="Produção",colour="Field") 
p4

multiplot(p1,p2,p3,p4,cols = 2)

grid.arrange(p1,p2,p3,p4)

# plot do modelo
ggplot(corte1,aes(x = corte1$temperature ,y=corte1$production,color=corte1$fator)) + 
  geom_smooth(method = "lm",formula = corte1$temperature ~ corte1$production) 

predicao <- predict(modelo,corte1)
ggplot(predicao,aes(x = corte1$temperature ,y=corte1$production,color=corte1$fator)) + 
  geom_smooth(method = "lm",formula = corte1$temperature ~ corte1$production) 



variosplots <- function (dados,plotPerPlot){
  a = 0;
  vetorPlot = c();
  while(a < 28){
    corte <- subset(dados,subset = field < 5)
    corte$fator <- factor(corte$field)
    ggplot(corte,aes(x = corte$teste,y=corte$production,color=corte$fator)) + geom_smooth(se = FALSE)
  }
}
variosplots(dados,1)

multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  library(grid)
  
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}

## Validacao
dadosValidar <- read.csv("tabelaTuplasValidar.csv")
dadosValidar$idade <- dadosValidar$age
dadosValidar$temperatura <- dadosValidar$temperature
dadosValidar$aguaSolo <- dadosValidar$solo
dadosValidar$precipitacao <- dadosValidar$Precipitation
resultado <- as.data.frame(predict(modelo,newdata = dadosValidar))
names(resultado) <- c("production")
resultado$Id <- seq(1,nrow(resultado),1)
resultadoFinal <- resultado[,c(2,1)]
write.csv(resultadoFinal,"submission.csv")




