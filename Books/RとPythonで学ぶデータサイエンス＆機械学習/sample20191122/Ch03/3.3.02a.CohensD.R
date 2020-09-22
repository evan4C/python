#乱数の種を設定（実行の度に同じ乱数を発生させる）
set.seed(120) #引数とする数値を変えると結果が変わる

#乱数でデータを2セット作成
#  rnorm(件数, 平均, SD)：正規分布にしたがう乱数
A <- rnorm(10000,  1, 1) #平均 1, SD1 
B <- rnorm(10000, -1, 1) #平均-1, SD1

#密度プロットを作成
ggplot()+
  geom_density( aes(x=A),      #描画の対象となる変数
                color="darkgreen", #線の色
                fill ="darkgreen", #塗り分けの色
                alpha=0.1)+        #透明度
  geom_density( aes(x=B),      #描画の対象となる変数
                color="orange",    #線の色
                fill ="orange",    #塗り分けの色
                alpha=0.1)+        #透明度
  xlab("group A vs.B")

#先ほどとはSDが異なるデータを2セット作る
C <- rnorm(10000,  1, 15) #平均 1, SD15 
D <- rnorm(10000, -1, 15) #平均-1, SD15 

#密度プロットを作成
ggplot()+
  geom_density( aes(x=C),      #描画の対象となる変数
                color="darkgreen", #線の色
                fill ="darkgreen", #塗り分けの色
                alpha=0.1)+        #透明度
  geom_density( aes(x=D),      #描画の対象となる変数
                color="orange",    #線の色
                fill ="orange",    #塗り分けの色
                alpha=0.1)+        #透明度
  xlab("group C vs.D")

#有意差検定をする準備としてデータを結合する
value1 <- c(A, B)
value2 <- c(C, D)
#説明変数を作る（グループ名のラベル）
# rep(値, 繰返し数)：1つの値を繰返してベクトルを作成
group1 <- c(rep("A", 10000), rep("B", 10000))
group2 <- c(rep("C", 10000), rep("D", 10000))
#有意確率と決定係数を確認
#　線形回帰モデルのp-valueはaovの結果と一致することに注意
#  有意確率はどちらも小さい
#  決定係数には大きな差がある
summary( aov(value1~group1) )  #分散分析(Prを確認)
summary( lm( value1~group1) )  #線形回帰モデル(R-squaredを確認)
summary( aov(value2~group2) )
summary( lm( value2~group2) )

#Cohens'dを算出するためのライブラリ
library(effsize)
#  Cohens'dには大きな差がある
cohen.d(A, B, hedges.correction=F) #Cohen's d を算出
cohen.d(C, D, hedges.correction=F) #Cohen's d を算出
