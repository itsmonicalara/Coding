'''Whats my base case? Having 0 chars in the list, return null
What is my other case? 
'''
class Solution(object):
    def reverseString(self, s):
    	words = input()
    	s.append(words)
    	if(len(s) == 0):
    		return ''
    	else: 
    		return s[-1] + self.reverseString(s[:-1])
    	

if __name__ == '__main__':
	ob = Solution()
	string_list = []
	ob.reverseString(string_list)
