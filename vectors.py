from vpython import *

class PrecessVector:
    def __init__(self, j, m=0.5):
        self.j = j

        self.jl = (j * (j + 1))**0.5
        self.jarrow = arrow(pos=vec(0., 0., 0.,), axis=vec((self.jl**2 - m**2)**0.5, m, 0.0),
                            round=True, shaftwidth=0.05, color=color.white)
        self.omega = self.jl

    @property
    def pos(self):
        return self.jarrow.pos

    @pos.setter
    def pos(self, value):
        self.jarrow.pos = value

    @property
    def axis(self):
        return self.jarrow.axis

    @axis.setter
    def axis(self, value):
        self.jarrow.axis = value

    def rotate(self, angle, axis=None, origin=None):
        if origin is None: origin = self.pos
        if axis is None: axis = vec(0., 1., 0.)
        self.jarrow.rotate(angle, axis=axis, origin=origin)

    def twist(self, dt):
        pass

class CoupledVector(PrecessVector):
    def __init__(self, v1, v2, j, m=0.0):
        super().__init__(j, m)
        self.jarrow.color = color.red

        self.v1 = v1
        self.v2 = v2

        self.pos=vec(0., 0., 0.)
        self.axis = self.jarrow.axis

    @property
    def pos(self):
        return self.jarrow.pos

    @pos.setter
    def pos(self, value):
        self.jarrow.pos = value
        self.v1.pos = value
        self.v2.pos = value + self.v1.axis

    @property
    def axis(self):
        return self.jarrow.axis

    @axis.setter
    def axis(self, value):
        self.jarrow.axis = value

        self.v1.pos = self.pos
        self.v1.axis = self.jarrow.axis.hat * self.v1.jl
        j1angle = acos((self.jl**2 + self.v1.jl**2 - self.v2.jl**2) / (2 * self.jl * self.v1.jl))
        self.v1.rotate(j1angle, axis=vec(0., 0., 1.), origin=self.pos)

        self.v2.pos = self.pos + self.v1.axis
        self.v2.axis = self.axis - self.v1.axis

    def rotate(self, angle, axis=None, origin=None):
        if origin is None: origin=vec(0.,0.,0.,)
        if axis is None: axis=vec(0.,1.,0.)
        self.v1.rotate(angle, axis=axis, origin=origin)
        self.v2.rotate(angle, axis=axis, origin=origin)
        self.jarrow.rotate(angle, axis=axis, origin=origin)

    def twist(self, dt):
        avg_omega = (self.v1.omega+self.v2.omega)/2.0
        self.v1.rotate(dt * avg_omega, axis=self.axis, origin=self.pos)
        self.v2.rotate(dt * avg_omega, axis=self.axis, origin=self.pos)
        self.v1.twist(dt)
        self.v2.twist(dt)

def make_axes(height):
    cylinder(pos=vec(0, 0, 0), axis=vec(0, height, 0), radius=0.03, color=color.yellow, opacity=0.5)
    cylinder(pos=vec(0, 0, 0), axis=vec(0, 0.01, 0), radius=height/2, color=color.yellow, opacity=0.5)

def LtoLet(l):
    l = int(l)
    return "SPDFGHKLMNOQRTUVWXY"[l]

if __name__ == "__main__":
    scene.width = scene.height = 800
    make_axes()

    v1 = PrecessVector(0.5, 0.5)
    v2 = PrecessVector(1.0, 1.0)
    v12 = CoupledVector(v1, v2, 1.5, 1.5)
    v3 = PrecessVector(2.0, 0.0)
    v123 = CoupledVector(v3, v12, 2.5, 2.5)
    v12.jarrow.color = color.green
    dt = 0.01
    attach_trail(v12.jarrow, color=color.cyan, type="curve", radius=0.01)

    while True:
        rate(100)
        v123.rotate(v123.omega * dt)
        v123.twist(dt)
