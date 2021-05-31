from copy import copy , deepcopy
import itertools
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
def goalCheck(arr , mode):
    # print("goaaaaaaaal check")
    global goalFrontier
    global sourceFrontier
    global goalVisit
    global sourceVisit
    state =  deepcopy(arr)
    if mode == 0:
        for i in range(len(goalFrontier)):
            if state == goalFrontier[i]:
                # print(i)
                return i
        for i in range(len(goalVisit)):
            if state == goalVisit[i]:
                # print(i)
                return i
        # for i in range(len(goalVisit)):
        #     if state == goalVisit[i]:
        #         print("yohooooooooooooooooooooooooooooooo")
        #         print(i)
        #         return i
    if mode == 1:
        for i in range(len(sourceFrontier)):
            if state == sourceFrontier[i]:
                return i
        for i in range(len(sourceVisit)):
            if state == sourceVisit[i]:
                return i
        # for i in range(len(sourceVisit)):
        #     if state == sourceVisit[i]:
        #         return i


    return -10

#our bfs algorithm
def bfs(mode):
    global depth
    global found
    global res
    global des
    global NumberOfNodes
    global NumberOfexpandedNodes
    global goalPathList
    global sourcePathList
    global goalFrontier
    global sourceFrontier
    global goalVisit
    global sourceVisit
    if found == True:
        return

    if mode == 0:
        # print("source frontier size = %d" %len(sourceFrontier))
        # print("source visited size = %d" %len(sourceVisit))

        if len(sourceFrontier) > 0:
            state = sourceFrontier.pop(0)
            sourceVisit.append(state)
            # print(state)
        else:
            print("state list is empty")
            return
        
        if len(sourcePathList) > 0:
            path = sourcePathList.pop(0)
        else:
            print("path list is empty")
            return

    if mode == 1:
        # print("goal frontier size = %d" %len(goalFrontier))
        # print("goal visited size = %d" %len(goalVisit))
        if len(goalFrontier) > 0:
            state = goalFrontier.pop(0)
            goalVisit.append(state)
            # print(state)
        else:
            print("goal state list is empty")
            return
        
        if len(goalPathList) > 0:
            path = goalPathList.pop(0)
        else:
            print("goal path list is empty")
            return
            
    if goalCheck(state , mode) > -1:

        # print("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
        if mode == 0:
            # if mode == 0:
            goalFrontierIndex = goalCheck(state , mode)
            # print("mode = 0")
            # print(goalVisit[goalFrontierIndex])
            # print(state)
            # print(path)
            # print(goalPathList[goalFrontierIndex])
            for i in range (1 , len(path)):
                finalPath.append(path[i])
            for i in range (len(goalPathList[goalFrontierIndex]) , 1 , -1):
                if goalPathList[goalFrontierIndex][i - 1] == "left":
                    finalPath.append("right")
                if goalPathList[goalFrontierIndex][i - 1] == "right":
                    finalPath.append("left")
                if goalPathList[goalFrontierIndex][i - 1] == "up":
                    finalPath.append("down")
                if goalPathList[goalFrontierIndex][i - 1] == "down":
                    finalPath.append("up")
        if mode == 1:
            sourceFrontierIndex = goalCheck(state , mode)
            # print("mode = 1")
            # print(sourceFrontier[sourceFrontierIndex])
            # print(state)
            # print(path)
            # print(sourcePathList[sourceFrontierIndex])
            for i in range (1 , len(sourcePathList[sourceFrontierIndex])):
                finalPath.append(sourcePathList[sourceFrontierIndex][i])
            for i in range (len(path) , 1 , -1):
                if path[i - 1] == "left":
                    finalPath.append("right")
                if path[i - 1] == "right":
                    finalPath.append("left")
                if path[i - 1] == "up":
                    finalPath.append("down")
                if path[i - 1] == "down":
                    finalPath.append("up")
        NumberOfNodes = NumberOfNodes + 1
        found = True
        return
    # print(depth)
    # NumberOfNodes = NumberOfNodes + 1

   
    # if found == True:
    #     if len(des) > 0:
    #         des.pop()
    #     return

    # for i in range(n):
    #     print(state[i])
    # print("****")
    # for i in range(n):
    #     print(stateVisit[i])
    # print("****")
    # print(path)
    # print("****")
    for i in range(n):
        for j in range(m):
            if state[i][j] == '#':
                jafarRow = i
                jafarCol = j

    if jafarCol > 0:
        #   if stateVisit[jafarRow][jafarCol - 1] == 0:
            leftChild = moveLeft(state)
            existCheck = False
            if mode == 0:
                for i in range(len(sourceVisit)):
                    if sourceVisit[i] == leftChild:
                        existCheck = True
                        break
                for i in range(len(sourceFrontier)):
                    if sourceFrontier[i] == leftChild:
                        existCheck = True
                        break
                if existCheck == False:
                    sourceFrontier.append(leftChild)
                    p = deepcopy(path)
                    p.append("left")
                    sourcePathList.append(p)
            if mode == 1:
                for i in range(len(goalVisit)):
                    if goalVisit[i] == leftChild:
                        existCheck = True
                        break
                for i in range(len(goalFrontier)):
                    if goalFrontier[i] == leftChild:
                        existCheck = True
                        break
                if existCheck == False:
                    goalFrontier.append(leftChild)
                    p = deepcopy(path)
                    p.append("left")
                    goalPathList.append(p)


    if jafarRow > 0:
        #   if stateVisit[jafarRow - 1][jafarCol] == 0:
            upChild = moveUp(state)
            existCheck = False
            if mode == 0:
                for i in range(len(sourceVisit)):
                    if sourceVisit[i] == upChild:
                        existCheck = True
                        break
                for i in range(len(sourceFrontier)):
                    if sourceFrontier[i] == upChild:
                        existCheck = True
                        break
                if existCheck == False:
                    sourceFrontier.append(upChild)
                    p = deepcopy(path)
                    p.append("up")
                    sourcePathList.append(p)
            if mode == 1:
                for i in range(len(goalVisit)):
                    if goalVisit[i] == upChild:
                        existCheck = True
                        break
                for i in range(len(goalFrontier)):
                    if goalFrontier[i] == upChild:
                        existCheck = True
                        break
                if existCheck == False:
                    goalFrontier.append(upChild)
                    p = deepcopy(path)
                    p.append("up")
                    goalPathList.append(p)


    if jafarCol < m - 1:
        #  if stateVisit[jafarRow][jafarCol + 1] == 0:
            rightChild = moveRight(state)
            existCheck = False
            if mode == 0:
                for i in range(len(sourceVisit)):
                    if sourceVisit[i] == rightChild:
                        existCheck = True
                        break
                for i in range(len(sourceFrontier)):
                    if sourceFrontier[i] == rightChild:
                        existCheck = True
                        break
                if existCheck == False:
                    sourceFrontier.append(rightChild)
                    p = deepcopy(path)
                    p.append("right")
                    sourcePathList.append(p)
            if mode == 1:
                for i in range(len(goalVisit)):
                    if goalVisit[i] == rightChild:
                        existCheck = True
                        break
                for i in range(len(goalFrontier)):
                    if goalFrontier[i] == rightChild:
                        existCheck = True
                        break
                if existCheck == False:
                    goalFrontier.append(rightChild)
                    p = deepcopy(path)
                    p.append("right")
                    goalPathList.append(p)


    if jafarRow < n - 1:
        #   if stateVisit[jafarRow + 1][jafarCol] == 0:
            downChild = moveDown(state)
            existCheck = False
            if mode == 0:
                for i in range(len(sourceVisit)):
                    if sourceVisit[i] == downChild:
                        existCheck = True
                        break
                for i in range(len(sourceFrontier)):
                    if sourceFrontier[i] == downChild:
                        existCheck = True
                        break
                if existCheck == False:
                    sourceFrontier.append(downChild)
                    p = deepcopy(path)
                    p.append("down")
                    sourcePathList.append(p)
            if mode == 1:
                for i in range(len(goalVisit)):
                    if goalVisit[i] == downChild:
                        existCheck = True
                        break
                for i in range(len(goalFrontier)):
                    if goalFrontier[i] == downChild:
                        existCheck = True
                        break
                if existCheck == False:
                    goalFrontier.append(downChild)
                    p = deepcopy(path)
                    p.append("down")
                    goalPathList.append(p)
