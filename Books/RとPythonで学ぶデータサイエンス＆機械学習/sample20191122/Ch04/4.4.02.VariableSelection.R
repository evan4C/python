#説明変数をどう選ぶか

#目的変数：年間の来店客数 y                   yVisit
#説明変数：年間の販促費 x                     xPromo
#　　　　　立地などに基づく商圏規模 z         zScale
#　　　　　年間のチラシ枚数 w                 WFlyer
#          年間の店頭でのキャンペーン応募数 v vEntry

#販促費x(原因)から来店客数 y(結果)への影響度合いを知りたい
#ただし xとyは zから影響を受ける
#       xはwに、wはyに影響する
#       xとyはともにvに影響する


#データの読込み
DF <- read.table("Promotion.csv",
                 sep = ",",                #カンマ区切りのファイル
                 header = TRUE,            #1行目はヘッダー(列名)
                 stringsAsFactors = FALSE) #文字列を文字列型で取込む

#データフレームの内容を表示
head(DF)
#要約統計量
summary(DF)

#目的変数の値のヒストグラム
hist(DF$yVisit, breaks=20, col="palegreen")

#散布図を描く
library(ggplot2)
ggplot(DF) +
  geom_point(aes(xPromo, yVisit), size=4, alpha=.5)

#相関係数
cor(DF[, -1])


#線形回帰モデル
#標準偏回帰係数を出力するライブラリ
library(lm.beta)

#直接に効果を知りたい変数のみを使う
LC1 <- lm( yVisit ~ xPromo, data=DF)
summary(lm.beta(LC1)) #標準偏回帰係数を追加して出力


#交絡変数（商圏規模）を加える
LC2 <- lm( yVisit ~ xPromo + zScale, data=DF)
summary(lm.beta(LC2))

#散布図を描く（商圏規模で色分け）
ggplot(DF) +
  geom_point(aes(xPromo, yVisit, color=zScale), 
             size=4, alpha=.5)


#合流点の変数（キャンペーン応募数）を加える
LC3 <- lm( yVisit ~ xPromo + vEntry, data=DF)
summary(lm.beta(LC3))

#散布図を描く（キャンペーン応募数で色分け）
ggplot(DF) +
  geom_point(aes(xPromo, yVisit, color=vEntry), 
             size=4, alpha=.5)


#中間変数（チラシの枚数）を加える
LC4 <- lm( yVisit ~ xPromo + wFlyer, data=DF)
summary(lm.beta(LC4))

#LC1に中間変数（チラシの枚数）を加えた場合
LC5 <- lm( yVisit ~ xPromo + zScale + wFlyer, data=DF)
summary(lm.beta(LC5))

