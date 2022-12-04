
class ExternalMethodTest:
    def __init__(self):
        pass

    def method_to_test(self):
        return self.internal_method()

    def internal_method(self):
        return False

# Run class method test below
#test = ExternalMethodTest()
#print(test.method_to_test())