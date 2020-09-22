#Rを使った相関分析

#東京都の自治体の特性指標データを読み込む
DF <- read.table( "TokyoSTAT_six.csv",
                  sep = ",",                #カンマ区切りのファイル
                  header = TRUE,            #1行目はヘッダー(列名)
                  stringsAsFactors = FALSE, #文字列を文字列型で取込む
                  fileEncoding="UTF-8")     #文字コードはUTF-8

#データの構造と項目の一覧を確認する
str(DF)

#データフレームから1列目と2列目を除いて先頭を表示
head(DF[, -c(1, 2)])

# カンマの前が行、後が列を表す
# 行は省略されているので全ての行が対象となる
# 列は1列目と2列目が除かれる

# 複数の行や列を指定する場合はc()で括りベクトルとして扱う
# マイナスをつけると除外するという意味になる


#(1)散布図マトリクスの表示

#標準のparis()を使う場合
pairs(DF[, -c(1, 2)]) 

#より進んだグラフィック表示を試みる

#23区とそれ以外を区別するラベルを作る(後で描画の際に使う)
DF$区部 <- "市町"          #区部という名前の列を作る
DF[1:23, ]$区部 <- "区"    #最初の23行の値を区に変更

#ライブラリlatticeのsplom()を使う
library(lattice)
splom(DF[, -c(1, 2, 9)],   #散布図からは区部(9列目)を除く
      groups=DF$区部,      #色分け
      axis.text.cex=.3,    #目盛りのフォントサイズ
      varname.cex=.5)      #項目名のフォントサイズ

#ライブラリGGallyのggpairs()で散布図マトリクスを描く
#少し時間がかかる
library(ggplot2)
library(GGally)
ggpairs(DF[, -c(1, 2)],                   #区部(9列目)も含める
        aes( colour=as.factor(区部),      #色分け
             alpha=0.5),                  #透明度
        upper=list(continuous=wrap("cor", size=3)) ) +
  #相関係数の文字サイズ
  theme(axis.text =element_text(size=6),  #軸の文字サイズ
        strip.text=element_text(size=6))  #項目の文字サイズ


#(2)相関行列の出力

#相関行列を計算してオブジェクトCORに格納
COR <- cor(DF[, -c(1, 2, 9)])
#CORの内容を表示
COR


#(3)相関係数のグラフ表示

#ライブラリ qgraph を使いr=.20を基準として視覚化
library(qgraph)
qgraph( COR, 
        minimum=.20,         #.20以上の相関関係を表示 
        labels=colnames(COR),#ラベルを省略せずに表示
        edge.labels=T,       #辺に相関係数を表示
        label.scale=F,       #項目名を一定の大きさで表示  
        label.cex=0.8,       #項目名のフォントサイズ
        edge.label.cex=1.4 ) #辺のフォントサイズ


#(4)相関係数について有意確率を求める

#2変数間の相関係数計算してオブジェクトTestResに格納
TestRes <- cor.test(DF$世帯あたり人数, DF$昼間人口比_per)
#TestResを表示
TestRes

#一般に、p-valueの値が0.05を下回れば有意とみなす

