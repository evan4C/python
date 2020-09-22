#決定木

#乱数の種を設定（実行の度に同じ乱数を発生させる）
set.seed(9999)

#顧客の解約データを読み込む
DF <- read.table( "CsLeave.csv", 
                  sep = ",",                #カンマ区切りのファイル
                  header = TRUE,            #1行目はヘッダー(列名)
                  stringsAsFactors = FALSE, #文字列を文字列型で取込む
                  fileEncoding="UTF-8")     #文字コードはUTF-8
#内容を確認
str(DF)
summary(DF)

#決定木(CART)のライブラリ
library(rpart)

#目的変数～説明変数の形で記述
#説明変数を"."とすることで、全ての項目が投入される
#ここではカテゴリの判別に使うのでmethodに"class"を指定
CRT1 <- rpart(契約 ~ ., 
                data = DF[, -1], method = "class")
#結果の確認
CRT1

#決定木の表示
#描画ライブラリの読込み
library(rpart.plot)

#rpart.plot：ツリーの表示
# tweak   ：図の中に表示する文字の大きさ
# roundint：分岐条件の数値を整数に丸めるかどうか
rpart.plot(CRT1, tweak=1.0, roundint=FALSE)

#type(0-4)とextra(0-9)で表示形式を変えられる
#under＝数値の表示位置（ノードの中：0, ノードの下：1）
rpart.plot(CRT1, 
           type=4,       #ルールを枝の途中に表示する
           extra=1,      #比率ではなくケース数を表示する
           roundint = FALSE,   #分岐条件の数値を丸めない
           under=TRUE)   #比率またはケース数を中ではなく下に表示

#prp：ツリーの表示（より細かい指定が可能）
prp(CRT1, 
    type = 4,               #分岐の表示書式：0-4 
    extra = 101,            #101で数、105で比率を表示
    nn = TRUE,              #ノード番号の表示
    tweak = 1.0,            #文字サイズ
    space = 0.1,            #ノード内の余白(標準は1.0)
    shadow.col = "grey",    #影の色を指定
    col = "black",          #ノードラベルの文字色 
    split.col = "brown3",   #分岐条件の文字色
    branch.col = "brown3",  #枝の色
    fallen.leaves = FALSE,  #末端ノードを下揃えしない
    roundint = FALSE,       #分岐条件の数値を丸めない
    box.col = c("pink", "palegreen3")[CRT1$frame$yval])
                            #比率の大小で色分け
# 文字サイズは描画前のPlotエリアの大きさでも変化する


#枝の数を増やす
#cp値の設定によって枝の数が変わる
CRT2 <- rpart(契約 ~ .,
              data = DF[, -1], 
              method = "class",
              control=rpart.control(minsplit=20,  #ノードの最小ケース数
                                    minbucket=10, #末端ノードの最小ケース数
                                    maxdepth=20,  #階層の最大数
                                    cp=0.005))    #cp値
#結果の確認
CRT2

#cp値の表示
printcp(CRT2)

#cp値ごとの予測誤差を図示
# xerror：交差妥当化に基づく誤差の程度（大きいと良くない）
plotcp(CRT2)


#枝の数を減らす
CRT3 <- rpart(契約 ~ .,
                data = DF[, -1], 
                method = "class",
                control=rpart.control(minsplit=20,  #ノードの最小ケース数
                                      minbucket=10, #末端ノードの最小ケース数
                                      maxdepth=20,  #階層の最大数
                                      cp=0.015))    #cp値
#結果の確認
CRT3

#ツリーの表示
prp(CRT3, 
    type = 4,               #分岐の表示書式：0-4 
    extra = 101,            #101で数、105で比率を表示
    nn = TRUE,              #ノード番号の表示
    tweak = 1.0,            #文字サイズ
    space = 0.1,            #ノード内の余白(標準は1.0)
    shadow.col = "grey",    #影の色を指定
    col = "black",          #ノードラベルの文字色 
    split.col = "brown3",   #分岐条件の文字色
    branch.col = "brown3",  #枝の色
    fallen.leaves = FALSE,  #末端ノードを下揃えしない
    roundint = FALSE,       #分岐条件の数値を丸めない
    box.col = c("pink", "palegreen3")[CRT1$frame$yval])
#比率の大小で色分け


#モデルに基づく予測値
#予測用のサンプルデータ(5件)を読み込む
DFnew <- read.table( "CsNew.csv", 
                     sep = ",",                #カンマ区切りのファイル
                     header = TRUE,            #1行目はヘッダ(列名)
                     stringsAsFactors = FALSE, #文字列を文字列型で取込む
                     fileEncoding="UTF-8")     #文字コードはUTF-8
#内容を確認
head(DFnew)

#新しいデータをモデルに当てはめる
PredY <- predict(CRT3, newdata=DFnew)
#predictの結果はNとYのそれぞれの確率(比率)で表される
PredY

#継続の確率（2列目の値）を0/1の値に変換する
PredY[, 2] >= 0.5
