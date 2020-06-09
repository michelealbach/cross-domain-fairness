# Cross Domain Fairness
# Michele Albach
# This file performs 1000 50/50 train test splits on the data from a particular domain from any of the three main surveys depending on commented code

import csv
import numpy as np
from sklearn import linear_model
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from scipy import stats

def load(domain,props):
    file = open("../data/SecondSurvey"+domain+".csv",'r')
#    file = open("../data/Accuracy"+domain+".csv",'r')
#    file = open("../data/NoRelevance"+domain+".csv",'r')
    data = list(csv.reader(file))
    file.close()

    X = []
    Y = []

    f = 8 # Number of features (7 for NoRel 8 for Second or Accuracy)
    f=f+1
    
    for i in range(1,len(data)): # For every respondent
        for k in range(int((len(data[0])-15)/f)): # For every feature
            skip=False
            # append a 1 to Y if rated fair or a 0 if rated unfair
            if data[i][15+k*f] == "Very Fair":
                Y.append(1)
            elif data[i][15+k*f] == "Fair":
                Y.append(1)
            elif data[i][15+k*f] == "Somewhat Fair":
                Y.append(1)
            elif data[i][15+k*f] == "Somewhat Unfair":
                Y.append(0)
            elif data[i][15+k*f] == "Unfair":
                Y.append(0)
            elif data[i][15+k*f] == "Very Unfair":
                Y.append(0)
            else: # rated as neutral or question skipped
                skip=True
            x = []
            for j in props: # For every property
                if j=='S':
                    # This property is skipped for this test
                    continue
                if skip==True:
                    break
                # Append a -3..3 for Strongly Disagree..Strongly Agree
                if data[i][16+k*f+j] == "Strongly Disagree":
                    x.append(-3)
                elif data[i][16+k*f+j] == "Disagree":
                    x.append(-2)
                elif data[i][16+k*f+j] == "Somewhat Disagree":
                    x.append(-1)
                elif data[i][16+k*f+j] == "Somewhat Agree":
                    x.append(1)
                elif data[i][16+k*f+j] == "Agree":
                    x.append(2)
                elif data[i][16+k*f+j] == "Strongly Agree":
                    x.append(3)
                else: # rated neutral or question skipped
                    x.append(0)
            if skip==False:
                X.append(x)
    X = np.asarray(X)
    Y = np.asarray(Y)
    return(X,Y)

def trainandpredict(X,Y):
    # Divide the data into 50% test, 50% train
    num_test = int((len(Y)/2)//1)
    num_train = len(Y)-num_test
    zeros = np.zeros(num_test)
    ones = np.ones(num_train)
    rand = np.concatenate([zeros,ones])
    np.random.shuffle(rand)

    Y_train = np.zeros(num_train)
    Y_test = np.zeros(num_test)
    X_train = np.zeros((num_train,X.shape[1]))
    X_test = np.zeros((num_test,X.shape[1]))
    train_indx = 0
    test_indx = 0

    for i in range(len(Y)):
        if rand[i] == 1:
            Y_train[train_indx] = Y[i]
            X_train[train_indx] = X[i]
            train_indx+=1
        else:
            Y_test[test_indx] = Y[i]
            X_test[test_indx] = X[i]
            test_indx+=1

    model = linear_model.LogisticRegression()
    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    # Repeat with all data in train to get coefficients
    model_w = linear_model.LogisticRegression()
    model_w.fit(X,Y)

    return accuracy_score(Y_test,Y_pred),roc_auc_score(Y_test,Y_pred), model_w.coef_[0]

def WithinDomain(domain,props):
    # 'domain' should be 'Bail', 'Unem', 'CPS', 'Hos', 'Loan', or 'Ins'
    # 'props' should be a list of the integers 0..7 (0..6 for NoRel) with any property that should be skipped as an 'S' instead
    [X,Y] = load(domain,props)
    accs = []
    # Complete 1000 train/test splits
    for test in range(1000):
        [acc,auc,weights] = trainandpredict(X,Y)
        accs.append(acc)
    mean=np.mean(accs) # Accuracy mean
    error = stats.sem(accs) # Standard Error
    row = ["Within "+domain]
    row.append(mean)
    row.append(error)
    i=0
    # Append a blank for skipped properties for the sake of the table
    for p in props:
        if p=='S':
            row.append("")
        else:
            row.append(weights[i])
            i=i+1
    return row

#print(WithinDomain("Bail",[0,1,2,3,4,5,'S',7]))
#print(WithinDomain("Bail",[0,1,2,3,4,5,'S']))
