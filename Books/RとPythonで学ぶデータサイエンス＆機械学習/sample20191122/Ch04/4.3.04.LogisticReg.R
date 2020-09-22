#目的変数が2値のカテゴリ変数の場合

#ロジスティック回帰の考え方
#簡単なサンプルデータ
y = c( 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1)
x = c(-5,-4,-3,-2,-1,-1, 1, 1, 2, 3, 4, 5)
#散布図を描画
plot(x, y,                      #xを横軸、yを縦軸
     col="blue", pch=16,            #pch=16で塗り潰した丸
     xlim=c(-5, 5), ylim=c(0, 1) )  #x軸とy軸の範囲を指定

#xの値からyの値(0か1か)を推定するモデル
GM <- glm(y ~ x, family=binomial(logit))
#回帰係数
GM$coefficients
GMb0 <- GM$coefficients[1]
GMb1 <- GM$coefficients[2]

#モデル上の予測値を追加
par(new=TRUE)                       #重ね描きの指定
plot(x, GM$fitted.values,           #xを横軸、予測値を縦軸
     col="orange", pch=16,          #pch=16で塗り潰した丸
     xlim=c(-5, 5), ylim=c(0, 1),   #x軸とy軸の範囲を指定
     axes=FALSE,                    #軸を表示しない
     xlab="", ylab="")              #軸ラベルを表示しない
par(new=FALSE)                      #重ね描きを解除

#plot()の中に回帰式を指定
plot(function(x) 1/(1+exp(-GMb0-GMb1*x)), 
     #変数xを生成する範囲を-5から5まで指定、前の図に追加
     -5, 5, col="red", add=TRUE)
#y=0.5の直線を引く
#   点(-5, 0.5)から点(5, 0.5)まで線を引けばよい
#   lines(X, Y)でXとYのベクトルを指定する（散布図と同じ）
lines(c(-5, 5), c(0.5, 0.5), col="grey")
#x=0の直線を引く
#   点(0, 0)から点(0, 1)まで線を引けばよい
lines(c(0, 0), c(-0, 1), col="grey")

#縦軸をロジット変換して図を描く
#yの予測値をロジット変換
LogitY <- log( GM$fitted.values/(1-GM$fitted.values) )
#散布図で描画
plot(x, LogitY,             #xを横軸、予測値を縦軸
     col="orange", pch=16)  #pch=16で塗り潰した丸
#plot()の中に回帰式を指定
plot(function(x) GMb0+GMb1*x, 
     #変数xを生成する範囲を-5から5まで指定、前の図に追加
     -5, 5, col="red", add=TRUE)
#y=0の直線を引く
lines(c(-5, 5), c(0, 0), col="grey")
#x=0の直線を引く
lines(c(0, 0), c(-5, 5), col="grey")



#顧客の解約データを読み込む
DF <- read.table( "CsLeave.csv", 
                  sep = ",",                #カンマ区切りのファイル
                  header = TRUE,            #1行目はヘッダー(列名)
                  stringsAsFactors = FALSE, #文字列を文字列型で取込む
                  fileEncoding="UTF-8")     #文字コードはUTF-8
#内容を確認
str(DF)
summary(DF)

#カテゴリ変数を数値から文字列に変換
DF$OL申込 <- as.character(DF$OL申込)
DF$C応募  <- as.character(DF$C応募)
DF$FM登録 <- as.character(DF$FM登録)
DF$ML購読 <- as.character(DF$ML購読)

#目的変数の内訳を確認
table(DF$契約)

#テーブルプロットによる可視化
library(tabplot)
#契約の有無（解約）によるソート
tableplot(DF[, -1], sortCol ="契約")
#通話分数によるソート
tableplot(DF[, -1], sortCol ="通話分数")

#目的変数が文字列で記述されているので、1と0に置換
DF$契約[DF$契約=="Y"] <- 1 #契約あり
DF$契約[DF$契約=="N"] <- 0 #契約なし（解約）
#そのままでは文字列なので、整数に変換
DF$契約 <- as.integer(DF$契約)

