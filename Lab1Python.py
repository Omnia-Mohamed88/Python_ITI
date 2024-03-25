#Q1
# user_input = input("Please Enter a Number: ")

# if user_input.isdigit() and 20 <= int(user_input) <= 50:
#     print(user_input + " is within the range of 20 and 50")
# else:
#     print("Invalid input or the output is outside the range")


##################################################################################

#Q2

# def calculate_area(length , width):
#     return length * width

# def calculate_perimeter(lenght,width):
#     return (2*(lenght+width))

# length = float(input("please enter the length of the rectangle "))
# width = float(input("please enter the width of the rectangle "))

# area_result = calculate_area(length,width)
# perimeter_result=calculate_perimeter(length,width)

# print("The area of the rectangle is " , area_result)
# print("The area of the rectangle is " , perimeter_result)


####################################################################################

#Q3

# def concate_string(str1, str2):
#     concate1 = str1 +" "+ str2
#     concate2 = f"{str1} {str2}"
#     return concate1 , concate2


# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# result1 = concate_string(string1, string2)

# print(f"Concatenation using f-string: {result1}")

#########################################################################################

#Q4
# def square_elements(input_list):
#     squared_list = []
#     for element in input_list:
#         squared_list.append(element ** 2)
#     return squared_list

# input_values = [1, 2, 3, 4, 5]
# result = square_elements(input_values)
# print(result)

##############################################################################################

#Q5
#methode 1
# def merge_dictionaries(dictionary1, dictionary2):
#     merged_dict = {}
    
#     for key, value in dictionary1.items():
#         merged_dict[key] = value
    
#     for key, value in dictionary2.items():
#         merged_dict[key] = value
    
#     return merged_dict

# dictionary1 = {'a': 1, 'b': 2}
# dictionary2 = {'c': 4, 'd': 3}

# result = merge_dictionaries(dictionary1, dictionary2)
# print(result)





#methode 2
# def merge_dictionaries (dictionary1 , dictionary2):
#     return ({**dictionary1,**dictionary2})

# dictionary1={'a':1 , 'b':2}
# dictionary2={'c':4 , 'd':3}

# print (merge_dictionaries(dictionary1,dictionary2))


##################################################################################################

#Q6

# def merge_lists(list1, list2):
#     return list1 + list2

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']

# result = merge_lists(list1, list2)

# print("Merged list:", result)

######################################################################################################

#Q7
#methode1
# def check_keys(dictionary, keys):
#     for key in keys:
#         if key not in dictionary:
#             return False
#     return True

# my_dict = {"name": "jone", "email": "jane@outlook.com", "age": 25, "job": "engineer", "address": "cairo, Egypt"}
# keys_to_check = ["job", "card_number"]

# result = check_keys(my_dict, keys_to_check)

# if result:
#     print("All keys exist")
# else:
#     print("Some keys are missing")




#methode2
# def check_keyes (dictionary,keys):
#     return all(key in dictionary for key in keys)
# my_dict = {"name": "jone", "email": "jane@outlook.com", "age": 25, "job": "engineer", "address": "cairo, Egypt"}

# keys = ["job", "card_number"]


# result = check_keyes(my_dict, keys)

# if result == True:
#     print("All keys exist")
# else:
#     print("Some keys are missing ")

####################################################################################################

#Q8
# result = 0

# for i in range(1, 101):
#     result += i

# print("Sum of numbers from 1 to 100:", result)

####################################################################################
#Q9
# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# input_number = 7
# result = check_even_odd(input_number)

# print(f"The number is {result}.")

########################################################################################################
#Q10


def reverse_string(input_string):
    reversed_str = ""
    index = len(input_string) - 1
    while index >= 0:
        reversed_str += input_string[index]
        index -= 1
    return reversed_str

input_str = "hello"
result = reverse_string(input_str)

print(f"The reversed string is '{result}'.")



###################################################################################

#Q11
# def palideron(input_str):
#     reversed_str = input_str[::-1]
#     return (input_str == reversed_str)

# result = palideron("heelo")
# print(result)

########################################################################################################
#Q12

# def remove_even_square_odd(list_number):
#     i=0
#     while(i<len(list_number)):
#         if(list_number[i]%2==0):
#             list_number.pop(i)
#         else:
#             list_number[i]=list_number[i]**2
#             i+=1

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# remove_even_square_odd(numbers)
# print(numbers)
            


#########################################################################################################
#Q13
# def is_prime(number):
#     if number <2:
#         return False
#     for i in range(2,number):
#         if number % i ==0:
#             return False
#     return True

# test_number = 17
# result = is_prime(test_number)
# print(f"{test_number} is prime: {result}")


##########################################################################################################
#Q14
# def factorial_number(number):
#     result = 1
#     for x in range(1, number + 1):
#         result *= x
#     return result
# number = 5
# factorial_result = factorial_number(number)
# print(f"The factorial of {number} is: {factorial_result}")


########################################################################################################
def perform_operations(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num

    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num

    squared_list = []
    for num in numbers:
        squared_list.append(num ** 2)

    return [total_sum, min_num, max_num, squared_list]

numbers = [1, 4, 7, 2, 9]
results = perform_operations(numbers)
print("Sum:", results[0])
print("Minimum:", results[1])
print("Maximum:", results[2])
print("Squared List:", results[3])







             

    
