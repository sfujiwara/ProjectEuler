--pfd' :: Integer -> [Integer] -> [Integer]
pfd' n (x:xs)
  | n < 0         = (-1):(pfd' (-n) (x:xs))
  | n == 1        = []
  | x * x > n     = [n]
  | mod n x == 0  = x:(pfd' (div n x) (x:xs))
  | otherwise     = pfd' n xs


pfd = (flip pfd') (2:[3, 5..])


main = do
  print $ maximum $ pfd 600851475143
