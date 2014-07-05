mod = 1e10

pow <- function(n, mod) {
	result <- 1
	for(i in 1:n) {
		result <- result*n
		if(result > mod) result <- result %% mod
	}
	return(result)
}

ans <- 0
for(i in 1:1000) {
	ans <- ans + pow(i, mod)
	if(ans > mod) ans <- ans %% mod
}

cat("Answer =", ans, "\n")
