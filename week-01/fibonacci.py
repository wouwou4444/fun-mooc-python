
import sys
print(sys.version_info)

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(dest="integer", type=int,
                    help="integer to give as an argument")
input_args = parser.parse_args()
number = input_args.integer


def fibonacci(n):
    if n <= 1:
        return(1)
    f2, f1 = 1, 1
    for i in range(2, n+1):
        f2, f1 = f1 + f2, f2
    return(f2)





output_message = f"** the number given is {number} and the square is {number**2}"


output_message2 = f"** the number given is {number} and the fibonacci value is {fibonacci(number)}"

print(output_message)
print(output_message2)