import math

def rgb(r, g, b):
    t = []
    for i in [r, g, b]:
        if i < 0:
            t.append(0)
        elif i > 255:
            t.append(255)
        else:
            t.append(i)
    r = t[0]
    g = t[1]
    b = t[2]
    hex1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B', 'C', 'D', 'E', 'F']
    c = ""
    c += hex1[math.floor(r / 16)]
    c += hex1[math.floor((r/16 - math.floor(r/16))*16)]
    c += hex1[math.floor(g / 16)]
    c += hex1[math.floor((g / 16 - math.floor(g / 16)) * 16)]
    c += hex1[math.floor(b / 16)]
    c += hex1[math.floor((b/16 - math.floor(b/16))*16)]
    return print(c)


rgb(220,20,60)
