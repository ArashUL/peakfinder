def peakfinder(NN, haxis,totalsigi,fs):
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy as sp

    #Removal of high frequency noise by using a filter
    from scipy.signal import savgol_filter 
    totalsig = savgol_filter(totalsigi, NN, fs)           # the strength of filter can be adjusted with the last number
    

    med = np.median (totalsig)
    medarray = np.ones(NN) * med        # defining a signal whose value is equal to the median of the main signal everywhere


    totalsig2 = np.zeros(NN)
    for i in range(len(haxis)):             # defining a signal with only the values of totalsig above the median: in effect, dividing the signal into zero and nonzero segments
        if totalsig[i] > med:
            totalsig2 [i] = totalsig[i]


    #putting each segment of the signal between zeros segments into a separate row of a matrix
    counter = 0      # to keep track of matrix row
    SegNum = 100     # the number we assume for the amount of signal segments between zero segments
    M1 = np.zeros((SegNum,NN))
    for i in range(len(haxis)):
        if totalsig2[i] != totalsig2[i-1]:    #to discard the zero segments
            if totalsig2[i] == 0:
                for m in range (0,i):         # to transfer the values of the signal in a nonzero segment into a matrix row
                    M1[counter,m] = totalsig2[m]  
                counter = counter+1          # to go to the next matrix row for the next nonzero segment
                for n in range (0,i):
                    totalsig2[n] = min(totalsig2)        # change the values of the signal for the segment we just transferred to zero (not in the matrix) so that the next matrix row would have nonzero values only for the next nonzero signal segment
        
    #### making two arrays with coordinates of maxima of each nonzero segment
    lmx = np.zeros(SegNum)   #local maximum y coordinate
    lmy = np.zeros(SegNum)   #local maximum y coordinate
    for i in range(SegNum):
        if max(M1[i,:]) != 0:
            lmy [i] = max(M1[i,:])
            for b in range (1001):        # to find which column the maximum value belongs to 
                if M1[i,b] == max(M1[i,:]):
                    lmx[i] = haxis[b]        # to keep track of the actual horizontal value 
        
    #discarding redundant rows with (0,0) coordinates by creating two new lists
    xfin = [lmx[0]]
    yfin = [lmy[0]]
    for i in range (1,SegNum):
        if lmy[i] != 0:
            yfin.append(lmy[i])
            xfin.append(lmx[i])

    #displaying the coordinates of the maxima in matrix format
    CoorMat = np.array([xfin,yfin])
    return [xfin]
    return [yfin]
    return [CoorMat]






