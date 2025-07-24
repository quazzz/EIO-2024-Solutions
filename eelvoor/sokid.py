# this problem focuses on odd amount of socks in the socks array
# so for the solution, it would be better to count 
# the amount of odd socks, check whether is the amount is also odd or no
# and then return the amount // 2, because of pairs
from collections import Counter # using it to count odd socks
# inputs
n = int(input())
# first condition, if the amount of socks is odd, they cannot be redrawn
if n % 2 > 0:
    print(-1)
    exit()
socks = Counter([input() for _ in range(n)])

total = 0

# counting odd socks 
for _, count in socks.items():
    if count % 2 > 0:
        total += 1

if total % 2 > 0: # whether the amount of odd socks is odd -> we cant redraw them
    print(-1) 
else: # amount of odd socks is even, we can redraw them into pairs
    print(total // 2)  
    
