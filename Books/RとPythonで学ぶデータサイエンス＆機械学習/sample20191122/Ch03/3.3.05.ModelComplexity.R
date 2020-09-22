#オーバーフィッティングと予測精度

#7件の簡単なサンプルデータ
DF <- data.frame(C1 = c(7.5, 8.8, 2.5, 4.0, 5.2, 1.5, 7.1),
                 C2 = c(5.8, 7.2, 6.0, 3.8, 8.3, 2.8, 4.2))
#内容を確認（最初の6件まで表示）
head(DF)

#図示
library(ggplot2)
ggplot(DF, aes(C1, C2))+   #x, yに相当するデータを指定
  geom_point( colour="orange", size=3 ) +  #色、サイズ
  xlim(0, 10) +  #x軸の描画範囲
  ylim(0, 10)    #y軸の描画範囲
  
#単純なモデル
Model1 <- lm(C2 ~ C1, data=DF ) 
#回帰係数の値を取り出す
a  <- Model1$coefficients
a    #回帰係数を表示
a[1] #１つずつ表示（b0）
a[2] #１つずつ表示（b1）

#モデルを数式で描画
ggplot(DF, aes(C1, C2))+
  geom_point( colour="orange", size=3 ) +
  xlim(0, 10) +  #x軸の描画範囲
  ylim(0, 10) +  #y軸の描画範囲
  stat_function(colour="red", alpha=0.6,
                fun=function(x) a[1] + a[2]*x )
# stat_function()で関数を描画
# fun=function(x)の後にxの関数を記述する
# xは最初にggplot()で指定したx軸と対応づけられる

#残差（予測値と実測値の差）
Model1$residuals

#C1が6,8,10のときのc2の値を予測
#元のデータと同じ形式の新しいデータフレームを作る
DFnew <- data.frame(C1 = c(6,  8,  10),
                    C2 = c(NA, NA, NA))
#内容を確認（最初の6件まで表示）
head(DFnew)

#predict()：モデルにデータを当てはめて予測値を得る
predict(Model1, newdata=DFnew)


#複雑なモデル
Model2 <- lm(C2 ~ C1+I(C1^2)+I(C1^3)+I(C1^4)+I(C1^5) , data=DF ) 
#回帰係数の値を取り出す
b  <- Model2$coefficients
b #回帰係数を表示

#モデルを数式で描画
ggplot(DF, aes(C1, C2))+
  geom_point( colour="orange", size=3 ) +
  xlim(0, 10) +  #x軸の描画範囲
  ylim(0, 10) +  #y軸の描画範囲
  stat_function(colour="red", alpha=0.6,
                fun=function(x) b[1] + b[2]*x + b[3]*x^2 +
                  b[4]*x^3 + b[5]*x^4 + b[6]*x^5)

#残差（予測値と実測値の差）
Model2$residuals

#C1が6,8,10のときのc2の値を予測
predict(Model2, newdata=DFnew)


#別のテストデータがあったと想定
DFts <- data.frame(C1 = c(4.8, 5.4, 3.2, 8.0, 1.4, 7.4, 5.7),
                   C2 = c(2.4, 6.2, 7.0, 7.7, 3.3, 9.5, 3.4))
#内容を確認（最初の6件まで表示）
head(DFts)

#新しいデータをModel1とModel2に当てはめて予測
pr1 <- predict(Model1, newdata=DFts)
pr2 <- predict(Model2, newdata=DFts)

#MSE（平均二乗誤差）を求める
# 予測値から実測値を引いて2乗（ベクトル演算）
# ベクトルに関数sum()を適用して和を求める
# 求めた和を要素の数（length()で求める）で割る
sum( (pr1 - DFts$C2)^2 ) / length(DFts$C2)
sum( (pr2 - DFts$C2)^2 ) / length(DFts$C2)

#MAE（平均絶対誤差）を求める
# abs()は絶対値を求める関数
sum( abs(pr1 - DFts$C2) ) / length(DFts$C2)
sum( abs(pr2 - DFts$C2) ) / length(DFts$C2)

#MAPE（平均絶対誤差率）を求める
sum( abs(pr1 - DFts$C2)/DFts$C2 ) / length(DFts$C2)
sum( abs(pr2 - DFts$C2)/DFts$C2 ) / length(DFts$C2)

