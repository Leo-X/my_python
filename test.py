# import math
# import random
# import math
# import builtins


def main():
    a = 10

    def test():
        nonlocal a
        a = a + 1
        print(a)
    test()
    print(a)


main()
