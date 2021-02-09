# @Author     :  lijishi
# @Contact    :  lijishi@buaa.edu.cn
# @Software   :  Pycharm & Python 3.7
# @Description:  LeetCode CN

class Solution:
    # 2021-02-07 https://leetcode-cn.com/problems/non-decreasing-array/
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                if i + 1 < len(nums) and i - 2 >= 0:
                    if nums[i + 1] < nums[i - 1] and nums[i - 2] > nums[i]:
                        return False
            if count > 1:
                return False
        return True

    # 2021-02-08 https://leetcode-cn.com/problems/longest-turbulent-subarray/
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n
        if n == 2:
            if arr[0] == arr[1]:
                return 1
            return n
        count, r = 0, 0
        if arr[0] == arr[1]:
            count = 1
        else:
            count = 2
        for i in range(2, n):
            if arr[i - 2] > arr[i - 1] < arr[i] or arr[i - 2] < arr[i - 1] > arr[i]:
                count += 1
            else:
                if arr[i - 1] == arr[i]:
                    count = 1
                else:
                    count = 2
            r = max(count, r)
        return r

    # 2021-02-09 https://leetcode-cn.com/problems/subarrays-with-k-different-integers/
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def atMostKDistinct(K):
            n = len(A)
            freq = [0] * (n + 1)
            ans, count = 0, 0
            left = right = 0
            while right < n:
                if freq[A[right]] == 0:
                    count += 1
                freq[A[right]] += 1
                right += 1
                while count > K:
                    freq[A[left]] -= 1
                    if freq[A[left]] == 0:
                        count -= 1
                    left += 1
                ans += right - left
            return ans
        return atMostKDistinct(K) - atMostKDistinct(K - 1)