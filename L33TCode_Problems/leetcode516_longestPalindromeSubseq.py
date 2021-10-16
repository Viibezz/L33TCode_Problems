#Solution1
#recursion memo
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         def F(i,j):
#             print(i,j)

#             if i == j:
#                 return 1
#             elif i > j:
#                 return 0
#             elif i < j:
#                 #case 1: the LPS uses both s[i] and s[j] so add 2
#                 if s[i] == s[j]:
#                     return 2 + F(i + 1,j - 1)
#                 #case 2 & 3: length is either one based on max
#                 else:
#                     return max( F(i + 1, j), F(i, j - 1) )
#         return F(0, len(s) - 1)


#Solution2
#dynamic programming
class Solution:
    def longestPalindromeSubseq(self, s):
        #make zeros table 
        table = [ [0]*len(s) for i in range(len(s)) ]

        #diagonal 1 in the table for as single char is palindrome
        for i in range(len(s)):
            table[i][i] = 1

        #check last two
        #if they match add 2 to table
        #else go back 2 characters and check if they match
        #if they match add 2 to table
        #else check i with outer j character and repeat
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                #case 1: the LPS uses both s[i] and s[j] so add 2
                if s[i] == s[j]:
                    table[i][j] = 2 + table[i + 1][j - 1] 
                #case 2 & 3: length is either one based on max
                #check for outer characters
                else:
                    table[i][j] = max(table[i + 1][j], table[i][j - 1])

        #return solution which will be total length at the end of the table
        return table[0][-1]

print(Solution.longestPalindromeSubseq("me", "abfed"))
