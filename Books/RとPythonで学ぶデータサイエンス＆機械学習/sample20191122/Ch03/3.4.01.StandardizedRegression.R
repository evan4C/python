#説明変数の効果の度合い

#目的変数：スタッフのモチベーション Score
#説明変数：10人あたりの年間の業務評価面接回数 Meeting
#　　　　　3年間に職務や待遇の変化があった人数の比率 Reassign

#データの読込み
DF <- read.table("ESSurvey.csv",
                  sep = ",",                #カンマ区切りのファイル
                  header = TRUE,            #1行目はヘッダー(列名)
                  stringsAsFactors = FALSE) #文字列を文字列型で取込む

#通常の線形回帰モデル
#"."を指定すると目的変数以外の全ての変数を使う
LE1 <- lm( Score ~ ., data=DF)
summary(LE1)

#データを標準化する
#scale()：標準化を行う関数
# scaleの出力結果はマトリクス形式なので、
# as.data.frame()を使ってデータフレームに直す
DFst <- as.data.frame( scale(DF) )

#平均値、中央値等を確認
summary(DFst)
#標準偏差を確認
# DFstのそれぞれの列単位に関数sd()を適用
# apply()の引数の2は「列単位」という指定を示す
apply(DFst, 2, sd)

#標準化されたデータに基づく線形回帰モデル
LE4 <- lm( Score ~ ., data=DFst)
summary(LE4)
#偏回帰係数（Estimate）の欄が標準偏回帰係数


#ライブラリlm.betaを使う（一般にはこちらが便利）
library(lm.beta)

#通常の方法で作成したモデルをインプットとする
LE5 <- lm.beta(LE1)
summary(LE5)
#通常の結果に標準偏回帰係数の情報が加わる


#参考：偏回帰係数から標準偏回帰係数を算出

#元のモデルLE1の偏回帰係数
LE1$coefficients
#目的変数の標準偏差
ySD  <- sd(DF$Score)
#説明変数の標準偏差
x1SD <- sd(DF$Meeting)
x2SD <- sd(DF$Reassign)

#各説明変数の標準偏回帰係数を求める
#標準偏回帰係数＝
#  偏回帰係数＊説明変数の標準偏差／目的変数の標準偏差
LE1$coefficients[2] * x1SD / ySD
LE1$coefficients[3] * x2SD / ySD
