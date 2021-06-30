# Cross Domain Fairness
# Michele Albach
# This file combines results from the main, replaced, and removed surveys to prepare files for demographic analyses

import csv

def combineFair(domain,feats):
    file = open("../../data/MainSurvey"+domain+".csv",'r')
    secdata = list(csv.reader(file))
    file.close()
    file = open("../../data/Accuracy"+domain+".csv",'r')
    accdata = list(csv.reader(file))
    file.close()
    file = open("../../data/NoRelevance"+domain+".csv",'r')
    nordata = list(csv.reader(file))
    file.close()

    nsecdata = []
    for i in range(len(secdata)):
        nresp = secdata[i][:15]
        for f in range(feats):
            nresp.append(secdata[i][15+f*9])
        nsecdata.append(nresp)
    naccdata = []
    for i in range(len(accdata)):
        nresp = accdata[i][:15]
        for f in range(feats):
            nresp.append(accdata[i][15+f*9])
        naccdata.append(nresp)
    nnordata = []
    for i in range(len(nordata)):
        nresp = nordata[i][:15]
        for f in range(feats):
            nresp.append(nordata[i][15+f*8])
        nnordata.append(nresp)

    
    data = nsecdata+naccdata[1:]+nnordata[1:]

    file = open("modifiedData/CombinedFair"+domain+".csv",'w')
    write = csv.writer(file)
    write.writerows(data)
    file.close()

combineFair("Bail",10)
combineFair("Unem",10)
combineFair("CPS",10)
combineFair("Hos",8)
combineFair("Loan",10)
combineFair("Ins",8)

def combineProps(domain,feats):
    file = open("../../data/MainSurvey"+domain+".csv",'r')
    secdata = list(csv.reader(file))
    file.close()
    file = open("../../data/Accuracy"+domain+".csv",'r')
    accdata = list(csv.reader(file))
    file.close()
    file = open("../../data/NoRelevance"+domain+".csv",'r')
    nordata = list(csv.reader(file))
    file.close()

    nsecdata = []
    for i in range(len(secdata)):
        nresp = secdata[i][:15]
        for f in range(feats):
            for p in range(8):
                nresp.append(secdata[i][15+f*9+p+1])
        nsecdata.append(nresp)
    naccdata = []
    for i in range(len(accdata)):
        nresp = accdata[i][:15]
        for f in range(feats):
            for p in range(8):
                nresp.append(accdata[i][15+f*9+p+1])
        naccdata.append(nresp)
    nnordata = []
    for i in range(len(nordata)):
        nresp = nordata[i][:15]
        for f in range(feats):
            for p in range(7):
                nresp.append(nordata[i][15+f*8+p+1])
                if p==0:
                    nresp.append("")
        nnordata.append(nresp)

    
    data = nsecdata+naccdata[1:]+nnordata[1:]

    file = open("modifiedData/CombinedProps"+domain+".csv",'w')
    write = csv.writer(file)
    write.writerows(data)
    file.close()

combineProps("Bail",10)
combineProps("Unem",10)
combineProps("CPS",10)
combineProps("Hos",8)
combineProps("Loan",10)
combineProps("Ins",8)

