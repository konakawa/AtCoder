S = input()

char_occurrences = {}

for char in S:
  if char in char_occurrences:
    char_occurrences[char] += 1
  else:
    char_occurrences[char] = 1

for char in char_occurrences.items():
  if char[1] == 1:
    print(char[0])
    break