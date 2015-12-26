for (a in 1:332) {
    for (b in a:499) {
        c <- 1000 - a - b
        if (a^2 + b^2 == c^2) {
            ans <- c(a, b, c)
            break
        }
    }
}

cat('Answer:', prod(ans), '\n')
