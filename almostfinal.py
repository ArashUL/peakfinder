import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
haxis = np.linspace(0,10*np.pi,1001)            # horizental axis array

sig1 = np.sin (haxis)
sig2 = np.sin (haxis*0.2)
sig3 = np.cos (haxis)
sig4 = np.sin (haxis+0.2)
sig5 = np.sin (haxis*0.1 + 0.1)

cleansig = sig1 + sig2 + sig3 + sig4 + sig5           # data signal as a sum of a few other simple signals


#Adding NOISE
nf = 0.2   # noise factor: a factor multiplied by noise
noisesig = nf * np.random.random_sample(1001)

totalsig = cleansig + noisesig

plt.plot(haxis, totalsig, color='b')




med = np.median (totalsig)
medarray = np.ones(1001) * med        # defining a signal whose value is equal to the median of the main signal everywhere
plt.plot(haxis, medarray)


totalsig2 = np.zeros(1001)
for i in range(len(haxis)):             # define a signal with only the values of totalsig above the median
    if totalsig[i] > med:
        totalsig2 [i] = totalsig[i]

#plt.plot(haxis, totalsig2, color='r')


#getting rid of noise : any data point which is less than 1% of global maximum value will be eliminated
for i in range(len(haxis)):             
    if (totalsig2[i]-med) < 0.05 * (max(totalsig2)-med):
        totalsig2 [i] = 0



counter = 0
SegNum = 100
M1 = np.zeros((SegNum,1001))
for i in range(len(haxis)):
    if totalsig2[i] != totalsig2[i-1]:
        if totalsig2[i] == 0:
            for m in range (0,i):
                M1[counter,m] = totalsig2[m]
            counter = counter+1
            for n in range (0,i):
                totalsig2[n] = min(totalsig2)        
        

#plt.plot(haxis,M1[0,:])

#### finding local maximums
lmx = np.zeros(SegNum)
lmy = np.zeros(SegNum)

for i in range(SegNum):
    if max(M1[i,:]) != 0:
        lmy [i] = max(M1[i,:])
        for b in range (1001):
            if M1[i,b] == max(M1[i,:]):
                lmx[i] = haxis[b]
        

ymod = [lmy[0]]
xmod = [lmx[0]]
for i in range (1,SegNum):
    if lmy[i] != 0:
        ymod.append(lmy[i])
        xmod.append(lmx[i])
        
plt.scatter(xmod, ymod, color='r')

CoorMat = np.array([xmod,ymod])
print(CoorMat)    








