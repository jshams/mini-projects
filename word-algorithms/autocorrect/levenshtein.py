def levenshtein(string1, string2):
    '''
    Return the Levenshtein Distance, also known as the Edit distance between
    two strings.

    This is the minimum number of insert, remove, or replace operations to
    convert string1 to string2.
    '''

    # early exit if the strings are equal
    if string1 == string2:
        return 0

    # create the matrix of 0s
    matrix = [[0] * (len(string1) + 1) for _ in range(len(string2) + 1)]
    # replace the 0s in the top row with incrementing nums from left to right
    matrix[0][::] = range(len(string1) + 1)
    # replace the 0s in the left col with incrementing nums from top to bottom
    for i in range(1, len(string2) + 1):
        matrix[i][0] = i

    # fill in the rest of the matrix
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            # when letters are equal, use the val up left
            if string1[i - 1] == string2[j - 1]:
                matrix[j][i] = matrix[j-1][i-1]
            # otherwise add 1 to the min from the top, left, and diag + 1
            else:
                matrix[j][i] = min(
                    matrix[j - 1][i - 1],
                    matrix[j - 1][i],
                    matrix[j][i - 1]
                ) + 1

    # the value of the bottom left corner of the matrix is the levenshtein dist
    return matrix[-1][-1]
