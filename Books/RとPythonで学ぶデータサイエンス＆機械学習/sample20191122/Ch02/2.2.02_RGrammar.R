#Rの文法
#一行ずつ実行してみましょう

#'#'はコメントを示します


#算術演算
3 + 2       #和
3 - 2       #差
3 * 2       #積
3 / 2       #商
3 ^ 2       #累乗

3^2         #スペースはなくてもよい


#オブジェクトへの格納（代入操作）
a <- 1      #1をAに格納
A <- 2	    #2をAに格納
b <- a + A  #a+Aをbに格納
print(b)    #bを表示
b	    #print()を書かなくても表示される


#ベクトル
a <- c(1, 2, 3)	#(1, 2, 3)をあに格納
A <- c(4:6)   	#(4, 5, 6)をAに格納
b <- a + A    	#a+Aをbに格納
b               #bを表示
b * 2           #b×2を表示

a <- c(1,2,3)   #スペースはなくてもよい

sum(a)          #ベクトルの要素の和


#文字列
fr1 <- "apple"		        #文字列
fr2 <- c("orange", "lemon") 	#文字列を要素とするベクトル
fruites <- c(fr1, fr2, fr1)     #要素を結合
fruites	                        #fruitesを表示		


#論理
bool <- c(TRUE, FALSE, F, T)    #論理値
bool                            #TはTRUEの略、FはFALSEの略
sum(bool)                       #T/Fは1/0として扱われる

"pen" == "pen"     #比較演算（同じ）
"pen" == "apple"
"pen" != "apple"   #比較演算（異なる）
"pen" != "pen"

1 < 2              #比較演算（より小さい）
1 >= 2             #比較演算（より大きいか同じ）

is_apple <- fr1 == "apple"       #比較演算の結果を格納
is_apple

is_apple <- fruites == "apple"   #比較演算の結果を格納
is_apple


#型
class(a)         #オブジェクトの型を表示する
class(fr1)
class(fruites)
class(is_apple)
str(a)           #型と構造、内容の一部を表示する
str(fr1)
str(fruites)
str(is_apple)


#ベクトルの要素を取り出す
Nums <- seq(4, 62, 2)   #4から62まで間隔が2の数列を作成
Nums
str(Nums)

head(Nums)     #最初の6つ
head(Nums, 8)  #最初の8つ
tail(Nums, 8)  #最後の8つ

Nums[3]      #3つめの要素
Nums[2:5]    #2つめから5つめまでの要素
Nums[-3]     #3つめ以外の要素


#要素の追加
Nums <- append(Nums, 64)          #最後に要素を追加
Nums

Nums <- append(Nums, 2, after=0)  #先頭に追加
Nums                              #'after'で位置を指定


#マトリクス（行列）
Nums <- matrix(Nums, 8, 4)   #Numsを8×4の行列に変換
Nums

#row（行）とcolumn（列）の指定
Nums[1, 2]   #row 1, column 2
Nums[2, 1]   #row 2, column 1
Nums[, 2]    #すべてのrow, column 2
Nums[2, ]    #row 2, すべてのcolumns

class(Nums)  #型の確認
str(Nums)


#関数を作成
#  ベクトルの要素を全て2乗して足す関数sumSquaresを作る
sumSquares <- function( a ){
  b <- sum( a^2 )   #aの2乗の和
  return(b)         #bの値を関数の戻り値として返す
}

sum(c(1, 2, 3))         #1 + 2 + 3
sumSquares(c(1, 2, 3))  #1 + 4 + 9
sum(Nums)               #2 + 4 + 6 +...
sumSquares(Nums)        #4 +16 +36 +...
