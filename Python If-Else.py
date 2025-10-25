import math
import os
import random
import re
import sys

    n = int(input().strip())

if n % 2 != 0:
    print("Weird")
if n in range(2, 5 + 1) and n % 2 == 0:
    print("Not Weird")
if n in range(6, 20 + 1 ) and n % 2 == 0:
    print("Weird")
if n % 2 == 0 and n > 20:
    print("Not Weird")
