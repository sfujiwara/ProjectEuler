## 無理やり素因数分解して解いたので, 数分掛かる
## 篩っぽくやるか, 素数列を予め求めて素因数分解を高速化した方が良さそう

library(gmp)

num_divisor_bef <- 2
ans <- 0
for (i in 3:10000000) {
    num_divisor <- 1
    res <- table(as.numeric(factorize(i)))
    for (j in res) {
        num_divisor <- num_divisor * (j+1)
    }
    if (num_divisor == num_divisor_bef) {
        ans <- ans + 1
    }
    num_divisor_bef <- num_divisor
}

print(c("Answer:", ans), quote=FALSE)

