N = int(input())

bits = ['0'] * 10
for i in range(10):
  bits[9 - i] = str(N % 2)
  N //= 2

print(''.join(bits))