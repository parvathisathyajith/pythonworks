class Grandparent:
    def m(self):
        print("Grand parent class m1 method")
class parent:
    def m(self):
        print("parent class m2 method")
class child(parent,Grandparent):
    def m3(self):
        print("child class m3 method")

child_instance=child()
child_instance.m3()
child_instance.m()              
