#多重共線性

#目的変数：スタッフのモチベーション Score
#説明変数：10人あたりの年間の業務評価面接回数 Meeting
#　　　　　3年間に職務や待遇の変化があった人数の比率 Reassign

#データの読込み
DF <- read.table("ESSurvey.csv",
                 sep = ",",                #カンマ区切りのファイル
                 header = TRUE,            #1行目はヘッダー(列名)
                 stringsAsFactors = FALSE) #文字列を文字列型で取込む

#データフレームの内容を表示
head(DF)
#要約統計量
summary(DF)

#目的変数の値のヒストグラム
hist(DF$Score, breaks=30, col="palegreen")

#ペアプロットを描く
pairs(DF)
#相関係数
cor(DF)

#通常の線形回帰モデル
#"."を指定すると目的変数以外の全ての変数を使う
LE1 <- lm( Score ~ ., data=DF)
summary(LE1)

#残差のヒストグラム
hist(LE1$residuals, breaks=25, col="yellow3")
#診断プロット
par(mfrow=c(2,2))
plot(LE1)
par(mfrow=c(1,1))

#モデルの多重共線性について確認
#ライブラリを読み込む
library(car)

#vif(): VIFを計算する関数
vif(LE1)
#10未満であることを目安とする



#交互作用項を含むモデル
#　LE1の式に交互作用項を加えた形で記述
LE2 <- lm( Score ~ .+ Meeting*Reassign, data=DF)
summary(LE2)

#残差のヒストグラム
hist(LE2$residuals, breaks=25, col="yellow3")
#診断プロット
par(mfrow=c(2,2))
plot(LE2)
par(mfrow=c(1,1))

#モデルについてVIFの値を確認
vif(LE2)

#交互作用項と各変数との相関係数を確認
cor(DF, DF$Meeting*DF$Reassign)



#中心化(centering)処理を行う
#※交互作用項と元の変数との相関を下げる効果がある
#　各変数について平均値との差を取り元の値を置き換える
DFc <- DF 
DFc$Meeting  <- DFc$Meeting  - mean(DF$Meeting)
DFc$Reassign <- DFc$Reassign - mean(DF$Reassign)

#各説明変数について平均が0になっていることを確認
summary(DFc)

#モデル
LE3 <- lm( Score ~ .+ Meeting*Reassign, data=DFc)
summary(LE3)

#VIFの値を確認
vif(LE3)

#交互作用項と各変数との相関係数を確認
cor(DFc, DFc$Meeting*DFc$Reassign)

#3つのモデルのAICを確認
AIC(LE1)
AIC(LE2)
AIC(LE3)



#これまでに作成した残業時間のモデルについてVIFを確認

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

#交互作用を含まないモデル
LM5 <- lm( overtime ~ section + tenure, data=DF)
#交互作用を含むモデル
LM6 <- lm( overtime ~ section + tenure 
           + section*tenure, data=DF)

#VIFの値を確認
vif(LM5)
vif(LM6)
#ライブラリcarのvif()関数の仕様：
# カテゴリ変数(3水準以上)がなければ通常のVIFを計算
# カテゴリ変数(3水準以上)がある場合、GVIFを計算

#この場合は右端の値 GVIF^(1/(2*Df))を確認
#極端に大きい値がないかを確認する

