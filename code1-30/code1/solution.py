class Solution():

    def two_sum_list(self, nums, target):
        # list的长度
        length = len(nums)

        # 如果list的长度为0或者1，很明显不符合题意
        if length <= 1:
            return 'data error, array is too short'

        i = 0
        while i < length:
            # 目标值 = 和值 - 工具人
            result = target - nums[i]

            # 根据工具人位置的不同，切片，得到新的list
            nums_other = nums[i+1:]

            # 判断目标值是否在新的切片list中
            # yes，返回工具人和目标值index的list
            # no，进入下一次循环
            if result in nums_other:
                return [i, nums_other.index(result) + i + 1]
            i += 1

    def two_sum_hash(self, nums, target):
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i + 1
            else:
                return map[nums[i]], i + 1

        return -1, -1

    def two_sum_enum(self, nums, target):
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return d[target-num], i
            d[num] = i
