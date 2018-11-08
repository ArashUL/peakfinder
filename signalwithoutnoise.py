# A Total Signal defined as a sum of a few other signals and plotted, without noise 
###
haxis is the array containing the values for the  horizantal axis
totalsig is the total signal made up of sig signals
###

import numpy as np
import matplotlib.pyplot as plt

haxis = np.linspace(0,10*np.pi,1001)    

sig1 = np.sin (haxis)
sig2 = np.sin (haxis*0.2)
sig3 = np.cos (haxis)
sig4 = np.sin (haxis+0.2)
sig5 = np.sin (haxis*0.1 + 0.1)

totalsig = sig1 + sig2 + sig3 + sig4 + sig5

plt.plot(haxis, totalsig)

