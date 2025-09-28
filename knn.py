import json
import pandas as pd
df = pd.read_csv("Titanic_Dataset_Normalized.csv")
selected_column = df[['Survived']]
def get_least_n_items(d, n):
    return sorted(d.items(), key=lambda x: x[1])[:n]

distances=json.load(open("distances.json","r"))
k = 9
result = get_least_n_items(distances, k)
survived=0
not_survived=0
for r in result:
    index, value = r
    status = selected_column.iloc[int(index)]['Survived']
    if status == 1:
        survived+=1
    else:
        not_survived+=1
    print(f"Index: {index}, Value: {value}, Survived: {status}") 
print(f"\nSurvived : {survived}")
print(f"Not survived : {not_survived}")

