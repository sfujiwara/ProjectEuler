sieve <- function(n) {
    isprime <- rep(TRUE, n)
    isprime[1] <- FALSE
    for(i in 2:sqrt(n)) {
        if(isprime[i]) isprime[seq(i*2, n, by=i)] <- FALSE
    }
    return(as.numeric(which(isprime)))
}


print(c('Answer:', sieve(1000000)[10001]), quote=FALSE)
