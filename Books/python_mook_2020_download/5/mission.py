import socket
import threading

event = threading.Event() # Eventオブジェクト

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
  event.wait()  # イベントが発生するまで待機
  event.clear() # フラグの初期化
  
# Tello EDUからのメッセージを受け取る関数
def recv():
  while True:
    try:
      data, server = sock.recvfrom(1518)
      print(data.decode(encoding="utf-8"))
      event.set()   # イベント発生
    except Exception:
      break
recvThread = threading.Thread(target=recv)
recvThread.start()
 
def main(): # メイン関数
  try:
    send_command('command') # コマンドモード開始
    send_command('takeoff')
    send_command('forward 100')
    send_command('flip b')
    send_command('back 70')
    send_command('land')
    print('--- END ---')
  except Exception as ex:
    print (ex)
  finally:
    sock.close()  # ソケット通信終了
  
if __name__ == '__main__':
  main()
