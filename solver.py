import matplotlib.pyplot as plt
import numpy as np
ROUNDING = 3

class Solver:
    def __init__(self, beam):
        self.beam = beam
        self.l = self.beam.length  # m
        self.q = self.beam.qload  # kN/m
        self.E = self.beam.E * 10**6  #kN/m2
        self.Iy = self.beam.Iy # m4
        pass

    def calc_moment(self):
        """
        Calculates bending moment.
        Returns:
        --------
        float
            bending moment value in kNm
        """
        M = (self.q*self.l**2)/8
        return round(M, ROUNDING)

    def calc_shear(self):
        """
        Calculates shear force.
        Returns:
        --------
        float
            shear force value in kN
        """
        V = self.q*self.l/2
        return round(V, ROUNDING)

    def plot_beam(self):
        """Plots beam with supports"""
        beam_color = 'black'
        plt.plot(0,0, marker = 6, markersize = 17, mfc = beam_color, mec = beam_color)
        plt.plot(self.l,0, marker = 6, markersize = 17, mfc = beam_color, mec = beam_color)
        plt.hlines(y=0, xmin=0, xmax=self.l, colors= beam_color)

    def plot_moment(self):
        """Plots bending moment"""
        step = 0.1
        x = np.arange(0,self.l+step,step)
        Ra = self.q*self.l/2
        Mx = (Ra*x - self.q*x**2/2)*-1
        self.plot_beam()
        plt.plot(x,Mx, color='blue')
        plt.xlim(-3,self.l+3)
        max_y = min(Mx)
        plt.annotate(text=str(max_y), xy=(self.l/2,max_y))
        plt.xlabel('L [m]')
        plt.ylabel('M [kNm]')
        plt.title('Moment zginajacy My')
        plt.axis('off')
        plt.savefig('Raport\\Figures\My.png')

    def plot_shear(self):
        pass

    def calc_deflection(self):
        """
        Calculates deflection.
        Returns:
        float
            value of deflection in mm
        """
        u = ((5/384)*((self.q*(self.l**4)) / (self.E*self.Iy)))*1000  #mm
        return round(u, ROUNDING)

    def plot_deflection(self):
        """Plots deflection"""
        step = 0.1
        x = np.arange(0, self.l+step, step)
        uz = (1/(self.E*self.Iy) * (((self.q*(x**4))/24) - (self.q*self.l*(x**3))/12 + ((self.q*(self.l**3)*x))/24))*-1         
        self.plot_beam()
        plt.plot(x, uz, color='blue')
        plt.xlim(-3, self.l+3)
        plt.show()
    