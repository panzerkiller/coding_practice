import sys
class Solution:
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls)
	
	def __init__(self, str1, str2):
		self.str1 = str1
		self.str2 = str2

	def valid_anagram(self):
		if len(self.str1) != len(self.str2):
			return False
		sort1 = sorted(self.str1)
		sort2 = sorted(self.str2)
		for i in range(0, len(self.str1)):
			if sort1[i] != sort2[i]:
				return False
		return True
def main():
	if len(sys.argv) < 2:
		print("run python lc242_valid_anagram.py word1 word2")
	ob = Solution(sys.argv[1], sys.argv[2])
	print(ob.valid_anagram())
if __name__ == "__main__":
	main()
