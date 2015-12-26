fib = 1:1:zipWith (+) fib (tail fib)

problem2 = sum $ takeWhile (<4000000) evenFib
  where evenFib = [e | e <- fib, mod e 2 == 0]

main = do
  print problem2
