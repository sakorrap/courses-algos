def PARTITION(A,p,r):
 x=A[r]
 i=p-1
 for j in range(p,r):
  if (A[j] <= x):
   i = i+1
   temp = A[j]
   A[j] = A[i]
   A[i] = temp
 temp = A[i+1]
 A[i+1] = A[r]
 A[r] = temp
 return i+1

def QUICKSORT(A,p,r):
 if (p<r) :
  q = PARTITION(A, p, r)
  QUICKSORT(A,p,q-1)
  QUICKSORT(A,q+1,r)
 return A

def main():
# givenArray = map(int,raw_input("Enter the input elements with delimiter as space :").split());
 givenArray=[55,10,2,33,12,44]
 print ("Given Array ", givenArray)
 start=0
 stop=len(givenArray) -1
 A = QUICKSORT(givenArray,start,stop)
 print ("Output :", A)
 print ("end ")
 
main()
 
  