#start******************************************************

    

#get inputs n is rows and m is columns'
n, m = map(int , input().split())
# print("First Number is: ", n)
# print("Second Number is: ", m)
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

#make one goal state************************
tmp = [] 
jafarIsStart = False
for i in range(n):
    for j in range(m):
        #height = states[i][j][0 : len(states[i][j]) - 1]
            if i == 0 and j == 0 and array[i][j] != "#":
                tmp.append(array[i][j][-1])
            elif i == 0 and j == 0 and array[i][j] == "#":
                jafarIsStart = True
                
            else:
                if jafarIsStart == True:
                    tmp.append(array[i][j][-1])
                    jafarIsStart = False
                check = True
                for i1 in range(len(tmp)):
                    if tmp[i1] == array[i][j][-1] or array[i][j][-1] == "#":
                        check = False
                        break
                if check == True:
                    tmp.append(array[i][j][-1])
goal = [] 
jafarGRow = 0
jafarGCol = 0
for k in range (len(tmp)):
    tmp1 = []
    for i in range(n):
        for j in range(m):
            if array[i][j][-1] == tmp[k]:
                tmp1.append(array[i][j])
    goal.append(tmp1)

for i in range(n):
    if len(goal[i]) == m - 1:
        jafarGRow = i
        goal[i].insert(0 , "#")

