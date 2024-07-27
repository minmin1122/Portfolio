"""作成：摩壽意  目的：ARIMAモデルを用いた連続データの予測"""

import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# データの読み込み(csvファイルの指定, "date"をインデックスに指定, 時間軸定義)
data = pd.read_csv('C:\\Users\\takumi\\Downloads\\ARIMA_source_Masui\\data.csv',index_col='date',parse_dates=True)
# 原型データの表示
plt.plot(data)
plt.ylabel('Value')
plt.xlabel('Date')
plt.show()

#成分分解(解析したいデータ, 加算または乗算, 周期の定義)
result = seasonal_decompose(data['value'],model='multiplicative',period=3)
result.plot()
plt.show()

# モデル構築
model = ARIMA(data['value'],order=(2,2,2)) # ARIMAモデル作成
model_fit = model.fit() # 学習
predict = model_fit.predict(10,40)   # 10日から40日までを予測

# 予測結果を出力
plt.plot(data,"blue")
plt.plot(predict,"red")
plt.ylabel('Value')
plt.xlabel('Date')
plt.show()
