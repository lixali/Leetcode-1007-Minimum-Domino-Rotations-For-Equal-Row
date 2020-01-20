'''
Question Leetcode 1007:  Minimum Domino Rotations For Equal Row
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.
''' 

'''
Time space analysis: it is going to be linear time and space; 

'''

'''
Logic: Go through A and B starting from A[0] and B[0]; create a hash table for A and B to record "values-number" pair; and at the same time, record if A[i] and B[i] is the same (because if they are the same; it doesn't need to be swapped;)
'''


from collections import defaultdict

class solution(object):
    
    def __init__(self):     ### the below hash tables are used throughout all functions, therefore use "self." to make them global
        self.values_in_A = defaultdict(int) ### defaultdict will make defauclt value in hash table to be 0 (for all keys)
        self.values_in_B = defaultdict(int)
        self.same_value = defaultdict(int)

    def check_domino_number (self, A, B):

        size_A = len(A) ### size_A equals size_B
        for i in range (size_A):   ### for loop to go through all values in two input lists ("A" and "B"), and then make count; linear time
            self.values_in_A[A[i]] += 1  ### the hash table size depends to how many unique values in two lists "A" and "B"; the worst case is also linear space
            self.values_in_B[B[i]] += 1
            
            if A[i] is B[i]:
                self.same_value[A[i]] += 1
            
        #for key in self.values_in_A:    ### this print is for debugging purpose to check what is in value 
            #print(self.values_in_A[key])
        ### this function doesn't return anything, values are passed to next function using "self."
            
    def min_domino_rotation (self, A, B):
        self.check_domino_number(A, B)     ### call the above function
        size_A = len(A) ### size_A equals size_B
        min_rotation = size_A
        for key in self.values_in_A:
            if self.values_in_A[key] + self.values_in_B[key] - self.same_value[key] is size_A:
                min_rotation = min(min_rotation, min(self.values_in_A[key], self.values_in_B[key]) - self.same_value[key])
                
        for key in self.values_in_B:
            if self.values_in_A[key] + self.values_in_B[key] - self.same_value[key] is size_A:
                min_rotation = min(min_rotation, min(self.values_in_A[key], self.values_in_B[key]) - self.same_value[key])
                
        if min_rotation is not size_A:
            return min_rotation
        else:
            return -1
        
class_1 = solution()
A = [2,2,3,2,2,6]
B = [1,2,2,2,2,2]
class_1.min_domino_rotation (A, B)

