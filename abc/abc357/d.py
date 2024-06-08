def mod_pow(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def mod_inv(a, m):
    return mod_pow(a, m - 2, m)

import sys
input = sys.stdin.read
n = input().strip()
l = len(n)
n = int(n)

mod = 998244353
r = 10 ** l
r_mod = r % mod

r_pow_n_mod = mod_pow(r_mod, n, mod)

sum = ((r_pow_n_mod - 1) * mod_inv(r_mod - 1, mod)) % mod

result = (n * sum) % mod

print(result)
