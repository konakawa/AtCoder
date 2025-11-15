X = int(input())

digit_occurrences = [0] * 10
while X > 0:
  digit_occurrences[X % 10] += 1
  X //= 10

head = 0
for i in range(1, 10):
  if digit_occurrences[i] > 0:
    head = i
    digit_occurrences[i] -= 1
    break

l = [head]
for i in range(10):
  while digit_occurrences[i] > 0:
    l.append(i)
    digit_occurrences[i] -= 1

print(int("".join(map(str, l))))