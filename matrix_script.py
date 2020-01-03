
"""


Title: Matrix script

Description: Neo has a complex matrix script. The matrix script is a N X M grid 

of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

To decode the script, Neo needs to read each column and select only the 

alphanumeric characters and connect them. Neo reads the column from top to 

bottom and starts reading from the leftmost column.



If there are symbols or spaces between two alphanumeric characters of the 

decoded script, then Neo replaces them with a single space '' for better 

readability.



Neo feels that there is no need to use 'if' conditions for decoding.



Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

"""

import math
import os
import random
import re
import sys
import string



first_multiple_input = raw_input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

s=''

for _ in xrange(n):
	matrix_item = raw_input()
	matrix.append(matrix_item)

for i in range (m):
for j in range (n):
	s+=matrix[j][i]

print(re.sub(r'\b[^a-zA-Z0-9]+\b',' ',s))


