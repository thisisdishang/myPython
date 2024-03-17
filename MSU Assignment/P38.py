'''Create a class Demo and also create method test () in it. Overload test () in four ways. First version takes no parameter,
the second takes one integer parameter, and the third takes two integer parameters and fourth takes one double parameter.'''

class Demo:
    def test(self, num1=None, num2=None, num3=None):
        if num3 is not None:
            print("test() method with one double parameter:", num1)
        elif num2 is not None:
            print("test() method with two integer parameters:", num1, num2)
        elif num1 is not None:
            print("test() method with one integer parameter:", num1)
        else:
            print("test() method with no parameters")

# Test the Demo class and its overloaded test() method
demo = Demo()

# Calling test() method with no parameters
demo.test()

# Calling test() method with one integer parameter
demo.test(10)

# Calling test() method with two integer parameters
demo.test(20, 30)

# Calling test() method with one double parameter
demo.test(3.14)
