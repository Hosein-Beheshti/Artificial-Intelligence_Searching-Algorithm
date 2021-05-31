from copy import copy , deepcopy
# takes an 2Darray then find "#" and 
# swap with left child and return new array 
def moveLeft(arr):
    tmpArr =  deepcopy(arr)

    for i in range(n):
        for j in range(m):
            if tmpArr[i][j] == '#':
                jafarRow = i
                jafarCol = j
    tmp = tmpArr[jafarRow][jafarCol - 1]
    tmpArr[jafarRow][jafarCol - 1] = "#"
    tmpArr[jafarRow][jafarCol] = tmp
    # print("hey")
    # print(arr)
    
    return tmpArr
# takes an 2Darray then find "#" and 
# swap with right child and return new array 
def  moveRight(arr):
    tmpArr =  deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if tmpArr[i][j] == '#':
                jafarRow = i
                jafarCol = j
    tmp = tmpArr[jafarRow][jafarCol + 1]
    tmpArr[jafarRow][jafarCol + 1] = "#"
    tmpArr[jafarRow][jafarCol] = tmp
    #print(arr)
    return tmpArr
# takes an 2Darray then find "#" and 
# swap with Up child and return new array 
def moveUp(arr):
    tmpArr =  deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if tmpArr[i][j] == '#':
                jafarRow = i
                jafarCol = j
    tmp = tmpArr[jafarRow - 1][jafarCol]
    tmpArr[jafarRow - 1][jafarCol] = "#"
    tmpArr[jafarRow][jafarCol] = tmp
    #print(arr)
    return tmpArr
# takes an 2Darray then find "#" and 
# swap with down child and return new array 
def moveDown(arr):
    tmpArr =  deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if tmpArr[i][j] == '#':
                jafarRow = i
                jafarCol = j
    tmp = tmpArr[jafarRow + 1][jafarCol]
    tmpArr[jafarRow + 1][jafarCol] = "#"
    tmpArr[jafarRow][jafarCol] = tmp
    #print(arr)
    return tmpArr
#goal check func
#takes an array and return 
# false if it's not final goal and return true if it's our goal
def goalCheck(arr):
    states =  deepcopy(arr)
    s = ""
    for i in range(n):
        for j in range(m):
            if states[i][j] == "#" and j != 0:
                return False

            height = states[i][j][0 : len(states[i][j]) - 1]
            if j == 0:
                if  states[i][j] != "#":
                    s = states[i][j][-1]
                else :
                    s = states[i][j + 1][-1]
            elif states[i][j] != "#" and states[i][j - 1] != "#": 
                #print("heeeeeeeeeeey")
                #print(states[i][j][0 : len(states[i][j - 1]) - 1])
                h1 = int(states[i][j][0 : len(states[i][j]) - 1])
                #print(h1)
                h2 = int(states[i][j - 1][0 : len(states[i][j - 1]) - 1])
                #print(h2)
                
                if h1 > h2:
                    return False

            if states[i][j][-1] != s and states[i][j] != "#":
                return False
    # print(states)
    global path
    path = deepcopy(des)

    return True
#our dfs algorithm
def dfs(states , d):
    global depth
    global found
    global res
    global des
    global NumberOfNodes
    global NumberOfexpandedNodes

    # print(depth)
    NumberOfNodes = NumberOfNodes + 1

    if goalCheck(states):
        # NumberOfNodes = NumberOfNodes + 1
        found = True
        res = states
        return
    if found == True:
        if len(des) > 0:
            des.pop()
        return
    # if d > depth:
    #     if len(des) > 0:
    #         des.pop()
    #     return

    leftExist = False
    rightExist = False
    upExist = False
    downExist = False

  
    # for i in range(n):
    #     print(states[i])
    # print("****")
    for i in range(n):
        for j in range(m):
            if states[i][j] == '#':
                jafarRow = i
                jafarCol = j
    
    if jafarCol > 0 and d <= depth:
        #print("left child is %s" % arr[jafarRow][jafarCol - 1])
        #dfs(moveLeft(states) , d = d + 1)
        leftChild = moveLeft(states)
        leftExist = True
        # print(states)
        # print(leftChild)
    if jafarRow > 0 and d <= depth:
        #print("UP child is %s" % arr[jafarRow - 1][jafarCol])
        #dfs(moveUp(states) , d = d + 1)
        upChild = moveUp(states)
        upExist = True
    if jafarCol < m - 1 and d <= depth:
        #print("right child is %s" % arr[jafarRow][jafarCol + 1])
        #dfs(moveRight(states) , d = d + 1)
        rightChild = moveRight(states)
        rightExist = True
    if jafarRow < n - 1 and d <= depth:
        #print("down child is %s" % arr[jafarRow + 1][jafarCol])
        #dfs(moveDown(states) , d = d + 1)
        downChild = moveDown(states)
        downExist = True
    
    if leftExist:
        if d + 1 <= depth:
            des.append("left")
            dfs(leftChild , d = d + 1)
    if upExist:
        if d + 1 <= depth:
            des.append("up")
            dfs(upChild , d = d + 1)
    if rightExist:
        if d + 1 <= depth:
            des.append("right")
            dfs(rightChild , d = d + 1)
    if downExist:
        if d + 1 <= depth:
            des.append("down")
            dfs(downChild , d = d + 1)
    if len(des) > 0:
        des.pop()
    NumberOfexpandedNodes = NumberOfexpandedNodes + 1

#get inputs n is rows and m is columns
n, m = map(int , input().split())
#print("First Number is: ", n)
#print("Second Number is: ", m)
#get n*m list includes height and name of student's classes
array=[]
for i in range(0,n):
    inputs = list(input().split())
    if len(inputs) != m:
        break
    array.append(inputs)

for i in range(n):
    for j in range(m):
     if array[i][j] == '#':
       jafarRow = i
       jafarCol = j

# print("i = %d j = %d" % (jafarRow,jafarCol))
# if jafarCol > 0:
#     print("left child is %s" % arr[jafarRow][jafarCol - 1])
# if jafarCol < m - 1:
#     print(m)
#     print(jafarCol)
#     print("right child is %s" % arr[jafarRow][jafarCol + 1])
# if jafarRow > 0:
#     print("UP child is %s" % arr[jafarRow - 1][jafarCol])
# if jafarRow < n - 1:
#     print("down child is %s" % arr[jafarRow + 1][jafarCol])




depth = 1
found = False
res = 0
path = 0
NumberOfNodes = 0
NumberOfexpandedNodes = 0

while(True):
    des = []
    dfs(array , 0)
    depth = depth + 1
    if found == True:
        break

# print(res)
# print(path)
# depth = 2
# dfs(array , 0)
print("depth = ",len(path))
for i in range(len(path)):
    print(path[i])
print("number of nodes is = %d" % NumberOfNodes)
print("number of expanded nodes is = %d" % NumberOfexpandedNodes)