'''Time:        46     68     98     66
Distance:   358   1054   1807   1080'''
import math

times = [46, 68, 98, 66]
distances = [358, 1054, 1807, 1080]

def getOptions(time, distance):
    opts = []
    for i in range(0, time+1):
        dist = (time-i)*i
        if dist > distance:
            opts.append((i, dist))
    #print(opts)
    return len(opts)

a = getOptions(46, 358)
b = getOptions(68, 1054)
c = getOptions(98, 1807)
d = getOptions(66, 1080)

quadratic(1, 66, 1080)

a * b * c * d

a = getOptions(46689866, 358105418071080)

b = -46689866
c = 358105418071080

def quadratic(a,b,c):
    x1 = (-b + math.sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b - math.sqrt(b**2-(4*a*c)))/(2*a)
    print(x1, x2)
    print(abs(x1-x2))

quadratic(1, b, c)
a