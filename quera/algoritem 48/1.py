x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())
ziba = 0
if (x1 == (x3 or x4)) or (y1 == (y3 or y4)):
    ziba += 1
else:
    ziba += 0

if (x2 == (x3 or x4)) or (y2 == (x3 or y4)):
    ziba += 1
else:
    ziba += 0

if ziba == 1:
    print("happy")
else:
    print("unhappy")
