def main():
	num = int(input())
	my_list = []
	for i in range(num):
		del my_list[:]
		string = input()
		for character in string:
			my_list.append(character)	
		sliced1 = my_list[0::2]
		str1 = ''.join(str(x) for x in sliced1)
		sliced2 = my_list[1::2]
		str2 = ''.join(str(x) for x in sliced2)
		print(str1 + " " + str2)

if __name__ == '__main__':
	main()