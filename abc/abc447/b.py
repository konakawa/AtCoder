S = input()

char_occurrences = {}

for char in S:
  if char in char_occurrences:
    char_occurrences[char] += 1
  else:
    char_occurrences[char] = 1

max_count = max(char_occurrences.values())
most_frequent_chars = [char for char, count in char_occurrences.items() if count == max_count]

result = ""
for char in S:
  if char not in most_frequent_chars:
    result += char

print(result)