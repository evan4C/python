#回帰モデルと説明・予測の向き

#目的変数：残業時間 overtime
#説明変数：勤続年数 tenure
#　　　　　部門 section（Ademin, IT, Sales ）

#データの読込み
DF <- read.table("StaffOvertime.csv",
                  sep = ",",                #カンマ区切りのファイル
                  header = TRUE,            #1行目はヘッダー(列名)
                  stringsAsFactors = FALSE) #文字列を文字列型で取込む

#IT部門のみを取り出す
#関数subset()で条件に合うデータだけを抽出する
DFsub <- subset(DF, section=="Admin")  　#!=はnot equalを示す

#データフレームの先頭を表示
head(DFsub)

#残業時間と勤続年数の関係を図示
library(ggplot2)
ggplot()+        #この例ではデータを一括で指定せず個別の描画の中で指定
  geom_point( aes(x=DFsub$tenure, y=DFsub$overtime), #データの指定
              colour="red", size=3, alpha=0.4 ) +    #色,サイズ,透明度
  stat_smooth(aes(x=DFsub$tenure, y=DFsub$overtime), #データの指定
              method="lm", se=F)                     #回帰直線

#勤続年数から残業時間を説明するモデル LMyx
LMyx <- lm( overtime ~ tenure, data=DFsub)
summary(LMyx)

#残業時間から勤続年数を説明するモデル LMxy
LMxy <- lm( tenure ~ overtime, data=DFsub)
summary(LMxy)


#以下は、予測値を使って2つの回帰直線を作図する手順

#予測に使うデータフレームを作る
#ゼロから作成してもよいが、コピーした方が楽
DFnew <- DFsub

#勤続年数（または残業時間）が0から40までの値のときに
#残業時間（または勤続年数）がいくらになるのかを予測

#予測のもとになる値として0から40までを等分した数列を作る
#もとのデータが101行あるので、便宜上101等分する
#0.0, 0.4, 0.8, 1.2, ...といった数列ができる

#予測用のデータの勤続年数を数列で置き換える
DFnew$tenure   <- seq(0, 40, length=101)
#予測用のデータの残業時間を数列で置き換える
DFnew$overtime <- seq(0, 40, length=101)

#IDとsectionは予測には関係ないので、そのままでよい

#作成したモデルと予測用のデータを使って予測を実行
#勤続年数xから残業時間yを予測する
pr_overtime <- predict(LMyx, newdata=DFnew)
#残業時間yから勤続年数xを予測する
pr_tenure   <- predict(LMxy, newdata=DFnew)

#予測結果（回帰直線）を散布図に重ねてプロットする
ggplot()+                                             #作図関数
  geom_point(aes( x=DFsub$tenure, y=DFsub$overtime),   #散布図
             colour="red", size=3, alpha=0.4 ) +        #元の実測データ
  geom_point(aes( x=DFnew$tenure, y=pr_overtime),      #散布図
             colour="blue3", size=0.5, alpha=0.8 ) +    #xからyを予測した値
  geom_point(aes( x=pr_tenure,    y=DFnew$overtime),   #散布図
             colour="green3", size=0.5, alpha=0.8 )     #yからxを予測した値
