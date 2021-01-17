# JUMP GAME
import pgzrun
import random  # 乱数のライブラリ
WIDTH = 800   
HEIGHT = 600

OUTSIDE = 999

# ゲームの初期化
def init():
  global player, score, objects, loopcount
  global gameover, titlemode
  # プレイヤーのスプライトを作成
  player = Actor('p1_walk01.png', (100, 300))
  player.anime = 0      # アニメカウンタ
  player.vy = 0         # 落下速度
  player.ground = False # 地面フラグ
  player.speed = 2      # スクロールの速度
  score = 0             # スコア
  loopcount = 0         # ループ回数
  gameover = 0          # ゲームオーバーカウンタ
  titlemode = True      # タイトル画面フラグ
  # 地面とコインのスプライトを管理するリスト
  objects = []          
  # リストに最初の地面のスプライトを格納する
  for i in range(int(WIDTH / 70)):
    objects.append(Actor('grass.png', \
      (i * 70, HEIGHT - 70)))

# 衝突時のプレイヤーの移動量を算出
def backward(num):  
  if num < 0: return(-(70 - abs(num)))
  else: return(70 - abs(num))

def draw():
  screen.fill((180, 250, 255))
  if titlemode == True:
    screen.draw.text('J U M P  G A M E', \
      left=250,top=250,fontsize=64,color='BLUE')
  else:
    for sp in objects:
      sp.draw()  # 地面とコインのスプライトを描画
    player.draw()  # プレイヤーのスプライトを描画
    screen.draw.text('SCORE : ' + str(score), \
      left=250,top=25,fontsize=64,color='BLUE')

def update():
  global player, objects
  global titlemode, loopcount, gameover, score
  
  if titlemode == True:
    if keyboard.space: titlemode = False
    return
  # プレイヤーを左に移動
  if keyboard.left: player.x -= 3
  # プレイヤーを右に移動
  if keyboard.right: player.x += 3  
  # プレイヤーは地面の上か？
  if player.ground == True: 
    # プレイヤーのジャンプ
    if keyboard.space:
      player.vy = -10  # ジャンプ開始
  else:
    # プレイヤーの落下
    player.vy += 0.2  # 0.2は重力加速度
    if player.vy > 10: player.vy = 10
    player.y += player.vy  

  player.anime = (player.anime + 1) % 60
  if player.anime == 0:
    player.image = 'p1_walk01.png'
  if player.anime == 30:
    player.image = 'p1_walk03.png'

  player.ground = False

  for obj in objects:
    # 地面またはコインを左に移動
    obj.x -= player.speed   
    # プレイヤーとの衝突判定
    dx = player.x - obj.x
    dy = player.y - obj.y
    if abs(dx) < 70 and abs(dy) < 70:
      # コインと衝突した場合
      if obj.image == 'coingold.png':
        score += 1  # スコアを加算
        obj.x = OUTSIDE  # コインを画面から消去
        player.speed += 0.25
      else: # 地面と衝突した場合
        if abs(dx) < abs(dy):
          # プレイヤーのY座標を修正
          player.y += backward(dy) 
          player.vy = 0
          # 地面フラグをオン
          if dy < 0: player.ground = True  
        else:
          # プレイヤーのX座標を修正
          player.x += backward(dx)  
 
  # 画面外の地面またはコインを消去する
  for obj in objects:
    if obj.x < -16 or obj.x == OUTSIDE:
      objects.remove(obj) 

  loopcount = (loopcount + 1) % 35
  if loopcount == 0:  
    pos = (WIDTH+70, (random.randrange(5)+4)*70)
    if random.randrange(4) > 0:
      # 地面のスプライトを追加
      objects.append(Actor('grass.png',pos))   
    else:
      # コインのスプライトを追加
      objects.append(Actor('coingold.png',pos))  

  if gameover == 0:
    # 画面外に出たらゲームオーバー
    if player.y > HEIGHT: gameover = 1
  else:
    gameover += 1
    if gameover > 180: init()

init()
pgzrun.go()
