is_palindrome <- function(n) {
    n_str <- strsplit(as.character(n), "")[[1]]
    return(all(n_str == rev(n_str)))
}

ans <- 0
for (a in 100:998) {
    for (b in a:999) {
        cand <- a * b
        if (is_palindrome(cand)) {
            ans <- max(ans, cand)
        }
    }
}
        
print(ans)
