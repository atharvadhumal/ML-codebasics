import numpy as np

q1 = np.array([
    [200, 220, 150],
    [150, 180, 210],
    [300, 340, 290]
])

q2 = np.array([
    [210, 250, 170], #Product 1
    [180, 120, 260], #Product 2
    [320, 310, 280]  #Product 3
])

print(q1 + q2) #adds up

print(q2-q1) #subtracts up

print((q2-q1)*100/q1) #percentage increase over q1 to q2

#house prediction example
features = np.array([
    [2000, 3], #house 1
    [1800, 3]  #house 2
])

weights = np.array([150, 50000])

print(np.dot(features, weights))

#cross product
c = np.array([1, 2, 3])
d = np.array([4, 5, 6])
print(np.cross(c, d))