# DRAW TEST
import pgzrun
WIDTH = 640  # 画面の幅
HEIGHT = 480  # 画面の高さ

def draw():
  screen.clear()  # 画面を消去

  # 直線を描く
  startpos = (150, 20)
  endpos = (250,120)
  screen.draw.line(startpos, endpos, 'BLUE') 

  # 四角形を描く
  rect1 = Rect((150, 150), (100, 100))
  screen.draw.rect(rect1, 'RED')
  rect2 = Rect((300, 150), (100, 100))
  screen.draw.filled_rect(rect2, 'RED')

  # 円を描く
  radius = 50
  pos = (200, 320)
  screen.draw.circle(pos, radius, 'GREEN')
  pos = (350, 320)
  screen.draw.filled_circle(pos, radius, 'GREEN')

  # 文字を描く
  screen.draw.text('Sample Text', left=150, \
    top=400, fontsize=32, color='YELLOW')

pgzrun.go() 
