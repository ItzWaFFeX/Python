from scipy.stats import binom

#Number of coin flips
n = 10

#Probability of getting heads
p = 0.5


prob = binom.pmf(2, n, p) + binom.pmf(3, n, p) + binom.pmf(4, n, p)

print(f'Probability of getting between 2 and 4 heads (inclusive): {prob:.4f}')
