seen = {}


def towers_of_hanoi_moves(n):
    '''memoized towers of hanoi'''
    if n == 1:
        return [(1, 3)]
    else:
        if n not in seen:
            toh_n_minus_one = towers_of_hanoi_moves(n - 1)
            pivoted = pivot_twice(toh_n_minus_one)
            seen[n] = pivoted[0] + [(1, 3)] + pivoted[1]
        return seen[n]


def pivot(lst_of_tuples, switch1, switch2):
    return [swap(tup, switch1, switch2) for tup in lst_of_tuples]


def pivot_twice(lst_of_tuples):
    p1 = [swap(tup, 2, 3) for tup in lst_of_tuples]
    p2 = [swap(tup, 1, 2) for tup in lst_of_tuples]
    return p1, p2


def swap(tup, switch1, switch2):
    if tup[0] == switch1:
        index0 = switch2
    elif tup[0] == switch2:
        index0 = switch1
    else:
        index0 = tup[0]
    if tup[1] == switch1:
        index1 = switch2
    elif tup[1] == switch2:
        index1 = switch1
    else:
        index1 = tup[1]
    return (index0, index1)


if __name__ == '__main__':
    import sys
    n = 5
    if len(sys.argv) > 1:
        n = sys.argv[1]
    else:
        n = input("Enter the number of rings you'd like to solve for: ")
    try:
        n = int(n)
    except ValueError:
        print(f'Invalid argument for n: "{n}".')
        print('Aborting...')
        exit()
    z = towers_of_hanoi_moves(n)
    print(
        f'With {n} rings in our tower the minumum number of moves is: {len(z)}'
    )
    if input('Would you like to see them? (yes) ') in ('yes', ''):
        print('The moves are:')
        print(z)
    else:
        print('Aborting...')
