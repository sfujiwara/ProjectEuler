## 数独用パッケージがある, ずるい
library(sudoku)

## 問題ファイルの読み込み
mat <- array(0, dim=c(9*50, 9))
puzzles <- readLines("p096_sudoku.txt")
row <- 1
for (i in 1:length(puzzles)) {
    if (i %% 10 != 1) {
        mat[row,] <- as.numeric(strsplit(puzzles[i], "")[[1]])
        row <- row + 1
    }
}

ans <- 0
for (i in 1:50) {
    ## 1 行で解ける, ずるい
    res <- solveSudoku(mat[((i-1)*9+1):(i*9),], print.it=FALSE)
    ans <- ans + 100*res[1,1] + 10*res[1,2] + res[1,3]
}

print(c('Answer:', ans), quote=FALSE)
