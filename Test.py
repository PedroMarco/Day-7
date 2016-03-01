__author__ = 'acpb859'
class A:
    def __init__(self, i = 4):
        self.i = i
class B(A):
    def __init__(self, j = 7):
        super().__init__() ## special method to access the method of the parent class
        self.j = j

def main():
    b = B(6)
    print(b.i)
    print(b.j)
main()