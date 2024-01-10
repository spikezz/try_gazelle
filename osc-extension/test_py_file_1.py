"""
This module is part of the unit test suite for testing the tool "build_space_graph". It explores
the potential relationships among Python source code components, focusing on classes and functions.
"""


class TestClass1:
    """Provides a basic test class with nested classes and functions for unit testing purposes."""

    # pylint: disable=R0903
    class TestclassInClass1:
        """A nested class within TestClass1 to test nested class behavior."""
        def __init__(self):
            """Initializes an instance of TestclassInClass1."""
            # pylint: disable=W0107
            pass

    def __init__(self):
        """Initializes an instance of TestClass1 and calls an internal function."""
        self.func1()

        # pylint: disable=W0612
        def func_in_init(arg_intern: int) -> None:
            """
            An internal function defined within the __init__ method of TestClass1.

            Args:
                arg_intern (int): An integer argument for demonstration purposes.
            """
            # pylint: disable=W0104
            arg_intern

    def func1(self) -> None:
        """A method of TestClass1 that defines a nested class."""

        # pylint: disable=W0612
        class TestclassInFunc1:
            """A nested class within the func1 method of TestClass1."""
            def __init__(self) -> None:
                """Initializes an instance of TestclassInFunc1."""
                # pylint: disable=W0107
                pass


class TestClass2(TestClass1):
    """
    A subclass of TestClass1 to test inheritance and the behavior of super() function.

    Inherits:
        TestClass1: The parent class from which it inherits.
    """
    def test_func_super(self) -> None:
        """
        A method to test the functionality of super() in the context of TestClass1's inheritance.
        """
        arg_test_class_1 = 0
        super().__init__()
        # pylint: disable=E1101
        self.func_in_init(arg_test_class_1)


# pylint: disable=W0613
def test_func_1(test_arg_1: int) -> None:
    """
    A standalone function for unit testing purposes.

    Args:
        test_arg_1 (int): An integer argument for demonstration purposes.
    """
    # pylint: disable=W0107
    pass
