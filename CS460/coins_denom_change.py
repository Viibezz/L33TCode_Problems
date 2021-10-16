#Input: (list of integers (denom), integer (value)) 
#Output: Return True if possible to get value using input list else return False
def denom_change(given_coins, given_value):
    #make table coins[]
    coins = []
    #cols decided by given value
    #rows = 0 + each given coin denomination
    c_cols = len(given_coins) + 1

    #initialize table with False elements
    temp_coins = []
    for i in range(c_cols):
        for j in range(given_value + 1):
            temp_coins.append(False)
        coins.append(temp_coins)
        temp_coins = []
    
    #When given value is 0, there's always change so column is True 
    for i in range(c_cols):
        coins[i][0] = True

    #Set elements to True if coin change is possible, set False otherwise
    for i in range(1, c_cols):
        for j in range(1, (given_value + 1) ):
            #the coin is not bigger
            if given_coins[i - 1] <= j:
                #True when there's a set of coin change denominations that add up or
                #True when there's change reached regardless of counting more coins
                coins[i][j] = coins[i-1][j - given_coins[i-1]] or coins[i-1][j]
            else:
                #False when there's no change
                coins[i][j] = coins[i-1][j]

    #Return solution, table element at that position
    return coins[len(given_coins)][given_value]

print("[5, 10], 12 --> " ,denom_change([5, 10], 12))
print("[5, 10], 0  --> " ,denom_change([5, 10], 0))
print("[5, 10], 5  --> " ,denom_change([5, 10], 5))
print("[5, 10], 15 --> " ,denom_change([5, 10], 15))


