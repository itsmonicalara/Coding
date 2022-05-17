# Theres a lot of forms to approach this. First we could sort the list and just get the 
# last number.
# Also compares each number with eachother.
# Use the max function on the list.

def largest_num(a_list):
    max_num = a_list[0]
   
    for ele in a_list:
        if ele > max_num :
             max_num = ele
      
    print(max_num)

if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    largest_num(numbers)