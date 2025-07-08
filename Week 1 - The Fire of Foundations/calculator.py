import argparse
import sys
from colorama import Fore, Style,init

init(autoreset=True)

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


def parse_args():
    parser = argparse.ArgumentParser(description="Calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("y", type=float, help="Second number")
    parser.epilog = "Example usage: python calculator.py add 5 3"
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        match args.operation:
            case "add":
                result = add(args.x, args.y)
            case "subtract":
                result = subtract(args.x, args.y)
            case "multiply":
                result = multiply(args.x, args.y)
            case "divide":
                result = divide(args.x, args.y)
            case _:
                raise ValueError("Unknown Operation")

        print(Fore.GREEN + Style.BRIGHT + f"Result: {result}")

    except Exception as e:
        print(Fore.RED + Style.DIM + f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
