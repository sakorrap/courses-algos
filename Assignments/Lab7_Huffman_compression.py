import Queue 

class HuffmanNode(object):
    def __init__(self, left=None, right=None, root=None):
        self.left = left
        self.right = right    

def create_tree(frequencies):
    p = Queue.PriorityQueue()
    for value in frequencies:   
        p.put(value)            
    while p.qsize() > 1:        
        l,r = p.get(), p.get()  
        node = HuffmanNode(l, r) 
        p.put((l[0]+r[0], node))      
    return p.get()               

weightedArray = [
    (8, 'a'), (1, 'b'), (2, 'c'), (4, 'd'), (6, 'e'), (1, 'f'), (1, 'g'), (2, 'h'), (5, 'i')]
print("Given array",weightedArray)
node = create_tree(weightedArray)

# Recursively walk the tree down to the leaves,
#   assigning a code value to each symbol
def get_huffmanCode(node, prefix="", code={}):
    if isinstance(node[1].left[1], HuffmanNode):
        get_huffmanCode(node[1].left,prefix+"0", code)
    else:
        code[node[1].left[1]]=prefix+"0"
    if isinstance(node[1].right[1],HuffmanNode):
        get_huffmanCode(node[1].right,prefix+"1", code)
    else:
        code[node[1].right[1]]=prefix+"1"
    return(code)

code = get_huffmanCode(node)
for i in sorted(weightedArray, reverse=True):
    print(i[1], code[i[1]])
