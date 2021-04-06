import math
from fastecdsa.curve import Curve
from fastecdsa.point import Point
import labmath


qx=  0xa3907079bb6c33bbbe9478e8c6d1e5812563b5d8e13d754d6c74fdedbd9456c8
qy = 0x8c5b704a4453ba857d37b0b40ada22763e1d54148c31194c7b52260766df3a61

xx = 0xa3907079bb6c33bbbe9478e8c6d1e5812563b5d8e13d754d6c74fdedbd9456c8
yy = 0x8c5b704a4453ba857d37b0b40ada22763e1d54148c31194c7b52260766df3a61
msb_of_r1 = '0x49bfb7c67d0d1c7a0b1151d56d3a9c4a8d7550b15e0cd4265ad7bfaa3549'
lsb_of_r2 = '0x7078'

p=0xc57d3e540e595f1304bf81dcdc471a1e4b8614472c5820f951f483c04d0c3d79

a = -3
b =88217653075733538010802362020423294317799277142495418239747303142947508953346
curv = Curve('curva', p, a, b, None, xx, yy)
curve = curv.G
 # 3179547229186215041788349730328093574817817367684014147655936757452044075920

distance = pow(7, 64, p)

ys = []
xs = []


for i in range(0x10000):
    s = msb_of_r1 + str(hex(i))[2:]
    y_squared = curv.evaluate(int(s,16))
    y = labmath.sqrtmod_prime(y_squared, p)
    point = (int(s,16), y)
    if curv.is_point_on_curve(point):
        point = Point(int(s,16), y, curve=curv)
        hx = point*distance
        q = Point(qx,qy, curve=curv)
        l = hx.x
        m = hex((l*q).x)
        #print(m[:6])
        if m[:6] == lsb_of_r2:
            print(l)
            print(m)
        

print(len(xs))
    

