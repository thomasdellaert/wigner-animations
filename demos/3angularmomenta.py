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
v1.jarrow.color = color.red
v2 = PrecessVector(j2, m2)
v2.jarrow.color = color.green
v3 = PrecessVector(j3, m3)
v3.jarrow.color = color.blue
v12 = CoupledVector(v1, v2, j12, m12)
v12.jarrow.color = color.yellow
v123 = CoupledVector(v12, v3, j, m)
v123.jarrow.color = color.white

# attach_trail(v2.jarrow, color=color.cyan, type="curve", radius=0.01)

scene2 = canvas(width=600, height=600)
scene2.caption = f"""Three coupled angular momenta, coupled the second way. 
j1={j1}, j2={j2}, j3={j3}, j23={j23}, j={j}, m={m}"""
scene2.center = vec(0, 1, 0)
make_axes(2)

w1 = PrecessVector(j1, m1)
w1.jarrow.color = color.red
w2 = PrecessVector(j2, m2)
w2.jarrow.color = color.green
w3 = PrecessVector(j3, m3)
w3.jarrow.color = color.blue
w23 = CoupledVector(w2, w3, j23, m23)
w23.jarrow.color = color.cyan
w123 = CoupledVector(w1, w23, j, m)
w123.jarrow.color = color.white

dt = 0.01
while True:
    rate(100)
    v123.rotate(v123.omega * dt)
    v123.twist(dt)

    w123.rotate(w123.omega * dt)
    w123.twist(dt)