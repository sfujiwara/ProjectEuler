primes' :: [Integer] -> [Integer]
primes' [] = []
primes' (x:xs) = x : primes' [y | y <- xs, mod y x /= 0]


primes = primes' [2..]

main = do
  print $ primes !! 10000
