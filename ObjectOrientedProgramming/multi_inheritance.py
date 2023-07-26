'''multi_inheritance.py'''
print(" ")

class A:
    def __init__(self) -> None:
        print("A")

class B:
    def __init__(self) -> None:
        print("B")

class C(A, B):
    pass

class D(B, A):
    pass

class E(A, B):
    def __init__(self) -> None:
        super().__init__()

c = C()
print(isinstance(c, A))
print(isinstance(c, B))
d = D()
e = E()
print(" ")