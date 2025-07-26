S = input()

passed_sharp = True

result = ""

for c in S:
  if c == "#":
    result += "#"
    passed_sharp = True
  else: # c == "."
    if passed_sharp:
      result += "o"
      passed_sharp = False
    else:
      result += "."

print(result)
