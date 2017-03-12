qtd_strs = int(input())

strs = [input() for i in range(qtd_strs)]

for str in strs:

  total = 0
  o_sum = 0
  for ch in str:
    if ch == 'O':
      o_sum += 1
      total += o_sum
    elif ch == 'X':
      o_sum = 0

  print(total)

