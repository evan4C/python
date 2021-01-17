import socket
import threading 

# UDPソケット生成
sock = socket.socket(socket.AF_INET, \
  socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, \
  socket.SO_REUSEADDR, True)
sock.bind(('', 9000))

tello_address = ('192.168.10.1', 8889)

# Tello EDUにコマンドを送る関数
def send_command(msg):
  msg = msg.encode(encoding="utf-8") 
  sock.sendto(msg, tello_address)
  
# Tello EDUからのメッセージを受け取る関数
def recv():
  while True:
    try:
      data, server = sock.recvfrom(1518)
      print(data.decode(encoding="utf-8"))
    except Exception:
      break
      
# recvThread生成
recvThread = threading.Thread(target=recv)
recvThread.start()

def main(): # メイン関数
  while True: 
    try:
      # コマンド入力待ち
      msg = input('')
    
      # 「end」が入力されたら接続を終了
      if 'end' in msg:
        print ('--- END ---')
        sock.close()  
        break

      # Tello EDUにコマンドを送る
      send_command(msg)

    # 例外発生時
    except Exception as ex:
      print (ex)
      sock.close() 

if __name__ == '__main__':
  main()