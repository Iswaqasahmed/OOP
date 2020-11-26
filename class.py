# simply clas:
#     statement 1
#      ...
#      ...
#      statement 2 


class simple:
    name = 'simple'
    def information(self):
        return 'information method'


x = simple()    # the class object is a parameterless function that returns a new instance of the class. 
print(x.name)     # attributes of class
print(x.information())     # attributes of class
print(simple().information())


class with_constructor:
    def __init__(self,firstName,lastName):    # __init__ bascially contructor 
        self.first = firstName;
        self.last = lastName;


names = with_constructor('waqas','ahmed')
print(names.first,names.last)
    

