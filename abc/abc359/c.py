Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

is_sum_even = (Sx + Sy) % 2 == 0

vertical_distance = abs(Ty - Sy)

horizontal_distance = (Tx - Sx)
is_horizontal_positive = horizontal_distance >= 0
horizontal_distance = abs(horizontal_distance)

result = 0

if is_sum_even:
    if is_horizontal_positive:
        result = vertical_distance + max(0, (horizontal_distance - vertical_distance) // 2)
    else:
        result = vertical_distance + max(0, (horizontal_distance - vertical_distance + 1) // 2)
else:
    if is_horizontal_positive:
        result = vertical_distance + max(0, (horizontal_distance - vertical_distance + 1) // 2)
    else:
        result = vertical_distance + max(0, (horizontal_distance - vertical_distance) // 2)

print(result)