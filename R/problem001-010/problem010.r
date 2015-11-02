sieve <- function(n) {
    isprime <- rep(TRUE, n)
    isprime[1] <- FALSE
    for(i in 2:sqrt(n)) {
        if(isprime[i]) isprime[seq(i*2, n, by=i)] <- FALSE
    }
    return(as.numeric(which(isprime)))
}


print(c('Answer:', sum(sieve(2000000))), quote=FALSE)
