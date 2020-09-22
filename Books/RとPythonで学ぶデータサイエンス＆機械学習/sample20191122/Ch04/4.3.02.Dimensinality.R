#FA/PCA

#ファイルを読み込んでデータフレームを作成する
DF <- read.table( "TokyoSTAT_P25.csv", 
                  sep = ",", 
                  header = TRUE, 
                  stringsAsFactors = FALSE, 
                  fileEncoding="UTF-8")     #文字コードはUTF-8

#データの概要を確認する
str(DF)
summary(DF[, -c(1:2)])

#50の区市町を何らかの基準でクラスタに分けたい　…クラスタリング
#人気度がどのような要因に基づくのかを分析したい…回帰分析
#前処理として次元圧縮を行う

#ライブラリの読込み
library(psych)
#fa.parallel：平行分析（PA）の実施（視覚的に適切な因子数を判断）
#fm＝因子抽出法（minres最小残差法、pa主因子法、ml最尤法）
#ここでは最尤法を選択
#1-2列目はIDなので除く
#3列目は次元圧縮の対象ではないので除く
result.prl <- fa.parallel(DF[, -(1:3)], fm="ml")



#FA（因子分析）の実行

#fa：因子分析の実行
#fm＝因子抽出法（minres最小残差法、pa主因子法、ml最尤法）
#ここでは最尤法を選択
#nfactors＝因子数（抽出したい軸の数）
#rotate＝回転法（直交回転:varimax等、斜交回転:promax等）
#scores＝因子得点算出法
#1-2列目はIDなので除く
#3列目は次元圧縮の対象ではないので除く
resultFA <- fa(DF[, -(1:3)],
               nfactors=3,             #因子数を指定
               fm = "ml",              #pa 主因子法, ols 最小二乗法, ml 最尤法
               rotate = "varimax",     #varimax 直交、promax 斜交
               scores = "regression")  #regression 回帰法

#結果の表示
#digits＝小数点以下表示桁の指定
#sort=TRUEを指定（各項目ごとの因子負荷量がソートされる）
print(resultFA, digits=2, sort=TRUE) 

#結果を図で表示
fa.diagram(resultFA, 
           rsize=0.8, e.size=0.1, #四角と円のサイズ
           marg=c(.5,5,.5,.5),    #余白の設定
           cex=.6)                #文字サイズ

#結果の見方
#MRi...：各項目ごとの因子負荷量（各変数がどれだけ因子に寄与しているか）
#h2：共通性--各変数の値の変動が因子でどれだけ説明できるかを表す
#u2＝1-h2：独自性（uniqueness）--取りこぼしの度合（救えなかった情報）

#因子負荷量(変数ごとの因子への寄与)の値をタテヨコにプロットする
#　因子負荷量は、resultFAの中のloadingsに格納されている

#第1因子と第2因子
#枠のみを作成する
#   type="n"で点を描かない
plot(resultFA$loadings[, 1],
     resultFA$loadings[, 2], type="n") 
#枠内にテキストを表示する
#   テキストは因子負荷量のリストの行の名前を取得して使う
text(resultFA$loadings[, 1],
     resultFA$loadings[, 2], 
     rownames(resultFA$loadings), col="steelblue")
#y=0の直線を引く
#   点(-1, 0)から点(1, 0)まで線を引けばよい
#   lines(X, Y)でXとYのベクトルを指定する（散布図と同じ）
lines(c(-1, 1), c(0, 0), col="grey")
#x=0の直線を引く
#   点(0, -1)から点(0, 1)まで線を引けばよい
lines(c(0, 0), c(-1, 1), col="grey")

#第3因子と第2因子についても同様
plot(resultFA$loadings[, 3],
     resultFA$loadings[, 2], type="n")
text(resultFA$loadings[, 3],
     resultFA$loadings[, 2], 
     rownames(resultFA$loadings), col="steelblue")
lines(c(-1, 1), c(0, 0), col="grey")
lines(c(0, 0), c(-1, 1), col="grey")

#因子得点(ケースごとの得点)はresultFAの中のscoresに格納されている
head(resultFA$scores)

#因子得点をデータフレームに変換
DFfa <- as.data.frame(resultFA$scores)
#行の名前を自治体名に変換
rownames(DFfa) <- DF$市町村

#意味を考えて因子に名前を付ける
names(DFfa) = c("ビジネス度","都会生活度","非高齢化度")
head(DFfa)

#因子得点について要約情報を表示
summary(DFfa)
#標準偏差
apply(DFfa, 2, sd)

#因子得点をもとにクラスタリング
kmFA <- kmeans(DFfa, 4, iter.max=50) 
#色ラベルの配列を作るためにクラスタ番号の配列をコピー
color.kmFA <- kmFA$cluster
head(color.kmFA)

#クラスタ番号を色名に変換する
#levels＝factor（カテゴリ変数）のラベルの指定
#クラスタの数に注意
color.kmFA <- as.factor(color.kmFA)
levels(color.kmFA) <- c("blue", "red", "green", "orange")
head(color.kmFA)

