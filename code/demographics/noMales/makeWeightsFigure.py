# Cross Domain Fairness
# Michele Albach
# This file makes a version of Figure 1 but using data without male respondents

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv

file = open("MainAccuraciesAndWeightsNoMales.csv")
secdata = list(csv.reader(file))
file.close()
file = open("ReplacedAccuraciesAndWeightsNoMales.csv")
accdata = list(csv.reader(file))
file.close()
file = open("RemovedAccuraciesAndWeightsNoMales.csv")
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
secrec = [6.0154, 5.844, 0.0, 8.661, 25.7826, 20.5548, 37.4326, 132.1214, 28.8958]
secunem = [0.511, 75.9777, 0.0, 11.4437, 46.5028, 22.909, 135.0763, 118.3158, 9.1506]
seccps = [2.8255, 64.8962, 0.0, 99.388, 66.9477, 101.8948, 138.3487, 14.302, 68.7373]
sechos = [44.8352, 0.9106, 0.0018, 133.5071, 86.0221, 0.1485, 4.685, 0.1952, 36.4109]
secloan = [112.8771, 12.7417, 0.0, 121.3209, 11.4823, 0.3645, 86.1002, 0.2031, 88.754]
secins = [0.0, 40.125, 0.0, 2.037, 11.5565, 49.0665, 143.4626, 122.6523, 87.5745]
accrec = [119.2148, 117.2453, 0.0001, 82.0032, 70.3405, 3.2216, 5.5138, 32.7746, 38.7489]
accunem = [32.7499, 19.598, 0.0, 137.3734, 1.1505, 80.8104, 78.7023, 129.415, 6.0367]
acccps = [2.2193, 5.4712, 0.0, 11.9993, 53.8755, 112.6523, 118.8029, 71.478, 112.1004]
acchos = [116.6886, 139.717, 1.027, 8.5203, 41.6466, 0.0, 47.0643, 1.9423, 10.3086]
accloan = [7.8263, 5.0647, 0.0, 0.9958, 88.4624, 0.0001, 30.9192, 43.8011, 115.3935]
accins = [0.0437, 65.8014, 0.1224, 141.1041, 0.5571, 12.2368, 97.8461, 130.2377, 56.0653]
norrec = [0.198, 0.0, 1, 9.7644, 26.0474, 0.0, 68.9305, 27.1987, 64.5635]
norunem = [26.0627, 0.6539, 1, 53.5909, 0.6744, 0.5665, 112.8515, 0.0053, 5.1493]
norcps = [31.3937, 0.0005, 1, 70.5049, 12.0761, 0.0, 101.5773, 40.0178, 141.0471]
norhos = [1.312, 127.413, 1, 70.1573, 98.1384, 0.0001, 10.4815, 13.4104, 65.3113]
norloan = [1.3032, 90.9769, 1, 66.431, 112.1119, 0.0, 63.7201, 80.8313, 69.7027]
norins = [0.3335, 56.9742, 1, 103.4879, 25.2221, 0.0, 106.9361, 6.0559, 92.3085]

# correctly reorder p-values
pvalues = [ro(secrec[1:])+ro(seccps[1:])+ro(sechos[1:])+ro(secins[1:])+ro(secloan[1:])+ro(secunem[1:]),ro(accrec[1:])+ro(acccps[1:])+ro(acchos[1:])+ro(accins[1:])+ro(accloan[1:])+ro(accunem[1:]),ro(norrec[1:])+ro(norcps[1:])+ro(norhos[1:])+ro(norins[1:])+ro(norloan[1:])+ro(norunem[1:])]

for i in [2,4,5,7,6,3]: # All domains
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

plt.savefig("Figure1NoMales.pdf")
