import numpy as np
import matplotlib.pyplot as plt

F = np.loadtxt('DNA-1D-PMF-chi.dat')

F1 = np.loadtxt('RNA-1D-PMF-chi.dat')

plt.plot(F[:,0], F[:,1],'b-',lw=4, label='A6-DNA')
plt.plot(F1[:,0], F1[:,1], 'r-', lw=4, label='A6-RNA')
plt.title('PMF along $\chi$',fontsize=18)
plt.xlabel("$\chi (\circ)$",fontsize=18)
plt.ylabel("PMF (kcal/mol)",fontsize=18)
plt.xticks([-180,-90,0,90,180])
plt.xlim(-180,180)
plt.tick_params(labelsize=18)
#plt.legend(fontsize=18)
plt.tight_layout()  
#plt.show()
plt.savefig('1d-compare-chi.pdf')
