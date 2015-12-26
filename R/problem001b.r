cat('Answer:', sum(ifelse((v <- 1:999)%%3 == 0 | v%%5 == 0, v, 0)), '\n')
