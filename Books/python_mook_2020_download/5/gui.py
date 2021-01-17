import tkinter as tk

# GUI画面生成
root = tk.Tk()
root.title(u'TelloEDU')
root.geometry('500x200')

# 飛行用のコマンド
def btnTakeoff(): # 離陸
  send_command('takeoff')
  
def btnLand(): # 着陸
  send_command('land')

def btnFlip(): # 後方宙返り
  send_command('flip b')
  
def btnUp(): # 上昇
  send_command('up 50')
  
def btnDown(): # 下降
  send_command('down 50')

def btnCcw(): # 左旋回
  send_command('ccw 30')

def btnCw(): # 右旋回
  send_command('cw 30')

def btnForward(): # 前進
  send_command('forward 50')
  
def btnBack(): # 後退
  send_command('back 50')
  
def btnLeft(): # 左
  send_command('left 50')
  
def btnRight(): # 右
  send_command('right 50')

# Tello EDUの情報
lblBattery=tk.Label(text=u'Battery: --')
lblHeight = tk.Label(text=u'Height: --')
lblYaw = tk.Label(text=u'Yaw: --')
lblBattery.place(x=10, y=10)
lblHeight.place(x=110, y=10)
lblYaw.place(x=210, y=10)

# 離陸、着陸、宙返り
btnTakeoff = tk.Button(text=u'離陸', \
  width=10, command=btnTakeoff)
btnLand = tk.Button(text=u'着陸', \
  width=10, command=btnLand)
btnFlip = tk.Button(text=u'宙返り', \
  width=10, command=btnFlip)
btnTakeoff.place(x=10, y=50)
btnLand.place(x=10, y=80)
btnFlip.place(x=10, y=130)

# 上昇、下降、旋回
btnUp = tk.Button(text=u'上昇', \
  width=5, command=btnUp)
btnDown = tk.Button(text=u'下降', \
  width=5, command=btnDown)
btnCcw = tk.Button(text=u'左旋回', \
  width=5, command=btnCcw)
btnCw = tk.Button(text=u'右旋回', \
  width=5, command=btnCw)
btnUp.place(x=200, y=50)
btnDown.place(x=200, y=110)
btnCcw.place(x=150, y=80)
btnCw.place(x=250, y=80)

# 前進、後退、左右
btnForward = tk.Button(text=u'前進', \
  width=5, command=btnForward)
btnBack = tk.Button(text=u'後進', \
  width=5, command=btnBack)
btnLeft = tk.Button(text=u'左', \
  width=5, command=btnLeft)
btnRight = tk.Button(text=u'右', \
  width=5, command=btnRight)
btnForward.place(x=390, y=50)
btnBack.place(x=390, y=110)
btnLeft.place(x=340, y=80)
btnRight.place(x=440, y=80)

# ここに通信用のプログラムを追加
import socket
import threading 

# UDPソケット生成
sock = socket.socket(socket.AF_INET, \
  socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, \
  socket.SO_REUSEADDR, True)
sock.bind(('', 9000))

# Tello EDUにコマンドを送る関数
tello_address = ('192.168.10.1', 8889)
def send_command(msg):
  msg = msg.encode(encoding="utf-8") 
  sock.sendto(msg, tello_address)
  
def recv():
  while True: 
    try:
      # メッセージを受信
      data, server = sock.recvfrom(1518)
      
      # 末尾の改行コードを削除
      strData = data.decode( \
        encoding="utf-8").strip()
      # バッテリー
      if strData.isdecimal() == True:  
        lblBattery['text']='Battery: ' \
          + strData + ' %'
      elif strData[-2:] == 'dm': # 高度
        lblHeight['text'] = \
          'Height: ' + strData
      elif strData[-1:] == ';':  # 傾き
        # 「;」で区切る
        splitData = strData.split(';')
        # 「:」で区切る
        yaw = splitData[2].split(':')
        lblYaw['text'] = \
          'Yaw: ' + yaw[1] + ' °'
      else:
        print(strData)
    except Exception as ex:
      break
recvThread=threading.Thread(target=recv)
recvThread.start()

import time

# Tello EDUをコマンドモードにする
send_command('command')

def get_info():
  while True:
    # バッテリー
    send_command('battery?')
    time.sleep(0.5)
    # 高度
    send_command('height?')
    time.sleep(0.5)
    # 傾き
    send_command('attitude?')
    time.sleep(0.5)
# chkThread生成
chkThread = \
  threading.Thread(target=get_info)
chkThread.setDaemon(True)
chkThread.start()

root.mainloop() # メインループ

sock.close() # 終了処理
print ('--- END ---')

