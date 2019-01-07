# task url: https://goo.gl/sbrktF 
import shlex
from collections import deque

tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True
k = int(tokenizer.get_token())
n = int(tokenizer.get_token())

def solve(llist, num, rest_k, n):
  if num+rest_k >= n:
    return
  if rest_k == 0:
    print (" ".join(llist))
    return
  for i in range(num+1, n):
    llist.append(str(i))
    solve(llist, i, rest_k-1, n)
    llist.pop()

llist = deque([])
for i in range(n):
  llist.append(str(i))
  solve(llist, i, k-1, n)
  llist.pop()
