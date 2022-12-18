from beam import Beam
from csvreader import CsvReader
from solver import Solver
# defining geometry and material
beam = Beam()
beam.length = 3.0 # m
beam.section = "10x22" # cm x cm
beam.material = "C24" 

# material properties depending on timber class


# defining load
dead_q_load = 4.00 # kN/m
live_q_load = 2.00 # kN/m
beam.qload = dead_q_load + live_q_load

# calculating internal forces

solver = Solver(beam)

#print(solver.calc_moment())
#print(solver.calc_shear())

#solver.plot_moment()
solver.plot_deflection()