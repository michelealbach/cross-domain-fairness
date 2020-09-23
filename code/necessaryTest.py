# Cross Domain Fairness
# Michele Albach
# This file determines that all eight properties are necessary by counting the percentage of respondents who selected each property at least once in their answers

import csv

def nec(domain):
    mainfile = open('../data/NecSufSurvey'+domain+'.csv','r')
    maindata = csv.reader(mainfile)
    mainresults=list(maindata)
    mainfile.close()

    reliabilityIndx = []
    relevanceIndx = []
    privacyIndx = []
    volitionalityIndx = []
    causesOutcomeIndx = []
    causesCycleIndx = []
    causesDisparityIndx = []
    causedByGroupIndx = []

    # For each property, append the index of all users that checked it
    for i in range(len(mainresults[0])):
        if "Reliability" in mainresults[0][i]:
            reliabilityIndx.append(i)
        if "Relevance" in mainresults[0][i]:
            relevanceIndx.append(i)
        if "Privacy" in mainresults[0][i]:
            privacyIndx.append(i)
        if "Volitionality" in mainresults[0][i]:
            volitionalityIndx.append(i)
        if "Causes Outcome" in mainresults[0][i]:
            causesOutcomeIndx.append(i)
        if "Causes Cycle" in mainresults[0][i]:
            causesCycleIndx.append(i)
        if "Causes Disparity" in mainresults[0][i]:
            causesDisparityIndx.append(i)
        if "Caused by Group" in mainresults[0][i]:
            causedByGroupIndx.append(i)


    reliability = 0
    relevance = 0
    privacy = 0
    volitionality = 0
    causesOutcome = 0
    causesCycle = 0
    causesDisparity = 0
    causedByGroup = 0

    # Count the respondents that checked each property at least once
    for result in mainresults:
        for i in reliabilityIndx:
            if result[i]=='true':
                reliability = reliability+1
                break
        for i in relevanceIndx:
            if result[i]=='true':
                relevance = relevance+1
                break
        for i in privacyIndx:
            if result[i]=='true':
                privacy = privacy+1
                break
        for i in volitionalityIndx:
            if result[i]=='true':
                volitionality = volitionality+1
                break
        for i in causesOutcomeIndx:
            if result[i]=='true':
                causesOutcome = causesOutcome+1
                break
        for i in causesCycleIndx:
            if result[i]=='true':
                causesCycle = causesCycle+1
                break
        for i in causesDisparityIndx:
            if result[i]=='true':
                causesDisparity = causesDisparity+1
                break
        for i in causedByGroupIndx:
            if result[i]=='true':
                causedByGroup = causedByGroup+1
                break

    row = [domain]
    # Append percentages
    row.append(relevance/(len(mainresults)-1))
    row.append(causesOutcome/(len(mainresults)-1))
    row.append(reliability/(len(mainresults)-1))
    row.append(causesDisparity/(len(mainresults)-1))
    row.append(causedByGroup/(len(mainresults)-1))
    row.append(causesCycle/(len(mainresults)-1))
    row.append(volitionality/(len(mainresults)-1))
    row.append(privacy/(len(mainresults)-1))

    return row

top_row = ["Percentage of respondents who checked the property at least once","Relevance","Causes Outcome","Reliability","Causes Disparity","Caused by Group","Causes Cycle","Volitionality","Privacy"]

rows = [top_row,nec("Bail"),nec("CPS"),nec("Hos"),nec("Ins"),nec("Loan"),nec("Unem")]

new_file = open('../results/Necessity.csv','w')
write = csv.writer(new_file)
write.writerows(rows)
new_file.close()
