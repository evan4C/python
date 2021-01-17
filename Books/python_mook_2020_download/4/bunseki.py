%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from sklearn import linear_model

SERVICE_NUM = 2 # 分析対象のフリマサービスの数
ITEM_NUM = 3 # 分析対象の商品の数
RECENT_DAYS = 5 # 直近で分析する日数

register_matplotlib_converters()

# グラフのサイズ設定
plt.figure(figsize=(15, 18))

# 線形回帰モデル生成
clf = linear_model.LinearRegression()

# CSV読み込み。1列目は日付型で読み込み、インデックスとする
df= pd.read_csv('data.csv',index_col=0, parse_dates=True)

# 説明変数設定
X = df.index.to_frame() # 全日
X_recent = X.tail(RECENT_DAYS) # 直近

# プロット先の番号を初期化
no = 1

# 商品ごとにメルカリとラクマのデータ分析とグラフ作成
for i, (col_name, Y) in enumerate(df.iteritems()):
    # メルカリとラクマの2列ごと同じグラフにプロット
    if i % SERVICE_NUM == 0:
        plt.subplot(ITEM_NUM, 1, no) # プロット先を設定
        plt.title('item' + str(no)) # タイトル
    else:
        no += 1 # プロット先を1進める

    # 全日のグラフ作成
    plt.plot(X, Y, label=col_name)

    # 全日で分析
    clf.fit(X, Y) # 学習
    plt.plot(X, clf.predict(X.values.astype(float)),
        linestyle='dashed', label=col_name + '_reg') # 回帰直線描画

    # 直近で分析
    clf.fit(X_recent, Y.tail(RECENT_DAYS)) # 学習
    label_recent = f'{col_name}_reg_recent_{RECENT_DAYS}days'
    plt.plot(X_recent, clf.predict(X_recent.values.astype(float)),
        linestyle='dotted', label=label_recent) # 回帰直線描画

    plt.legend() # 凡例表示

plt.show()