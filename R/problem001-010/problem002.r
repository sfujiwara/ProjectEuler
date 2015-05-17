## クロージャを使うとメモ化再帰が格好良く書けることに気付いた
fibonacci <- (function() {
    memo <- numeric(1000)
    memo[1] <- 1
    memo[2] <- 1
    f <- function(n) {
        if (memo[n] != 0) {
            return(memo[n])
        }
        else {
            memo[n] <<- f(n-1) + f(n-2)
            return(memo[n])
        }
    }
    return(f)
})()


ans <- 0
n <- 1

while (TRUE) {
    val <- fibonacci(n)
    if (val >= 4000000) break
    ans <- ans + val * (val %% 2 == 0)
    n <- n + 1
}

print(c("Answer:", ans), quote=FALSE)
