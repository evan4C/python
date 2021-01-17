# KEY TEST
import pgzrun

def update():
  # SPACEキーが押されているか？
  if keyboard.space == True:
    print("SPACE")

# 何らかのキーが押されたら実行される
def on_key_down(key):
  # keyには押されたキーの情報が入る
  print(key)

# 何らかのキーから指が離れたら実行される
def on_key_up(key):
  # keyには指が離れたキーの情報が入る
  print(key)

pgzrun.go()   
