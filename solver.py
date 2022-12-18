import matplotlib.pyplot as plt
import numpy as np

class Solver:
    def __init__(self, beam):
        self.beam = beam
        pass

    def calc_moment(self):
        l = self.beam.length
        q = self.beam.qload
        M = (q*l**2)/8
        return M

    def calc_shear(self):
        l = self.beam.length
        q = self.beam.qload
        V = q*l/2
        return V

    def plot_beam(self):
        l = self.beam.length
        beam_color = 'black'
        plt.plot(0,0, marker = 6, markersize = 17, mfc = beam_color, mec = beam_color)
        plt.plot(l,0, marker = 6, markersize = 17, mfc = beam_color, mec = beam_color)
        plt.hlines(y=0, xmin=0, xmax=l, colors= beam_color)

    def plot_moment(self):
        l = self.beam.length
        q = self.beam.qload
        step = 0.1
        x = np.arange(0,l+step,step)
        Ra = q*l/2
        Mx = (Ra*x - q*x**2/2)*-1
        self.plot_beam()
        plt.plot(x,Mx, color='blue')
        plt.xlim(-3,l+3)
        max_y = min(Mx)
        plt.annotate(text=str(max_y), xy=(l/2,max_y))
        plt.xlabel('L [m]')
        plt.ylabel('M [kNm]')
        plt.title('Moment zginajacy My')
        plt.axis('off')
        plt.savefig('Raport\\Figures\My.png')

    def plot_shear(self):
        pass

    def calc_deflection(self):
        l = self.beam.length
        q = self.beam.qload
        E = self.beam.E
        Iy = self.beam.Iy
        u = (5/384)*(q*l**4 / E*Iy)
        return u

    def plot_deflection(self):
        l = self.beam.length
        q = self.beam.qload
        E = self.beam.E
        Iy = self.beam.Iy
        step = 0.1
        x = np.arange(0,l+step,step)
        uz = (1/E*Iy * ((q*x**4/24) - (q*l*x**3)/12 + (q*l**3*x)/24 ))*-1         
        self.plot_beam()
        plt.plot(x,uz, color='blue')
        plt.xlim(-3,l+3)
        plt.show()
    