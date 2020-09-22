#対数とロジット関数

#サンプルデータを読み込む
DF <- read.table( "incomex.csv", 
                   sep = ",",                #カンマ区切りのファイル
                   header = TRUE,            #1行目はヘッダ(列名)
                   stringsAsFactors = FALSE, #文字列を文字列型で取込む
                   fileEncoding="UTF-8")     #文字コードはUTF-8
#内容を確認
head(DF)
summary(DF)

#incomeのヒストグラム
hist(DF$income, breaks=50, col="cyan4")

#対数関数
plot(log, 0.01, 100)
#指数関数（eの累乗）
plot(exp, -5, 5)

#対数変換してヒストグラムを表示
hist(log10(DF$income), breaks=50, col="cyan4")  #常用対数
hist(log(DF$income),   breaks=50, col="cyan4")  #自然対数

#expenseのヒストグラム
hist(DF$expense,       breaks=50, col="brown")
hist(log(DF$expense),  breaks=50, col="brown")

#散布図を表示
plot(DF$income, DF$expense, col="brown")
#片対数変換
plot(DF$income, log(DF$expense), col="brown") #縦軸を対数変換
#両対数変換
plot(log(DF$income), log(DF$expense), col="brown") #両軸を対数変換


#サンプルデータを読み込む
# 表形式のデータではないため、関数scan()を使って読み込む
# what=numeric()で、数値データであることを指定する
rate <- scan("chratio.csv",  what = numeric())
#内容を確認
summary(rate)

#ratioのヒストグラム
hist(rate,   breaks=50, col="cadetblue")
hist(1-rate, breaks=50, col="cadetblue") #1から引いた値

#対数変換してヒストグラムを表示
hist(log(rate),   breaks=50, col="cadetblue")
hist(log(1-rate), breaks=50, col="cadetblue")  #1から引いた値

#ロジット関数
Logit   <- function(x){ log(x/(1-x)) }
#標準シグモイド関数
Sigmoid <- function(x){ 1/(1+exp(-x)) }
# いくつかのライブラリが関数を提供しているのでそれを使ってもよい

#ロジット関数
plot(Logit, 0, 1)
#標準シグモイド関数
plot(Sigmoid, -5, 5)

#ロジット関数で変換してヒストグラムを表示
hist(Logit(rate),   breaks=50, col="cadetblue")
hist(Logit(1-rate), breaks=50, col="cadetblue")  #1から引いた値

