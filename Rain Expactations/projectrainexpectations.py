import scipy.stats as stats

prob = 1-stats.binom.cdf(12,18,30)

print(prob)