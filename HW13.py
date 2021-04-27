#Ben Moreau HW13

import numpy as np

print("input the number of draws per exp:")
N=int(input())
print("input the number of exp:")
Ne=int(input())
print("input the range of numbers you wish to draw from:")
print("lower limit:")
ranger = int(input())
print("upper limit:")
rangerr = int(input())
ress=[]
c_m =0
means=[]
print("A")
for m in range(Ne):
    ress=[]
    for i in range(N):
        ress.append(np.random.randint(ranger,rangerr+1))
        #print(max(ress),min(ress))
    c_m = sum(ress)/N
    means.append(c_m)

from matplotlib import pyplot as plt

plt.hist(means,density = True,label=(str(Ne)+" exps,"+str(N)+" draws"),alpha=.8,stacked=True)
means=[]
for m in range(Ne*10):
    ress=[]
    for i in range(N*10):
        ress.append(np.random.randint(ranger,rangerr+1))
        #print(max(ress),min(ress))
    c_m = sum(ress)/N/10
    means.append(c_m)

from matplotlib import pyplot as plt

plt.hist(means,density = True,label=(str(Ne*10)+" exps,"+str(N*10)+" draws"),alpha=.8,stacked=True)
means=[]
for m in range(int(Ne/10)):
    ress=[]
    for i in range(int(N/10)):
        ress.append(np.random.randint(ranger,rangerr+1))
        #print(max(ress),min(ress))
    c_m = sum(ress)/N*10
    means.append(c_m)

from matplotlib import pyplot as plt

plt.hist(means,density = True,label=(str(Ne/10)+" exps,"+str(N/10)+" draws"),alpha=.8,stacked=True)
    
'''   
x  = np.linspace(ranger,rangerr,1/N)
n_mean_max=0
for i in range(len(means)):
    if(means[i]==ranger/2+rangerr/2):
        n_mean_max+=1
y = n_mean_max/len(means)*np.exp((-(x-ranger/2+rangerr/2)**2)/2) #make a gaussian fit to the plot
plt.plot(x,y)
'''
plt.legend()
plt.xlabel("Mean of an experiment")
plt.ylabel("Non-normalized probabiltiy of getting this mean")
plt.show()
