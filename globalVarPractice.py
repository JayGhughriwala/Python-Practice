print("This is a practice of the global variable ")
val = 123
def func():
    global val
    val = 200
    print(val)
func()