def main():
	my_dict = {}
	num = int(input())
	for i in range(num):
		key,value = input().split()
		my_dict[key] = value
	while True:
		try:
			name = input()
			if name in my_dict:
				print(name + "=" + my_dict[name])
			else:
				print("Not found")
		except:
			break

if __name__ == '__main__':
	main()

