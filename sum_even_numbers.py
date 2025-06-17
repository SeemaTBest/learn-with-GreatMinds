def sum_even_numbers(number):
    total = 0

    for num in number:
        if num %2==0:
            total += num
    return total
    
num_list= [2,4,6,8,10]
print("sum of even numbers" , sum_even_numbers(num_list))



