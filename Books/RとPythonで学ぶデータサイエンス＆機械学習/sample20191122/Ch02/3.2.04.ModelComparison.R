#交互作用とモデル間の比較

#目的変数：残業時間 overtime
#説明変数：勤続年数 tenure
#　　　　　部門 section（Ademin, IT, Sales ）

#データの読込み
DF <- read.table("StaffOvertime.csv",
                 sep = ",",                #カンマ区切りのファイル
                 header = TRUE,            #1行目はヘッダー(列名)
                 stringsAsFactors = FALSE) #文字列を文字列型で取込む

#データフレームの先頭を表示
head(DF)

#便宜的に、3次元で表わせる場合を考える（管理部門とIT部門のみ）
#関数subset()で条件に合うデータだけを抽出する
DFsub <- subset(DF, section!="Sales")  　#!=はnot equalを示す

#複数の要因を考慮したモデル（部門の違いと勤続年数）
lm( overtime ~ section + tenure, data=DFsub)
#より詳しく表示
LM3 <- lm( overtime ~ section + tenure, data=DFsub)
summary(LM3)


#部門で色分けして残業時間と勤続年数の関係を図示(管理部門とIT部門)
library(ggplot2)
ggplot(DFsub, aes( x=tenure, y=overtime) )+   #x軸とy軸を指定
  geom_point( aes(colour=section,             #部門で色分け
                  shape =section),            #部門で形も変える
              size=3, alpha=0.7 )+        #サイズ,透明度
  stat_smooth( method="lm",                   #回帰直線を描く
               se=F)                          #信頼区間の描画を省略
#元のデータ（3部門）で同様に図示
ggplot(DF,    aes( x=tenure, y=overtime) )+   #x軸とy軸を指定
  geom_point( aes(colour=section,             #部門で色分け
                  shape =section),            #部門で形も変える
              size=3, alpha=0.7 )             #サイズ,透明度



#データを抽出しなおす（管理部門と営業部門のみ）
DFsub <- subset(DF, section!="IT")  　 #!=はnot equalを示す

#部門によって勤続年数の効果に違いがあることを想定したモデル
lm( overtime ~ section + tenure + section*tenure, data=DFsub)
#より詳しく表示
LM4 <- lm( overtime ~ section + tenure 
           + section*tenure, data=DFsub)
summary(LM4)


#元のデータを使ってモデルを作る

#交互作用を含まないモデル
LM5 <- lm( overtime ~ section + tenure, data=DF)
#交互作用を含むモデル
LM6 <- lm( overtime ~ section + tenure 
                      + section*tenure, data=DF)

#モデルの詳細を表示
summary(LM5)
summary(LM6)

#AIC(赤池情報量基準)を使ってモデルを比較
#モデルの複雑さとデータへの適合のバランスを見る指標
#小さい方がよい
AIC(LM5)
AIC(LM6)
#参考：BIC(ベイズ情報量基準)を使った比較
#指標値の見方はAICと同じ
BIC(LM5)
BIC(LM6)

#目的変数の値について、モデル上の理論値を求める
#＝モデルを元のデータDFに当てはめて、DFの説明変数に
#　基づく予測値を算出する

#ここではモデルを作成した際のデータをそのまま使う
#説明変数の値のみが予測に使われる
head(DF$overtime)       #実測値
head(LM5$fitted.values) #理論値（元データに基づく予測値）
head(LM5$residuals)     #残差（予測値－実測値）

#実測値を横軸に、理論値（予測値）を縦軸にプロットする
#　モデルが完璧にデータに適合していれば、点は対角線（y=x）
#　の上に並ぶはず（対角線からの縦方向のずれが残差を表す）
ggplot()+
  geom_point(aes(x=DF$overtime, y=LM5$fitted.values),
             colour="orange", size=4, #pr5をオレンジで表示
             shape=16, alpha=.6 ) +　 #shape=16：●
  geom_point(aes(x=DF$overtime, y=LM6$fitted.values),
             colour="brown",  size=3, #pr6をブラウンで表示
             shape=17, alpha=.6 ) +   #shape=17：▲
  xlab("実測値") +                    #軸ラベル
  ylab("モデル上の理論値(元のデータに基づく予測値)") +
  stat_function(aes(x=DF$overtime), colour="black",
                fun=function(x) x )   #y=Xに沿って線を引く

#残差の分布を密度プロットで比較
ggplot()+
  geom_density( aes(x=LM5$residuals), #LM5の残差
                color="orange",       #枠線をオレンジ
                fill ="orange",       #塗りもオレンジ
                alpha=0.2  ) +        #透明度を指定
  geom_density( aes(x=LM6$residuals), #LM6の残差
                color="brown",        #枠線をブラウン
                fill ="brown",        #塗りもブラウン
                alpha=0.2  ) +        #透明度を指定
  xlab("残差(モデル上の理論値－実測値)")  #軸ラベル

#残差の2乗の分布を密度プロットで比較
ggplot()+
  geom_density( aes(x=LM5$residuals^2), #LM5の残差(2乗)
                color="orange",         #枠線をオレンジ
                fill ="orange",         #塗りもオレンジ
                alpha=0.2  ) +          #透明度を指定
  geom_density( aes(x=LM6$residuals^2), #LM6の残差(2乗)
                color="brown",          #枠線をブラウン
                fill ="brown",          #塗りもブラウン
                alpha=0.2  ) +          #透明度を指定
  xlab("残差の2乗")  #軸ラベル

