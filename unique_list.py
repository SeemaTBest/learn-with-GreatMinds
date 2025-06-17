def unique_list(input_list):
    unique_list_test = list(set(input_list))
    print("Original list:", input_list)
    print("Unique list:", unique_list_test)

# Call the function with a list
my_list = [1, 2, 4, 5, 6, 7, 8, 8, 9]
unique_list(my_list)