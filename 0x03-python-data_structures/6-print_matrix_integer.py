#!/usr/bin/python

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print(matrix[i][j])
            else:
                print(matrix[i][j], end=' ')
