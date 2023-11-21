# import salutations
from salutations import print_hi, print_hello_world, PI
import sys as system
import computations.mathematics

if __name__ == '__main__':
    # print(dir(salutations))
    print_hi('PyCharm')
    print_hello_world()
    print(PI)
    print(system.path)
    print(computations.mathematics.addition(3, 5))
    print(type(PI))
