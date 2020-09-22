#ライブラリを読み込む
library(ggplot2)  #拡張グラフィック

#ファイルsample.csvを読み込みデータフレームDFに格納
#ヘッダ付データの場合、header=Tを指定する必要がある
DF <- read.table( "sample.csv",
                  sep = ",",      #カンマ区切り
                  header = TRUE ) #ヘッダー(列名)あり

#最初の6行を表示
head(DF)

#データ型などの確認
str(DF)

#要約統計量の確認
summary(DF)

#原点に近いデータを識別する
id <- DF$varA^2 + DF$varB^2 < 1
head(id)

#IDという名前で新しい列を作る
#値には全て"steelblue"を入れておく
DF$ID <- "steelblue"

#原点に近いデータのみIDの値を"darkblue"とする
DF$ID[id==T] <- "darkblue" 

#それぞれのデータがいくつあるかを確認
table(DF$ID)

#データフレームの内容を確認
head(DF)

#散布図を色分けして表示
#colorは色の指定、alphaは透明度、sizeは点の大きさ
ggplot() +
  geom_point(aes(DF$varA, DF$varB),
             color=DF$ID, size=4, alpha=0.6)

