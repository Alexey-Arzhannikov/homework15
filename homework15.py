
def test_function():
    inner_function()


def inner_function():
    def other_f():
        print("Я в области видимости функции test_function")
    other_f()


test_function()
inner_function()
