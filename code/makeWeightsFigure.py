# Cross Domain Fairness
# Michele Albach
# This file makes Figure 1

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv

file = open("../results/MainAccuraciesAndWeights.csv")
secdata = list(csv.reader(file))
file.close()
file = open("../results/ReplacedAccuraciesAndWeights.csv")
accdata = list(csv.reader(file))
file.close()
file = open("../results/RemovedAccuraciesAndWeights.csv")
nordata = list(csv.reader(file))
file.close()

# Figure labels
props = [["Relevance","Causes\nOutcome","Reliability","Causes\nDisparity","Caused\nBy Group","Causes\nCycle","Volitionality","Privacy"],["Increases\nAccuracy","Causes\nOutcome","Reliability","Causes\nDisparity","Caused\nBy Group","Causes\nCycle","Volitionality","Privacy"],["","Causes\nOutcome","Reliability","Causes\nDisparity","Caused\nBy Group","Causes\nCycle","Volitionality","Privacy"]]
batches = ["Relevance","Replaced (with Increases Accuracy)","Removed"]
second = [[],[],[],[],[],[],[],[]]
accuracy = [[],[],[],[],[],[],[],[]]
norel = [[],[],[],[],[],[],[],[]]

# Reorder p-values to be correct property order
def ro(ps):
    newps = []
    for i in [1,4,0,6,7,5,3,2]:
        newps.append(ps[i])
    return newps

# p-values obtained separately using statsmodels since sklearn does not provide a simple way to do so, and then bonferonni corrected by multiplying by the number of tests done
secrec = [0.0067, 10.5551, 0.0, 41.5965, 84.4832, 0.0001, 61.3715, 125.0368, 5.4949]
secunem = [0.007, 0.1558, 0.0, 62.1044, 138.4647, 3.5108, 123.7587, 48.1734, 128.0963]
seccps = [0.099, 9.7535, 0.0, 137.6998, 29.9637, 3.3741, 43.3066, 0.3957, 123.2693]
sechos = [89.0791, 10.0866, 0.0, 58.0173, 72.5076, 0.0004, 33.7425, 2.1981, 114.4793]
secloan = [121.2059, 79.2299, 0.0, 127.3354, 115.5545, 0.7609, 21.2221, 0.1883, 41.9311]
secins = [0.0, 8.1424, 0.0, 43.7872, 87.5388, 1.6696, 5.8313, 60.9281, 102.2031]
accrec = [0.1501, 16.3887, 0.0, 18.7781, 13.5015, 0.0125, 17.6236, 49.6019, 45.8476]
accunem = [21.7998, 49.5749, 0.0, 9.8477, 0.0039, 0.5827, 6.6362, 3.0219, 127.9073]
acccps = [1.1084, 88.5077, 0.0, 43.7485, 7.3643, 0.1677, 130.5307, 21.9615, 20.5863]
acchos = [69.4909, 138.1862, 0.0, 51.1617, 59.0063, 0.0, 39.1324, 0.0001, 17.5444]
accloan = [0.0129, 38.7748, 0.0, 57.1698, 111.0975, 0.0, 26.2205, 4.4539, 105.8185]
accins = [0.2099, 68.2103, 0.0, 13.1474, 2.4539, 0.0, 6.3059, 10.0552, 12.8978]
norrec = [38.1261, 0.0, 1, 40.3754, 1.8753, 0.0, 141.8555, 0.3709, 42.2879]
norunem = [33.6333, 0.0, 1, 97.0878, 0.0, 0.0, 43.6977, 0.0002, 11.6343]
norcps = [0.1553, 0.0, 1, 99.9547, 0.0001, 0.0, 42.1805, 2.8329, 102.6971]
norhos = [80.6355, 0.0, 1, 17.4725, 119.7931, 0.0, 62.8929, 0.0076, 6.6014]
norloan = [4.8617, 0.0011, 1, 99.7036, 16.4826, 0.0, 134.1411, 0.2008, 126.7606]
norins = [6.0369, 0.2243, 1, 20.2084, 37.6668, 0.0, 121.7505, 10.87, 93.9553]

