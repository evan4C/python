#簡単な線形回帰モデル

#目的変数：残業時間 overtime
#説明変数：勤続年数 tenure
#　　　　　部門 section（Ademin, IT, Sales ）

#データの読込み
DF <- read.table("StaffOvertime.csv",
                  sep = ",",                #カンマ区切りのファイル
                  header = TRUE,            #1行目はヘッダー(列名)
                  stringsAsFactors = FALSE) #文字列を文字列型で取込む

#データの構造と項目の一覧を確認する
str(DF)

#データフレームの先頭と最後を表示
head(DF)
tail(DF)

#関数summary()を使って平均値,中央値などを表示
summary(DF)

#ヒストグラムを表示（x軸の区間は30分割する）
hist(DF$overtime, breaks=30, col="orange2")
hist(DF$tenure,   breaks=30, col="steelblue")

#残業時間と勤続年数の関係を図示（標準のplot()関数）
plot(DF$tenure, DF$overtime)

#残業時間と勤続年数の関係を図示
library(ggplot2)
ggplot(DF, aes( x=tenure, y=overtime) )+           #x軸とy軸を指定
  geom_point(colour="purple", size=3, alpha=0.7)+  #色,サイズ,透明度
  stat_smooth(method="lm", se=T)                   #回帰直線を加える
  # seは回帰直線を描く際に上下に幅（95％信頼区間）を持たせる指定
  # se=Tで直線に幅を加えて描く（se=Fで直線のみを描く）  

#関数lm()を使って回帰モデルを作成する
#扱う変数を括弧内に 目的変数~説明変数 の形で記述
#これだけでは詳しい情報は表示されない
lm( overtime ~ tenure, data=DF)

#モデルを一旦LM1という名前でオブジェクトに格納する
LM1 <- lm( overtime ~ tenure, data=DF)

#一旦格納したモデルを関数summary()で表示する
#この場合はより詳しい情報が表示される
summary(LM1)

