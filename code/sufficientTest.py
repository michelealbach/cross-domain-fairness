# Cross Domain Fairness
# Michele Albach
# This file determines that the eight properties are sufficient to each domain by determining the percentage of respondents who listed anything in the 'other' box

import csv

def suf(domain):
    mainfile = open('../data/NecSufSurvey'+domain+'.csv','r')
    maindata = csv.reader(mainfile)
    mainresults=list(maindata)
    mainfile.close()

    otherIndx = []

    # Append the index of all respondents who filled in the 'other' box
    for i in range(len(mainresults[0])):
        if "Other" in mainresults[0][i]:
            if "Respondent" in mainresults[0][i]:
                continue
            if "Ethnicity" in mainresults[0][i]:
                continue
            otherIndx.append(i)

    other = 0

    # Count the number of respondents
    for result in mainresults:
        if result[0]=="Study ID":
            continue
        for i in otherIndx:
            if result[i]!='':
                other = other+1
                break

    # Return the percentage
    return [domain,float(other)/(len(mainresults)-1)]

top_row = ["Domain","Percentage of respondents who filled out the 'other' option at least once"]

rows = [top_row,suf("Bail"),suf("CPS"),suf("Hos"),suf("Ins"),suf("Loan"),suf("Unem")]

new_file = open('../results/Sufficiency.csv','w')
write = csv.writer(new_file)
write.writerows(rows)
new_file.close()

