problem1 = sum [x | x <- [1..1000], mod x 3 == 0 || mod x 5 == 0]

main = do
  print problem1
