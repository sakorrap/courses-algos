listX = map(int,raw_input("Enter the input elements with delimiter as space :").split());
for elem in range(len(listX)):
 insertSortElem = elem
 hold = listX[elem]
 while ((insertSortElem > 0) and (listX[insertSortElem-1] > hold)):
  listX[insertSortElem] = listX[insertSortElem -1]
  insertSortElem-=1
 listX[insertSortElem]= hold
print "sorted array ", listX