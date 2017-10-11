def merge(givenarray, begin, mid, end):
 print ("In merge with arguments ", begin, mid, end)
 
 begin1=begin
 end1=mid
 begin2=mid+1
 end2=end
 p=begin1
 q=begin2
 tempArray = []
 while ((p <= end1) and (q <=end2)):
  print ("inside while" , p,q,end1,end2)
  if(givenarray[p] <= givenarray[q]):
   tempArray.append(givenarray[p])
   
   p+=1
  else:
   tempArray.append(givenarray[q])
   
   q+=1
  print ("Sorted array before while", tempArray)
 if (p>end1):
  print ("P exosted :", q, givenarray[q])
  while (q <= end2):
   print ("Append q", q) 
   tempArray.append(givenarray[q])
   q+=1
   
 if (q>end2):
  print ("q exosted :", p, givenarray[p])
  while (p<= end1):
   tempArray.append(givenarray[p])
   p+=1
 
 for i in range(len(tempArray)):
  givenarray[begin+i]=tempArray[i]
  print ("Sorted array :", tempArray)

def mergeSort(givenArray,start,stop):
 mid=0
 if start<stop :
  mid = (start + stop)//2;
  print ("In if loop, with start and stop as :", start, stop)
  mergeSort(givenArray,start,mid)
  mergeSort(givenArray,mid+1,stop)
  merge(givenArray,start,mid,stop)
 print ("Final sorted array :", givenArray)

def main():
# givenArray = map(int,raw_input("Enter the input elements with delimiter as space :").split());
 givenArray=[55,10,2,33,12,44]
 print ("Given Array ", givenArray)
 start=0
 stop=len(givenArray) -1
 mergeSort(givenArray,start,stop)
 print ("end ")
 
main()
