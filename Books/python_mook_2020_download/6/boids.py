import pygame
from pygame.locals import *
import sys
import math
import random

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

  # 分離のルール
  def separation(self, r_s):
    tvx = tvy = c = 0
    # 自分以外の全エージェントを処理する
    for a in self.others:
      # 近過ぎるか？a[1]は距離
      if a[1] < r_s and a[1] != 0:
        # 離れる方向の単位ベクトルを蓄積
        tvx -= (a[0].x - self.x) / a[1]
        tvy -= (a[0].y - self.y) / a[1]
        c += 1
    if c != 0:
      # 単位ベクトルの平均を求める
      self.vx_s, self.vy_s = tvx / c, tvy / c
    else:
      self.vx_s, self.vy_s = self.vx, self.vy

  # 整列のルール
  def alignment(self, r_a):
    tvx = tvy = c = 0
    # 自分以外の全エージェントを処理する
    for a in self.others:
      # 周囲のエージェントか？a[1]は距離
      if a[1] < r_a:
        tvx += a[0].vx
        tvy += a[0].vy
        c += 1
    if c != 0:
      # 速度の平均を求める
      self.vx_a, self.vy_a = tvx / c, tvy / c
    else:
      self.vx_a, self.vy_a = self.vx, self.vy

  # 結合のルール
  def cohesion(self, r_c):
    tx = ty = c = 0
    # 自分以外の全エージェントを処理する
    for a in self.others:
      # 周囲のエージェントか？a[1]は距離
      if a[1] < r_c:
        tx += a[0].x
        ty += a[0].y
        c += 1
    if c != 0:
      tx, ty = tx / c, ty / c # 重心を求める
      d = math.sqrt((tx - self.x)**2 + \
        (ty - self.y)**2)
      if d != 0:
        # 重心を向いた単位ベクトルを求める
        self.vx_c = (tx - self.x) / d
        self.vy_c = (ty - self.y) / d
    else:
      self.vx_c, self.vy_c = self.vx, self.vy

  def rule(self, agent_list, r_s, r_a, r_c):
    # 他エージェントとの距離を求める
    self.others = \
      tuple([(a, math.sqrt((a.x - self.x)**2 \
      + (a.y - self.y)**2)) \
      for a in agent_list if a!=self])
    if len(self.others) < 1: return
    # 3つのルールを適用
    self.separation(r_s)
    self.alignment(r_a)
    self.cohesion(r_c)

    tvx = self.vx_s * 1.0 + self.vx_a * 0.4 + \
      self.vx_c * 0.2
    tvy = self.vy_s * 1.0 + self.vy_a * 0.4 + \
      self.vy_c * 0.2
    n = math.sqrt(tvx**2 + tvy**2)
    # 新しい速度を設定
    self.vx, self.vy = 2 * tvx / n, 2 * tvy / n

# メイン
WINDOW_W, WINDOW_H = 1000, 700
pygame.init()
screen = \
  pygame.display.set_mode((WINDOW_W, WINDOW_H))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)
agent_list = []
rule_on = 1 # ルールの適用/非適用に使うフラグ

while True:
  clock.tick(60)
  screen.fill((255, 255, 255))
  
  for a in agent_list:  
    if rule_on == 1:
      # ルールを適用
      a.rule(agent_list, 15, 30, 50)
    a.update(WINDOW_W, WINDOW_H)
    a.draw(screen)

  s1="agents : " + str(len(agent_list))
  s2="rule : on" if rule_on==1 else "rule : off"
  text=font.render(s1 + "   " + s2,True,(0,0,0))
  screen.blit(text, (1, 1)) 

  for e in pygame.event.get():
    if e.type==MOUSEBUTTONDOWN and e.button==1:
      vx = random.uniform(-1.5, 1.5)
      vy = random.uniform(-1.5, 1.5)
      a = Agent(e.pos[0], e.pos[1], vx, vy)
      agent_list.append(a)
    # マウスの中ボタンを押したときの処理
    if e.type==MOUSEBUTTONDOWN and e.button==2:
      rule_on = 1 - rule_on # フラグの切り替え
    if e.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()


