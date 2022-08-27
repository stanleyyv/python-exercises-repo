# Goal: print out this:
# XXXXX
# XX
# XXXXX
# XX
# XX

# Single loop with string multiplier
nums = [5,2,5,2,2]
for x in nums:
    print (x*"X")

# Nested loop
nums = [5,2,5,2,2]
for num in nums:
    for x in range(num):
        print("x", end="")
    print("")
