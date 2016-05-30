__author__ = 'chao-shu'
# -*- coding:utf-8 -*-
import re
import random

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
    distanceList = [[] for k in range(8)]
    while i < 8:
        while j < 8:
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
        route.append([0]+random.sample((1,2,3,4,5,6,7),7)+[0])
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
        while i<8:
            sum = sum + distanceList[line[i]][line[i+1]]
            i = i + 1
        routeLength.append(sum)
    # print routeLength
    return routeLength
# routeLength = routeLength(route)


def minRoutes(routeLength):
    s= []
    i = 0
    j = 0
    while i<8:
        minRoute = min(routeLength)
        if routeLength[i] == minRoute:
            s.append(i)
            a = routeLength[i]
            routeLength[i]=9999
            # minRoute = min(routeLength)
            # minRoutes()
            break
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
    routeLength[i] = a
    return s
# print minRoutes()



#交配,并且互换错误
# routeBak = []
# routeLenth = routeLength(route)
# s = minRoutes(routeLenth)
# routeBak = []
# for o in route[s[0]]:
#     routeBak.append(o)
# i = random.randint(1,6)
# j = random.randint(i,7)
# print i,j
# print s

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

#迭代50次
q = 0
while q<100:
    # routeLenth = []
    i = random.randint(1,6)
    j = random.randint(i,7)
    routeLenth = routeLength(route)
    s = minRoutes(routeLenth)
    min1 = [route[s[0]],route[s[1]]]
    # print "min1:",min1
    # b = random.randint(0,6)
    # c = random.randint(0,7)
    # if b == c:
    #     c = b + 1
    # route_max = [route[b],route[c]]
    # for xm in route:
    #     if xm == route[b] or xm == route[c]:
    #         route_max.append(xm)
    # print "max:",route_max

    routemin_1 = [route[s[0]]]
    # for x in route[s[0]]:
    #     routemin_1.append(x)
    routemin_2 = [route[s[1]]]
    # for y in route[s[1]]:
    #     routemin_2.append(y)
    # print "roumin1,2:",routemin_1,routemin_2
    # print "S=" ,s
    # print "i,j=",i,j
    a = route[s[0]][i:j+1]
    route[s[0]][i:j+1] = route[s[1]][i:j+1]
    route[s[1]][i:j+1] = a
    routeBak = []
    for o in route[s[0]]:
         routeBak.append(o)
    rectify(i,j,s)
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

    # xl = random.randint(1,4)
    # xt = random.randint(5,7)
    # mmt = routemin_1[0][xl]
    # routemin_1[0][xl] = routemin_1[0][xt]
    # routemin_1[0][xt] = mmt

    route =mmlist + routemin_1 + routemin_2
    # print "route = ",route
    q = q+1
    print "len:",len(route)
    print '本次最短路径为:',route[s[0]]
    print "1,2",routemin_1,routemin_2
    print "mmlist",mmlist
    print "routemax",route_max
    print "route",route
print '最终最短路径为:',route[s[0]]
print '最后结果:',routeLenth

