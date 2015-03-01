print(c('Answer:', sum((v <- 1:999)[v%%3 == 0 | v%%5 == 0])), quote=FALSE)
