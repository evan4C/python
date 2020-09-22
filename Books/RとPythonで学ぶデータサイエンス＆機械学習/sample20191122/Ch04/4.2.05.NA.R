#欠損値

#5件の簡単なサンプルデータ
DF <- data.frame(英語 = c(98, 85, 72, NA, 85),
                 数学 = c(NA, 67, 86, 78, 92),
                 国語 = c(85, 88, 76, 92, NA))
#内容を表示
DF

#平均値を出す
mean(DF$英語)          #結果はNAとなる
mean(DF$英語, na.rm=T) #NAを識別しNAを除いた値で算出

#要約統計量を確認
summary(DF) #NAを識別しNAを除いた値で算出

#欠損値を判別する関数
is.na(DF$英語)

#欠損値でないデータだけを抽出して表示
notNA <- !is.na(DF$英語) #論理演算で!はnotを表す
notNA                    #欠損値でないものがTRUE
DF[notNA, 1]             #TRUEに相当する行の1列目を表示

#リストワイズ
na.omit(DF) #3件がNAを含むので2件だけとなる

#相関係数
cor(DF)                              #結果はNAとなる
cor(DF, use="complete.obs")          #リストワイズ（2件）
cor(DF, use="pairwise.complete.obs") #ペアワイズ（4件）

#データフレームをコピー
DFa <- DF
#欠損値を平均値で置き換える
DFa[!notNA, 1] <- mean(DF$英語, na.rm=T)

#元のデータと置換後のデータで平均値を比較
mean(DFa$英語)
mean(DF$英語, na.rm=T)
#元のデータと置換後のデータで分散を比較
var(DFa$英語)
var(DF$英語, na.rm=T)
#平均値を補充した結果、分散が小さくなってしまったことがわかる

