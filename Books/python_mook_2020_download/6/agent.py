import pygame
from pygame.locals import *
import sys
import random

# Agentクラス
class Agent:
  def __init__(self, x, y, vx, vy):
    self.x, self.y = x, y # 位置
    self.vx, self.vy = vx, vy # 速度

  def update(self, WINDOW_W, WINDOW_H):
    # 位置に速度を足して移動する
    self.x += self.vx 
    self.y += self.vy
    # ウインドウの端で跳ね返るための処理
    if self.x > WINDOW_W: # 右端
      self.vx, self.x = -self.vx, WINDOW_W
      return
    if self.x < 0: # 左端
      self.vx, self.x = -self.vx, 0
      return
    if self.y > WINDOW_H: # 下
      self.vy, self.y = -self.vy, WINDOW_H
      return
    if self.y < 0: # 上
      self.vy, self.y = -self.vy, 0

  def draw(self, screen):
    x, y = int(self.x), int(self.y)
    # 小さな赤い丸を描く
    pygame.draw.circle(screen,(255,0,0),(x,y),5)

# メイン

# ウインドウの幅と高さ
WINDOW_W, WINDOW_H = 1000, 700
pygame.init() # Pygameを初期化
# 画面を作成
screen = \
  pygame.display.set_mode((WINDOW_W, WINDOW_H))
# 時間を管理するためのClockオブジェクトを生成
clock = pygame.time.Clock()
# Fontオブジェクトを生成
font = pygame.font.Font(None, 28)
agent_list = [] # エージェントを格納するリスト

while True: # 無限ループ
  clock.tick(60) # 60fpsに設定
  # ウインドウを白で塗りつぶす
  screen.fill((255, 255, 255))

  # 各エージェントを処理する
  for a in agent_list:  
    a.update(WINDOW_W, WINDOW_H)
    a.draw(screen)

  # エージェントの数を表示
  s1 = "agents : " + str(len(agent_list))
  text = font.render(s1, True, (0, 0, 0))
  screen.blit(text, (1, 1))

  # イベントを処理する
  for e in pygame.event.get():
    # マウスの左ボタンが押された時の処理
    if e.type==MOUSEBUTTONDOWN and e.button==1:
      # 速度を乱数で設定
      vx = random.uniform(-1.5, 1.5)
      vy = random.uniform(-1.5, 1.5)
      # エージェントを生成
      a = Agent(e.pos[0], e.pos[1], vx, vy)
      # 生成したエージェントをagent_listに追加
      agent_list.append(a)
    if e.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()


