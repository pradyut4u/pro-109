import plotly.figure_factory as pff
import pandas as pd
import csv
import statistics

df = pd.read_csv(r"D:/python/py/pro-109.csv")
fig = pff.create_distplot([df["reading score"].tolist()],["Reading"])
fig.show()

Readinglist = df["reading score"].tolist()

rmean = statistics.mean(Readinglist)
rmode = statistics.mode(Readinglist)
rmedian = statistics.median(Readinglist)
sd = statistics.stdev(Readinglist)

print(rmean)
print(rmedian)
print(rmode)
print(sd)

#Range 1

cal = rmean - sd
cal2 = rmean + sd

newlist = [q for q in Readinglist if q > cal and q < cal2]

l1 = len(newlist)
l2 = len(Readinglist)

per = (l1/l2)*100
print(per)

#Range 2

cal3 = rmean - 2*sd
cal4 = rmean + 2*sd

newlist2 = [w for w in Readinglist if w > cal3 and w < cal4]

l3 = len(newlist2)

per2 = (l3/l2)*100
print(per2)

#Range 3

cal5 = rmean - 3*sd
cal6 = rmean + 3*sd

newlist3 = [e for e in Readinglist if e > cal5 and e < cal6]

l4 = len(newlist3)

per3 = (l4/l2)*100
print(per3)