import numpy as np

# Width
w = 10
# Height
h = 10
# Border
b = [(1, 1), (1, h - 1), (w - 1, h - 1), (w - 1, 1)]

# Obstacles
o1 = [(8, 6), (10, 20), (22, 16)]
o2 = [(27, 17), (33, 15), (35, 31), (27, 31)]
o3 = [(16, 40), (26, 41), (35, 39), (14, 32)]

os = [o1, o2, o3]

# s = [2, 2]
# d = [40, 40]

# Starting point
s = (2, 2)
# Destination
d = (7, 4)

# Straight move cost
sm = 1
# Diagonal move cost
dm = 1.5

# Solution 1
# Get [slope, intersect] of lines of o
# def get_lines(o):
#     n = len(o)
#     ls = []
#     for i in range(n):
#         x1 = o[i][0]
#         y1 = o[i][1]
#         x2 = o[(i + 1) % n][0]
#         y2 = o[(i + 1) % n][1]

#         if x1 == x2:
#             l = [x1, 0]
#         elif y1 == y2:
#             l = [0, y1]
#         else:
#             a = [[x1, 1], [x2, 1]]
#             b = [y1, y2]
#             # y = slope*x + intersect                
#             l = np.linalg.solve(a, b)
#             ls.append(l)
#     return ls
#     # do something here

# def get_intersection(ls):
#     return True
#     # return intersect

# def is_in(p, os):
#     ls = []
#     for o in os:
#         o.append(list(p))
#         ls.append(get_lines(o))
#         del o[len(o) - 1]

#     its = get_intersection(ls)
#     for i in range(len(its)):
#         for it in its[i]:
#             if it not in os[i]:
#                 return True
#     return False

# Solution 2:
# Compute the sign of the z-component of the cross product of 2 vectors
def z_sign(o):
    n = len(o)
    zs = []
    for i in range(n):
        print(o[i])
        # vector1.x = point1.x - point2.x
        ax = o[i][0] - o[(i + 1) % n][0]
        # vector1.y = point1.y - point2.y
        ay = o[i][1] - o[(i + 1) % n][1]

        # vector2.x = point2.x - point3.x
        bx = o[(i + 1) % n][0] - o[(i + 2) % n][0]
        # vector2.y = point2.y - point3.y
        by = o[(i + 1) % n][1] - o[(i + 2) % n][1]

        z = ax*by - bx*ay
        zs.append(np.sign(z))
    return zs

def get_max_min(o):
    x_max = o[0][0]
    y_max = o[0][1]
    x_min = o[0][0]
    y_min = o[0][1]
    for p in o:
        if p[0] > x_max:
            x_max = p[0] 
        if p[1] > y_max:
            y_max = p[1]
        if p[0] < x_min:
            x_min = p[0]
        if p[1] < y_min:
            y_min = p[1]
    print([x_min, y_max, x_max, y_min])
    return [x_min, y_max, x_max, y_min]


# Check if point p get inside obstacle o
def is_in(p, o):
    print(p)
    m = get_max_min(o)
    # p.x < x_min or p.y > y_max or p.x > x_max or p.y < y_min 
    if p[0] < m[0] or p[1] > m[1] or p[0] > m[2] or p[1] < m[3]:
        return False
    return True

    # # o.order_point_instead_of_append(p)
    # o.append(list(p))
    # z = z_sign(o)
    # del o[len(o) - 1]

    # r = True if -1 in z and 1 in z else False
    # return r

# Check if point p get outside barrier
def is_out(p, b):
    # point.x < barier_left.x point.x >= barrier_right.x or point.y >= barrier_top.y or point.y <= barrier_bottom.y
    # if (p[0] <= b[0][0] or p[0] >= b[2][0] or p[1] >= b[1][1] or p[1] <= b[3][1]):
    if (p[0] < b[0][0] or p[0] > b[2][0] or p[1] > b[1][1] or p[1] < b[3][1]):
        return True
    return False

# Get adjacent point of p
def get_next(p):
    next = []
    for i in range(p[0] - 1, p[0] + 2):
        for j in range(p[1] - 1, p[1] + 2):
            if not((i == p[0]) and (j == p[1])):
                next.append((i, j))
    return next

# Get path from start to dest in track
def get_path(start, dest, track):
    path = []
    path.append(dest)
    cur = dest
    while start not in path:
        pre = track[cur]
        path.append(pre)
        cur = pre
    path.reverse()
    return path



def stupid_traverse(start, dest):
    visited = []
    path = []
    # track[point] = previous point
    track = {}
    cost = 0
    # queue[point] = cost from root
    queue = {}
    # Insert start
    queue[tuple(start)] = cost

    # Loop
    while len(queue) != 0:   
        # Pop point with min cost
        mc = min(queue, key=queue.get)
        # print('mc', mc)
        visited.append(mc)
        path.append(mc)
        cost = queue.get(mc)
        del queue[mc]
        if (mc == dest):
            path = get_path(start, dest, track)
            return [path, cost]
        # Get children
        next = get_next(mc)
        for n in next:
            if n not in visited and not is_out(n, b):
                # Add new point with correspond cost
                if n not in queue.keys():                    
                    if n[0] == mc[0] or n[1] == mc[1]:
                        queue[n] = cost + sm
                    else:
                        queue[n] = cost + dm
                    track[n] = mc
                # Update better cost for available point
                else:
                    if n[0] == mc[0] or n[1] == mc[1]:
                        # queue[n] = ((cost + sm) > queue[n]) and queue[n] or (cost + sm)
                        if cost + sm < queue[n]:
                            queue[n] = cost + sm
                            track[n] = mc
                    else:
                        # queue[n] = ((cost + dm) > queue[n]) and queue[n] or (cost + dm)
                        if cost + dm < queue[n]:
                            queue[n] = cost + dm
                            track[n] = mc

[path, cost] = stupid_traverse(s, d)
print('path', path)
print('cost', cost)

