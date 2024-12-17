from time import sleep
from datetime import datetime
def all_info_from_trackf(path):
    satel = open(path, "r", encoding='utf-8')
    coors = [line.strip() for line in satel.readlines()][6:]
    coors = [coors[i].split() for i in range(len(coors))]
    return coors
coordinates = [0, 0]
satel = all_info_from_trackf("C:\\Users\\User\\Desktop\\Shim\\python\\TrackF.txt")
steps = 800 * 50
angle = [0, 0]
now = datetime.now().time()
satel[0][1], satel[0][2] = float(satel[0][1]), float(satel[0][2])
if satel[0][1] > 180:
    angle[0] = float(format(-(360 - satel[0][1]), ".6f"))
else:
    angle[0] = float(format(satel[0][1], ".6f"))
angle[1] = float(format(90 - satel[0][2], "6f"))
angle[0] = round(float(format(steps * angle[0] / 360, '.6f'))) - coordinates[0]
angle[1] = round(float(format(steps * angle[1] / 360, '.6f'))) - coordinates[1]
print(*angle, abs(angle[0]), abs(angle[1]))
coordinates[0] += angle[0]
coordinates[1] += angle[1]
for i in satel:
    while i[0] > str(now):
        now = datetime.now().time()
    i[1], i[2] = float(i[1]), float(i[2])
    if i[1] > 180:
        angle[0] = float(format(-(360 - i[1]), ".6f"))
    else:
        angle[0] = float(format(i[1], ".6f"))
    angle[1] = float(format(90 - i[2], "6f"))
    angle[0] = round(float(format(steps * angle[0] / 360, '.6f'))) - coordinates[0]
    angle[1] = round(float(format(steps * angle[1] / 360, '.6f'))) - coordinates[1]
    print(*angle, abs(angle[0]), abs(angle[1]))
    coordinates[0] += angle[0]
    coordinates[1] += angle[1]
    #sleep(0.98)
print(*coordinates, abs(coordinates[0]), abs(coordinates[1]))