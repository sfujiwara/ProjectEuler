library(gmp)

a <- 1777
b <- 1855
ans <- 1
for (i in 1:b) {
    ans <- powm(a, ans, 10^8)
}
print(c("Answer:", as.integer(ans[1])), quote=FALSE)
