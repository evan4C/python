#フィッティングと決定係数

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
LMyx <- lm( overtime ~ tenure, data=DFsub )
summary(LMyx)

#実測値の平均
M <- mean(DFsub$overtime)

#理論値（元のデータの説明変数に基づく予測値）を求める
f <- predict(LMyx, newdata=DFsub)
#予測値の平均
Mf <- mean(f)

#実測値の平均と理論値の平均を表示
M   #実測値の平均
Mf  #予測値の平均
#多少の誤差は出るが同じなので、以下ではMを使う

#残差の二乗和
S  <- sum((f - DFsub$overtime)^2)
#実測値の分散（平均からの差の二乗和）
Vy <- sum((DFsub$overtime - M)^2)
#予測値の分散（平均からの差の二乗和）
Vf <- sum((f - M)^2)

#値を比較
Vy      #実測値の分散
Vf + S  #予測値の分散+残差

#これらから決定係数を求める
R2 = 1 - S/Vy

#lmの結果からR2とadj R2を取得
R2_lm    <- summary(LMyx)$r.squared
R2adj_lm <- summary(LMyx)$adj.r.squared

#値を比べてみる
R2     #手計算のR2
R2_lm  #lm()のR2
R2adj_lm #lm()の調整済みR2

#xとyの相関係数を求めて二乗する
cor(DFsub$tenure, DFsub$overtime) ^ 2
