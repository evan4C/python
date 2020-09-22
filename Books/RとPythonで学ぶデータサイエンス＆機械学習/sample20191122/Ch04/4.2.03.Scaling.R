#スケーリング


#正規分布に沿ったデータを作る
#　rnorm()：正規乱数を発生させる
#　ケース数500、mean=120、SD=85
x <- rnorm(500, 120, 85)
summary(x)  #平均値、最小値、最大値など
sd(x) 　　　#標準偏差（不偏分散の平方根）
hist(x, breaks=100)

#中心化 (centering)
#mean=0となるようにスケーリングする
X <- x - mean(x)
summary(X)
#以下の方が便利
#　scale()：中心化または標準化を行う
#  scale=TRUEで標準化、FALSEで中心化
#  デフォルトはTRUEなのでFALSEを指定
X <- scale(x, scale=F)
summary(X)
sd(X)
hist(X, breaks=100)


#正規化 (min-max normalization)
#全体が0から１に収まるようにスケーリングする
X <- (x - min(x))/(max(x) - min(x))
summary(X)
sd(X)
hist(X, breaks=100)

#全体がある範囲に収まるようにスケーリングする
A=10
B=20
X <- (x-min(x)) * (B-A) / (max(x)-min(x)) + A
summary(X)
sd(X)
hist(X, breaks=100)


#標準化 (standardization, Z-Score)
#mean=0、SD=1となるように変換する
X <- (x - mean(x)) / sd(x)
summary(X)
#以下の方が便利
X <-  scale(x)
summary(X)
sd(X)
hist(X, breaks=100)

#偏差値
#mean=0、SD=1となるように変換する
X <- (x-mean(x)) * 10 / sd(x) + 50
summary(X)
sd(X)
hist(X, breaks=100)
