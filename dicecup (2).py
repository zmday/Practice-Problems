# import system
import sys

# user input
d1, d2 = map(int, input().split())


# verify if the input matches constraints
if d1 <= 4 & d2 >= 20:
    sys.exit()
else:
    smallest = min(d1, d2)+1
    largest = max(d1, d2)+1
    print(*tuple(range(smallest, largest +1)), sep = "\n")
