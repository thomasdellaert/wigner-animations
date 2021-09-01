from vectors import PrecessVector, CoupledVector, make_axes
from vpython import *

j1 = 0.5
m1 = 0.5
j2 = 1.0
m2 = 1.0
j3 = 1.0
m3 = 0.0
j12 = 1.5
m12 = 0.5
j23 = 2.0
m23 = 1.0
j = 1.5
m = 1.5

scene = canvas(title='Three coupled angular momenta', width=600, height=600)
scene.caption= f"""Three coupled angular momenta, coupled the first way. 
j1={j1}, j2={j2}, j12={j12}, j3={j3}, j={j}, m={m}"""
scene.center = vec(0, 1, 0)
make_axes(2)

v1 = PrecessVector(j1, m1)
v2 = PrecessVector(j2, m2)
v3 = PrecessVector(j3, m3)
v12 = CoupledVector(v1, v2, j12, m12)
v12.jarrow.color = color.green
v123 = CoupledVector(v12, v3, j, m)

# attach_trail(v2.jarrow, color=color.cyan, type="curve", radius=0.01)

scene2 = canvas(width=600, height=600)
scene2.caption = f"""Three coupled angular momenta, coupled the second way. 
j1={j1}, j2={j2}, j3={j3}, j23={j23}, j={j}, m={m}"""
scene2.center = vec(0, 1, 0)
make_axes(2)

v1_2 = PrecessVector(j1, m1)
v2_2 = PrecessVector(j2, m2)
v3_2 = PrecessVector(j3, m3)
v23_2 = CoupledVector(v2_2, v3_2, j23, m23)
v23_2.jarrow.color = color.blue
v123_2 = CoupledVector(v1_2, v23_2, j, m)

dt = 0.01
while True:
    rate(100)
    v123.rotate(v123.omega * dt)
    v123.twist(dt)

    v123_2.rotate(v123_2.omega * dt)
    v123_2.twist(dt)