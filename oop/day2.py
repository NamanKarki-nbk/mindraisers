# class Parent:
#     def view(self):
#         print("Hello i am parent")
        

# class Child(Parent):
#     def view(self):
#         print("Hello i am  child")
#         super().view()
        


# obj1 = Child()
# obj1.view()

# #MRO=> METHOD RESOLUTION ORDER
# #multiple inheritance support garcha
# #using mro() method

# print(Child.mro())

# #checking manually

# # child + [Parent2, Parent1]
# #MRO(Child) = [Child] + merge(MRO(Parent1), MRO(Parent2), [Parent1, Parent2])
# #this is called C3 lineralization algorithm


#multilevel
# class ABC:
#     name ="ABC"
    
# class DEF:
#     name = "DEF"
    
# class GrandParent():
#     name = "GrandParent"
#     def GrandParent(self):
#         print("Grandparent")
        
# class Parent(GrandParent,ABC):
#     name = "Parent"
#     def Parent(self):
#         print("parent")
        

# class Child(Parent,GrandParent):
#     name = "Child"
#     def Child(self):
#         print("Child")
        
# #parent ra child eutai class bata inherit garna paudaina

# c1 = Child()
# print(c1.name)



#super()=> mro order follow garers class lai call garcha ani fallback huncha jun class le call garya tesmai