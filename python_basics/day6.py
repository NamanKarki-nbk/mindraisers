#positional arguments
def positional_args(*args):
    print(f"Args: {args}")
positional_args("hello", "1",2,3,4,5)

#keyword arguments
def keyword_arg(**kwargs):
    print(f"Kwargs: {kwargs}") 
keyword_arg(a="Happy", b="maybe", c="oneday")

#lambda function
a=lambda x: x**3
result = a(5)
print(result)

#map function
dict1 ={
    'num':2,
    'num2': 4,
    'num3': 7
    
}

gg = map(lambda value: value**3, dict1.values())
print(gg)
print(list(gg))

bb =map(lambda val: (val[0], val[1]**3),dict1.items())
print(dict(bb))


#filter
ff = filter(lambda value:  value[1]%2!=0, dict1.items())
print(dict(ff))