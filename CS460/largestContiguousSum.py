#finds largest contiguous sum, Input is array of ints A
#output is sum, followed by the largest sequence from A
def largestContiguousSum(A):
    #empty list
    if len(A) == 0:
        a = []
        return (0, a)
    else:
        largestSum = 0 #Sum to be returned and compared against
        maxAtEnd = 0 #current iteration max

        #indicies for returning
        startIndex = 0	
        tempStart = 0
        endIndex = 0

        #loops through all elements of the array
        for i in range(0, len(A)):

            #checks the max of current index, index + the previous max + or zero
            maxAtEnd = max( A[i]+maxAtEnd, 0)

            #if the maxatend is the new largest replace the old largest and update the indicies
            if maxAtEnd > largestSum:
                largestSum = maxAtEnd
                startIndex = tempStart
                endIndex = i

            #if the end is less than zero then the next will not need it and can update the new start index
            if maxAtEnd <= 0:
                maxAtEnd = 0
                tempStart = i+1

            B = A[startIndex:endIndex+1] #truncates the given array to the largest contiguous subsequence
	
        return(largestSum, B)

print(largestContiguousSum([]))
print(largestContiguousSum([1,2,3, -3]))
print(largestContiguousSum([5, 15,-30, 10, -5, 40, 10]))