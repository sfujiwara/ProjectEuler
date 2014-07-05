ans <- 0
for(i in 1:100) {
	for(j in 1:100) {
		if(choose(i, j) > 1000000) ans <- ans+1
	}
}
