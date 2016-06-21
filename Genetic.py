__author__ = 'chao-shu'
# -*- coding:utf-8 -*-
import re
import random

"""
    遗传算法求最短路径
"""

#读取文件并计算各个城市之间的距离矩阵
def distance(A,B):
    return ((float(A[0]) - float(B[0]))**2 + (float(A[1]) - float(B[1]))**2)**0.5
#距离矩阵的求取
def distanceArr():
    file = open('30个城市.txt','r')
    fileString = file.read()
    file.close()
    fileList = fileString.split(";")
    fileNumStr = []
    for l in fileList:
        fileNumStr.append(re.findall('[0-9]+', l))
    # print fileNumStr
    i = 0
    j = 0
    distanceList = [[] for k in range(30)]
    while i < 30:
        while j < 30:
            distanceList[i].append(int(distance(fileNumStr[i],fileNumStr[j])))
            j = j + 1
        i = i + 1
        j = 0
    return  distanceList
distanceList = distanceArr()
for l in distanceList:print l

#假设从第0号点出发，最后回到第一点，产生8个随机的初代.
def  route():
    route = []
    i = 0
    while i < 8:
        route.append([0]+random.sample((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29),29)+[0])
        i = i + 1
    return route
route = route()
print "初代：",route

#选出路径最短的2条线路s[0]s[1]
def routeLength(ro):
    routeLength = []
    for line in ro:
        i = 0
        sum = 0
        while i<30:
            sum = sum + distanceList[line[i]][line[i+1]]
            i = i + 1
        routeLength.append(sum)
    # print routeLength
    return routeLength
# print "路径长度",routeLength(route)


def minRoutes(routeLength):
    s= []
    i = 0
    j = 0
    k = 0
    while i<8:
        minRoute = min(routeLength)
        if routeLength[i] == minRoute and k == 0:
            s.append(i)
            # a = routeLength[i]
            routeLength[i] = str(routeLength[i])
            k = k + 1
            i = i + 1
            # minRoute = min(routeLength)
            # minRoutes()
            # break
        elif routeLength[i] == minRoute and k>0:
            routeLength[i] = str(routeLength[i])
            i = i + 1
        else:i=i+1
    while j<8:
        minRoute = min(routeLength)
        if routeLength[j] == minRoute:
            s.append(j)
            # routeLength[j]=9999
            # minRoute = min(routeLength)
            # minRoutes()
            break
        else:j=j+1
    qq = 0
    while qq<8:
        routeLength[qq] = int(routeLength[qq])
        qq = qq + 1
    return s
# print minRoutes()



#交配,并且互换错误
#

def rectify(i,j,s):
    #交叉配对
    # for o in route[s[0]]:
    #     routeBak.append(o)
    # print route
    for m in range(i,j+1):
        for n in range(0,i):
            if route[s[0]][m] == route[s[0]][n]:
                route[s[0]][n] = route[s[1]][m]
        for n in range(j+1,len(route[s[0]])-1):
            if route[s[0]][m] == route[s[0]][n]:
                route[s[0]][n] = route[s[1]][m]
    for m in range(i,j+1):
        for n in range(0,i):
            if route[s[1]][m] == route[s[1]][n]:
                route[s[1]][n] = routeBak[m]
        for n in range(j+1,len(route[s[0]])-1):
            if route[s[1]][m] == route[s[1]][n]:
                route[s[1]][n] = routeBak[m]
    if len(route[s[0]]) == (len(set(route[s[0]]))+1) and len(route[s[1]]) == (len(set(route[s[1]]))+1):
        return True
    else:
        rectify(i,j,s)

#第一次交配结果
# print route

#迭代500次
q = 0
while q<=200000:
    # routeLenth = []
    i = random.randint(1,28)
    j = random.randint(i,29)
    routeLenth = routeLength(route)
    # print "chadu",routeLenth
    s = minRoutes(routeLenth)
    # min1 = [route[s[0]],route[s[1]]]

    routemin_1 = []
    for x in route[s[0]]:
        routemin_1.append(x)
    routemin_2 = []
    for y in route[s[1]]:
        routemin_2.append(y)
    a = route[s[0]][i:j+1]
    route[s[0]][i:j+1] = route[s[1]][i:j+1]
    route[s[1]][i:j+1] = a
    routeBak = []
    for o in route[s[0]]:
         routeBak.append(o)
    rectify(i,j,s)
    bianyi = 0
    while bianyi<=3:
        bianyi_1 = random.randint(0,7)
        bianyi_2 = random.randint(1,14)
        bianyi_3 = random.randint(15,29)
        bianyi_nn = route[bianyi_1][bianyi_2]
        route[bianyi_1][bianyi_2] = route[bianyi_1][bianyi_3]
        route[bianyi_1][bianyi_3] = bianyi_nn

        bianyi_2 = random.randint(1,14)
        bianyi_3 = random.randint(15,29)
        bianyi_nn = route[bianyi_1][bianyi_2]
        route[bianyi_1][bianyi_2] = route[bianyi_1][bianyi_3]
        route[bianyi_1][bianyi_3] = bianyi_nn

        bianyi_2 = random.randint(1,14)
        bianyi_3 = random.randint(15,29)
        bianyi_nn = route[bianyi_1][bianyi_2]
        route[bianyi_1][bianyi_2] = route[bianyi_1][bianyi_3]
        route[bianyi_1][bianyi_3] = bianyi_nn

        bianyi_2 = random.randint(1,14)
        bianyi_3 = random.randint(15,29)
        bianyi_nn = route[bianyi_1][bianyi_2]
        route[bianyi_1][bianyi_2] = route[bianyi_1][bianyi_3]
        route[bianyi_1][bianyi_3] = bianyi_nn
        bianyi_2 = random.randint(1,14)
        bianyi_3 = random.randint(15,29)
        bianyi_nn = route[bianyi_1][bianyi_2]
        route[bianyi_1][bianyi_2] = route[bianyi_1][bianyi_3]
        route[bianyi_1][bianyi_3] = bianyi_nn
        bianyi = bianyi + 1
    while True:
        b = random.randint(1,(len(route)-2))
        c = random.randint(1,len(route)-2)
        if b == c:
            c = b - 1
        if b!=s[0]and b!=s[1]and c!=s[0]and c!=s[1]:
            break

    route_max = [route[b],route[c]]

    mmlist = []
    kk = 0
    for mm in route:
        if kk<2:
            if mm not in route_max:
                mmlist.append(mm)
            else:
                kk = kk + 1
        else:
            mmlist.append(mm)

    route =mmlist + [routemin_1] + [routemin_2]
    q = q+1
    print "迭代次数：",q
    # print '本次最短路径为:',route[s[0]]
    print '本次结果:',routeLenth[s[0]]
    if routeLenth[s[0]]<=435:
         break

    # print "route",route
    # print 's:',s
print "s[0]",s[0]
print routeLenth
print '最终最短路径为:',route[s[0]]
print '最后结果:',routeLenth[s[0]]

