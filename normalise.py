import pandas as pd

data = pd.read_csv('Titanic_Dataset.csv')

min_age = data['Age'].min()
max_age = data['Age'].max()
print(min_age,max_age)
data['Age_normalized'] = round((data['Age'] - min_age) / (max_age - min_age),1)

print("\nMin and Max of Age_normalized:")
print(f"Min: {data['Age_normalized'].min()}, Max: {data['Age_normalized'].max()}")


output_file = 'Titanic_Dataset_Normalized.csv'
data.to_csv(output_file, index=False)
print(f"\nDataset with normalized Age saved to: {output_file}")