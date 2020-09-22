#ダミー変数を使った回帰モデル

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

#部門別に平均値や中央値を確認する
#tapply()関数とsummary()関数を組み合わせる
#tapply(x, m, f)：
# xの値をmでグループ分けして関数fを適用
tapply(DF$overtime, DF$section, summary)

#boxplot()で中央値と四分位を視覚化
boxplot(overtime ~ section, data=DF, col="green")

#関数lm()を使って回帰モデルを作成する
#扱う変数を括弧内に 目的変数~説明変数 の形で記述
#sectionは自動的にダミー変数(IT, Sales)に展開される
lm( overtime ~ section, data=DF)

#モデルを一旦LM2という名前でオブジェクトに格納する
LM2 <- lm( overtime ~ section, data=DF)

#一旦格納したモデルを関数summary()で表示する
#この場合はより詳しい情報が表示される
summary(LM2)

#分散分析で全体の傾向に偏りがあると言えるかを検証
#aov()：分散分析
AOV <- aov(overtime ~ section, data=DF)
summary(AOV)

#グループが2つだけの場合は分散分析だけでよい
#グループが3つ以上の場合は多重比較で各グループ間の差を見る
#TukeyHSD()：テューキー法による多重比較
TukeyHSD(AOV)
