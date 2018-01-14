def main():
    for i in inclusive_range(0, 25, 5):
        print(i, end = ' ')


def inclusive_range(*args):
    number_of_arguments = len(args)

    if number_of_arguments < 1:
        raise TypeError('Requires at least one arguments')
    elif number_of_arguments == 1:
        start, end, step = 0, args[0], 1
    elif number_of_arguments == 2:
        start, end, step = args[0], args[1], 1
    elif number_of_arguments == 3:
        start, end, step = args[0], args[1], args[2]
    else:
        raise TypeError('Too many arguments')

    while start <= end:
        yield start
        start = start + step


if __name__ == '__main__':
    main()
