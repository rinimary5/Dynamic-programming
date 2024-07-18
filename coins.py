def minNoOfCoins(n,denoms):
    nums=[float('inf') for x in range(n+1)]
    nums[0]=0
    for denom in denoms:
        for amount in range(len(nums)):
            if denom<=amount:
                nums[amount]=min(nums[amount],1+nums[amount-denom])
    return nums[n] if nums[n]!=float('inf') else -1
n=int(input("Enter the amount"))
coin=list(map(int,input("Enter the coin denominations").split()))
print(minNoOfCoins(n,coin))
