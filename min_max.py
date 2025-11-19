import sys
import os

# Try command-line arguments first
if len(sys.argv) == 3:
    file_name = sys.argv[0]
    a = int(sys.argv[1])
    b = int(sys.argv[2])
# If no CLI arguments, try Jenkins environment variables
elif "A" in os.environ and "B" in os.environ:
    a = int(os.environ["A"])
    b = int(os.environ["B"])
    print("Values taken from Jenkins environment variables")
# Otherwise, use defaults
else:
    a = 10
    b = 20
    print("Default values taken")

# Comparison
if a > b:
    print(f"Max value is {a}")
elif a < b:
    print(f"Max value is {b}")
elif a == b:
    print("Both values are equal")
else:
    print("Invalid Input")
