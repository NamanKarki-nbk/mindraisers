# #positional arguments
# def positional_args(*args):
#     print(f"Args: {args}")
# positional_args("hello", "1",2,3,4,5)

# #keyword arguments
# def keyword_arg(**kwargs):
#     print(f"Kwargs: {kwargs}") 
# keyword_arg(a="Happy", b="maybe", c="oneday")

# #lambda function
# a=lambda x: x**3
# result = a(5)
# print(result)

# #map function
# dict1 ={
#     'num':2,
#     'num2': 4,
#     'num3': 7
    
# }

# gg = map(lambda value: value**3, dict1.values())
# print(gg)
# print(list(gg)) ##type cast nagari print garyo vane object return garcha

# bb =map(lambda val: (val[0], val[1]**3),dict1.items())
# print(dict(bb))


# #filter
# ff = filter(lambda value:  value[1]%2!=0, dict1.items())
# print(dict(ff))

# #reduce 
# from functools import reduce

# list1 = [1,2,3,4,5]
# kk = reduce(lambda x,y: x+y, list1)
# print(kk)

# #zip
# list2 = ["naman", "hello",7,8,9]
# print(list(zip(list1,list2)))

# #slicing
# print(list1[::-1])


#task
#map
result=[]
list1 = [1,2,3,4,5]
for i in list1:
    result.append(i+5)
print(result)


#filter
result1=[]
list2 = [2,4,5,6,9]
for i in list2:
    if i % 2 != 0:
        result1.append(i)
print(result1)


#reduce
result2=0
for i in list2:
    result2 += i
print(result2)

#zip
name = ["naman", "dipan", "suhan", "puuq"]
age =[23,22,22,24]
result3 = []

for i in range(len(name)):
    result3.append((name[i], age[i]))
    
result3 = result3
print(result3)