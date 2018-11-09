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
nf = 0   # noise factor: a factor multiplied by noise
noisesig = nf * np.random.random_sample(1001)


totalsig = cleansig + noisesig

#plt.plot(haxis, totalsig)



med = np.median (totalsig)
medarray = np.ones(1001) * med
#plt.plot(haxis, medarray)


totalsig2 = np.zeros(1001)

for i in range(len(haxis)):             # define a signal with only the values of totalsig above the median
    if totalsig[i] > med:
        totalsig2 [i] = totalsig[i]

#plt.plot(haxis, totalsig2, color='r')





counter = 0
SegNum = 10
M1 = np.zeros((SegNum,1001))
for i in range(len(haxis)):
    if totalsig2[i] != totalsig2[i-1]:
        if totalsig2[i] == 0:
            for m in range (0,i):
                M1[counter,m] = totalsig2[m]
            counter = counter+1
            for n in range (0,i):
                totalsig2[n] = min(totalsig2)        
        
print(M1)

#plt.plot(haxis, M1[3,:], color='r')

#### finding local maximums


MaxCo = np.zeros((2, 1001))

for i in range(len(haxis)):
        if totalsig[i] > ymax:
            ymax = totalsig[i]
            xmax = haxis [i]
    
    










#### find glonal max
#ymax = 0
#xmax = 0
#for i in range(len(haxis)):
#        if totalsig[i] > ymax:
#            ymax = totalsig[i]
#            xmax = haxis [i]
    
#print (xmax, ymax)

