#分布の形を捉える

#高校生の身長データを読み込む
DF <- read.table( "height.csv", 
                  sep = ",",                #カンマ区切りのファイル
                  header = TRUE,            #1行目はヘッダー(列名)
                  stringsAsFactors = FALSE) #文字列を文字列型で取込む

#データの構造と項目の一覧を確認する
str(DF)

#データフレームの先頭を表示
head(DF)

#身長のヒストグラムを描く
hist(DF$height)

#色、分割数を変えてタイトルをつける
hist(DF$height, col="steelblue", breaks=50,
     main="高校生の身長の分布")


#ライブラリggplot2を使って描く
library(ggplot2)  #ライブラリの読み込み
#変数（データ項目）はaes()の中に、定数は外に書く
ggplot(DF)+                         #データフレームの指定
  geom_histogram( aes(height),       #描画の対象となる変数
                  fill="steelblue",  #塗り色の指定
                  alpha=0.8,         #透明度の指定
                  binwidth=1 )       #階級の幅(例では1cm刻み)

#密度プロットを描く
ggplot(DF)+                          #データフレームの指定 
  geom_density( aes(height) ) +          #描画の対象となる変数
  theme(axis.text=element_text(size=12), #文字サイズの指定 
       axis.title=element_text(size=14,face="bold"))


#性別で色分けしてヒストグラムを描く
ggplot(DF)+                          #データフレームの指定
  geom_histogram( aes(x   =height,     #描画の対象となる変数
                      fill=gender),    #塗り分けの対象となる変数
                  position="identity", #重ねて描くという指定
                  alpha=0.5,           #透明度の指定
                  binwidth=1 )         #階級の幅(例では1cm刻み)

#色を指定することも可能
ggplot(DF)+                          #データフレームの指定
  geom_histogram( aes(x   =height,     #描画の対象となる変数
                      fill=gender),    #塗り分けの対象となる変数
                  position="identity", #重ねて描くという指定
                  alpha=0.5,           #透明度の指定
                  binwidth=1 )+        #階級の幅(例では1cm刻み)
  #色分けの指定を足す
  #注意：前の行から+でつなげるのを忘れないこと）
  scale_fill_manual( values=c("darkgreen", "orange") )+
  #軸の文字サイズを変更する
  theme(axis.text =element_text(size=12, face="bold"), #軸の数値
        axis.title=element_text(size=14) )             #軸の名称

#性別で色分けして密度プロットを描く
ggplot(DF)+                          #データフレームの指定
  geom_density( aes(x    =height,      #描画の対象となる変数
                    color=gender) )+   #色分けの対象となる変数
  #色分けの指定を足す
  scale_color_manual( values=c("darkgreen", "orange") )

#中を塗ることも可能
ggplot(DF)+                          #データフレームの指定
  geom_density( aes(x    =height,      #描画の対象となる変数
                    color=gender,      #色分けの対象となる変数
                    fill =gender),     #塗り分けの対象となる変数
                    alpha=0.3  )+      #透明度の指定
  #色分けの指定を足す
  scale_color_manual( values=c("darkgreen", "orange") )+
  scale_fill_manual(  values=c("darkgreen", "orange") )+
  #軸の文字サイズとタイトルのフォントを変更する
  theme(axis.text =element_text(size=12, face="bold"), #軸の数値
        axis.title=element_text(size=14) )             #軸の名称


#性別でグループ分けをしてボックスプロットを描く
boxplot(DF$height ~ DF$gender,       #値(縦軸)とグループ分けを指定
                     col="orange")     #色の指定

boxplot(DF$height ~ DF$gender,       #値(縦軸)とグループ分けを指定
                     col="orange",     #色の指定
                     horizontal=T,     #向きの指定（Tで横、Fで縦）
        main="高校生の身長の分布")     #タイトル


#ライブラリggplot2を使って描く
ggplot(DF)+                          #データフレームの指定
  geom_boxplot( aes(y    =height,      #縦軸の変数
                    x    =gender,      #グループ化を行う変数
                    fill =gender),     #塗り分けの対象となる変数
                    alpha=0.7 )        #透明度の指定

#バイオリンプロットを描く
ggplot(DF)+                          #データフレームの指定
  geom_violin(  aes(y    =height,      #縦軸の変数
                    x    =gender,      #グループ化を行う変数
                    fill =gender),     #塗り分けの対象となる変数
                    alpha=0.5 )        #透明度の指定

#バイオリンプロットにボックスプロットを重ねて描く
ggplot(DF)+                          #データフレームの指定
  geom_violin(  aes(y    =height,      #縦軸の変数
                    x    =gender,      #グループ化を行う変数
                    fill =gender),     #塗り分けの対象となる変数
                    alpha=0.5 )+       #データフレームの指定
  geom_boxplot( aes(y    =height,      #縦軸の変数
                    x    =gender),     #グループ分けを行う変数
                    fill ="grey",      #色の指定
                    width=.2,          #幅を狭くする（20％）
                    alpha=0.7)+   　   #透明度の指定
  #色分けの指定を足す
  scale_color_manual( values=c("darkgreen", "orange") )+
  scale_fill_manual(  values=c("darkgreen", "orange") )
