# Randomizing data, generating summary statistics, and histrogram 

import numpy as np

mu = 80
sigma = 10

x = np.ramdom.normal(mu, sigma, 100)

print("Random Normal Array Mean Centered", x[:10])


print("mean", np.mean(x)) 
