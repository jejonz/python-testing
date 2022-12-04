from math import sqrt

def external_dependency():
    return False

def function_to_test():
    return external_dependency()

def function_to_test_using_math(value):
    return sqrt(value)