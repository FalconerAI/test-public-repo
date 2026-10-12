import argparse

parser = argparse.ArgumentParser(description="Synthetic staging smoke greeting CLI")
parser.add_argument("--person", required=True, help="Person to greet")
args = parser.parse_args()
print(f"Hello, {args.person}!")
