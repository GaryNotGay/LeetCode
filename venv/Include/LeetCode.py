# @Author     :  lijishi
# @Contact    :  lijishi@buaa.edu.cn
# @Software   :  Pycharm & Python 3.7
# @Description:  LeetCode CN

class Solution:
    # 2021-02-07 https://leetcode-cn.com/problems/non-decreasing-array/
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        stack = [nums[-1]]
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if (nums[i] <= stack[-1]):
                stack.append(nums[i])
            else:
                stack.append(stack[-1])
                count += 1
        count2 = 0
        stack = [nums[0]]
        for i in range(1, n):
            if (nums[i] >= stack[-1]):
                stack.append(nums[i])
            else:
                stack.append(stack[-1])
                count2 += 1
        return min(count, count2) <= 1