# correctly reorder p-values
pvalues = [ro(secrec[1:])+ro(seccps[1:])+ro(sechos[1:])+ro(secins[1:])+ro(secloan[1:])+ro(secunem[1:]),ro(accrec[1:])+ro(acccps[1:])+ro(acchos[1:])+ro(accins[1:])+ro(accloan[1:])+ro(accunem[1:]),ro(norrec[1:])+ro(norcps[1:])+ro(norhos[1:])+ro(norins[1:])+ro(norloan[1:])+ro(norunem[1:])]

for i in range(2,8): # All domains
    ind = 0
    for j in [4,7,3,9,10,8,6,5]: # All properties reordered
        second[ind].append(float(secdata[i][j]))
        accuracy[ind].append(float(accdata[i][j]))
        # need to skip relevance for removed data
        if j==4:
            norel[ind].append(0)
        elif j==3:
            norel[ind].append(float(nordata[i][j]))
        else:
            norel[ind].append(float(nordata[i][j-1]))            
        ind+=1

x = np.array([0,3,6,9,12,15,18,21])
width = 0.3

rec = [[],[],[]]
unem = [[],[],[]]
cps = [[],[],[]]
hos = [[],[],[]]
loan = [[],[],[]]
ins = [[],[],[]]

for i in range(8):
    rec[0].append(second[i][0])
    rec[1].append(accuracy[i][0])
    rec[2].append(norel[i][0])
    unem[0].append(second[i][5])
    unem[1].append(accuracy[i][5])
    unem[2].append(norel[i][5])
    cps[0].append(second[i][1])
    cps[1].append(accuracy[i][1])
    cps[2].append(norel[i][1])
    hos[0].append(second[i][2])
    hos[1].append(accuracy[i][2])
    hos[2].append(norel[i][2])
    loan[0].append(second[i][4])
    loan[1].append(accuracy[i][4])
    loan[2].append(norel[i][4])
    ins[0].append(second[i][3])
    ins[1].append(accuracy[i][3])
    ins[2].append(norel[i][3])
    
# Create figure
fig, axs = plt.subplots(3, sharey=True, figsize=(7,5))
for i in range(3):
    axs[i].bar(x-width*2.5, rec[i], width, label='Bail')
    axs[i].bar(x-width*1.5, cps[i], width, label='CPS')
    axs[i].bar(x-width/2, hos[i], width, label='Hospital')
    axs[i].bar(x+width/2, ins[i], width, label='Insurance')
    axs[i].bar(x+width*1.5, loan[i], width, label='Loan')
    axs[i].bar(x+width*2.5, unem[i], width, label='Unemployment')
    axs[i].set_title(batches[i],fontsize=10)
    axs[i].set_yticks([0,0.5,1])
    axs[i].set_yticklabels([0,0.5,1],fontsize=7)
    axs[i].set_xticks(x)
    axs[i].set_xticklabels(props[i],fontsize=7)
    axs[i].axhline(0,color = "black",lw = 0.25)
    for bar,p in zip(axs[i].patches,pvalues[i]):
        if p<0.01:
            axs[i].text(bar.get_x()+width/2,bar.get_height(),'**',ha='center',fontsize=5)
        elif p<0.05:
            axs[i].text(bar.get_x()+width/2,bar.get_height(),'*',ha='center',fontsize=5)
    axs[i].legend(fontsize=5,ncol=6,frameon=False)
    axs[i].text(21.1,0.68,'* - p<0.05',fontsize = 5)
    axs[i].text(20.93,0.8,'** - p<0.01',fontsize = 5)
axs[1].set_ylabel("Weights",fontsize=9)
axs[2].set_xlabel("Properties",fontsize=9)

plt.subplots_adjust(hspace=0.6)

plt.savefig("../results/Figure1.pdf")
