def main():
	my_dict = {}
	num = int(input())
	for i in range(num):
		key,value = input().split()
		my_dict[key] = value
	for i in range(0, num):
		name = input()
		if name in my_dict:
			print(name + "=" + my_dict[name])
		else:
			print("Not found")

if __name__ == '__main__':
	main()