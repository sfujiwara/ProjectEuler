n <- 2903040
ans <- 0
for(i in 3:n) {
	num <- strsplit(as.character(i), character(0))[[1]]
	
	if (i == sum(factorial(as.integer(num)))) {
		print(i)
		ans <- ans+i
	}
}

num2vec <- function(n) {
	return(as.numeric(strsplit(as.character(n), character(0))[[1]]))
}

n <- 50000
ans <- 0

for(i in 3:n) {
	if(i == sum(factorial(num2vec(i)))) print(i)
}
