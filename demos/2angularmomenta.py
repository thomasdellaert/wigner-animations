from vectors import PrecessVector, CoupledVector, make_axes
from vpython import *

j1 = 0.5
m1 = 0.5
j2 = 1.0
m2 = 1.0
j = 1.5
m = 1.5

scene = canvas(title='Two coupled angular momenta', width=600, height=600)
scene.caption= """Two coupled angular momenta. Note that their projection onto the 
z-axis is not constant, but the total length of the J vector is constant"""
scene.center = vec(0, 1, 0)
make_axes(2)

v1 = PrecessVector(j1, m1)
v2 = PrecessVector(j2, m2)
v12 = CoupledVector(v1, v2, j, m)
v12.jarrow.color = color.magenta

# attach_trail(v2.jarrow, color=color.cyan, type="curve", radius=0.01)

scene2 = canvas(title='Two uncoupled angular momenta', width=600, height=600)
scene2.caption = """Two uncoupled angular momenta. Note that their projections remain 
constant, but the length of the resultant vector changes"""
scene2.center = vec(0, 1, 0)
make_axes(2)

v1_2 = PrecessVector(j1, m1)
v2_2 = PrecessVector(j2, m2)
v12_2 = arrow(pos=v1_2.pos, axis=v1_2.axis+v2_2.axis, round=True, shaftwidth=0.05)

dt = 0.01
while True:
    rate(100)
    v12.rotate(v12.omega * dt)
    v12.twist(dt)

    v1_2.rotate(v1_2.omega * dt)
    v2_2.pos = v1_2.axis
    v2_2.rotate(v2_2.omega * dt)
    v12_2.axis = v1_2.axis+v2_2.axis

    c = (v12_2.axis.mag - v1_2.m - v2_2.m) / (v1_2.jl + v2_2.jl - v1_2.m - v2_2.m)
    v12_2.color = vec(1, c, 1)
