from math import sqrt


def get_distance(a, b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


def print_map(pos: list[int], v: set):
    s = ''
    for i in range(10, -5, -1):
        for j in range(-15, 15):
            try:
                p2 = pos.copy()
                p2.reverse()
                x = p2.index((j, i))
            except ValueError:
                x = -1
            if (j, i) in v:
                s += '#'
            elif x != -1:
                s += 'H' if x == len(pos)-1 else str(len(pos)-1-x)
            else:
                s += '.'
        s += '\n'
    s += '\n'
    with open('output.txt', 'a+') as f:
        f.write(s)


with open("./input2.txt") as f:
    data = f.read().splitlines()
nodes = 10
h = (0, 0)
t = (0, 0)
dir_to_move = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}
visited_pos = {t}
sqrt_2 = 2**0.5
pos = [h]*nodes
h_index = 0
for line in data:
    s = line.split(" ")
    if len(s) < 2:
        break
    direction = s[0]
    move = dir_to_move[direction]
    times = int(s[1])
    for i in range(times):
        pos[0] = tuple(map(lambda a, b: a+b, pos[0], move))
        for i in range(1, nodes):
            dist = get_distance(pos[i-1], pos[i])
            #print('h', h, 'move', move, 'last_h', last_h, 't', t, 'dist', dist)
            if dist >= 2:
                a, b = pos[i], pos[i-1]
                x_dir = -1 if b[0] < a[0] else 1 if b[0] > a[0] else 0
                y_dir = -1 if b[1] < a[1] else 1 if b[1] > a[1] else 0
                pos[i] = tuple(map(lambda a, b: a+b, pos[i], (x_dir, y_dir)))
        visited_pos.add(pos[-1])
        #print_map(pos, visited_pos)

print(len(visited_pos))
