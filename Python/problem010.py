# -*- coding: utf-8 -*-

# Answer: 142913828922

import numpy as np
from eulermath import prime

print 'Answer:', np.sum(prime.sieve(20000000))
