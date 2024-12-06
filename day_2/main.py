#    --- Advent Of Code 2024: day 2 ---
# part 1

ans = 0
#reads from input file and split unnecessary spaces
with open('./input.txt') as file:
    lines = file.read().strip().split('\n')

def is_safe(nums):
    inc = nums[1] > nums[0] # checks if it is increment
    if inc:
        for i in range(1, len(nums)):
            dif = nums[i] - nums[i-1] # find differences(dif)
            if not 1<=dif<=3:
                return False
        return True
    else: #reverse of code above because below code is for dsecrement order lists
        for i in range(1, len(nums)):
            dif = nums[i] - nums[i-1]
            if  not -3<=dif <=-1:
                return False
        return True
    
#part 2
def is_really_safe(nums):
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        if is_safe(nums[:i] + nums[i+1:]):
            return True
    return False

for line in lines:
    nums= [int(i) for i in line.split()]
    ans += is_really_safe(nums) # is_safe if part 1. is_really_safe() if part 2 needed

print(f'Safe numbers are {ans}')
