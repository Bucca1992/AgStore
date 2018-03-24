class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in nums]
        max_ans = 0
        for i in xrange(len(nums)):
            max_ans_of_i = 1
            for j in xrange(i):
                if nums[j] < nums[i]:
                    max_ans_of_i = max(max_ans_of_i, dp[j] + 1)
            dp[i] = max_ans_of_i
            max_ans = max(max_ans_of_i, max_ans)
        return max_ans
