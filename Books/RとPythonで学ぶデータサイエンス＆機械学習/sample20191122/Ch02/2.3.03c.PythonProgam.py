# -*- coding: utf-8 -*-

## Pythonによるプログラミング

## #はコメントを表します

#---------------------------------------------------------------
### 制御構造(if, for)、自作関数の作成(def)  

# 関数を定義する例を示します。  
# Rで作成したものと同じく、注文のサイズに応じて価格を返す関数を作ります。
# 関数の中で、if文による条件分岐を使っています。
#---------------------------------------------------------------

#自作関数の作成  def
#条件分岐  if

#ディクショナリ
Price = { "Kids":None, "Short":2.45, "Medium":2.85, "Tall":3.25, "Grand":3.65 }

#関数を定義
def get_price( c ) :               #自作関数 get_price() を作成
    if c == "Kids" :                 #もし与えられた値が"Kids"なら
        return("sorry")                 # "sorry"を帰す
    else :                           #それ以外の場合
        return( Price[ c ] )          #  ディクショナリから値を取得

#関数の呼び出し
print( get_price( "Short" ) )

#---------------------------------------------------------------
# さきほどの関数を呼び出して繰り返し実行します。  
# 繰り返し処理にはfor文を使います。
#---------------------------------------------------------------

#繰り返し（ループ）

order_list = ["Medium", "Tall",   "Kids",   "Short", "Tall", "Kids",
              "Kids",   "Medium", "Short",  "Tall",  "Kids", "Short",
              "Medium", "Tall",   "Medium", "Short", "Tall", "Short",
              "Short",  "Grand" ]

len(order_list)            #リストの要素の数
order_price = []           #空のリスト

for i in range( len(order_list) ) :   #0から(リストの要素数-1)まで繰り返し
    order_price.append( get_price( order_list[i] ) )     #リストに値を追加
    
print( order_price )

#---------------------------------------------------------------
### クラスとメソッド

# クラスとは新しいオブジェクトをつくる際の「ひな型」です。  

# >ひな型をもとに作成されるオブジェクトをインスタンスと呼びます。  
#  人間をクラスとすれば、Johnはインスタンスです。  

# クラスの定義の中で、メソッドと呼ばれる機能を記述します。  

# >メソッドは、そのクラスに属するオブジェクトだけが持つ機能です。  
#  実行する際は " オブジェクト名.メソッド名() " のように記述します。
#---------------------------------------------------------------

#クラスとメソッド

#クラスの定義
class Human:
    #コンストラクタ　身長mと体重kgを受け取ってBMIを計算
    #                インスタンスが作成されると実行される
    def __init__(self, height, weight):
        self.BMI = weight / (height**2)
        
    #メソッド value : BMIの値を四捨五入して少数2桁までの値を返す
    def value(self):
        return round(self.BMI, 2)  #self.BMIをコンストラクタから受けとる
                                    #関数round()で四捨五入する
        
    #メソッド is_fat : 適正体重かどうかを診断してprint()で文字列を表示
    def is_fat(self):
        if self.BMI < 18.5 :       #self.BMIをコンストラクタから受けとる
            print("Under")         #self.BMIの値によって異なる文字列を表示
        elif self.BMI >= 30 :
            print("Over")
        else :
            print("OK!")

#実行
if __name__ == '__main__':
    John = Human(1.80, 82)    #クラスHumanからインスタンスJohnを生成
    Taro = Human(1.65, 88)    #　JohnもTaroもHumanである
    
    print( John.value() )     #メソッド.value()を実行
    print( Taro.value() )     #  実行すると値だけが返ってくるのでprint()で表示
    
    print( "\n" )
    John.is_fat()             #メソッド.is_fat()を実行
    Taro.is_fat()             #　.is_fat()の中でprint()が実行される
    