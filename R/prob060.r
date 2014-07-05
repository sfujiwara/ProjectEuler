library(gmp)
library(igraph)

# エラトステネスの篩でn以下の素数列を返す関数
sieve <- function(n) {
	flag <- rep(TRUE, n)
	flag[1] <- FALSE
	for(i in 2:sqrt(n)) {
		if(flag[i]) flag[seq(i*2, n, by=i)] <- FALSE
	}
	return(which(flag))
}

are_interesting <- function(x, y) {
	# 任意の順で結合
	xy <- as.numeric(paste(x, y, sep=""))
	yx <- as.numeric(paste(y, x, sep=""))
	
	if (isprime(xy) & isprime(yx)) return(TRUE)
	else return(FALSE)
}

prime_list <- sieve(10000)
p1 <- numeric(0)
p2 <- numeric(0)

for(i in 1:length(prime_list)) {
	for(j in i:length(prime_list)) {
		if(are_interesting(prime_list[i], prime_list[j])) {
			p1[length(p1)+1] <- prime_list[i]
			p2[length(p2)+1] <- prime_list[j]
		}
	}
}

edge <- data.frame(p1,p2)
vers <- data.frame(unique(c(p1,p2)))
g <- graph.data.frame(edge, directed=FALSE, vers)

ans <- cliques(g, min=5)
print( V(g)[ans[[1]]])
