def main():
    try:
        fh = open('texts.txt')

        for line in fh:
            print(line.strip())

    except IOError as error:
        print('There is a error in code:', error)


if __name__ == '__main__':
    main()
