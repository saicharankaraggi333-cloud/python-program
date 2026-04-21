class A:
    def display_A(self):
        print("from class-A")
class B(A):
    def display_B(self):
        print("from class-B")
class C(A):
    def display_C(self):
        print("from class-C")
s=B()
p=C()
s.display_A()
s.display_B()
p.display_C()