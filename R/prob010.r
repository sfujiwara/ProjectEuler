# エラトステネスの篩でn以下の素数列を返す関数
sieve <- function(n) {
	flag <- rep(TRUE, n)
	flag[1] <- FALSE
	for(i in 2:sqrt(n)) {
		if(flag[i]) flag[seq(i*2, n, by=i)] <- FALSE
	}
	return(which(flag))
}

prime <- sieve(2000000)
ans <- 0
for(i in 1:length(prime)) ans = ans+prime[i]
cat("Answer =", ans, "\n")

# これだと何かオーバーフローが発生する?
# print(sum(sieve(2000000)))
