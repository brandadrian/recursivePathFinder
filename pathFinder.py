class createnode:
 def __init__(self,val):
   self.data=val
   self.child=[]

def traverse(node, path = []):
    path.append(node.data)
    if len(node.child) == 0:
        print(path)
        path.pop()
        print(path)
    else:
        for child in node.child:
            traverse(child, path)
        path.pop()

def printarray(path):
  print(path)


root = createnode(10)
root.child.append(createnode(2))
root.child.append(createnode(4))

root.child[0].child.append(createnode(15))
root.child[0].child.append(createnode(20))
root.child[0].child.append(createnode(25))
root.child[0].child.append(createnode(30))

root.child[1].child.append(createnode(45))
root.child[1].child.append(createnode(50))
root.child[1].child.append(createnode(55))
root.child[1].child.append(createnode(60))
path=[]
total_val=30
traverse(root)

###################
#Expected output:
#
#[10, 2, 15]
#[10, 2, 20]
#[10, 2, 25]
#[10, 2, 30]
#[10, 4, 45]
#[10, 4, 50]
#[10, 4, 55]
#[10, 4, 60]
