import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
# the number of line 1 is between 5 and 20, the smallest number is 5 and the largest number is 20.
# the number of line 2 is an odd number which between 3 and 10, the smallest number is 3 and the largest number is 9. line 2 had not produced a 4.
# the number of line 3 contains decimals, the smallest number is 2.5 and the largest number is 5.5.
print(random.randint(1,100))