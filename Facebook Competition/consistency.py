# string S made of uppercase letters

vowels = ['A', 'E', 'I', 'O', 'U']

seconds = 0
def consistency(string):
	if vowels not in string:
		print('Theres not vowels in the word')
	else:
		print('Theres vowels in the word')

n = int(input("Number of elements:"))
lst = []

for i in range(0, n):
	ele = input()
	lst.append(ele)
print(lst)