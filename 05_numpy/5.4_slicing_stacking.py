import numpy as np

# a = np.array({6,7,8,9})
# a[0:2] #prints 6 and 7

# a[2:] #prints from index2 to remaing all

# a[-1] #prints 9

# b = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# b[1, 2] #prints 6 

# b[2, 0] #prints 7


#hstack
#customer ID name

# c = np.array([
#     [101, "abc"],
#     [102, "dce"],
#     [103, "xyz"]
# ])

# #Customer ID, purchase amount, purchase date

# d = np.array([
#     [101, 250.50, '2023-08-01'],
#     [102, 150.50, '2023-08-02'],
#     [103, 370.50, '2023-08-03']
# ])

# #hstack means horizontal stacking -->

# print(np.hstack((c, d)))

# e = np.array([
#     [104, "venkat"],
#     [105, "john"],
#     [106, "kathy"]
# ])

# #vstack means vertical stacking ^
# print(np.vstack((c, e)))

transactions = np.array([
    [101, "Mohan", 250.50, '2023-08-01'],
    [102, "Mohan", 150.50, '2023-08-01'],
    [103, "Mohan", 300.75, '2023-08-01'],
    [104, "Mohan", 200.01, '2023-08-01'],
    [105, "Mohan", 150.25, '2023-08-01'],
    [106, "Mohan", 250.50, '2023-08-01']
])

#hsplit: horizontally split
print(np.hsplit(transactions, [3])) #split from column 3 horizontally

#vertical split
print(np.vsplit(transactions, [4])) #the index 5 after 4th index will go in column other array seperate

monthly_sales = np.array([30, 33, 35, 28, 42])

results = monthly_sales < 32