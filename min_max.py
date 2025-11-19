import sys

if len(sys.argv) == 3:
    file_name = sys.argv[0]
    a = int(sys.argv[1])
    b = int(sys.argv[2])


if a > b:
    print(f"Max value is {a}")
elif a < b:
    print(f"Max value is {b}")
elif a == b:
    print("Both values are equal")
else:
    print("Invalid Input")