# for i in range(n):
#     print(goal[i])

for i in range(n):
    for j in range(m - 1):
        for k in range(j  + 1 , m):
            if goal[i][j] != "#" and goal[i][k] != "#":
                x1 = int(goal[i][j][0 : len(goal[i][j]) - 1])
                x2 = int(goal[i][k][0 : len(goal[i][k]) - 1])
                if x1 < x2:
                    tmp = goal[i][k]
                    goal[i][k] = goal[i][j]
                    goal[i][j] = tmp


# print("goaaaaaaaaal is :")
# print(goal)

# print(len(goals))


# for i in range(len(goals)):
#     print("x")
#     print(goals[i])

#source variables defination
sourceFrontier = []
sourceVisit = []


sourceFrontier.append(array)
# print(array)
# stateVisit = [[0 for x in range(m)] for y in range(n)]
# stateVisit[jafarRow][jafarCol] = 1
# sourceVisit.append(array)

p = []
p.append("start")
sourcePathList = []
sourcePathList.append(p)

#goal variables defination
goalFrontier = []
goalVisit = []

# g = itertools.permutations(goal)
# print(g)

# print("*******")
def perm(a, k=0):
   if k == len(a):
    g = deepcopy(a)
    goalFrontier.append(g)
    # print(a)
   else:
      for i in range(k, len(a)):
         a[k], a[i] = a[i] ,a[k]
         perm(a, k+1)
         a[k], a[i] = a[i], a[k]

perm(goal)
# print("*******")
# for i in range(len(goalFrontier)):
#      print(goalFrontier[i])
# goalFrontier.append(goal)
# for i in range(len(g)):
#     goalFrontier.append(g.pop)
# print(len(goalFrontier))
# goalFrontier.append(goal)
# stateVisit = [[0 for x in range(m)] for y in range(n)]
# stateVisit[jafarGRow][jafarGCol] = 1
# goalVisit.append(goal)

p = []
p.append("start")
goalPathList = []

for i in range(len(goalFrontier)):
    goalPathList.append(p)

depth = 1
found = False
res = 0
NumberOfNodes = 0
NumberOfexpandedNodes = 0
finalPath = []

count = 0
while(True):
    # print("source")
    # print("sourcce frontier is :")
    # print(sourceFrontier)
    # print("sourcce visited is :")
    # print(sourceVisit)
    bfs(0)
    if found == True:
        # print("founded")
        break
    if len(sourceFrontier) == 0:
        break
    # print("goal")
    # print("goal frontier is :")
    # print(goalFrontier)
    # print("goal visited is :")
    # print(goalVisit)
    bfs(1)
    if found == True:
        # print("founded")
        break
    if len(goalFrontier) == 0:
        break
# print("visits = %d" % len(goalVisit))
NumberOfNodes = len(sourceVisit) + len(goalVisit) + len(sourceFrontier) + len(goalFrontier)
NumberOfexpandedNodes = len(sourceVisit) + len(goalVisit) 
print("depth = %d" % len(finalPath))
for i in range(len(finalPath)):
    print(finalPath[i])

print("number of nodes is = %d" % NumberOfNodes)
print("number of expanded nodes is = %d" % NumberOfexpandedNodes)