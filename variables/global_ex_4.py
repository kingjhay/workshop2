x = "awesome"


def myfunc():
    global x
    # x = awesome
    print("Python is " + x)
    x = "fantastic"
    # x = fantastic


myfunc()
print("Python is " + x)

# Output: Python is awesome
# Output: Python is fantastic