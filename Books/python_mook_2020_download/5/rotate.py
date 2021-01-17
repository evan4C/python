import numpy as np

# 変換前の座標
p1 = np.matrix([[50], [50], [0]])  # x, y, z の順

# x軸まわりに45度回転するための行列
th = np.radians(45)
X = np.matrix([[1, 0, 0], [0, np.cos(th), np.sin(th)], [0, -np.sin(th), np.cos(th)]])

# 変換後の座標
p2 = X * p1
print(p2.astype('int16'))