import plotly.figure_factory as pff
import pandas as pd
import csv
import statistics

df = pd.read_csv(r"D:/python/py/pro-109.csv")
fig = pff.create_distplot([df["writing score"].tolist()],["Writing"])
fig.show()

Writinglist = df["writing score"].tolist()

wmean = statistics.mean(Writinglist)
wmode = statistics.mode(Writinglist)
wmedian = statistics.median(Writinglist)
sd = statistics.stdev(Writinglist)

print(wmean)
print(wmedian)
print(wmode)
print(sd)

#Range 1

cal = wmean - sd
cal2 = wmean + sd

newlist = [q for q in Writinglist if q > cal and q < cal2]

l1 = len(newlist)
l2 = len(Writinglist)

per = (l1/l2)*100
print(per)

#Range 2

cal3 = wmean - 2*sd
cal4 = wmean + 2*sd

newlist2 = [w for w in Writinglist if w > cal3 and w < cal4]

l3 = len(newlist2)

per2 = (l3/l2)*100
print(per2)

#Range 3

cal5 = wmean - 3*sd
cal6 = wmean + 3*sd

newlist3 = [e for e in Writinglist if e > cal5 and e < cal6]

l4 = len(newlist3)

per3 = (l4/l2)*100
print(per3)