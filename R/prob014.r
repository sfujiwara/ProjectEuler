lim <- 10000000
cache <- numeric(lim)
cache[1] <- 1

check_length <- function(n) {
	if(n > lim) {
		if(n%%2 == 0) return(1 + check_length(n/2))
		else return(1 + check_length(3*n+1))
	}
	else if(cache[n] != 0) return(cache[n])
	else if(n%%2 == 0) {
		cache[n] <<- 1 + check_length(n/2)
		return(cache[n])
	}
	else {
		cache[n] <<- 1 + check_length(3*n+1)
		return(cache[n])
	}
}

max_length <- 0
for(i in 500000:999999) {
	tmp <- check_length(i)
	if(tmp > max_length) {
		max_length <- tmp
		ans <- i
	}
}

cat("Answer =", ans, "\n")
