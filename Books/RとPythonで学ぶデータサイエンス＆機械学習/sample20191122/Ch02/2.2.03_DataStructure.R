#データ構造と制御構造



#リスト
Cup   <- c("Kids", "Short", "Medium", "Tall", "Grand") #ベクトル
Fl.oz <- c(7, 10, 14, 18, 24)                          #ベクトル

Sizelist <- list(Cup, Fl.oz)    #2つのベクトルを束ねてリストを作る
Sizelist

class(Sizelist)   #型を確認
str(Sizelist)     #型と構造

Sizelist[1]       #リストの1つめ(リスト)
Sizelist[[1]]     #リストの1つめ(ベクトル)
Sizelist[[1]][2]  #そのベクトルの2つめの要素(文字列)

Sizelist[2]
Sizelist[[2]]
Sizelist[[2]][2]



#データフレーム
DFSize <- as.data.frame(Sizelist)      #データフレームに変換

colnames(DFSize) <- c("cup", "fl.oz")  #列名(ヘッダー)をつける

head(DFSize)     #最初の6行

class(DFSize)    #型の確認
str(DFSize)      #型と構造

View(DFSize)     #データフレームの表示（RStudioの左上ペイン）


DFSize$cup       #列名を指定してデータを取り出す
DFSize$fl.oz

DFSize$USD <- c(NA, 2.45, 2.85, 3.25, 3.65)
                 #'USD'という名前で列を作成
DFSize$USD

head(DFSize)     #最初の6行
str(DFSize)      #型と構造


DFSize[2, 3]     #row 2, column 3
DFSize[2, ]      #row 2, 全てのcolumn
DFSize[, 3]      #全てのrow, column 2
DFSize[, "USD"]  #全てのrow, column名"USD"

DFSize$USD[2]    #ベクトル DFSize$USD の２つめの要素
                 #この場合は DFSize[2, 3]と同じ

DFSize[DFSize$cup=="Short", ]
                 #cupが"Short"である行（列は全て）
                 #この場合は DFSize[2, ]と同じ

DFSize[DFSize$cup=="Short", "USD"]
                 #cupが"Short"である行、かつ列名が"USD"
                 #この場合は DFSize[2, 3]と同じ

#データフレームの列どうしの演算
DFSize$UnitPrice <- DFSize$USD / DFSize$fl.oz 
head(DFSize)
str(DFSize)


#注意）データフレームはリストの特殊な形
DFSize$fl.oz  #数値のベクトル
DFSize[, 2]   #数値のベクトル, 'DFSize$fl.oz'と同じ

DFSize[2]     #これはベクトルではなく1列だけのデータフレーム
              #　リストの2つめを取り出したことを意味する
DFSize[[2]]   #これは数値のベクトル, 'DFSize$fl.oz'と同じ
              #　リストの2つめの要素を取り出したことを意味する



#型の変換
class(DFSize$fl.oz)  #型の確認
class(DFSize$cup)

str(DFSize$cup)      #型と構造
DFSize[1, 1]
#'Factor'はカテゴリ変数で、実態は整数にラベルを付けたもの
#'Levels'はカテゴリの分類の名称を示す
# 　例 : DFSize[1, 1] の値は 2 だが "Kids" とラベル付けされている

#注意）Factor型は煩雑なので、できるだけ文字列型を使った方がよい


DFSize$cup <- as.character(DFSize$cup)  #文字列型への変換

class(DFSize$cup)  #型を確認
DFSize[1, 1]       #要素は文字列となっている

str(DFSize)        #型と構造




#条件分岐（if）

which(c("P","Q","R","S") == "Q")   #"which()"は値のインデックスを返す

choice <- "Short"
which(DFSize$cup == choice)        #この場合"Short"は2番目にある

idx <- which(DFSize$cup == choice) #"Short"のインデクスをidxに格納
DFSize$USD[idx]                    # DFSize$USD[2] の値が返される

get_price <- function( c ){        #関数"get_price()"を作る
  if(c == "Kids"){                   #もし、与えられたcが"Kids"なら
    return("sorry")                       #値として"sorry"を返す
  } else {                            #そうでなければ
    idx <- which(DFSize$cup == c)         #cが何番目かを調べてidxに格納
    return( DFSize$USD[idx] )             #idxに対応するUSDの値を返す
  }
}

choice <- "Medium"
get_price( choice )

choice <- "Kids"
get_price( choice )


#ループ（for）

#Rでは','の後は改行して続けることが可能
order_list <- c("Medium", "Tall",   "Kids",   "Short", "Tall", "Kids",
                "Kids",   "Medium", "Short",  "Tall",  "Kids", "Short",
                "Medium", "Tall",   "Medium", "Short", "Tall", "Short",
                "Short",  "Grand")

length(order_list)         #order_listの要素数
order_price <- NULL        #order_priceに'NULL'（何もない状態）を設定


for(i in 1:length(order_list)){      #i=1から2,3,...と要素数まで繰り返し
  order_price <- append(order_price,                #order_priceに
                        get_price(order_list[i]))   #get_priceの結果を追加
}
order_price
#ただし、forループは実行が遅いので上の方法は推奨されない
#Rでは以下の方法で処理した方がよい（結果は同じ）

#sapply()：リストの全ての要素に、指定した関数を一度に実行する
sapply(order_list, get_price)   #order_listの全ての要素にget_priceを実行

