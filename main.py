from beam import Beam
from anastruct import SystemElements
from anastruct.fem import node
from anastruct.vertex import Vertex
from matplotlib.pyplot import plot
import numpy as np
import matplotlib.pyplot as plt


#defining geometry and material
beam = Beam()
beam.length = 3.0 # m
beam.section = "10x22" # cm x cm
beam.material = "C24" 

#modulus needs to be readed from file depending on timber class
#E=

#definition of fem geometry
p1 = Vertex (0,0)
p2 = Vertex (beam.length,0)

#creating beam element
ss = SystemElements(EA=E*A,EI=E*I) 
ss.add_element(location=[p1,p2], g=cw)

#defining load
dead_q_load = 4.15
