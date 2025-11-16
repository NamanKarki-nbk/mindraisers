#Set is the unordered collection of unique items which are mutable

a = {1, "naman", '3.5', 4.5}
print(a)
# ans => {1, 4.5, '3.5', 'naman'}

#add le set ma item add garincha
b = a.add("karki")
print(b)
# ans => None because inplace modification huncha

a.add("karki")
print(a)
# ans => {1, 4.5, '3.5', 'naman', 'karki'}

a.remove('3.5') #yo ni inplace huncha
print(a)
#ans => {1, 4.5, 'naman', 'karki'}

#there are other methods like :
# a.clear() #empties the set
# a.pop() #removes and returns an arbitrary element from the set
# a.union() #returns the union of two sets
# a.intersection() #returns the intersection of two sets
# a.difference() #returns the difference of two sets
# a.symmetric_difference() #returns the symmetric difference of two sets
# a.update() #updates the set with the union of itself and others
# a.copy() #returns a shallow copy of the set
# a.issubset() #returns True if the set is a subset of another set

#Dictionary is the  collection of key-value pairs which are mutable
d = {"name": "Naman", "age": 20, "city": "Kathmandu"}
print(d)
#ans => {'name': 'Naman', 'age': 20, 'city': 'Kathmandu'}

#accessing the value using key
print(d["name"])
#ans => Naman

#adding a new key-value pair
d["country"] = "Nepal"
print(d)
#ans => {'name': 'Naman', 'age': 20, 'city': 'Kathmandu', 'country': 'Nepal'}

#updating the value of an existing key
d["age"] = 21
print(d)
#ans => {'name': 'Naman', 'age': 21, 'city': 'Kathmandu', 'country': 'Nepal'}

#removing a key-value pair
d.pop("city")
print(d)
#ans => {'name': 'Naman', 'age': 21, 'country': 'Nepal'}

d.popitem() #removes and returns an arbitrary key-value pair
print(d)
#ans => {'name': 'Naman', 'age': 21}

print(d.get("city")) #returns the value for the given key
#ans => None because city key is not present

#other methods like:
# d.clear() #empties the dictionary
# d.keys() #returns a view object of all the keys in the dictionary
# d.values() #returns a view object of all the values in the dictionary
# d.items() #returns a view object of all the key-value pairs in the dictionary
# d.update() #updates the dictionary with the key-value pairs from another dictionary
# d.copy() #returns a shallow copy of the dictionary
