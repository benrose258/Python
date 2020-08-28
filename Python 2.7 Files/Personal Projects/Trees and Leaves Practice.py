#Trees and Leaves Practice

Species = ("J",("N",(),()),("F",("S",(),()),("A",("T",(),()),("H",("L",(),()),("W",(),())))))

def leaf(Tree):
    #Leaves have () to the left and right!
    if Tree[1] == () and Tree[2] == ():
        return True
    else:
        return False

def leafhelp(Tree):
    #Leaves have () to the left and right!
    if Tree[0] == () and Tree[1] == ():
        return True
    else:
        return False

def grandLeaf(grandTree):
    checkLeaf = grandTree[1:]
    if leaf(checkLeaf[0]) and leaf(checkLeaf[1]) == True:
        return True
    else:
        return False

def find(species,Tree):
    if Tree == ():
        return False
    else:
        #Check if the species we are searching for is equal to the first item in the tree
        checkitem = Tree[0]
        if checkitem[0] == species:
            return True
        #Check if the first item is a leaf. If it is, then we cannot check any more items.
        elif leafhelp(checkitem) == True:
            return False
       #If it isn't a leaf, then you can continue to check in the next part of the tree, which
       #will be made up of the two branches, which each need to be checked.
        else:
            return find(species,Tree[1]) or find(species,Tree[2])

   #Graphic representation of the tree can be found in the slides.
        
   #The variable "Tree" is the entire list of items you are checking. Species refers to
   #the one species you are trying to find.
        
   #If there is nothing left in the tree(because we checked everything with recursion),
   #then the root isn't in the tree, so we return false.

def size(Tree):
    if Tree == ():
        return 0
    else:
        if leaf(Tree) == True:
            return 1
        else:
            return 1 + size(Tree[1]) + size(Tree[2])

def numLeafs(Tree):
    if leaf(Tree) == True:
        return 1
    else:
        return numLeafs(Tree[1]) + numLeafs(Tree[2])

def listAll(Tree):
    if Tree == ():
        return []
    else:
        if leaf(Tree) == True:
            return [Tree[0]]
        else:
            return [Tree[0]] + listAll(Tree[1]) + listAll(Tree[2])

def sumTree(Tree):
    return sum(listAll(Tree))

def sumTree2(Tree):
    if Tree == ():
        return 0
    else:
        if leaf(Tree) == True:
            return Tree[0]
        else:
            return Tree[0] + sumTree2(Tree[1]) + sumTree2(Tree[2])

def mirrorTree(Tree):
    root = Tree[0]
    Left = Tree[1]
    Right = Tree[2]

    LeftRoot = Left[0]
    LeftLeft = Left[1]
    LeftRight = Left[2]

    RightRoot = Right[0]
    RightLeft = Right[1]
    RightRight = Right[2]

    newLeft = (LeftRoot,LeftRight,LeftLeft)
    newRight = (RightRoot,RightRight,RightLeft)
    newTree = (root,newRight,newLeft)
    print newTree


