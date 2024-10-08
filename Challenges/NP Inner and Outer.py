inner

The inner tool returns the inner product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.inner(A, B)     #Output : 4
outer

The outer tool returns the outer product of two arrays.

import numpy

A = numpy.array([0, 1])
B = numpy.array([3, 4])

print numpy.outer(A, B)     #Output : [[0 0]
                            #          [3 4]]
Task

You are given two arrays:  and .
Your task is to compute their inner and outer product.

Input Format

The first line contains the space separated elements of array .
The second line contains the space separated elements of array .

Output Format

First, print the inner product.
Second, print the outer product.

Sample Input

0 1
2 3
Sample Output

3
[[0 0]
 [2 3]]



import numpy


# Input the arrays
A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)

# Compute the inner product
inner_product = numpy.inner(A, B)
print(inner_product)

# Compute the outer product
outer_product = numpy.outer(A, B)
print(outer_product)
