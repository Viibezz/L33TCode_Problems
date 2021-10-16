# import numpy as np
# def LongestCommonSubsequence(X,Y):
#     m = len(X)
#     n = len(Y)
#     M = np.array([[None for x in range(n+1)] for x in range(m+1)])

#     for i in range(m+1):
#         for j in range(n+1):
#             if(i == 0 or 0 == j):
#                 M[i,j] = 0
#             elif(X[i-1] == Y[j-1]):
#                 M[i,j] = 1 + M[i-1, j-1]
#             else:
#                 M[i,j] = max(M[i, j-1], M[i-1, j])
#            #print "(i, j) = ({},{}) X[i-1], Y[j-1] = {}, {}\n{}".format(i,j, X[i-1], Y[j-1], M)
                
#     #print M
#     return M[m,n]    

#Input: 2 strings
#Output: return Longest Common Subsequence
def LCS(A, B):
    #make zeros table[]
    table = []
    temp_table = []
    # 0 + length of first string
    for i in range(len(A) + 1):
        # 0 + length of second string
        for j in range(len(B) + 1):
            temp_table.append(0)
        table.append(temp_table)
        temp_table = []

    #fill table per case
    for i in range(len(A) + 1):
        for j in range(len(B) + 1):
            #LCS is empty then 0
            if(i == 0 or j == 0):
                table[i][j] = 0
            #case when characters are same add one
            elif(A[i - 1] == B[j - 1]):
                table[i][j] = table[i - 1][j - 1] + 1
            #case the strings are not equal lengths then
            #check the longer string for common subsequence
            else:
                table[i][j] = max(table[i][j - 1], table[i - 1][j])

    #Returns solution which is last element at table position
    return table[len(A)][len(B)]


print(LCS("aaRxAxCxE", "bbRyAyCxE"))
print(LCS("AxBxC", "AyB"))
print(LCS("AxBxC", ""))