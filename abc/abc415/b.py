S = input()

is_second = False

place_first = 0
place_second = 0

for i, s in enumerate(S):
  if s == '#':
    if is_second:
      place_second = i + 1
      is_second = False
    else:
      place_first = i + 1
      is_second = True
  if place_second > place_first:
    print(f"{place_first},{place_second}")
    place_first  = 0
    place_second = 0
