#価格弾力性モデル

#データの読込み
DF <- read.table("TPPrice.csv",
                  sep = ",",            #カンマ区切りのファイル
                  header = T,           #1行目はヘッダー(列名)
                  fileEncoding="UTF-8") #文字コードはUTF-8
#データの内容
head(DF)
#統計要約量
summary(DF)

#販売数の分布
hist(DF$Sales, breaks=15, col="steelblue")
#価格の分布
hist(DF$Price, breaks=15, col="steelblue")

#価格と販売数の関係
library(ggplot2)
ggplot(DF, aes(Price, Sales))+                  #描画の対象となる変数
  geom_point(size=3, color="blue", alpha=0.5 )+ #大きさ、色、透明度
  xlab("Price") + #x軸ラベル
  ylab("Sales")   #y軸ラベル

#単純な回帰モデル
#Sales = b0 + b1*Price
LS1 <- lm(Sales ~ Price, data=DF)
summary(LS1)

#残差の診断
par(mfrow=c(2,2))
plot(LS1)
par(mfrow=c(1,1))

#目的変数の対数化
#販売数量の分布
hist(log(DF$Sales), breaks=15, col="steelblue")

#目的変数を対数化したモデル
#log(Sales) = b0   + b1*Price
#    Sales  = e^b0 * e^(b1*Price)
LS2 <- lm(log(Sales) ~ Price, data=DF)
summary(LS2)

#残差の診断
par(mfrow=c(2,2))
plot(LS2)
par(mfrow=c(1,1))

#理論的な価格弾力性を考慮したモデル
#目的変数と説明変数の双方を対数化
#log(Sales) = b0   + b1*log(Price)
#    Sales  = e^b0 * Price^b1
LS3 <- lm(log(Sales) ~ log(Price), data=DF)
summary(LS3)

#切片と回帰係数
LS3b0 <- LS3$coefficients[1]
LS3b1 <- LS3$coefficients[2]

#パラメータの値を表示
LS3b0
LS3b1
exp(LS3b0)

#散布図で曲線を記述
#stat_function()でe^b0 * Price^b1を記述
#eの累乗は関数exp()で算出できる
ggplot(DF, aes(Price, Sales))+                  #描画の対象となる変数
  geom_point(size=3, color="blue", alpha=0.5 )+ #大きさ、色、透明度
  xlab("Price") + 
  ylab("Sales") +
  stat_function(colour="purple", 
                fun=function(x) exp(LS3b0)*x^LS3b1)

#-100円から800円までの範囲でモデルを描画
#標準のplot()関数を使う
plot(function(x) exp(LS3b0)*x^LS3b1,
        -100, 800, col="purple", ylim=c(-50, 1000))
lines(c(-100, 800), c(0,      0), col="grey")  #x=0の直線を加える
lines(c(   0,   0), c(-50, 1000), col="grey")  #y=0の直線を加える
