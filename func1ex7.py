def has_33(nums):
    for i in range(len(nums) - 1):
     if nums[i] == 3 and nums[i + 1] == 3:
      return True
    return False
num1=[1, 3, 2, 3]
num2=[1, 3, 3, 2]
print(has_33(num1))
print(has_33(num2))
