__author__ = 'chao-shu'
import random
a = [1,2,3,4,5,6,7,8]
b = a[2:5]
print b
random.shuffle(b)
print b
a[2:5]=b
print b,a