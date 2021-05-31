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
def goalCheck(arr):
    # print("goaaaaaaaal check")
    global goals
    state =  deepcopy(arr)
    gt = deepcopy(goals)
    for i in range(len(gt)):
        if gt[i] == state:
            return True
    return False
    

# heuristic func **********************************
def heuristic(arr):
    global goals
    state = deepcopy(arr)
    tmp_goals = deepcopy(goals)
    minCost = 0
    for k in range(len(goals)):
        cost = 0
        g = tmp_goals.pop(0)
        # print(g)
        for i in range(n):
            for j in range(m):
                for i1 in range(n):
                    for j1 in range(m):
                        if state[i][j] == g[i1][j1]:
                            # print("state is",state[i][j])
                            # print("goal is",g[i1][j1])
                            # print(abs(i - i1))
                            # print(abs(j - j1))
                            cost = cost + abs(i - i1)
                            cost = cost + abs(j - j1)
        # print("k = ",k)
        # print("cost = ",cost)

        if k == 0:
            minCost = cost
        else:
            if cost < minCost:
                minCost = cost
    return minCost

#our bfs algorithm
def A_star():
    global found
    global NumberOfNodes
    global NumberOfexpandedNodes
    global sourcePathList
    global sourceFrontier
    global sourceVisit
    global costs

    while(True):
        if found == True:
            break

        # print("source frontier size = %d" %len(sourceFrontier))
        # print("source visited size = %d" %len(sourceVisit))

        if len(sourceFrontier) > 0:
            min = 0
            index = 0
            for i in range(len(sourceFrontier)):
                if i == 0:
                    min = costs[i]
                    index = i
                else:
                    if costs[i] < min:
                        min = costs[i]
                        index = i

            # print("min = ",min)
            # print("index = ",index)
            # print("real cost = ", costs[index])
            state = sourceFrontier.pop(index)
            sourceVisit.append(state)
            # print(state)
        else:
            print("state list is empty")
            return
        
        if len(sourcePathList) > 0:
            path = sourcePathList.pop(index)
        else:
            print("path list is empty")
            return

        if len(costs) > 0:
            cost = costs.pop(index)
        else:
            print("costs list is empty")
            return

        # print("state = ", state)
        # print("path = ", path)
        # print("cost = ", cost)
        # print("frontier size = ", len(sourceFrontier))
        # print("visited size = ", len(sourceVisit))
        # print("costs = ", costs)

        # call goal check on current state
        if goalCheck(state):
            # print("*********found**********")
            finalPath.append(path)
            found = True
            return

        # find '#' location on our state
        for i in range(n):
            for j in range(m):
                if state[i][j] == '#':
                    jafarRow = i
                    jafarCol = j

        # make left child
        if jafarCol > 0:
            leftChild = moveLeft(state)
            existCheck = False

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
                c = 0
                c = c + heuristic(state)
                c = c + len(path) + 1
                costs.append(c)


        # make up child
        if jafarRow > 0:
            upChild = moveUp(state)
            existCheck = False
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
                c = 0
                c = c + heuristic(state)
                c = c + len(path) + 1
                costs.append(c)

        # make right child
        if jafarCol < m - 1:
            rightChild = moveRight(state)
            existCheck = False

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
                c = 0
                c = c + heuristic(state)
                c = c + len(path) + 1
                costs.append(c)

        # make down child
        if jafarRow < n - 1:
            downChild = moveDown(state)
            existCheck = False

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
                c = 0
                c = c + heuristic(state)
                c = c + len(path) + 1
                costs.append(c)

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

goals = []
# find all possible goals
def perm(a, k=0):
   if k == len(a):
    g = deepcopy(a)
    goals.append(g)
    # print(a)
   else:
      for i in range(k, len(a)):
         a[k], a[i] = a[i] ,a[k]
         perm(a, k+1)
         a[k], a[i] = a[i], a[k]

perm(goal)

#source variables defination
sourceFrontier = []
sourceVisit = []
sourcePathList = []
costs = []

sourceFrontier.append(array)
costs.append(heuristic(array))

p = []
p.append("start")
sourcePathList.append(p)

# print(array)

found = False
NumberOfNodes = 0
NumberOfexpandedNodes = 0
finalPath = []

A_star()
depth = len(finalPath[0]) - 1
print("depth = ", depth)
for i in range(1 , len(finalPath[0])):
    print(finalPath[0][i])


# count = 0
# while(False):
#     # print("source")
#     # print("sourcce frontier is :")
#     # print(sourceFrontier)
#     # print("sourcce visited is :")
#     # print(sourceVisit)
#     bfs(0)
#     if found == True:
#         print("founded")
#         break
#     if len(sourceFrontier) == 0:
#         break

NumberOfNodes = len(sourceVisit)+ len(sourceFrontier)
NumberOfexpandedNodes = len(sourceVisit)
print("number of nodes is = %d" % NumberOfNodes)
print("number of expanded nodes is = %d" % NumberOfexpandedNodes)
# print("depth = %d" % len(finalPath))
# for i in range(len(finalPath)):
#     print(finalPath[i])
