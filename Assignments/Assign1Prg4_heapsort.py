def maxHeapify(A,j,heapSize):
 print "for ",(j-1),"heapSize ",heapSize," for array ",A
 leftChildIndex = 2*j - 1
 rightChildIndex = 2*j
 largestIndex = j-1
 if (leftChildIndex <heapSize and A[leftChildIndex] > A[largestIndex]):
  largestIndex = leftChildIndex
  print "left is greater", A[leftChildIndex], "than", A[largestIndex]
 print leftChildIndex
 print rightChildIndex
 print largestIndex
 #print A[rightChildIndex]
 #print A[largestIndex]
 if (rightChildIndex <heapSize and A[rightChildIndex] > A[largestIndex]):
  largestIndex = rightChildIndex
 if (largestIndex != j-1):
  print "not equal for index ", j-1
  temp = A[j-1]
  A[j-1]=A[largestIndex]
  A[largestIndex]=temp
  maxHeapify(A,largestIndex,heapSize)
 
#End of maxHeapify

def buildMaxHeap(A):
 heapSize = len(A)
 for j in range(len(A)//2, 0, -1):
  maxHeapify(A,j,heapSize)

def heapSort(A):
 buildMaxHeap(A)
 return A

def main():
# givenArray = map(int,raw_input("Enter the input elements with delimiter as space :").split());
 givenArray=[55,10,2,33,12,44, 71]
 print "Given Array ", givenArray
 print "final array", heapSort(givenArray)
main()