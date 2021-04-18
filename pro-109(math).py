import plotly.figure_factory as pff
import pandas as pd
import csv
import statistics

df = pd.read_csv(r"D:/python/py/pro-109.csv")
fig = pff.create_distplot([df["math score"].tolist()],["Math"])
fig.show()

Mathlist = df["math score"].tolist()

mmean = statistics.mean(Mathlist)
mmode = statistics.mode(Mathlist)
mmedian = statistics.median(Mathlist)
sd = statistics.stdev(Mathlist)

print(mmean)
print(mmedian)
print(mmode)
print(sd)

#Range 1

cal = mmean - sd
cal2 = mmean + sd

newlist = [q for q in Mathlist if q > cal and q < cal2]

l1 = len(newlist)
l2 = len(Mathlist)

per = (l1/l2)*100
print(per)

#Range 2

cal3 = mmean - 2*sd
cal4 = mmean + 2*sd

newlist2 = [w for w in Mathlist if w > cal3 and w < cal4]

l3 = len(newlist2)

per2 = (l3/l2)*100
print(per2)

#Range 3

cal5 = mmean - 3*sd
cal6 = mmean + 3*sd

newlist3 = [e for e in Mathlist if e > cal5 and e < cal6]

l4 = len(newlist3)

per3 = (l4/l2)*100
print(per3)