import numpy as np
import matplotlib.pyplot as plt
def init(n):
    return np.array([i for i in range(0,n)])

def select2(x):
    l = len(x)
    i = np.random.randint(0, l)
    j = i
    while (j == i):
        j = np.random.randint(0, l)
    return (i,j)

    
def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

def isDerangement(a):
    l = len(a)
    for i in range(0, l):
        if a[i] == i:
            return False
    return True

def permute(a):
    while not isDerangement(a):
        a = np.random.permutation(a)
    return a #must assign the return value to take effect

def alg(a, b):
    (i, j) = select2(b)
    swap(a, i, j)
       


n = 5 #length of array
der_len = 4 #der size we are interested in, for example n-1
p = [i for i in range(0, der_len)]
p = np.array(p)
b = init(n)
h = []

total = 0
for i in range(0,10000): #trials
    a = init(n)
    a = permute(a)
    while (len(a)==n):
        alg(a, b)
        a = a[a!=b]

    #this makes array a a derangement    
    ind = np.argsort(a)

    #there is no need to do this because I think
    #one can just argue a one-to-one correspondence
    #between the two forms
    #for j in range(0, len(a)):
    #    a[ind[j]] = j

    #so just do a=ind
    a = ind
    
    #convert derangement to a number
    if len(a)==der_len:
        total = total + 1
        v = np.sum(a*(der_len**p))
        h.append(v)
        
h = np.array(h)
h = np.sort(h)

print("total:", total)

q = []
count = 1
i = 1
while i<len(h):
    while i<len(h) and h[i]==h[i-1]:
        count = count + 1
        i = i + 1
    print(count/len(h), count, "derangement:", h[i-1])
    q.append(count/len(h))
    count = 1
    i = i + 1
    
         
plt.plot(q)
plt.show()
