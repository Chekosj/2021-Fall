#################
#               #
# Problem Set 0 #
#               #
#################

import math

#
# Setup
#

class BinaryTree:
    # left : BinaryTree
    # right : BinaryTree
    # key : string
    # temp : int
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.temp = None



#
# Problem 1
#

# Sets the temp of each node in the tree T
# ... to the size of that subtree
def calculate_size(T):
    if T == None: #Check to make sure tree actually exists
        return 0
    T.temp = (calculate_size(T.left) + 1 + calculate_size(T.right))
    return(T.temp)

#
# Problem 3
#

# Outputs a subtree subT of T of size in the interval [L,U] 
# ... and removes subT from T by replacing the pointer 
# ... to subT in its parent with `None`
def FindSubtree(T, L, U): 
    # Instructions:
    # Implement your Part 2 proof in O(n)-time
    # The return value is a subtree that meets the constraints

    if T == None:
        return 0 
    if (calculate_size(T) > U) & (calculate_size(T) >= 2*L) : 
        if T.left == None :
            FindSubtree ()


    pass



# T = BinaryTree(None,1)

# T.left = BinaryTree(None,2)
# T.right = BinaryTree(None,3)
# T.left.left = BinaryTree(None,4)
# T.right.right = BinaryTree(None,5)
# T.right.right.left = BinaryTree(None,6)
# T.right.right.right = BinaryTree(None,7)
# T.right.right.right.right = BinaryTree(None,8)

# def Balance(T: BinaryTree):
#     calculate_size(T)
#     if T.temp<=2:
#         return T
#     else:
#         L = math.floor(T.temp/3)
#         U = math.ceil(2*T.temp/3)
#         subT = FindSubtree(T,L,U)
#         newT = BinaryTree()
#         newT.left = Balance(T)
#         newT.right = Balance(subT)
#         return newT

# print (Balance (T))



t = math.ceil(2*8/3)

print (t)