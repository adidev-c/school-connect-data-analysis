import pandas as pd
import numpy as np
import json

df = pd.read_csv("Titanic_Dataset.csv")

df["Gender"] = df["Gender"].map({"Male": 0, "Female": 1})
df["Embarked"] = df["Embarked"].map({"C": 0, "Q": 1, "S": 2})

features = ["Age", "Gender", "Pclass", "Embarked", "TravelingAlone"]
X = df[features].copy()

reference = np.array([61, 0, 2, 2, 1])

distances = np.linalg.norm(X.values - reference, axis=1)

distances_dict = {
    int(pid): round(dist, 2)
    for pid, dist in zip(df["PassengerID"], distances)
}

with open("distances.json", "w") as f:
    json.dump(distances_dict, f, indent=4)

print("Distances saved to distances.json")
