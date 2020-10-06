# Cross Domain Fairness
# Michele Albach
# This file makes Figure 2

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import csv

file = open("../results/MainCombsAccuraciesAndWeights.csv")
secdata = list(csv.reader(file))
file.close()
file = open("../results/ReplacedCombsAccuraciesAndWeights.csv")
accdata = list(csv.reader(file))
file.close()
file = open("../results/RemovedCombsAccuraciesAndWeights.csv")
nordata = list(csv.reader(file))
file.close()

# Baselines obtained by counting the proportion of Fair/Unfair reponses for every domain in each of the three datasets and taking the larger value of the two
baselines = [0.6113801452784504, 0.5614754098360656, 0.5454545454545454, 0.7429718875502008, 0.6942003514938488, 0.6763540290620872, 0.5748299319727891, 0.622739555186032, 0.5198135198135199, 0.5428240740740741, 0.6945080091533181, 0.6954545454545454, 0.7288528389339514, 0.5578034682080925, 0.641916906622789, 0.5910112359550562, 0.5981416957026713, 0.7198622273249139, 0.6613138686131387, 0.7193181818181819, 0.5437037037037037]

# Categories
cats = ["All Properties","Relevance/Accuracy (R/A)","All Without R/A (WO)","Causes Outcome (CO)","Reliability (R)","Causes Disparity (CD)","Caused By Group (CG)","Causes Cycle (CC)","Volitionality (V)","Privacy (P)","Baseline (B)"]
cats_short = ["All","R/A","WO","CO","R","CD","CG","CC","V","P","B"]
secs = []
secerrs = []
accs = []
accerrs = []
nors = []
norerrs = []
indxs = [1,11,3,14,10,16,17,15,13,12]
norindxs = [1,12,9,14,15,13,11,10]
for i in [0,1,3,4,6,5,2]: # All domains reordered
    sec = []
    secerr = []
    acc = []
    accerr = []
    nor = []
    norerr = []
    for indx in indxs:
        sec.append(float(secdata[17*i+indx][1]))
        secerr.append(float(secdata[17*i+indx][2]))
        acc.append(float(accdata[17*i+indx][1]))
        accerr.append(float(accdata[17*i+indx][2]))
    for indx in norindxs:
        nor.append(float(nordata[15*i+indx][1]))
        norerr.append(float(nordata[15*i+indx][2]))
    sec.append(baselines[i])
    secerr.append(0)
    acc.append(baselines[7+i])
    accerr.append(0)
    nor.append(baselines[14+i])
    norerr.append(0)
    secs.append(sec)
    secerrs.append(secerr)
    accs.append(acc)
    accerrs.append(accerr)
    nors.append(nor)
    norerrs.append(norerr)

# GH accuracies obtained by running our code on GH data taken from https://github.com/nina-gh/procedurally_fair_learning/tree/master/human_perception_of_fairness
GHaccs = [0.9082927631578946,0.9082499999999999,0.8320010964912283,0.7753081140350878,0.7330120614035087,0.5751173245614036,0.5511666666666666,0.5875975877192982,0.5328432017543859,0.7332785087719298,0.5422149122807017]
GHerrs = [0.00022464213798349127,0.00023110603732890922,0.0002999893126803957,0.0002999525302617958,0.0003458581589686803,0.0005379344344970847,0.0005448646076695766,0.0004435633287222637,0.00037342372522886834,0.00036367079026726446,0]

# Create subplots
fig = plt.figure(figsize=(7,5))
gs = gridspec.GridSpec(2, 5)
ax1 = fig.add_subplot(gs[0:2,0:2])
ax1.set_title('All Pooled',fontsize=10)
ax2 = fig.add_subplot(gs[0,2])
ax2.set_title('Bail',fontsize=10)
ax3 = fig.add_subplot(gs[0,3])
ax3.set_title('CPS',fontsize=10)
ax4 = fig.add_subplot(gs[0,4])
ax4.set_title('Hospital',fontsize=10)
ax5 = fig.add_subplot(gs[1,2])
ax5.set_title('Insurance',fontsize=10)
ax6 = fig.add_subplot(gs[1,3])
ax6.set_title('Loan',fontsize=10)
ax7 = fig.add_subplot(gs[1,4])
ax7.set_title('Unemployment',fontsize=10)

axs = [ax1,ax2,ax3,ax4,ax5,ax6,ax7]

# Create each subplot
for i in range(len(axs)):
    axs[i].grid()
    axs[i].set_axisbelow(True)
    axs[i].set_ylim([0.5,1])
    axs[i].set_yticks([0.5,0.6,0.7,0.8,0.9,1.0])
    if i==0:
        axs[i].set_yticklabels([0.5,0.6,0.7,0.8,0.9,1.0],fontsize=10)
    else:
        axs[i].set_yticklabels([])
    ps = 20 if i==0 else 10
    axs[i].scatter(range(11),secs[i],s=ps,marker="s",label="Relevance")
    axs[i].errorbar(range(11),secs[i],yerr=secerrs[i],ls='none')
    axs[i].scatter(range(11),accs[i],s=ps,marker="^",label="Replaced")
    axs[i].errorbar(range(11),accs[i],yerr=accerrs[i],ls='none')
    axs[i].scatter([2,3,4,5,6,7,8,9,10],nors[i],s=ps,marker="o",label="Removed")
    axs[i].errorbar([2,3,4,5,6,7,8,9,10],nors[i],yerr=norerrs[i],ls='none')
    if i==1:
        axs[i].scatter(range(11),GHaccs,s=ps,marker="*",label="GH18")
        axs[i].errorbar(range(11),GHaccs,yerr=GHerrs,ls='none')
    axs[i].set_xticks(range(11))
    if i==0:
        axs[i].set_xticklabels(cats,fontsize=6,rotation=35,ha="right")
        axs[i].set_ylabel("Model Accuracies",fontsize=9)
        axs[i].legend(fontsize=8)
    else:
        axs[i].set_xticklabels(cats_short,fontsize=6,rotation=90)
        axs[i].legend(fontsize=5)
axs[4].set_xlabel("Models",fontsize=9)

# Save
plt.subplots_adjust(hspace=0.3)
fig.subplots_adjust(bottom=0.16)
plt.savefig("../results/Figure2.pdf")



