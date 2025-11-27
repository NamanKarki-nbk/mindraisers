class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        super().show()
        print("B")


class C(A):
    def show(self):
        super().show()
        print("C")


class D(B, C):
    def show(self):
        super().show()
        print("D")


class E(D):
    def show(self):
        super().show()
        print("E")


e = E()
e.show()
print(E.mro())


#calculating mro manually
#algorithm = > MRO(X) = [X] + merge(MRO(paren1), MRO(parent2), ..., [parent1, parent2])

#MRO(A) => [A]
#MRO(B)=> [B,A]
#MRO(C)=> [C,A]
#MRO(D)=> [D]+merge(MRO(B), MRO(C), [B,C])
#=> merge([B,A], [C,A], [B,C])
#=> D,B ([A], [C,A], [C])
#=> D,B,C([A], [A])
#=> D,B,C,A

#MRO(E) => [E,D]
#=> [E,D,B,C,A,Object]