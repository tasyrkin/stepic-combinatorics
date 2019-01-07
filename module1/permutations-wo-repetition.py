# task url: https://goo.gl/iDwV77 
import shlex
from collections import deque

tokenizer = shlex.shlex(posix=True)
tokenizer.whitespace_split=True
n = int(tokenizer.get_token())
k = int(tokenizer.get_token())

def solve(llist, lset, level, k, n):
  if level >= k:
    print (" ".join(llist))
    return
  for i in range(n):
    if i not in lset:
      lset.add(i)
      llist.append(str(i))
      solve(llist, lset, level+1, k, n)
      llist.pop()
      lset.remove(i)

solve(deque([]), set([]), 0, k, n)

