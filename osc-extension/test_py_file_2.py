"""
This module is part of a unit test suite designed to test the tooling "build_space_graph". 
It explores the potential relationships between different components of Python source code, 
specifically focusing on function calls and class instantiations.
"""
import test_py_file_1
from test_py_file_1 import test_func_1


# pylint: disable=W0613
def test_func_2(test_arg_2: int) -> None:
    """
    A test function that demonstrates the usage of another function from a different module.

    Args:
        test_arg_2 (int): An integer argument to be passed to the 'test_func_1' function.
    """
    arg_1 = 7
    test_func_1(arg_1)


# Creating an instance of TestClass2 from the imported module
test_class = test_py_file_1.TestClass2()
# Calling a method of the instantiated class
test_class.func1()

# Passing an argument to the test function
# pylint: disable=C0103
arg_2 = 6
test_func_2(arg_2)
