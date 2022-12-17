from beam import Beam
from csvreader import CsvReader

#defining geometry and material
beam = Beam()
beam.length = 3.0 # m
beam.section = "10x22" # cm x cm
beam.material = "C24" 

#material properties depending on timber class
csvreader = CsvReader(path="data\wood_classes.csv")
E = csvreader.get_key_value(key_value=beam.material, prop_name="E_0mean")



#defining load
dead_q_load = 4.15
