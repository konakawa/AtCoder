N = int(input())
Ts = list(map(int, input().split()))

indexed_Ts = [(t, i) for i, t in enumerate(Ts)]
indexed_Ts.sort()

print(" ".join([str(i + 1) for t, i in indexed_Ts[:3]]))