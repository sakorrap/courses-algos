#Python 1 Test program

listX = map(int,raw_input("Enter the input elements with delimiter as space :").split());

for element in range(len(listX)):
 for sortingElement in range(len(listX)-1-element):
  if (listX[sortingElement]>listX[sortingElement+1]):
   temp = listX[sortingElement]
   listX[sortingElement]=listX[sortingElement+1]
   listX[sortingElement+1] = temp
 print "sorted array", element
 print "is ", listX
print "End of Array"
  
