# install.packages("remotes")
remotes::install_github("rfsaldanha/microdatasus")
library(microdatasus)

dados<-
  fetch_datasus(
  year_start = 2022,
  year_end = 2022,
  uf = "DF",
  information_system = "SINASC"
  )

View(dados)

dados<-
  dados |> 
  dplyr::select(c('IDADEMAE',
                  'ESTCIVMAE','ESCMAE','CODOCUPMAE',
                  'QTDFILVIVO','QTDFILMORT','GESTACAO',
                  'GRAVIDEZ','PARTO','CONSULTAS',
                  'DTNASC','SEXO','RACACOR','PESO'
  ))

View(dados)

