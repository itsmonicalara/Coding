def main():
	n = int(input())
	arr = list(map(int, input().rstrip().split()))
	my_list = reversed(arr)
	print(*my_list)

if __name__ == '__main__':
	main()
