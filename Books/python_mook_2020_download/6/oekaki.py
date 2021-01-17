import pygame
from pygame.locals import *
import sys

pygame.init()
# サイズを設定して画面を生成
screen = pygame.display.set_mode((800, 800))
# 2次元リストを生成
cells = [[0] * 40 for i in range(40)]

while True: # 無限ループ
  screen.fill((255, 255, 255)) # 背景を白にする

  # 正方形を描画する2重ループ
  for y in range(0, 40):
    for x in range(0, 40):
      if cells[y][x] == 1:
        # 四角形の座標と縦横の長さを設定
        rect = Rect(x * 20, y * 20, 20, 20)
        # 緑色(0,255,0)の四角形を描く
        pygame.draw.rect(screen,(0,255,0),rect)

  # マウスからの入力を処理する
  for e in pygame.event.get():
    if e.type == MOUSEBUTTONDOWN:
      mx, my = int(e.pos[0]/20),int(e.pos[1]/20)
      cells[my][mx] = 1 - cells[my][mx] 
    if e.type == QUIT:
      pygame.quit()
      sys.exit()
      
  pygame.display.update()

