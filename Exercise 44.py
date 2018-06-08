class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEOFRE PARENT altered()")
        # calls the parent function altered()
        # must supply the child class when calling super!
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

print("Implicit Inheritance:")
dad.implicit()
son.implicit()

print("\nOverride Inheritance:")
dad.override()
son.override()

print("\nAltering Inheritance:")
dad.altered()
son.altered()