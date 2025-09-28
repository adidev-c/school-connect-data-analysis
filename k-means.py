import pandas as pd
from numpy.linalg import norm
import json
df = pd.read_csv("Titanic_Dataset.csv")
ids = df["PassengerID"]
df = df.drop(columns=["PassengerID"])

df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
df["Embarked"] = df["Embarked"].map({"C": 0, "Q": 1, "S": 2})

age_min, age_max = df["Age"].min(), df["Age"].max()
df["Age"] = round((df["Age"] - age_min) / (age_max - age_min), 1)

c1 = df.loc[ids == 4].values[0]
c2 = df.loc[ids == 46].values[0]


cluster = {}
for pid, row in zip(ids, df.values):
    d1 = norm(row - c1)
    d2 = norm(row - c2)
    cluster[pid] = 1 if d1 < d2 else 2
json.dump(cluster,open("cluster.json","w"),indent=4)

p99 = cluster[99]

p9 = df.loc[ids == 9].values[0]
dist_9_c2 = norm(p9 - c2)

cluster_counts = pd.Series(cluster).value_counts()

print("Passenger 99 -> Cluster", p99)
print("Distance (Passenger 9 <-> Passenger 46) =", round(dist_9_c2, 3))
print("Cluster sizes:\n", cluster_counts)
