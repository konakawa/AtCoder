h, w = map(int, input().split())
s_y, s_x = map(int, input().split())

c_s_s = []

for i in range(h):
    c_s_s.append(list(input()))

x = list(input())

for c in x:
    if c == 'L':
        if s_x - 1 >= 1: 
            if c_s_s[s_y - 1][s_x - 2] != '#':
                s_x -= 1
    elif c == 'R':
        if s_x + 1 <= w:
            if c_s_s[s_y - 1][s_x] != '#':
                s_x += 1
    elif c == 'U':
        if s_y - 1 >= 1:
            if c_s_s[s_y - 2][s_x - 1] != '#':
                s_y -= 1
    elif c == 'D':
        if s_y + 1 <= h:
            if c_s_s[s_y][s_x - 1] != '#':
                s_y += 1

print(s_y, s_x)