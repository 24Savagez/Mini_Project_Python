import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

usd_train_path = "Train_USA30IDXUSD_H1.csv"
use_test_path = "Test _USA30IDXUSD_H1.csv"
btc_path = "BTCUSD_H1.csv"


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return (mae)


usd_train_data = pd.read_csv(usd_train_path)
use_test_data = pd.read_csv(use_test_path)
btc_data = pd.read_csv(btc_path)

# print(usd_train_data.columns)

y = usd_train_data.Close

features = ['Open', 'High', 'Low']

X = pd.get_dummies(usd_train_data[features])
X_test = pd.get_dummies(use_test_data[features])
X_Btc_test = pd.get_dummies(btc_data[features])

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# usd_model = DecisionTreeRegressor(max_leaf_nodes=5000, random_state=0)
usd_model = RandomForestRegressor(random_state=1)
usd_model.fit(train_X, train_y)

predicted_usd_price = usd_model.predict(val_X)
print(mean_absolute_error(val_y, predicted_usd_price))

price_y = []
for x in val_y:
    price_y.append(x)

print("\nprediction  ==   price_close  === diff")
for i in range(10):
    print(f"{predicted_usd_price[i]:.4f}   -   {price_y[i]:.4f}  = {abs((predicted_usd_price[i]) - (price_y[i])):.4f}")

# option
max_leaf_nodes_candidate = [5, 25, 50, 100, 250, 500, 750, 1000, 4000]
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in max_leaf_nodes_candidate}
best_tree_size = min(scores, key=scores.get)

final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)
final_model.fit(X, y)

final_predicted_usd_price = final_model.predict(val_X)
print(f"\nfrom max_leaf {best_tree_size}")
print(mean_absolute_error(val_y, final_predicted_usd_price))

price_y = []
for x in val_y:
    price_y.append(x)

print("\nprediction  ==   price_close  === diff")
for i in range(10):
    print(f"{final_predicted_usd_price[i]:.4f}   -   {price_y[i]:.4f}  = {abs((final_predicted_usd_price[i]) - (price_y[i])):.4f}")
