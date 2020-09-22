#分布と外れ値

#データを読み込む
DF <- read.csv("SalesAndRatio.csv", header=T)

#内容を確認
head(DF)

#要約統計量
summary(DF)

#欠損値を除く
DF <- na.omit(DF)

#ヒストグラム
hist(DF$sales, col="steelblue", breaks=100)
hist(DF$ratio, col="orange",    breaks=100)

#散布図
library(ggplot2)
ggplot(DF, aes(x=sales, y=ratio))+
  geom_point(colour="brown3", 
             alpha=0.5, size=3)

#回帰直線
ggplot(DF, aes(x=sales, y=ratio))+
  geom_point(colour="brown3", 
             alpha=0.5, size=3)+
  geom_smooth(method="lm", colour="orange")
  #この状態で回帰直線を引いても意味はない


#分布を変換する（物差しを伸び縮みさせる）

#salesについて常用対数をとる
#　　自然対数の場合はlog(X)を使う
DF$Sales <- log10(DF$sales)
#ヒストグラム
hist(DF$Sales, col="steelblue", breaks=100)

#ratioについて対数オッズをとる
#　　ここではcarライブラリの関数logit()を使う
library(car)
DF$Ratio <- logit(DF$ratio)
#ヒストグラム
hist(DF$Ratio, col="orange", breaks=100)

#散布図と回帰直線
ggplot(DF, aes(x=Sales, y=Ratio))+
  geom_point(colour="brown3", 
             alpha=0.5, size=3)+
  geom_smooth(method="lm", colour="orange")



#空間密度に基づく外れ値の検出
library(DMwR)

#標準化
DF$Sales_S <- scale(DF$Sales)
DF$Ratio_S <- scale(DF$Ratio)

#lofactor() : 近傍の空間密度を計算
#　kは密度推定に用いる近傍のケースの数(任意に決める)
#　標準化後の値を用いる
Scores <- lofactor(DF[, c("Sales_S", "Ratio_S")], k=10)

#lofの値をヒストグラムで表示
hist(Scores, col="pink3", breaks=300)

#lof値が2を超えているかどうかをTRUE/FALSEで配列化
DF$over <- Scores > 2.0
head(DF)
#lof値が2を超えているものがいくつあるか
table(DF$over)

#該当のケース(外れ値)を表示
DF[DF$over==T, ]

#変換した値による散布図(外れ値を色分け)
ggplot(DF, aes(x=Sales, y=Ratio))+
  geom_point(aes(colour=DF$over, shape=DF$over), 
             alpha=0.5, size=3)

#変換前の値による散布図(外れ値を色分け)
ggplot(DF, aes(x=sales, y=ratio))+
  geom_point(aes(colour=DF$over, shape=DF$over), 
             alpha=0.5, size=3)



#変換前の値で相関係数を計算
cor(DF$sales, DF$ratio)
#変換後の値で相関係数を計算
cor(DF$Sales, DF$Ratio)
#外れ値を除いて相関係数を計算
cor(DF[DF$over==F, ]$Sales, DF[DF$over==F, ]$Ratio)
