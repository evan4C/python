#クラスタリング


#顧客ごとのRFMデータを使う

#データを読み込む
DF <- read.table( "CustomerRFM.csv", 
                  sep = ",",                #カンマ区切りのファイル
                  header = TRUE,            #1行目はヘッダー(列名)
                  stringsAsFactors = FALSE, #文字列を文字列型で取込む
                  fileEncoding="UTF-8")     #文字コードはUTF-8
#内容を確認
head(DF)
summary(DF)

#数値項目だけを取り出す（年月は数値型に変換）
DFn <-DF[, c(2:4)]
DFn$recency <- as.Date( DFn$recency )       #文字列を日付型に変換
DFn$recency <- as.numeric( DFn$recency )    #日付型を数値に変換

#scale()を使って標準得点に変換する(物差しをそろえる)
#変換結果はマトリクスなのでデータフレームに戻す必要
DFn <- data.frame( scale(DFn) )
summary(DFn)

#行の名前rownamesを行数から顧客IDに変更しておく
rownames(DFn) <- DF$ID
head(DFn)



#階層型クラスタリングを実行する

#dist()で距離行列を計算する
DIST <- dist( DFn )
head(DIST)

#階層型クラスタリングを実行し樹形図を表示
result.hc <- hclust( DIST, method = "ward.D2" )
plot( result.hc, hang=0.2 )

#クラスタ数を指定してクラスタ番号のラベルを取得する
num.hc <- cutree( result.hc, k=4 )  #クラスタ番号を取得
num.hc <- factor( num.hc )          #数値をカテゴリに変換
head(num.hc)
# Levels:はカテゴリの水準（グループ）を示す
# 1,2,...という値に"1","2",...というラベルが対応
# この例は値とラベルが同じだが通常は"東京","大阪"などを対応させる

#クラスタごとの数を確認(樹形図と見比べておく)
table( num.hc )

#クラスタで分けて各変数のボックスプロットを描く
#変数が3つ(3列)あるので、for文で1列ごとに描く
for (i in 1:3) { 
  boxplot( DFn[, i] ~ num.hc, 
           main = colnames(DFn)[i], 
           #タイトル(main)を列の名前から取得
           col="steelblue" )
}



#k-meansによるクラスタリング

#対象データの後にクラスタ数を指定する(以下の例では3)
#iter.maxは最大繰り返し数
km <- kmeans(DFn, 4, iter.max=30) 

#クラスタ番号のラベルを確認する
head(km$cluster)

#クラスタごとの数を確認
table(km$cluster)

#クラスタで分けて各変数のボックスプロットを描く
#変数が3つ(3列)あるので、for文で1列ごとに描く
for (i in 1:3) { 
  boxplot( DFn[, i] ~ km$cluster, 
           main = colnames(DFn)[i], 
           #タイトル(main)を列の名前から取得
           col="coral2" )
}



#散布図を描く
#ライブラリGGallyのggpairs()で散布図マトリクスを描く
#少し時間がかかる
library(ggplot2)
library(GGally)
ggpairs(DFn,
        aes( colour=num.hc,  #クラスタ番号で色分け
             shape =num.hc,  #形も分ける
             alpha=0.9),     #透明度
        lower=list(continuous=wrap("points",size=4)),
        #左下に散布図を描く
        upper=list(continuous=wrap("cor",   size=4)) ) +
        #右上に相関係数を記述する
  theme_bw() #背景を白に指定

#3D描画ライブラリを読み込む
library("threejs")

#色指定の作成（クラスタ番号の配列をもとに色名に変換）

#色ラベルの配列を作るためにクラスタ番号の配列をコピー
#ここでは階層クラスタリングの結果を使う
color.hc <- num.hc
head(color.hc)

#クラスタ番号を色の名前に変換する
#levels()：factor（カテゴリ変数）のラベルの指定
levels(color.hc) = c("lightpink", "green4", "deepskyblue4", "plum2")
head(color.hc)
# Levels:はカテゴリの水準（グループ）を示す
# 1,2,...という整数の値に色の名称が対応

#factorの実体は整数なので文字列に変換（ラベルの値が実体となる）
color.hc <- as.character(color.hc)
head(color.hc)

#scatterplot3js：3Dプロット
#引数の最初に3次元データを指定（matrix形式に変換）
#color ：色分けのために各サンプルに対応する色名の配列を指定
#labels：各ケースのラベル（この場合は顧客ID）を指定
#size  ：各プロットの大きさ
#この場合は座標データ、色、ラベルを全て別のオブジェクトから拾っている
scatterplot3js(as.matrix(DFn),  #座標データ
               color=color.hc,  #色の指定(文字列のベクトル)
               labels=DF$ID,    #各ケースのラベル
               size=.5)

## プロットをもとにクラスタを解釈する
## それぞれはどのようなクラスタか？

