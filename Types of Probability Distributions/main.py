import scipy.stats as stats

prob = 1 - stats.binom.cdf(6 ,10 , 0.5)

print(prob)