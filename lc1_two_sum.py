class Solution:
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super().__new__(cls)   

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def twoSum(self):
        hmap= {}
        # nums = self.nums
        for i in range(0, len(self.nums)):
            diff = self.target - self.nums[i]
            if diff in hmap:
                return hmap[diff], i
            else:
                hmap[self.nums[i]] = i
    def qc(self):
        print(self.nums)
        print(self.target)

def main():
    nums = [2,7,11,15]
    target = 9
    ob = Solution(nums, target)
    print(ob.twoSum())
    ob.qc()

if __name__ == "__main__":
    main()
