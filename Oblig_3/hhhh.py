import numpy as np

def x_lt(N, K, alpha=0.5, A=1):
    return A * (N^alpha) * (K^(1-alpha))

# Test med enkelttall
print(x_lt(16, 16))

# Test med rekkevidde (1 til 16)
N_range = np.arange(1, 17) # 17 fordi slutten ikke telles med
K_range = np.arange(1, 17)

print(x_lt(N_range, K_range))