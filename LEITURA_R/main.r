dados_short <- read.csv(file = 'heart_rate.csv', header=TRUE)
dados_long <- read.csv(file = 'heart_rate_long.csv', header=TRUE)
media_short = mean(dados_short[,3])
media_short
desvio_padrao_short = sd(dados_short[,3])
desvio_padrao_short
media_long = mean(dados_long[,3])
media_long
desvio_padrao_long = sd(dados_long[,3])
desvio_padrao_long