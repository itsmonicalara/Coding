def sort_numbers(arr):
    for i in range(0,len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return(arr)

def delete_repeated(arr):
    arr = list(dict.fromkeys(arr)) 
    return(arr)

def runner_up(n,arr):   
    sort_numbers(arr)
    delete_repeated(arr)    
    for i in range(0,len(arr)):
        if(i == len(arr) - 1):
            print(arr[i])



n = int(input())
arr = list(map(int, input().split())) 
runner_up(n,arr)
