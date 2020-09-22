#要約統計量を算出する

#高校生の身長データを読み込む
DF <- read.table( "height.csv", 
                  sep = ",",                #カンマ区切りのファイル
                  header = TRUE,            #1行目はヘッダー(列名)
                  stringsAsFactors = FALSE) #文字列を文字列型で取込む

#データフレームを指定して要約統計量を算出する
summary(DF)

#対象となる変数（項目）を指定して算出する
summary(DF$height)


#個別の関数を使って算出する
mean(DF$height)    #平均
median(DF$height)  #中央値
min(DF$height)     #最小値
max(DF$height)     #最大値
var(DF$height)     #分散（不偏分散）
sd(DF$height)      #標準偏差SD（不偏分散の平方根）

#参考：varとsd
#　　　確認のため不偏分散を計算してvに代入し、vと√vを表示
v <- sum( (DF$height-mean(DF$height))^2 ) / (length(DF$height)-1)
v ; sqrt(v)


#男女の数を確認する
#tableは集計を行う関数(カテゴリごとに数を数える)
table(DF$gender)

#男女別に統計量を算出する
#　tapply(対象, カテゴリ項目, 適用する関数)
#　対象をカテゴリの分類で分けてそれぞれに関数を適用する
#　この例では、heightをgenderで分けてsummaryを適用する
tapply(DF$height, DF$gender, summary)

#分散を男女別に算出する
tapply(DF$height, DF$gender, var)
