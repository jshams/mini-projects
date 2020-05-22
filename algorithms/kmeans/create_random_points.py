import random


def create_random_coords(n, dims=2, minimum=None, maximum=None):
    if minimum is None:
        minimum = 0
    if maximum is None:
        maximum = n ** 2

    def get_random(): return random.randint(
        minimum, maximum) + round(random.random(), 2)

    return [[get_random() for _ in range(dims)] for _ in range(n)]


def write_coords_to_file(coords, FILENAME='sample_blob.txt'):
    f = open(FILENAME, 'w+')
    for coord in coords:
        f.write(', '.join([str(c) for c in coord]) + '\n')
    f.close()


if __name__ == '__main__':
    from sys import argv

    n_coordinates = 10
    dims = 2

    if len(argv) == 3:
        n_coordinates = int(argv[1])
        dims = int(argv[2])

    points = create_random_coords(n_coordinates, dims=dims)
    write_coords_to_file(points)
