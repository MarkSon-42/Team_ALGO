def solution(nums):

    nums.sort()    
    max_num = nums[-1] + nums[-2] + nums[-3]
    
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                result.append(nums[i] + nums[j] + nums[k])
        
    count = 0
    
    for item in result:     
        is_find = False
        for i in range(2, max_num):
            if item != i and item % i == 0:
                is_find = True
                break
        if is_find == False:
            count += 1
    
    answer = count
    return answer
