import argparse

parser = argparse.ArgumentParser(description="Synthetic staging smoke greeting CLI")
parser.add_argument("--name", required=True, help="Name to greet")
args = parser.parse_args()
print(f"Hello, {args.name}!")
