# SHOOTING GAME
import pgzrun
import math
import random
WIDTH = 800   
HEIGHT = 600  
OUTSIDE = 999

# スプライトのクラス。Actorクラスを継承
class Spclass(Actor):
  def __init__(self, x, y, angle, num):
    Actor.__init__(self,charas[num].imagename,(x,y))
    self.angle = angle       # 角度
    self.hp = charas[num].hp # 体力
    self.count = 0           # カウンタ
    self.num = num           # キャラクターの種類

# 爆発クラス。Spclassクラスを継承
class Explosion(Spclass):
  def update(self):
    if self.count > 20: self.x = OUTSIDE

# 自機の弾のクラス。Spclassクラスを継承
class Shot(Spclass):
  def update(self):
    self.pos = spritemove(self.pos, self.angle, 8)
    # 衝突判定
    hitbox = Rect((self.x-15, self.y-15), (30, 30))
    for sp in objects:
      if charas[sp.num].enemy==False or sp.hp==99:
        continue
      if sp.colliderect(hitbox):
        objects.append(Explosion(sp.x, sp.y, 0, 0))
        self.x = OUTSIDE
        sp.hp -= 1
        break

# 敵の弾のクラス。Spclassクラスを継承
class EnemyShot(Spclass):
  def update(self):
    self.pos = spritemove(self.pos, self.angle, 4)

# 自機のクラス。Spclassクラスを継承
class Player(Spclass):
  def update(self):
    if keyboard.up   : self.y -= 4
    if keyboard.down : self.y += 4
    if keyboard.left : self.x -= 4
    if keyboard.right: self.x += 4
    if self.x < 35: self.x = 35
    if self.y < 35: self.y = 35
    if self.x > (WIDTH-35 ): self.x = WIDTH-35
    if self.y > (HEIGHT-35): self.y = HEIGHT-35
    if keyboard.space!=0 and (self.count % 16)==0:
      objects.append(Shot(self.x, self.y,   0, 1))
      objects.append(Shot(self.x, self.y,  30, 1))
      objects.append(Shot(self.x, self.y, -30, 1))

    # 衝突判定
    hitbox = Rect((self.x-10,self.y-10), (20,20))
    for sp in objects:
      if charas[sp.num].enemy == True:
        if sp.colliderect(hitbox):
          self.hp -= 1
          sp.hp -= 1
          break

# 敵のクラス。Spclassクラスを継承
class Enemy(Spclass):
  def update(self):
    self.x += int((self.count % 200) / 100) * 2 - 1
    self.y += 2
    if random.randrange(100) != 0: return
    px, py = player.pos
    newangle = -90 - math.degrees( \
      math.atan2(py - self.y, px - self.x))
    newsp = EnemyShot(self.x, self.y, newangle, 2)
    objects.append(newsp)

# ボスのクラス。Spclassクラスを継承
class Boss(Spclass):
  def update(self):
    if self.count < 100: self.y += 1
    else:
      rad = math.radians(self.count - 100)
      self.x = (WIDTH / 2) + (math.sin(rad) * 200)
    if self.count > 150 and (self.count % 5) == 0:
      newangle = (self.count * 4) % 360
      objects.append(EnemyShot(self.x, self.y, \
        newangle, 2))

# キャラクター情報のクラス
class Characlass:
  def __init__(self, filename, hp ,enemy):
    self.imagename = filename  # 画像ファイル名
    self.hp = hp               # 体力
    self.enemy = enemy         # 敵フラグ

# 指定した角度に移動
def spritemove(pos, angle, speed):
  x, y = pos
  rad = math.radians(-90 - angle)
  x += (math.cos(rad)) * speed
  y += (math.sin(rad)) * speed
  return x, y

# ゲーム初期化
def init():
  global player, objects, bosstimer
  global titlemode, gameover, stars
  stars = []
  for i in range(10):
    pos = (random.randrange(WIDTH), \
      random.randrange(HEIGHT))
    stars.append(Rect(pos,(3, 3)))

  objects = []  # スプライトのリスト
  player = Player(WIDTH / 2, HEIGHT * 3 / 4, 0, 3)
  objects.append(player)  # 自機をリストに格納
  bosstimer = 60 * 20
  titlemode = True
  gameover = 0

def draw():
  screen.clear()
  for rect in stars:
    screen.draw.rect(rect, 'WHITE')

  if titlemode == True:
    screen.draw.text('S H O O T I N G  G A M E', \
      left=150,top=240,fontsize=64,color='YELLOW')
  else:
    for sp in objects: sp.draw()
    if gameover > 0:
      screen.draw.text('G A M E  O V E R', \
        left=200,top=240,fontsize=64,color='YELLOW')

def update():
  global bosstimer, gameover, titlemode
  if titlemode == True:
    if keyboard.space: titlemode = False
    return

  for i in range(len(stars)):
    stars[i].y += (i+1)  # 星を動かす
    if stars[i].y > HEIGHT: stars[i].y = 0

  bosstimer -= 1
  if bosstimer==0:
    objects.append(Boss(WIDTH/2,0,0,5))  # ボス出現
  elif bosstimer > 0 and random.randrange(100)==0:
    x = random.randrange(WIDTH - 200) + 100
    objects.append(Enemy(x, 0, 0, 4))

  for sp in objects:
    sp.update()
    sp.count += 1
    if sp.hp <= 0:
      objects.append(Explosion(sp.x, sp.y, 0, 0))
      sp.x = OUTSIDE
    if sp.x<-35 or sp.x>(WIDTH+35) or sp.y<-35 \
      or sp.y>(HEIGHT+35):
      if sp.num == 5: bosstimer = 60 * 20
      objects.remove(sp)  # 画面外のスプライトを消去

  if gameover == 0:
    if (player in objects) == False: gameover = 1
  else:
    gameover += 1
    if gameover > 180: init()

charas = []
# 0:爆発
charas.append(Characlass("shield3.png", 1, False))
# 1:自機の弾
charas.append(Characlass("laserblue01.png",1,False))
# 2:敵の弾
charas.append(Characlass("laserred01.png",99,True))
# 3:自機
charas.append(Characlass("playership1_blue.png", \
  1, False))
# 4:敵  
charas.append(Characlass("enemyred1.png", 3, True))
# 5:ボス
charas.append(Characlass("enemygreen5.png",15,True))

init()
pgzrun.go()

