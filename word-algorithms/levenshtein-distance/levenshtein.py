def levenshtein(string1, string2, display_solution=False):
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
    for j in range(1, len(string2) + 1):
        for i in range(1, len(string1) + 1):
            # when letters are equal, use the val diag
            if string1[i - 1] == string2[j - 1]:
                matrix[j][i] = matrix[j - 1][i - 1]

            # otherwise add 1 to the min from the top, left, and diag + 1
            else:
                matrix[j][i] = min(
                    matrix[j - 1][i - 1],
                    matrix[j - 1][i],
                    matrix[j][i - 1]
                ) + 1

    if display_solution is True:
        reversenshtein(string1, string2, matrix)

    # the value of the bottom left corner of the matrix is the levenshtein dist
    return matrix[-1][-1]


def reversenshtein(string1, string2, matrix):
    '''
    Given the matrix calculated by levenshtein, and the two strings used to
    create that matrix, backtrack through the matrix and give instructions on
    the steps of converting one string to the another.

    Go through the matrix from the end (-1, -1) till the start (0, 0) and trace
    the steps required to move from string1 to string2. As the steps are
    calculated, print them to the console.

    [
        [0, 1, 2],
        [1, 1, 1],
        [2, 2, 2]
    ]

    The rules are as follows:
    Beginning with the bottom-right corner of the matrix, move diagonally (up
    then left), left, or up. The chosen direction should be based off which
    move results in the next smallest value at each of their positions.
    Continue moving, until reaching the top-left position.
    A diagonal move means a replacement occurs. If the characters being
    replaced are the same in their respective word positions, or the change of
    values at from the start and end positions are the same (these conditions
    are directly correlated, they mean the same thing), there is no replacement
    occuring. Otherwise replace the repective char in string1 with the
    respective char in string2.
    A left move is a deletion. In this case simply delete the char at the
    respective index in string1.
    An up move indicates an insertion. In this case, insert the char at the
    respective index in string2 at the repective index in string1.
    '''
    print(f'Edit "{string1}" -> "{string2}"')
    print()

    print_matrix(string1, string2, matrix)

    print()
    print(f'Number of operations: {matrix[-1][-1]}')

    print('Edit operations:')
    j = len(string1)
    i = len(string2)

    mod_str = string1

    while (i, j) != (0, 0):

        left = (i, j - 1) if j > 0 else None
        up = (i - 1, j) if i > 0 else None
        diag = (i - 1, j - 1) if (i > 0 and j > 0) else None

        next_move = min(
            filter(bool, (diag, up, left)),
            key=lambda ij: matrix[ij[0]][ij[1]]
        )

        i, j = next_move

        # moving left is a deletion
        if next_move == left:
            del_char = string1[j]
            print(f'\tDelete the char "{del_char}" at index {j}')

            old_mod_str = mod_str
            mod_str = mod_str[:j] + mod_str[j + 1:]
            print(f'\t\t"{old_mod_str}" -> "{mod_str}"')

        # moving up is an addition
        elif next_move == up:
            add_char = string2[i]
            print(f'\tInsert the char "{add_char}" at index {j}')

            old_mod_str = mod_str
            mod_str = mod_str[:j] + add_char + mod_str[j:]
            print(f'\t\t"{old_mod_str}" -> "{mod_str}"')

        # moving diagonally is substitution (unless chars/positions are equal)
        else:
            replaced = string1[j]
            replacement = string2[i]
            if replaced != replacement:
                print(f'\tReplace the char "{replaced}", at index {j}, '
                      f'with "{replacement}"')

                old_mod_str = mod_str
                mod_str = mod_str[:j] + replacement + mod_str[j + 1:]
                print(f'\t\t"{old_mod_str}" -> "{mod_str}"')


def print_matrix(string1, string2, matrix):
    print('  '.join('  ' + string1))
    for char, arr in zip(' ' + string2, matrix):
        print(char, arr)


if __name__ == '__main__':
    string1 = 'real'
    string2 = 'tree'

    ans = levenshtein(string1, string2, display_solution=True)
