## 最小重み全域木を 1 つ見つけるだけ
## igraph の minimum.spanning.tree() はプリム法で解いている
## 重みが無い場合は unweighted algorithm というのも選べるが, 何者なのか謎

library(igraph)

## ここのデータの読み込みと加工はもうちょっと綺麗に書けそう
adjmat <- as.matrix(read.csv("p107_network.txt", head=FALSE))
adjmat[adjmat=="-"] <- 0
adjmat <- matrix(as.numeric(adjmat), nrow=40)

g <- graph.adjacency(adjmat, weighted=TRUE, mode=c("undirected"))
mst <- minimum.spanning.tree(g)
ans <- sum(adjmat)/2 - sum(E(mst)$weight)
print(c('Answer:', ans), quote=FALSE)