#factorの実体は整数型なので文字列に変換（ラベルの値が実体となる）
color.kmFA <- as.character(color.kmFA)
head(color.kmFA)

#因子得点(サンプルごとの点数)の値を色分けしてプロットする
#ラベル(市町村名＝DFfaの行の名前)を rownames(DFfa) で表示
#クラスタの色名color.kmFAで色分けをして表示
plot(DFfa$ビジネス度, 
     DFfa$都会生活度, type="n")
text(DFfa$ビジネス度, 
     DFfa$都会生活度, rownames(DFfa), col=color.kmFA)
lines(c(-10, 10), c(0, 0), col="grey")
lines(c(0, 0), c(-10, 10), col="grey")

plot(DFfa$非高齢化度, 
     DFfa$都会生活度, type="n")
text(DFfa$非高齢化度, 
     DFfa$都会生活度, rownames(DFfa), col=color.kmFA)
lines(c(-10, 10), c(0, 0), col="grey")
lines(c(0, 0), c(-10, 10), col="grey")



#主成分分析
resultPCA <- prcomp(DF[, -(1:3)], scale=TRUE)

#結果の要約
summary(resultPCA)

#各変数ごとの主成分（固有ベクトル）
#第3主成分まで表示
resultPCA$rotation[, 1:3]

#各ケースごとの主成分得点
#5自治体、第3主成分まで表示
resultPCA$x[1:5, 1:3]

#主成分得点(サンプルごとの点数)の値をタテヨコにプロットする
biplot(resultPCA)

#主成分得点をデータフレームに変換
DFpca <- as.data.frame(resultPCA$x)
#行の名前を自治体名に変換
rownames(DFpca) <- DF$市町村

#主成分得点について要約情報を表示
summary(DFpca)[, 1:2]
#標準偏差
apply(DFpca, 2, sd)[1:2]

#主成分得点をもとにクラスタリング
#ここでは第3主成分までを使う
kmPCA <- kmeans(DFpca[, 1:2], 4, iter.max=50) 
#色ラベルの配列を作るためにクラスタ番号の配列をコピー
color.kmPCA <- kmPCA$cluster
head(color.kmPCA)

#クラスタ番号を色名に変換する
#levels＝factor（カテゴリ変数）のラベルの指定
color.kmPCA <- as.factor(color.kmPCA)
levels(color.kmPCA) <- c("blue", "red", "green", "orange")
head(color.kmPCA)

#factorの実体は整数型なので文字列に変換（ラベルの値が実体となる）
color.kmPCA <- as.character(color.kmPCA)
head(color.kmPCA)

#主成分得点(サンプルごとの点数)の値を色分けしてプロットする
#ラベル(市町村名＝DFfaの行の名前)を rownames(DFpca) で表示
#クラスタの色名color.kmFAで色分けをして表示
plot(DFpca$PC1, DFpca$PC2, type="n")
text(DFpca$PC1, DFpca$PC2, rownames(DFpca), col=color.kmPCA)
lines(c(-20, 20), c(0, 0), col="grey")
lines(c(0, 0), c(-10, 10), col="grey")



#結果の保存

#元のデータに因子得点とクラスタ番号を付加
DF <- cbind(DF, DFfa)          #列どうしを結合
DF$kmFA <- color.kmFA          #色の名前で付加

#元のデータに主成分得点（第2まで）とクラスタ番号を付加
DF <- cbind(DF, DFpca[, 1:2])  #列どうしを結合
DF$kmPCA <- color.kmPCA        #色の名前で付加

#データを確認して保存
str(DF)
write.table(DF, row.names=F,
            file="TokyoSTAT_fa_pca.csv")



#人気度の分布
summary(DF$人気度)
hist(DF$人気度,      col="ivory3")
hist(log(DF$人気度), col="ivory3")

#クラスタごとの人気度の分布
boxplot(log(DF$人気度) ~ DF$kmFA, col="grey")

#回帰分析（25項目の行政指標を使う）
Lm1 <- lm(log(人気度) ~ ., data=DF[, c(3:28)])
summary(Lm1)

#多重共線性の確認
library(car)
vif(Lm1)

#因子得点を使った回帰分析（因子得点のみを説明変数に使う）
Lm2 <- lm(log(人気度) ~ ., data=DF[, c(3, 29:31)])
summary(Lm2)
#標準偏回帰係数βを算出
library(lm.beta)          #βを算出するライブラリ
Lm2beta <- lm.beta(Lm2)   #関数lm.beta()でβを計算
summary(Lm2beta)

#多重共線性の確認（相関のない因子を抽出したため1となる）
vif(Lm2)

#Lm2による人気度予測結果（理論的な推定値）
pred <- predict(Lm2, newdata=DF)
#結果は対数化されているので、指数化して戻す
exp(pred)

#実測値と理論上の推定値
plot(log(DF$人気度), pred, type="n")
text(log(DF$人気度), pred, DF$市町村, col=color.kmFA)
lines(c(0, 10), c(0, 10), col="grey")

