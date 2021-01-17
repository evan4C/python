# 申し込み側の選好（リストのリスト）
proposer = [['A', 'B', 'C'], ['A', 'C', 'B'], ['C', 'A', 'B']]
# 受け入れ側の選好（リストのリスト）
receiver = [[1, 2, 3], [1, 2, 3], [2, 3, 1]]

# DAアルゴリズム関数の定義
def da_algorithm (proposer, receiver):
  n = len(proposer)

  # データを変換
  _proposer = []
  _receiver = []
  for i, j in zip(proposer, receiver):
    _proposer.append(list(map(lambda x: ord(x) - ord('A'), i)))
    _receiver.append(list(map(lambda x: x - 1, j)))

  for i in range(n):  # ランク外を追加
    _receiver[i].append(n)
  
  order = [0] * n
  match_temp = [n] * n
  
  for i in range(n):
    p = i
    while p != n:
      r = _proposer[p][order[p]]
      print(str(p + 1) + " ---> " + str(chr(r + 65)))
      if _receiver[r].index(p) < _receiver[r].index(match_temp[r]):
        print("accepted")
        p_rejected = match_temp[r] 
        match_temp[r] = p 
        p = p_rejected
      else:
        print(str(p + 1) + " was rejected from " + str(chr(r + 65)))
        order[p] = order[p] + 1
  return [[match_temp[i] + 1, chr(i + 65)] for i in range(n)]

match = da_algorithm(proposer, receiver)
print(match)



