# Namespace : 
# 1. Built-in Namespace.
# 2. Global Namespace.
# 3. Local Namespace.
# 4. Enclosed Namespace.

print(dir())

myNameSpace = 10
print(dir()) # its also show my myNameSpace 


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

a = 3
def variable():
    global a
    a = 4
    print(a)
print(a)
variable()
