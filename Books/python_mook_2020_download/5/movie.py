import socket
import threading
import cv2

event = threading.Event()   # イベント
videoWriter = False    # ビデオライター
isVideo = False        # 録画フラグ・オフ

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

# 録画開始
def start_rec():
  global videoWriter
  global isVideo
  FOURCC = cv2.VideoWriter_fourcc(*'mp4v')
  FPS = 30.0
  SIZE = (960, 720)
  videoWriter = cv2.VideoWriter( \
    'video0001.mp4', FOURCC, FPS, SIZE)
  isVideo = True
  print('rec...')  

# 録画停止
def stop_rec():
  global isVideo
  isVideo = False
  videoWriter.release()
  print("...rec stop")
  
# 飛行用のコマンド  
def flight_mission():
  send_command('takeoff')
  start_rec() # 録画開始
  send_command('up 100')
  send_command('cw 360')
  send_command('down 100')
  stop_rec()  # 録画終了
  send_command('land')

def main(): # メイン関数
  try:
    send_command('command') 
    send_command('streamon')
    
    # ビデオキャプチャ生成
    cap=cv2.VideoCapture('udp://0.0.0.0:11111')
      
    while True:
      # キャプチャ画像を画面に表示
      ret, frame = cap.read()
      cv2.imshow('TelloEDU', frame)
      
      # 動画保存
      if isVideo:
        videoWriter.write(frame)
      
      # キー入力待ち
      key = cv2.waitKey(1)
      if key == ord('m'):
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
    send_command('streamoff') 
    sock.close()
    print('--- END ---')
  
if __name__ == '__main__':
  main()


