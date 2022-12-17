import math

class Beam:
    def __init__(self, length = 1.0, section = "10x20", material = "C18", q_load = 0.0):
        """This is beam element class.
        Section defined as bxh in cm, b-width, h-height
        """
        self.length = length
        self.section = section
        self.material = material
        self.qload = q_load
        self.section_properties()
    
    def get_section_dim(self):
        bxh = self.section.split('x')
        b = float(bxh[0])*10 # mm
        h = float(bxh[1])*10 # mm
        return b, h

    def section_properties(self):
        b, h = self.get_section_dim()
        self.A = b*h
        self.Iy = (b*(h**3))/12 # mm4
        self.Iz = (h*(b**3))/12 # mm4
        self.Wz = (h*(b**2))/6 # mm3
        self.Wy = (b*(h**2))/6 # mm3
        self.iy = math.sqrt(self.Iy/self.A) # mm
        self.iz = math.sqrt(self.Iz/self.A) # mm



