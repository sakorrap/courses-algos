import math

def BUCKET_SORT(A):
  B = [[]]
  n = len(A)
  for i in range(n-1):
    B.append([-1])
  for i in range(n):
    index = int(math.floor(n * A[i]))
    temp= []
    temp.append(A[i])
    B[index].append(temp)
  for i in range(len(B)):
    if type(B[i]) is list:
      B[i] = insertion_sort(B[i])
  for i in range(len(B)):
    if -1 in B[i]:
      B[i].remove(-1)
  B = filter(None, B)
  return B

def insertion_sort(A):
  j = 0
  while j < len(A):
    i = 0
    while i < (len(A)-1-j):
      if A[i] > A[i+1]:
        k = A[i]
        A[i] = A[i+1]
        A[i+1] = k
      i=i+1
    j=j+1
  return A
A = [0.3,0.1,0.8,0.4,0.2,0.6]
print(BUCKET_SORT(A))
