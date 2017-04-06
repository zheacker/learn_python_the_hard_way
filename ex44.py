## All about inheritance

# implicit inheritance
print "This is implicit inheritance\n"
# When you define a function in the parent class
# but not in the child class, the child gets shit from the parent

class Parent(object):
    """docstring for parent."""
    def implicit(self):
        print "this function, implicit(), lives in the Parent class"

class Child(Parent):
    """docstring for Child."""
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# override explicitly
print "\n\nThis explicitly overrides a parent's function\n"
# You might want the child class to behave differently than the parent
# You need to override the parent's function explicitly
# You do this by defining a function of the same name in both classes
# The child class's function will override the parent's

class Parent(object):
    """docstring for Parent."""
    def override(self):
        print "PARENT override() function"

class Child(object):
    """docstring for Child."""
    def override(self):
        print "CHILD override() function"

dad = Parent()
son = Child()

dad.override()
son.override()

# Alter before or after
print "\n\nThis is how you alter the parent's function, either before or after it runs\n"

# This is a special case of overriding; first you override
# Then you use the `super` function to get the parent's version
# of the function

class Parent(object):
    """docstring for Parent."""
    def altered(self):
        print "PARENT altered() function"

class Child(Parent):
    """docstring for Child."""
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()

# All 3 combined
print "\n\nThis demonstrates all 3 interaction types\n"

class Parent(object):
    """docstring for Parent."""
    def override(self):
        print "PARENT override() function"

    def implicit(self):
        print "PARENT implicit() function"

    def altered(self):
        print "PARENT altered() function"

class Child(Parent):
    """docstring for Child."""
    def override(self):
        print "CHILD override() function"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
