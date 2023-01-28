import math
from csvreader import CsvReader

class Beam:
    def __init__(self, length = 1.0,
                 section = "", material = "", q_load = 0.0):
        """This is beam element class.
        Section defined as bxh in cm, b-width, h-height
        """
        self.length = length
        self.section = section
        self.material = material
        self.qload = q_load
        self.__get_sec_material()
        self.__section_properties()
    
    def __get_sec_material(self):
        csvreader = CsvReader(path="data\wood_classes.csv")
        self.E = float(csvreader.get_key_value(
            key_value=self.material, prop_name="E_0mean"))
            
    def __get_section_dim(self):
        bxh = self.section.split('x')
        b = float(bxh[0])/100  # m
        h = float(bxh[1])/100  # m
        return b, h

    def __section_properties(self):
        b, h = self.__get_section_dim()
        self.A = b*h
        self.Iy = (b*(h**3))/12  # m4
        self.Iz = (h*(b**3))/12  # m4
        self.Wz = (h*(b**2))/6  # m3
        self.Wy = (b*(h**2))/6  # m3
        self.iy = math.sqrt(self.Iy/self.A)  # m
        self.iz = math.sqrt(self.Iz/self.A)  # m



