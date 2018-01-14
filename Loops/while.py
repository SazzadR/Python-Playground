def main():
    a, b = 0, 1

    while b < 50:
        number = a + b
        print(number)
        a = b
        b = number


if __name__ == '__main__':
    main()
