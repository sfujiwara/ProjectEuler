isPalindrome x = (show x) == (reverse $ show x)

problem4 = maximum [x * y | x <- [100..999], y <- [x..999], isPalindrome (x * y)]

main = do
  print problem4
