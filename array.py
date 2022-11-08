import numpy as np

#1 Print each item of the array individually
array = np.array([1, 2, 3, 4])

def printItems(array):
    for i in array:
        print(i)
print('1.')
printItems(array)

#2 Caclulate the sum of all items in the array without using a loop
def sumItems(array):
    return np.sum(array)
print('2.')
sumItems(array)

#3 Multiply each item in the array by 3 without using a loop
def multiplyItems(array):
    return array * 3
print('3.')
multiplyItems(array)