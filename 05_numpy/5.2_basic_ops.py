import numpy as np
rev_q1 = np.array([10, 9 , 12])
rev_q1.ndim

rev = np.array([[10, 12, 9], [15, 11, 13]])
rev.ndim
print(rev.ndim)

print(rev)
#if i want to access the 0th index of second array i will do
rev[1,0] #here 1 means the index 1 array which is [15, 11, 13] and 0 means the 0th index of the array which is the 15

#if you want to change it 
rev[1, 0] = 14 #this is change the 15 to 14

rev.min() #gives minimum revenue
rev.max() #gives maximum revenue

rev.sum(axis=1)
#adds up the q1 revenue which is 12, 10, 9 = 31 and also q2 revenue and displays it