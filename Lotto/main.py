import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

lotto_file_path = "Lotto_Dataset.csv"

lotto_data = pd.read_csv(lotto_file_path)
print(lotto_data.describe())
lotto_data = lotto_data.dropna(axis=0)

y = lotto_data.Down_1

lotto_features = ['Up_100', 'Up_10', 'Up_1']

X = lotto_data[lotto_features]

lotto_model = DecisionTreeRegressor(random_state=2)

lotto_model.fit(X, y)

predictions = lotto_model.predict(X)

pre = []
for num in predictions:
    pre.append(round(num))

true = y.to_list()
same = 0
for i in range(len(predictions)):
    print(pre[i], "=", true[i])
    if pre[i] == true[i]:
        same += 1
    print("\n")

print(f"{same / len(predictions)} %")
