def solution(nums):

    poketmon = len(nums) // 2
    types = len(set(nums))
    
    return min(poketmon, types)