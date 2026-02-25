# 1's compliment = flip the bits 
# 2's compliment = 1's compliment + 1 

# swapping two numbers without using a temporary variable:
# a = a ^ b
# b = a ^ b
# a = a ^ b

# check if ith bit is set or not:
# if (n & (1 << i)) != 0:
    # print("ith bit is set")

# set the ith bit of a number:
# n = n | (1 << i)

# clear the ith bit of a number:
# n = n & ~(1 << i)

# toggle the ith bit of a number:
# n = n ^ (1 << i)

# remove the rightmost set bit of a number:
# n = n & (n - 1)

# check if a number is a power of 2:
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

# count the number of set bits in a number:
def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


