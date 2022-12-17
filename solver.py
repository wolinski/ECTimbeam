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
    def plot_moment(self):
        l = self.beam.length
        q = self.beam.qload
        step = 0.1
        x = np.arange(0,l+step,step)
        Ra = q*l/2
        Mx = (Ra*x - q*x**2/2)*-1
        # target is to split plot beam into different function
        beam_color = 'black'
        plt.plot(0,0, marker = 6, markersize = 17, mfc = beam_color, mec = beam_color)
        plt.plot(l,0, marker = 6, markersize = 17, mfc = beam_color, mec = beam_color)
        plt.hlines(y=0, xmin=0, xmax=l, colors= beam_color)
        plt.plot(x,Mx, color='blue')
        plt.xlim(-3,l+3)
        max_y = min(Mx)
        print(max_y)
        plt.annotate(text=str(max_y), xy=(l/2,max_y))
        plt.xlabel('L [m]')
        plt.ylabel('M [kNm]')
        plt.title('Moment zginajacy My')
        #plt.show()
        plt.axis('off')
        plt.savefig('Raport\\Figures\My.png')
    