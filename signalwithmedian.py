import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
haxis = np.linspace(0,10*np.pi,1001)            # horizental axis array

sig1 = np.sin (haxis)
sig2 = np.sin (haxis*0.2)
sig3 = np.cos (haxis)
sig4 = np.sin (haxis+0.2)
sig5 = np.sin (haxis*0.1 + 0.1)

cleansig = sig1 + sig2 + sig3 + sig4 + sig5            # data signal as a sum of a few other simple signals


#NOISE
nf = 0    # noise factor: a factor multiplied by noise
noisesig = nf * np.random.random_sample(1001)


totalsig = cleansig + noisesig

plt.plot(haxis, totalsig)



med = np.median (totalsig)
medarray = np.ones(1001) * med
plt.plot(haxis, medarray)







