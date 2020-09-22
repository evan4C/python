#残差の分布

#目的変数：残業時間 overtime
#説明変数：勤続年数 tenure
#　　　　　部門 section（Ademin, IT, Sales ）

#データの読込み
DF <- read.table("StaffOvertime.csv",
                 sep = ",",                #カンマ区切りのファイル
                 header = TRUE,            #1行目はヘッダー(列名)
                 stringsAsFactors = FALSE) #文字列を文字列型で取込む

#データフレームの先頭を表示
head(DF)

#交互作用を含むモデル
LM6 <- lm( overtime ~ section + tenure 
           + section*tenure, data=DF)
summary(LM6)

#残差の分布
library(ggplot2)
ggplot()+
  geom_density( aes(x=LM6$residuals), #LM6の残差
                color="brown",        #枠線をブラウン
                fill ="brown",        #塗りもブラウン
                alpha=0.2  ) +        #透明度を指定
  xlab("残差(モデル上の理論値－実測値)")  #軸ラベル

#標準で用意されているプロットを使って表示
par(mfrow=c(2,2))
plot(LM6)
par(mfrow=c(1,1))


