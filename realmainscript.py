### NN, fs, haxis and totalsigi are the four parameters for peakfinderfuction, haxis and totalsigi are the input signal axis values and can be imported as data signal instead of defining them as below
##

NN = 1001                                     #number of data points
haxis = np.linspace(0,10*np.pi,NN)            # horizontal axis array including 1001 points
fs = 18                                       # filter parameter to adjust, see filter description in the function

## defining the signal values
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
noisesig = nf * np.random.random_sample(NN)
totalsigi = cleansig + noisesig



# the script
import peakfinderfunction.py as pff
pff.peakfinder(NN, haxis,totalsigi,fs)

plt.scatter(xfin, yfin, color='r')     # plotting the maxima
plt.plot(haxis, totalsigi, linewidth = 0.3 , color='g')
print(CoorMat)