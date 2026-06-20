"""Command line interface for calculator."""

import argparse

from app.calculator import add, subtract


def main() -> None:
    """Run calculator CLI."""
    parser = argparse.ArgumentParser(description="Simple calculator CLI")
    parser.add_argument("operation", choices=["add", "subtract"])
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.a, args.b)
    else:
        result = subtract(args.a, args.b)

    print(result)


if __name__ == "__main__":
    main()
