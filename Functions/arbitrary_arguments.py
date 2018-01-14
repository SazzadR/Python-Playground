def main():
    test_function(1, 2, 3, 4, 5)


def test_function(*args):
    print(args)
    for i in args:
        print(i)


if __name__ == '__main__':
    main()
