import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# function for comparing different models
def score_model(model, X_t, X_v, y_t, y_v):
    model.fit(X_t, y_t)
    predict = model.predict(X_v)
    return mean_absolute_error(y_v, predict)


# read the data
X_full = pd.read_csv("daily_EUR_USD.csv")
X_test = pd.read_csv("test_daily_EUR_USD.csv")

# obtain target and prediction
y = X_full.close
features = ['open', 'high', 'low']

X = X_full[features].copy()
X_test = X_test[features].copy()
# break off validation set from trianing data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

# print(X_train.head())

# define the models
model_1 = RandomForestRegressor(n_estimators=50, random_state=0)
model_2 = RandomForestRegressor(n_estimators=100, random_state=0)
model_3 = RandomForestRegressor(n_estimators=100, criterion='mae', random_state=0)
model_4 = RandomForestRegressor(n_estimators=200, min_samples_split=20, random_state=0)
model_5 = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=0)

models = [model_1, model_2, model_3, model_4, model_5]

maes = []
for i in range(0, len(models)):
    mae = score_model(models[i], X_train, X_valid, y_train, y_valid)
    maes.append(mae)
    print(f"Model {i + 1} MAE: {mae}")

best_mess = min(maes)
print(f"\nbest_mess : {best_mess:.5f}\n")

# define best model
best_model = models[maes.index(best_mess)]

# fit the model to the training data
best_model.fit(X, y)

# generate test predictions
prediction_euusd = best_model.predict(X_test)
print(f"{prediction_euusd[0]:.5f}")
print(f"{prediction_euusd[1]:.5f}")
print(f"{prediction_euusd[2]:.5f}")

# check result
# close_test = pd.read_csv("check_daily_EUR_USD.csv")
# close_price = close_test["close"].values.tolist()
#
# for x in range(0, len(close_price)):
#     print(f"{close_price[x]} - {prediction_euusd[x]:.5f} = {float(close_price[x]) - float(prediction_euusd[x]):.5f}")

# print(f"{prediction_euusd}")
# save predicitons
# output = pd.DataFrame({"ID": X_test.index, "close": prediction_euusd})
# output.to_csv("prediction_close.csv", index=False)
# print("Finished")
