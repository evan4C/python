#測距センサーテスト (GP2Y0E03)
import smbus
import time
bus = smbus.SMBus(1)  #I2Cの初期化
i2cadr = 0x40  #I2Cデバイスアドレス
shiftbit = 1   #測距センサーの設定(1=128cm / 2=64cm)
bus.write_byte_data(i2cadr ,0x35 ,shiftbit) #測距センサーを初期化
distold = 127
while 1:
    dh = bus.read_byte_data(i2cadr ,0x5e) #距離 上位バイト
    dl = bus.read_byte_data(i2cadr ,0x5f) #距離 下位バイト
    dist = ((dh*16+dl)/16)/pow(2,shiftbit) #距離を算出する
    speed = 0
    if (dist<127) and (distold<127):
        speed = distold-dist #速度を算出

    text = 'distance='+'{:.3f}'.format(dist)+'[cm] , speed='+'{:.3f}'.format(speed)+'[cm/sec]'
    print(text)
    distold = dist
    time.sleep(1)
