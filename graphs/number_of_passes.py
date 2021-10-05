
""""
  Write a function that takes in an integer matrix of potentially unequal height
  and width and returns the minimum number of passes required to convert all
  negative integers in the matrix to positive integers.


  A negative integer in the matrix can only be converted to a positive integer
  if one or more of its adjacent elements is positive. An adjacent element is an
  element that is to the left, to the right, above, or below the current element
  in the matrix. Converting a negative to a positive simply involves multiplying
  it by -1

  zeros can't convert negatives to positives
"""

import copy


def minimumPassesOfMatrix(matrix):
    return _minimumPassesOfMatrix(matrix)


def _minimumPassesOfMatrix(matrix, oldMatrix=None, num_of_passes=0, to_convert=None):

    # create a deep copy of the matrix so we can't compare later if something has changed
    oldMatrix = copy.deepcopy(matrix)

    if to_convert is None:
        to_convert = set()

    positives_in_pass = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 0:
                positives_in_pass.add((row, col))
            if matrix[row][col] < 0:
                to_convert.add((row, col))

    hasPositives = len(positives_in_pass) > 0
    hasNegatives = len(to_convert) > 0

    # if the array has no negatives, we are done
    if not hasNegatives:
        return num_of_passes

    # for this function call, try to convert negatives around the positives number found
    for (row, col) in positives_in_pass:
        try_converting_neighbours(matrix, row, col, to_convert)
    # increase number of passes
    num_of_passes += 1

    # if the conversion, did not affect our matrix, we quit and return -1
    if matrix == oldMatrix:
        return -1

    # if there are still negatives and positives number in matrix, we need to do another pass
    # ( make a recursive call with updated values)
    if hasNegatives and hasPositives:
        return _minimumPassesOfMatrix(matrix, oldMatrix, num_of_passes, to_convert)

    return num_of_passes if hasPositives else -1


def try_converting_neighbours(matrix, row, col, to_convert):

    if matrix[row][col] <= 0:
        return

    # if the number is positve, call conversion on up,down,left,right
    convert(matrix, row + 1, col, to_convert)
    convert(matrix, row - 1, col, to_convert)
    convert(matrix, row, col + 1, to_convert)
    convert(matrix, row, col - 1, to_convert)


def convert(matrix, row, col, to_convert):

    row_inbounds = 0 <= row < len(matrix)
    col_inbounds = 0 <= col < len(matrix[0])

    if not row_inbounds or not col_inbounds:
        return

    # only try to make a number positive, if it is negative
    isNegative = matrix[row][col] < 0
    if isNegative:
        matrix[row][col] = -matrix[row][col]
        if (row, col) in to_convert:
            to_convert.remove((row, col))
