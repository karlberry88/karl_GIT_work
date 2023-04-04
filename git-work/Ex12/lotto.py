# lotto numbers 1
import random

randomlist = []

for a in range(0, 6):
    numbers = random.randint(1, 50)
# while loop
    randomlist.append(numbers)

randomlist2 = sorted(randomlist, key=int)
print("# 1 ", randomlist)

print(" And The Winning Lotto Numbers Are:", randomlist2)


# lotto numbers 2
print("--"*100)

nums = random.sample(range(1, 50), 6)
nums2 = sorted(nums, key=int)
print("#2  And The Winning Lotto Numbers Are:", nums2)

# lotto style readout

print("--" *100)
print("1st ball is:", nums[0])
print("2nd ball is:", nums[1])
print("3rd ball is:", nums[2])
print("4th ball is:", nums[3])
print("5th ball is:", nums[4])
print("6th and final ball is:", nums[5])


print('Tonights Winning Lotto Numbers Are ', nums2)
print("P.S YOU STILL HAVE TO GO TO WORK TOMORROW")
print("-" *100)