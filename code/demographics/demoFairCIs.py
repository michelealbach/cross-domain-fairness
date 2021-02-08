# Cross Domain Fairness
# Michele Albach
# This file obtains 95% Bonferroni corrected confidence intervals for the weights of the demographic information when used to predict fairness judgements

import csv
import numpy as np
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from scipy import stats
import statsmodels.api as sm


def trainandpredict(X,Y):
    try:
        # Bootstrap sample points with replacement
        numsam = len(X)
        rand = []
        for i in range(numsam):
            rand.append(np.random.randint(len(Y)))

        Y_train = np.zeros(numsam)
        X_train = np.zeros((numsam,X.shape[1]))
        
        train_indx = 0
        for i in range(len(rand)):
            Y_train[i] = Y[rand[i]]
            X_train[i] = X[rand[i]]

        model = linear_model.LogisticRegression()
        model.fit(X_train,Y_train)
        
        return model.coef_[0]
    except:
        # Not enough points of each side to train, return zeros to skew towards non-significant
        return [0,0,0,0,0,0,0,0,0]

def load(domain):
    file = open("CombinedFair"+domain+".csv",'r')
    data = list(csv.reader(file))
    file.close()

    ages = ["18-29","30-39","40-49","50-59","60-69","70 up"]
    eds = ["Less than high School","High School","Associate or Diploma","Bachelor","Graduate"]
    gens = ["Female","Male","Nonbinary"]
    incs = ["<25000","25000-50000","50000-75000","75000-100000",">100000"]
    eths = ["Aboriginal","Asian","Black","Caucasian","Hispanic"]

    rows = []

    # Prep data
    for f in range(15,len(data[0])):
        X = []
        Y = []
        for i in range(1,len(data)):
            if data[i][f] == "Very Fair":
                Y.append(1)
            elif data[i][f] == "Fair":
                Y.append(1)
            elif data[i][f] == "Somewhat Fair":
                Y.append(1)
            elif data[i][f] == "Somewhat Unfair":
                Y.append(0)
            elif data[i][f] == "Unfair":
                Y.append(0)
            elif data[i][f] == "Very Unfair":
                Y.append(0)
            else:
                continue
            x = []
            try:
                x.append(ages.index(data[i][2]))
                x.append(eds.index(data[i][3]))
                x.append(gens.index(data[i][4]))
                x.append(incs.index(data[i][6]))
            except:
                Y.pop()
                continue
            for j in range(5):
                if data[i][7+j]=='true':
                    x.append(1)
                else:
                    x.append(0)
            X.append(x)
        base = max(sum(Y)/len(Y),1-sum(Y)/len(Y))
        X = np.asarray(X)
        Y = np.asarray(Y)

        coefs = [[],[],[],[],[],[],[],[],[]]
        numtests = 1000000
        for test in range(numtests):
            weights=trainandpredict(X,Y)
            for i in range(9):
                coefs[i].append(weights[i])
        row = [domain,data[0][f]]
        for i in range(9):
            mean = np.mean(coefs[i])
            std = np.std(coefs[i])
            new = coefs[i]
            # Get bonferroni corrected confidence intervals
            for j in range(int((numtests*0.05/4536)//2)):
                new.pop(new.index(min(new)))
                new.pop(new.index(max(new)))
            ci = [min(new),max(new)]
            row.append(ci[0])
            row.append(ci[1])
            # Check for significance
            if ci[0]<=0 and ci[1]>=0:
                row.append("")
            else:
                row.append("SIG")
        rows.append(row)
    return rows

# Make Table
toprow = [["Domain","Feature","Age","","","Education","","","Gender","","","Income","","","Aboriginal","","","Asian","","","Black","","","Caucasian","","","Hispanic","","","Random Int","",""]]
allrows=toprow+load("Bail")+load("CPS")+load("Hos")+load("Ins")+load("Loan")+load("Unem")

file = open("../../results/DemoFairCIs.csv",'w')
write = csv.writer(file)
write.writerows(allrows)
file.close()
