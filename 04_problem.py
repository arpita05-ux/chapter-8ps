'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3

sum(n) = 1 + 2 + 3 + 4 + 5.....n-1 + n
sum(n) = (n-1) + n

 '''




def sum(n):
    if(n==1):     #base case - is used so that recursion doesn't go infintly . or This stops the recursion.
        return 1
    return sum(n-1) + n   #recursive case

print(sum(4))
