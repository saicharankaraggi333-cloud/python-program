class A:
    def display_A(self):
        print("from class-A")
class B(A):
    def display_B(self):
        print("from class-B")
class C(A):
    def display_C(self):
        print("from class-C")
class D(B,C):
    def display_D(self):
        print("from class-D")
s=D()
s.display_A()
s.display_B()
s.display_C()
s.display_D()