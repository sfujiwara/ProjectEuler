isPythagorean a b c = a^2 + b^2 == c^2


problem9 = [a * b * c | a <- [1..499], b <- [a..499], let c = 1000 - a - b, isPythagorean a b c]


main = do
  print problem9
