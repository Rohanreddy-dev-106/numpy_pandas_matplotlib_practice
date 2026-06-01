import numpy as np
import  pandas as pd
from matplotlib import pyplot as plt

#normal series
names=["rohan","sai", "reddy"]
s=pd.Series(names)
print(s)
print("________________")

#series with list
runs=[31,56,71,100]
s2=pd.Series(runs)
print(s2)
print("________________")

#series with  custum  indexing
subjects = ["Mathematics", "Physics", "Chemistry", "English", "Computer Science"]
marks = [85, 78, 82, 90, 88]
data=pd.Series(marks,index=subjects,name="Marks")
print(data)

print("________________")
#series with dict
marks_dict = {
    "Mathematics": 85,
    "Physics": 78,
    "Chemistry": 82
}
dataM=pd.Series(marks_dict,name="Marks")
print(dataM)
print("________________")

#attributs in pd

print(dataM.size)
print(dataM.dtype)
print(dataM.name)
print(dataM.is_unique)
print(dataM.index)
print(dataM.values)
print("-----------------")

csv=pd.read_csv("Datasets/subs.csv",index_col="Subscribers gained")
df= csv.squeeze() #converts  a dataframe to series
print(df)

bo=pd.read_csv("Datasets/bollywood.csv",index_col="movie")
series=bo.squeeze()
# print(series)

print(series.head(2))
print()
print(series.tail(2))
print()
print(series.sample(2))
print()
print(series.value_counts())# frequency count
print()
print(series.count())
print()
# print(series.sum())
# print(series.product())
print()
# print(df.mean())#median mode std var
# print(series.mode())
print()
print(series.describe())

# series.value_counts().plot(kind="pie")
# plt.show()
print("_____________________")
#indexing in  series using iloc[position] for slicing also same
series.iloc[0]
series.iloc[-1]
