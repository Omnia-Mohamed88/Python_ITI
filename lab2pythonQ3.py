import json
import math

numbers=[4,9,16,25,36]
sqrt_function = lambda x: math.sqrt(x)
sqr_of_numbers=list(map(sqrt_function,numbers))

result_dic = {}
for i in range(len(numbers)):
    result_dic[numbers[i]]=sqr_of_numbers[i]

with open('result.json','w') as json_file:
    json.dump(result_dic,json_file)

print("Dictionary:", result_dic)


