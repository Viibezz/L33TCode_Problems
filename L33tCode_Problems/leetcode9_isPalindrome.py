class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: int
        """
        given = x
        negative = False
        if (x < 0):
            negative = True
            x *= (-1)
            
        #x = 123 --> x = 321
        #get last number
        last_i = x % 10
        #assign to number
        y = last_i
        #remove last number
        x //= 10
        #get last number and append till end
        while (x > 0):
            last_i = x % 10
            y = (y * 10 + last_i)
            x //= 10
        # [-2^31, 2^31 -1]
        if ( (y > (2 ** 31) -1) ):
            return 0
        #negative case
        if negative == True:
            y *= (-1)

        if given == y and negative != True:
            return True
        else:
            return False

print(Solution.reverse("me",121))
