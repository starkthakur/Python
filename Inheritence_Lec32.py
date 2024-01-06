class Parent():

    def print_last_name(self):
        print("Thakur")

class Child(Parent):

    def print_first_name(self):
        print("Ashish")

    def print_last_name(self):
        print("Rockstar")


bucky = Child()
bucky.print_first_name()
bucky.print_last_name()