#一般化線形モデル
#  binomialは目的変数が二項分布に従うという仮定を示す
#   (logit)は線形モデルをlogit変換することを示す
GC1 <- glm(契約 ~ 年齢, 
             family=binomial(logit), data=DF)
summary(GC1)
#パラメータの値
GC1$coefficients
#切片と回帰係数（描画のために取り出しておく）
GC1b0 <- GC1$coefficients[1]
GC1b1 <- GC1$coefficients[2]
#年齢が1才増えると、オッズは何倍？
exp(GC1b1)
#年齢が10才増えると、オッズは何倍？
exp(GC1b1*10)

#実測値を年齢ごとに平均（契約継続の比率）
y_Age <- tapply(DF$契約, DF$年齢, mean)
#年齢のラベル(20から90までの数字)
Age   <- as.integer( names(y_Age) )
#縦軸を契約継続の比率、横軸を年齢でプロットする
plot(Age, y_Age, col="blue", pch=16,
     xlim=c(-90, 100), ylim=c(0, 1))
#plot()の中に回帰式を指定
plot(function(x) 1/(1+exp(-GC1b0-GC1b1*x)), 
     #変数xを生成する範囲を-5から5まで指定、前の図に追加
     -90, 100, col="red", add=TRUE)

#疑似決定係数の算出
library(BaylorEdPsych)
PseudoR2(GC1)[1]



#説明変数を"."とすることで、全ての項目が投入される
#ただし、1列目はIDなので除く
GC2 <- glm(契約 ~ ., 
             family=binomial(logit), data=DF[, -1])
summary(GC2)
#疑似決定係数の算出
PseudoR2(GC2)[1]

#ステップワイズ法で有用な変数のみを残す
GC3 <- step(GC2)
summary(GC3)
#疑似決定係数の算出
PseudoR2(GC3)[1]
#VIFの算出
library(car)
vif(GC3)

#オッズの比を計算
exp(GC3$coefficients[3]*10)  #年齢が10歳高い
exp(GC3$coefficients[4])     #B社機種（A社との比較）
exp(GC3$coefficients[5])     #C社機種（A社との比較）
exp(GC3$coefficients[10]*10) #通話が10分長い
exp(GC3$coefficients[11]*10) #通話回数が10回多い

#通話分数と回数との相関
cor.test(DF$通話分数, DF$通話回数)

#料金コースと他の変数との関係
boxplot(DF$年齢 ~ DF$コース, col="orange")
mosaicplot(table(DF$コース, DF$機種), shade=TRUE)



#モデルに基づく予測値
#予測用のサンプルデータ(5件)を読み込む
DFnew <- read.table( "CsNew.csv", 
                  sep = ",",                #カンマ区切りのファイル
                  header = TRUE,            #1行目はヘッダ(列名)
                  stringsAsFactors = FALSE, #文字列を文字列型で取込む
                  fileEncoding="UTF-8")     #文字コードはUTF-8
#内容を確認
head(DFnew)

#カテゴリ変数を数値から文字列に変換
DFnew$OL申込 <- as.character(DFnew$OL申込)
DFnew$C応募  <- as.character(DFnew$C応募)
DFnew$FM登録 <- as.character(DFnew$FM登録)
DFnew$ML購読 <- as.character(DFnew$ML購読)

#新しいデータをモデルに当てはめる
PredY <- predict(GC3, newdata=DFnew)
#predictの結果はロジット変換された確率であることに注意
PredY
#標準シグモイド関数を使って変換前の値に戻す
PredY <- 1/(1 + exp(-PredY))
PredY

#以下の方法でも同じ
PredY <- predict(GC3, newdata=DFnew, type="response")
#　type="response" でロジット変換前の値を取得できる
PredY

#継続の確率を0/1の値に変換する
PredY >= 0.5

