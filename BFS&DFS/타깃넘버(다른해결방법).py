def solution(numbers, target):
    answer = dfs(numbers,target,0,0)
    return answer

def dfs(numbers, target, current_sum,depth):
    answer=0
    if depth == len(numbers):
        if current_sum==target:
            return 1
        else:
            return 0
    else:
        answer+=dfs(numbers,target,current_sum+numbers[depth],depth+1)
        answer+=dfs(numbers,target,current_sum-numbers[depth],depth+1)
        return answer