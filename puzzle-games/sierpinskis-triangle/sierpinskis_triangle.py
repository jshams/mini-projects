import turtle


def move_pen_to_start():
    pen.setheading(180)
    pen.pu()
    pen.fd(300)
    pen.lt(90)
    pen.fd(300)
    pen.pd()


def draw_triangle(length):
    '''
    draws an equilateral triangle with the specifies length given.

    params:
        length (int): denotes the length of a triangle side
    '''
    pen.setheading(180)  # set the direction of the pen to left
    for _ in range(3):  # draw 3 sides
        pen.rt(120)  # rotate the pen 120 degrees clockwise
        pen.fd(length)  # draw side
        # pen will end up facing left (180)


def sierpinski_order_n_recursive(n, length=None):
    '''
    draws a sierpinskis triangle of specified order with a specified
    triangle length.

    params:
        n (int):
            Specifies the recursion depth of the triangle.
        length=None (int):
            Specifies the side length of triangle sides.
            If none is specified, a side length is optimized for the
            specified n.
    '''
    if length is None:
        length = get_length(n)
    if n == 1:
        draw_triangle(length)
    else:
        # this is just like calling draw_triangle()
        sierpinski_order_n_recursive(n - 1, length)
        pen.rt(120)
        pen.fd(length * 2 ** (n - 2))
        sierpinski_order_n_recursive(n - 1, length)
        pen.lt(120)
        pen.fd(length * 2 ** (n - 2))
        sierpinski_order_n_recursive(n - 1, length)
        pen.fd(length * 2 ** (n - 2))


def get_length(n):
    '''
    given an integer n, representing the order of Sierp Tri
    return an integer representing the length of each side that
    would allow the drawing to appear within the draw screen.

    params:
        n (int):
            Specifies the recursion depth of a sierpinski triangle.
    '''
    return 640 / (2 ** (n - 1))


def hanlde_input(message, key, error_message):
    inp = input(message)
    try:
        inp = key(inp)
    except:
        print(error_message.format(inp))
        inp = hanlde_input(message, key, error_message)
    return inp


if __name__ == '__main__':
    # used for command line arguments
    from sys import argv
    from time import sleep
    length = None
    if len(argv) == 1:
        print("Welcome to Sierpinski's Triangle illustrator.")
        # get the value for n
        input_message = 'Enter an integer representing the depth of triangle: '
        error_message = 'Invaid input: "{}". Valid input must be a number.'
        n = hanlde_input(input_message, int, error_message)

        specify_len = input(
            'Would you like to specify side width (not recommended)? (y/[n]) ')
        if specify_len == 'y':
            length = hanlde_input(
                'Enter a side length: ', int,
                'Invalid input for side length: "{}". Input must be a number.')
    if len(argv) > 1:
        try:
            n = int(argv[1])
        except ValueError:
            print(f'Invalid argument for depth - {argv[-1]}')
            exit()
    if len(argv) > 2:
        try:
            length = int(argv[2])
        except ValueError:
            print(f'Invalid argument for length - {argv[-1]}')
            exit()

    pen = turtle.Turtle()
    pen.speed(10)  # sets the pen draw speed to max
    move_pen_to_start()
    sierpinski_order_n_recursive(n, length)
    sleep(10)
