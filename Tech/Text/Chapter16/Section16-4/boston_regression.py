from sklearn import datasets
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame

# データセット読み込み
boston = datasets.load_boston()
boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df["Price"] = boston.target
print(boston_df[:10])

# 訓練データを作る
rooms_train = DataFrame(boston_df["RM"])
y_train = boston.target
model = linear_model.LinearRegression()
model.fit(rooms_train, y_train)

# 部屋数のデータを作る
rooms_test = DataFrame(np.arange(rooms_train.min(), rooms_train.max(), 0.1))
prices_test = model.predict(rooms_test)

plt.scatter(rooms_train, y_train, c="b", alpha=0.5)
plt.plot(rooms_test, prices_test, c="r")
plt.title("Boston House Prices dataset")
plt.xlabel("rooms")
plt.ylabel("price $1000's")
plt.show()
