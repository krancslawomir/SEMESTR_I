
#Konwersja danych na data frame.
data_frame <- function(index){
  df <- data.frame()
  start=3+14*(index -1)
  end=16+14*(index -1)
  
  for(i in 1:12)
    df <- rbind(df,data.frame(matrix(unlist(Data[(start+14*10*(i-1)):(end+14*10*(i-1))]),nrow = 17)))
  
  return(df)
}

#Generowanie tablicy z wartościami średnimi dla danych.
# i dla miesięcy
# j dla województw
sr_tab <- function(Frame){
  means <- data.frame()
  for(j in 1:17){
    numbers <- list(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
    for(i in 1:12){
      numbers <- mapply("+", numbers, Frame[j+17*(i-1),] , SIMPLIFY = FALSE)
    }
    tmp <- data.frame(matrix(unlist(numbers),nrow=1)/12)
    means <- rbind(means,tmp)
  }
  
  return (means)
}


  #Importowanie danych.
  Data <-(read.csv(file = ".\\CENY_2917_CTAB_20200214095158.csv",header = TRUE,sep = ';', dec = ',', stringsAsFactors = FALSE, encoding = 'UTF-8'))
  wojewodztwo <- c("Polska","Dolnoslaskie","Kujawsko-Pomorskie","Lubelskie","Lubuskie","Lodzkie","Malopolskie",
                    "Mazowieckie","Opolskie","Podkarpackie","Podlaskie","Pomorskie","Slaskie","Swietokrzyskie",
                    "Warminsko-Mazurskie","Wielkopolskie","Zachodniopomorskie")
  years <- c("2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019")

  #Wyciągadnie wartości poszczególnych prodouktów.
  
  chleb <- data_frame(1)
  chleb_sr <- sr_tab(chleb)
  
  kielbasa_suszona <- data_frame(2)
  kielbasa_suszona_sr <- sr_tab(kielbasa_suszona)
  
  mleko3 <- data_frame(3)
  mleko3_sr <- sr_tab(mleko3)
  
  smietana <- data_frame(4)
  smietana_sr <- sr_tab(smietana)
  
  pomarancze <- data_frame(5)
  pomarancze_sr <- sr_tab(pomarancze)
  
  piwo <- data_frame(6)
  piwo_sr <- sr_tab(piwo)
  
  oczyszczanie_garnituru <- data_frame(7)
  oczyszczanie_garnituru_sr <- sr_tab(oczyszczanie_garnituru)
  
  olej_napedowy <- data_frame(8)
  olej_napedowy_sr <- sr_tab(olej_napedowy)
  
  bilet_kino <- data_frame(9)
  bilet_kino_sr <- sr_tab(bilet_kino)
  
  mydlo <- data_frame(10)
  mydlo_sr <- sr_tab(mydlo)
  


chleb_plot <- unlist(chleb_sr[1,])
kielbasa_plot <- unlist(kielbasa_suszona_sr[1,])
mleko3_plot <- unlist(mleko3_sr[1,])
smietana_plot <- unlist(smietana_sr[1,])
pomarancze_plot <- unlist(pomarancze_sr[1,])
piwo_plot <- unlist(piwo_sr[1,])
oczyszczanie_plot <- unlist(oczyszczanie_garnituru_sr[1,])
olej_plot <- unlist(olej_napedowy_sr[1,])
bilet_plot <- unlist(bilet_kino_sr[1,])
mydlo_plot <- unlist(mydlo_sr[1,])
  

#Rysowanie wykresów średnich cen 

barplot(chleb_plot,
        main = "Średnia cena bochenka chleba pszenno-żytniego ",
        ylim = range(pretty(c(0,chleb_plot))),
        xlab = "Lata",
        ylab = "Cena [zł]",
        names.arg = c("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"),
        col = "blue",
        border = "black")


barplot(kielbasa_plot,
        main = "Średnia cena 1kg kiełbasy suszonej ",
        ylim = range(pretty(c(0,kielbasa_plot))),
        xlab = "Lata",
        ylab = "Cena [zł]",
        names.arg = c("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"),
        col = "blue",
        border = "black")


barplot(mleko3_plot,
        main = "Średnia cena mleka o zawartości tłuszczu 3-3,5% ",
        ylim = range(pretty(c(0,mleko3_plot))),
        xlab = "Lata",
        ylab = "Cena [zł]",
        names.arg = c("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"),
        col = "blue",
        border = "black")


barplot(smietana_plot,
        main = "Średnia cena śmietany o zawartości tłuszu 18% za 200g ",
        ylim = range(pretty(c(0,smietana_plot))),
        xlab = "Lata",
        ylab = "Cena [zł]",
        names.arg = c("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"),
        col = "blue",
        border = "black")


barplot(pomarancze_plot,
        main = "Średnia cena 1kg pomarańczy ",
        ylim = range(pretty(c(0,pomarancze_plot))),
        xlab = "Lata",
        ylab = "Cena [zł]",
        names.arg = c("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"),
        col = "blue",
        border = "black")


barplot(piwo_plot,
        main = "Średnia cena piwa jasnego butelkowanego ",
        ylim = range(pretty(c(0,piwo_plot))),
        xlab = "Lata",
        ylab = "Cena [zł]",
        names.arg = c("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"),
        col = "blue",
        border = "black")


barplot(oczyszczanie_plot,
        main = "Średnia cena oczyszczania chemiczego męskiego garnituru ",
        ylim = range(pretty(c(0,oczyszczanie_plot))),
        xlab = "Lata",
        ylab = "Cena [zł]",
        names.arg = c("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"),
        col = "blue",
        border = "black")


barplot(olej_plot,
        main = "Średnia cena 1l oleju napędowego ",
        ylim = range(pretty(c(0,olej_plot))),
        xlab = "Lata",
        ylab = "Cena [zł]",
        names.arg = c("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"),
        col = "blue",
        border = "black")


barplot(bilet_plot,
        main = "Średnia cena biletu do kina ",
        ylim = range(pretty(c(0,bilet_plot))),
        xlab = "Lata",
        ylab = "Cena [zł]",
        names.arg = c("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"),
        col = "blue",
        border = "black")

barplot(mydlo_plot,
        main = "Średnia cena mydła toaletowego ",
        ylim = range(pretty(c(0,mydlo_plot))),
        xlab = "Lata",
        ylab = "Cena [zł]",
        names.arg = c("2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"),
        col = "blue",
        border = "black")