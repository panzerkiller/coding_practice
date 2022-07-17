class Solution:
	def __new__(cls, *args,**kwargs):
		return super().__new__(cls)
	
	def __init__(self, strs):
		self.strs = strs

	def groupAnagrams(self):
		hashmap = {}
		for s in self.strs:
			ss = str(sorted(s))
			hashmap.setdefault(ss, [])
			hashmap[ss].append(s)
		return hashmap.values()

if __name__ == "__main__":
	strs = ["eat","tea","tan","ate","nat","bat"]
	ob = Solution(strs)
	print(ob.groupAnagrams())
