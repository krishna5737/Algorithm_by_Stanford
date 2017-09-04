import sys
from heapq import *

sys.setrecursionlimit(1800)

V = {}

class BT:
  def __init__(self, left = None, right = None, value = None):
    self.value = value
    self.left = BT(None, None, left) if left else None
    self.right = BT(None, None, right) if right else None
    V[self.value] = self

  def getLength(self, fn):
    if not (self.left and self.right):
      return 0

    leftLength = self.left.getLength(fn) if self.left else 0
    rightLength = self.right.getLength(fn) if self.right else 0

    return(1 + fn(leftLength, rightLength))


def huffman(character):

  if len(character) == 2:
    return BT(character[0][1], character[1][1])
  (pa, a) = heappop(character)
  (pb, b) = heappop(character)
  ab = str(a) + '_' + str(b)
  heappush(character, (pa + pb, ab))
  M = huffman(character)
  V[ab].__dict__.update(BT(a, b).__dict__)
  return M


if __name__ == '__main__':
  input_file_name = 'huffman.txt'
  character = []

  with open(input_file_name) as f:
    f.readline() 
    nam = 0
    for line in f:
      nam += 1
      heappush(character, (int(line.rstrip()), nam))
      
  tree = huffman(character)
  print(tree.getLength(min)) 
  print(tree.getLength(max)) 
