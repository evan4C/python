#basket ball game
import pygame
import smbus
import math
WIDTH = 1100
HEIGHT = 680
BOARDX = int(WIDTH*5/6)
GOALX = int(WIDTH*5/6)
GOALY = int(HEIGHT/2)
STARTX = int(WIDTH/8)
STARTY = int(HEIGHT*5/6)
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
NAVY = (  0,  0, 128)
GREEN = (  0, 128,  0)
CYAN = (  0, 255, 255)
RED = (255,  0,  0)
bus = smbus.SMBus(1)  #I2Cの初期化
i2cadr = 0x40  #I2Cデバイスアドレス(測距センサー GP2Y0E03)
shiftbit = 1   #測距センサーの設定(1=128cm / 2=64cm)
bus.write_byte_data(i2cadr ,0x35 ,shiftbit) #測距センサーを初期化

#角度と速度からXY移動量を算出
def getvectol(degree,speed):
    rad = math.radians(degree)
    tempx1 = (math.cos(rad))*speed  #X軸の移動量
    tempy1 = (math.sin(rad))*speed  #Y軸の移動量
    return (tempx1,tempy1)

#sprite class
class Spclass(pygame.sprite.Sprite):
    def __init__(self, x,y,filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.centerx = x  #X座標
        self.rect.centery = y  #Y座標
        self.x = x  #X座標
        self.y = y  #Y座標
        self.x1 = 0  #X
        self.y1 = 0  #Y
        self.score = 0 
#ボール
class Ball(Spclass):
    def update(self):
        if (self.x1!=0) and (self.y1!=0):
            self.x += self.x1  #X軸の移動
            self.y += self.y1  #Y軸の移動
            self.y1 = self.y1+0.0130

        if self.x > GOALX:self.x1 = -self.x1

        if (abs(self.x-GOALX)<64) and (abs(self.y-GOALY)<64):
            self.y = HEIGHT
            self.score = self.score+1

        if (self.x<0) or (self.y > (HEIGHT-32)):
            self.x = STARTX
            self.y = STARTY
            self.x1 = 0
            self.y1 = 0

        self.rect.centerx = self.x  #X軸
        self.rect.centery = self.y  #Y軸
#ゴール
class Goal(Spclass):
    def update(self):
        pass

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
myfont = pygame.font.Font(None ,48)  #Fontオブジェクト作成
myclock = pygame.time.Clock()        #Clockオブジェクト作成
bgsurface = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
allgroup = pygame.sprite.Group()
endflag = 0
while endflag==0:
    allgroup.empty()
    ball = Ball(STARTX, STARTY, "ball.png")
    allgroup.add(ball)  #ボールを追加
    goal = Goal(GOALX, GOALY ,"goal.png")
    allgroup.add(goal)  #ゴールを追加
    time = 60 #残り時間
    angle = 270 #発射角度
    gameover = 0
    speedtotal = 0
    measurecnt = 0 #測定回数
    distold = 127
    seq = 0
    while endflag==0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: endflag=1

        dh = bus.read_byte_data(i2cadr ,0x5e)  #距離 上位バイト
        dl = bus.read_byte_data(i2cadr ,0x5f)  #距離 下位バイト
        dist = ((dh*16+dl)/16)/pow(2,shiftbit)  #距離を算出
        speed = 999 #測定エラー
        if (dist<127) and (distold<127):
            speed = (distold-dist)/(1/60)  #手の速度を算出

        if seq==0: #画面クリア
            bgsurface.fill(CYAN)
            measurecnt = 0
            seq = 1
        elif seq==1: #手が止まるのを待つ
            if (speed!=999) and (abs(speed)<15):
                measurecnt = measurecnt+1
                if measurecnt>=5:
                    speedtotal = 0
                    measurecnt = 0
                    seq = 2
            else:
                seq = 0
        elif seq==2: #手が動くのを待つ
            angle = angle+0.5  #発射角度を変更
            if angle>360: angle = 270
            if (speed!=999) and (speed>15):
                speedtotal = speedtotal+speed
                measurecnt = measurecnt+1
                if measurecnt>=5:
                    speedave = speedtotal/measurecnt #平均速度を算出
                    print("speed="+str(speedave)+"[cm/sec]")
                    seq = 3
                    if speedave<70: #ボール発射
                        tx1,ty1 = getvectol(angle,speedave/10)
                        ball.x1 = tx1
                        ball.y1 = ty1
            else:
                speedtotal = 0
                measurecnt = 0
        elif seq==3:  #ボールの軌跡を描く
            dot = [ball.x-1, ball.y-1, 3, 3]
            pygame.draw.rect(bgsurface, RED ,dot)
            if (ball.x1==0) and (ball.y1==0):seq=0

        distold = dist
        board = [GOALX+32,0,10,HEIGHT]
        pygame.draw.rect(bgsurface, NAVY ,board)  #壁を描く
        ground = [0,HEIGHT-40,WIDTH,40]
        pygame.draw.rect(bgsurface, GREEN ,ground)  #床を描く
        screen.blit(bgsurface,(0,0))
        allgroup.update()
        allgroup.draw(screen) #スプライト表示
        tx1,ty1 = getvectol(angle,80)
        pygame.draw.line(screen, BLACK, (STARTX,STARTY), (STARTX+tx1,STARTY+ty1), 8) #発射角度
        imagetext = myfont.render("SCORE:"+str(ball.score), True, BLACK)
        screen.blit(imagetext, (400, 40)) #スコア表示
        if time<=0: #残り時間が0の場合
            ball.y1 = 0
            ball.x1 = 0
            seq = 4
            imagetext = myfont.render("TIME OVER", True, WHITE)
            gameover += 1
            if gameover >= 300:break
        else:
            time = time-(1/60)
            imagetext = myfont.render("LEFT TIME:"+str(int(time)), True, WHITE)

        screen.blit(imagetext, (400, HEIGHT-40)) #タイム表示
        myclock.tick(60)
        pygame.display.flip()

pygame.quit()
