__author__ = 'chao-shu'
# -*- coding:utf-8 -*-
import re
import random

"""
    模拟退火法求最短路径
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

#产生一个随机初代
def route_beign():
    route = [0]+random.sample((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29),29)+[0]
    return route
route_1 = route_beign()
print route_1

#以距离作为评价函数
def routeLength(ro):
    i = 0
    sum = 0
    while i<30:
        sum = sum + distanceList[ro[i]][ro[i+1]]
        i = i + 1
    return  sum
# print routeLength(route_1)

#定义初始温度,以及降温速度
T = 10000
r = 0.99999
j = 0
k = 1
while T >=1:
    #变异新的路径
    route_2 = []
    for i in route_1:
        route_2.append(i)

    bianyi_1 = random.randint(1,14)
    bianyi_2 = random.randint(15,29)
    # bianyi_nn = route_2[bianyi_1]
    # route_2[bianyi_1] = route_2[bianyi_2]
    # route_2[bianyi_2] = bianyi_nn

    bianyi_nn = route_2[bianyi_1:bianyi_2+1]
    random.shuffle(bianyi_nn)
    route_2[bianyi_1:bianyi_2+1] = bianyi_nn


    # print bianyi_1,bianyi_2,route_2

    #变异前后的评价函数值（路径长度）对比
    dE = routeLength(route_2) - routeLength(route_1)
    if dE < 0:
        route_1 = route_2
    else:
        if (k)>random.uniform(0,1):
            route_1 = route_2
    print "canshu:",k
    j = j + 1
    T = r*T
    k = k*r
    print "wendu,cishu",T,j,routeLength(route_1)

print "路径：",route_1
print "路径长度",routeLength(route_1)

