import matplotlib.pyplot as plt
import statistics
import numpy as np

def estimate_mean(n, delta):
    fd=open("data.txt")
    frequency=int(fd.readline())
    lowbon=float(fd.readline())
    upbon=float(fd.readline())
    amount=frequency//n
    array=[]
    meanarray=[]
    for i in range(frequency):
        number=float(fd.readline())
        array.insert(i,number)
    fd.close()

    sampledict={}
    for k in range(amount):
        sampledict[k]=array[(3*k):(3*k+3)]

    bin_pmf_dict={}
    for i in range(amount):
        bin_pmf_dict[i]=statistics.mean(sampledict[i])

    bin=(upbon-lowbon)/delta


    bins=[]
    pointer=0
    for i in range(bin):
        for j in range(len(bin_pmf_dict)):
            if ((bin_pmf_dict[j]>=pointer)&(bin_pmf_dict<pointer+delta)):
                bins[i]=bins[i]+1

plt.plot([],[])
plt.xlabel('Probability')
plt.ylabel('Sampling Mean')
plt.show()