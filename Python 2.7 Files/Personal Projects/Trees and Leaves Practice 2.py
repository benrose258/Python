#Trees and Leaves Practice Document 2

Species = ("J",("N",(),()),("F",("S",(),()),("A",("T",(),()),("H",("L",(),()),("W",(),())))))

def leaf(Tree):
    if Tree[1] == () and Tree[2] == ():
        return True
    else:
        return False

def find(species,Tree):
    if Tree[0] == species:
        return True
    elif leaf(Tree) == True:
        return False
    else:
        return find(species,Tree[1]) or find(species,Tree[2])

def size(Tree):
    if Tree == ():
        return 0
    elif leaf(Tree) == True:
        return 1
    else:
        return 1 + size(Tree[1]) + size(Tree[2])

def numLeaves(Tree):
    if Tree == ():
        return 0
    elif leaf(Tree) == True:
        return 1 + numLeaves(Tree[1]) or numLeaves(Tree[2])
    else:
        return numLeaves(Tree[1]) + numLeaves(Tree[2])

def height(Tree):
    if Tree == ():
        return 0
    elif leaf(Tree) == False:
        return 1 + height(Tree[1]) + height(Tree[2])
    else:
        return 0

def listAll(Tree):
    if Tree == ():
        return []
    elif leaf(Tree) == True:
        return [Tree[0]]
    else:
        return [Tree[0]] + listLeaves(Tree[1]) + listLeaves(Tree[2])

def listLeaves(Tree):
    if Tree == ():
        return []
    else:
        return [Tree[0]] + listLeaves(Tree[1]) + listLeaves(Tree[2])

def lca(species1,species2,Tree):
    if Tree == ():
        return None
    else:
        Root = Tree[0]
        Left = Tree[1]
        Right = Tree[2]
        if find(species1,Left)==True and find(species2,Left)==True:
            return lca(species1,species2,Left)
        elif find(species1,Right) == True and find(species2,Right) == True:
            return lca(species1,species2,Right)
        else:
            return Root

def maxTree(Tree):
    if Tree == ():
        return 0
    elif leaf(Tree) == True:
        return Tree[0]
    else:
        return max(maxTree(Tree[1]), maxTree(Tree[2]))
    
def sumTree(Tree):
    if Tree == ():
        return 0
    else:
        if leaf(Tree) == True:
            return Tree[0]
        else:
            return Tree[0] + sumTree(Tree[1]) + sumTree(Tree[2])

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
