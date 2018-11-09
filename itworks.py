import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

haxis = np.linspace(0,10*np.pi,1001)            # horizental axis array including 1001 points

# defining a few basic signals
sig1 = np.sin (haxis)
sig2 = np.cos (haxis*0.2)
sig3 = np.cos (haxis) 
sig4 = np.sin (haxis+0.2) 
sig5 = np.sin (haxis*0.1 + 0.1) 
sig6 = np.array(haxis**0.3 - haxis**0.2) 

# total signal as a sum of the basic signal, clean (no noise)
cleansig = sig1 + sig2 + sig3 + sig4 + sig5 + sig6         


#Adding NOISE
nf = 1.4   # noise factor to adjust noise strength
noisesig = nf * np.random.random_sample(1001)

totalsigi = cleansig + noisesig

plt.plot(haxis, totalsigi, linewidth = 0.3 , color='g')



#Removal of high frequency noise by using a filter
from scipy.signal import savgol_filter 
totalsig = savgol_filter(totalsigi, 1001, 18)           # the strength of filter can be adjusted with the last number
plt.plot(haxis, totalsig, linewidth = 0.7, color='k')  # high frequency noise removed


med = np.median (totalsig)
medarray = np.ones(1001) * med        # defining a signal whose value is equal to the median of the main signal everywhere
plt.plot(haxis, medarray)


totalsig2 = np.zeros(1001)
for i in range(len(haxis)):             # defining a signal with only the values of totalsig above the median: in effect, dividing the signal into zero and nonzero segments
    if totalsig[i] > med:
        totalsig2 [i] = totalsig[i]

#plt.plot(haxis, totalsig2, color='r')


#putting each segment of the signal between zeros segments into a separate row of a matrix
counter = 0      # to keep track of matrix row
SegNum = 100     # the number we assume for the amount of signal segments between zero segments
M1 = np.zeros((SegNum,1001))
for i in range(len(haxis)):
    if totalsig2[i] != totalsig2[i-1]:    #to discard the zero segments
        if totalsig2[i] == 0:
            for m in range (0,i):         # to transfer the values of the signal in a nonzero segment into a matrix row
                M1[counter,m] = totalsig2[m]  
            counter = counter+1          # to go to the next matrix row for the next nonzero segment
            for n in range (0,i):
                totalsig2[n] = min(totalsig2)        # change the values of the signal for the segment we just transferred to zero (not in the matrix) so that the next matrix row would have nonzero values only for the next nonzero signal segment
        

#plt.plot(haxis,M1[0,:])    # to check how each matrix row looks like


#### making two arrays with coordinates of maxima of each nonzero segment
lmx = np.zeros(SegNum)   #local maximum y coordinate
lmy = np.zeros(SegNum)   #local maximum y coordinate
for i in range(SegNum):
    if max(M1[i,:]) != 0:
        lmy [i] = max(M1[i,:])
        for b in range (1001):        # to find which column the maximum value belongs to 
            if M1[i,b] == max(M1[i,:]):
                lmx[i] = haxis[b]        # to keep track of the actual horizental value 
        
#discarding redundant rows with (0,0) coordinates by creating two new lists
xfin = [lmx[0]]
yfin = [lmy[0]]
for i in range (1,SegNum):
    if lmy[i] != 0:
        yfin.append(lmy[i])
        xfin.append(lmx[i])

plt.scatter(xfin, yfin, color='r')     # plotting the maxima

#displaying the coordinates of the maxima in matrix format
CoorMat = np.array([xfin,yfin])
print(CoorMat)    








