n, m, k = map(int, input().split())

inputs_array = []
for i in range(m):
    inputs_array.append(input().split())

count = 0
for comb in range(2**n):
    fg = True
    for inputs in inputs_array:
        count_ = 0
        c = int(inputs[0])
        r = inputs[-1]
        if r == 'o':
            for i in range(1, len(inputs)-1):
                if (comb >> (int(inputs[i])-1)) & 1:
                    count_ += 1
            if count_ < k:
                fg = False
                break
        else:
            for i in range(1, len(inputs)-1):
                if (comb >> (int(inputs[i])-1)) & 1:
                    count_ += 1
            if count_ >= k:
                fg = False
                break
    if fg:
        count += 1
print(count)