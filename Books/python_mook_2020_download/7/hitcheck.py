# HIT CHECK
import pgzrun
WIDTH = 800 
HEIGHT = 600 

def draw():
  screen.clear()
  player.draw()
  enemy.draw()
  screen.draw.rect(hitbox, 'RED')
  screen.draw.text('colliderect : ' + str(hitstatus), \
    left=150, top=100, fontsize=32, color='YELLOW')

def update():
  global hitstatus, enemy
  # 衝突判定
  hitstatus = enemy.colliderect(hitbox)
  enemy.y += 1
  if enemy.y > HEIGHT:enemy.y = 0

player = Actor('playership1_blue.png', (WIDTH/2,HEIGHT/2))
enemy = Actor('enemyred1.png', (WIDTH/2,0))
# 衝突判定の領域を設定
hitbox = Rect((player.x - 30, player.y-30), (60, 60))

pgzrun.go() 

