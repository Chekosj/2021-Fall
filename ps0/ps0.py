#################
#               #
# Problem Set 0 #
#               #
#################



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
    # Set the temp for each node in the tree
    # The return value is up to you
    
    # Your code goes here
    if T == None: #Check to make sure tree actually exists
        return 0
    T.temp = (calculate_size(T.left) + 1 + calculate_size(T.right))
    return(T.temp)
    
    # for T.left in T:
    #     return calculate_size(T.left)


    
    
    # else:
    #     T.temp == (calculate_size(T.left) + 1 + calculate_size(T.right)) #Attempting to add up what the value for current temp should be
    #     return (T.left) and (T.right) #Need to return Left and make it go all the way then go to the right and go all the way down. 
    #                                   #Not sure how I would do that yet.



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

    # Your code goes here
    pass


