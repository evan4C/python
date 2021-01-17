import socket
import threading
import cv2

event = threading.Event()   # イベント
photoNum = 0     # 静止画番号
isShoot = False  # 静止画撮影フラグ

# UDPソケット生成
sock = socket.socket(socket.AF_INET, \
  socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, \
  socket.SO_REUSEADDR, True)
sock.bind(('', 9000))

# Tello EDUにコマンドを送る関数
tello_address = ('192.168.10.1', 8889)
def send_command(msg):
  print(msg)
  msg = msg.encode(encoding="utf-8") 
  sock.sendto(msg, tello_address)
  event.wait()
  event.clear()
  
# Tello EDUからのメッセージを受け取る関数
def recv():
  while True:
    try:
      data, server = sock.recvfrom(1518)
      print(data.decode(encoding="utf-8"))
      event.set()
    except Exception:
      break
recvThread = threading.Thread(target=recv)
recvThread.start()

# 静止画撮影の準備
def shoot():
  global photoNum
  global isShoot
  photoNum += 1
  isShoot = True
  
# 飛行コマンド   
def flight_mission():
  send_command('takeoff')
  for i in range(4):
    send_command('forward 100')
    send_command('cw 135')
    shoot()
    send_command('ccw 45')
  send_command('land')

def main(): # メイン関数
  global isShoot
  try:
    send_command('command')  
    send_command('streamon') 
    
    # ビデオキャプチャ生成
    cap=cv2.VideoCapture('udp://0.0.0.0:11111')
      
    while True:
      # キャプチャ画像を画面に表示
      ret, frame = cap.read()
      cv2.imshow('TelloEDU', frame)
      
      # 静止画保存
      if isShoot:
        cv2.imwrite( \
          'img{:04}.png'.format(photoNum),frame)
        isShoot = False
      
      # キー入力待ち
      key = cv2.waitKey(1)
      if key == ord('m'):  # mキー
        # 飛行スレッド開始
        flightThread = threading.Thread( \
          target=flight_mission)
        flightThread.start()

      if key == 27:  # ESCキー
        break

  except Exception as ex:
    print (ex)
  finally:
    # 終了処理
    cap.release()
    cv2.destroyAllWindows()
    send_command('streamoff') # カメラ入力停止
    sock.close()
    print('--- END ---')
  
if __name__ == '__main__':
  main()


