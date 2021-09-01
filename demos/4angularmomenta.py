from vectors import PrecessVector, CoupledVector, make_axes, LtoLet
from vpython import *

lc = 1.0
lo = 2.0
sc = 0.5
so = 0.5
J = 2.0
mJ = 0.0

L = 2.0
S = 1.0
scene = canvas(title='LS Coupling', width=600, height=600)
scene.caption= f"""Four angular momenta with LS coupling.
lc and lo are coupled first, and then sc and so. Then L and S are coupled.
lc={lc}, lo={lo}, sc={sc}, so={so}, L={L}, S={S}, J={J}, m={mJ}
The associated term symbol is {int(2*S+1)}{LtoLet(L)}_{J} m={mJ}"""
scene.center = vec(0, 1, 0)
make_axes(2)

vlc = PrecessVector(lc)
vlo = PrecessVector(lo)
vlc.jarrow.color = vec(0, 0.5, 0)
vlo.jarrow.color = vec(0, 0.5, 0)
vL = CoupledVector(vlc, vlo, L)
vL.jarrow.color = color.green

vsc = PrecessVector(sc)
vso = PrecessVector(so)
vsc.jarrow.color = vec(0, 0, 0.5)
vso.jarrow.color = vec(0, 0, 0.5)
vS = CoupledVector(vsc, vso, S)
vS.jarrow.color = color.blue
vJ = CoupledVector(vL, vS, J, mJ)

# attach_trail(v2.jarrow, color=color.cyan, type="curve", radius=0.01)

jc = 1.5
jo = 1.5
scene2 = canvas(title='JJ Coupling', width=600, height=600)
scene2.caption = f"""Four coupled angular momenta with JJ coupling. 
lc and sc are coupled together, as are lo and jo. Then jc and jo are coupled
lc={lc}, lo={lo}, sc={sc}, so={so}, jc={jc}, jo={jo}, J={J}, m={mJ}
The associated term symbol is ({jc}, {jo})_{J} m={mJ}"""
scene2.center = vec(0, 1, 0)
make_axes(2)

wlc = PrecessVector(lc)
wsc = PrecessVector(sc)
wlo = PrecessVector(lo)
wso = PrecessVector(so)
wlc.jarrow.color = vec(0, 0.5, 0)
wlo.jarrow.color = vec(0, 0.5, 0)
wsc.jarrow.color = vec(0, 0, 0.5)
wso.jarrow.color = vec(0, 0, 0.5)
wjc = CoupledVector(wlc, wsc, jc)
wjo = CoupledVector(wlo, wso, jo)
wjc.jarrow.color = color.cyan
wjo.jarrow.color = color.cyan
wJ = CoupledVector(wjc, wjo, J, mJ)

K = 1.5
scene3 = canvas(title='JK Coupling', width=600, height=600)
scene3.caption = f"""Four coupled angular momenta with JK coupling. 
lc and sc are coupled together, then lo is coupled in, and then so
lc={lc}, lo={lo}, sc={sc}, so={so}, jc={jc}, K={K}, J={J}, m={mJ}
The associated term symbol is {int(2*S+1)}[{K}]_{J} m={mJ}"""
scene3.center = vec(0, 1, 0)
make_axes(2)

xlc = PrecessVector(lc)
xsc = PrecessVector(sc)
xlo = PrecessVector(lo)
xso = PrecessVector(so)
xlc.jarrow.color = vec(0, 0.5, 0)
xlo.jarrow.color = vec(0, 0.5, 0)
xsc.jarrow.color = vec(0, 0, 0.5)
xso.jarrow.color = vec(0, 0, 0.5)
xjc = CoupledVector(xlc, xsc, jc)
xK = CoupledVector(xjc, xlo, K)
xjc.jarrow.color = color.cyan
xK.jarrow.color = vec(0, 1, 0.5)
xJ = CoupledVector(xK, xso, J, mJ)

dt = 0.01
while True:
    rate(100)
    vJ.rotate(vJ.omega * dt)
    vJ.twist(dt)

    wJ.rotate(wJ.omega * dt)
    wJ.twist(dt)

    xJ.rotate(xJ.omega * dt)
    xJ.twist(dt)