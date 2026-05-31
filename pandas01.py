import numpy as np
import  pandas as pd

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

csv=pd.read_csv("Datasets/subs.csv")
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
