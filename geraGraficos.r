library("ggplot2")
library("zoo")
library(grid)

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

dados$fator <- factor(dados$field)
ggplot(dados,aes(x = dados$teste,y=dados$production,color=dados$fator))+
 geom_smooth(se = FALSE)

corte1 <- subset(dados,subset = dados$field < 7)
p1 <- ggplot(corte1,aes(x = corte1$teste,y=corte1$production,color=corte1$fator))+
  geom_smooth(se = FALSE) + labs(x="Field",y="Produção",colour="Field") 

corte1 <- subset(dados,subset = dados$field >= 7 & dados$field < 14)
p2 <-ggplot(corte1,aes(x = corte1$teste,y=corte1$production,color=corte1$fator))+
  geom_smooth(se = FALSE) + labs(x="Field",y="Produção",colour="Field") 

corte1 <- subset(dados,subset = dados$field >= 14 & dados$field < 21)
p3 <-ggplot(corte1,aes(x = corte1$teste,y=corte1$production,color=corte1$fator))+
  geom_smooth(se = FALSE) + labs(x="Field",y="Produção",colour="Field") 

corte1 <- subset(dados,subset = dados$field >= 21 & dados$field < 28)
p4 <-ggplot(corte1,aes(x = corte1$teste,y=corte1$production,color=corte1$fator))+
  geom_smooth(se = FALSE) + labs(x="Field",y="Produção",colour="Field") 

multiplot(p1,p2,p3,p4,cols = 2)

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
  

